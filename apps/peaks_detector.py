"""
THe basic app for listening BCI and sending singals do BackEnd
"""

import sys
import numpy as np
import pylsl
from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import bci.data_utils as tl_data
from .websocket_client import WebSocketClient

SAMPLING_FREQ = 250
RECORD_HISTORY = 5 * SAMPLING_FREQ
PLOT_OFFSET = 4 * SAMPLING_FREQ
EEG_CHANNELS = 1
SIGNAL_RANGE = [-250, 250]
FRAME_REFRESH = 100  # miliseconds
MEASURE_FRAME = int(0.1 * SAMPLING_FREQ)

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = pylsl.resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = pylsl.StreamInlet(streams[0])

websocket = WebSocketClient('ws://192.168.7.14:8000/ws/bci/U123/')


class Window(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure(figsize=(20, 5))
        # data
        self.signals = None
        self.biting = False

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some timer connected to `plot` method
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(FRAME_REFRESH)

        # set the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def update(self):
        """ plot some random stuff """
        chunk, tstamps = inlet.pull_chunk(timeout=0.0, max_samples=2048)
        # IMPORTANT: drop the timestemps because it does not reflect the measurement time
        if tstamps:
            ys = np.asarray(chunk)

            if self.signals is None:
                self.signals = ys.copy()
            else:
                self.signals = np.vstack([self.signals, ys])[-RECORD_HISTORY:]

        self.detection()
        self.plot()

    def detection(self):
        if self.signals is None or len(self.signals) < RECORD_HISTORY:
            return
        sig = tl_data.filter_signal(self.signals[:, 0], bands=[1, 120])
        measure = np.mean(sig[-MEASURE_FRAME:] ** 2)
        # print (measure)
        if measure > 10000 and not self.biting:
            self.on_event_bite()
            self.biting = True
        else:
            self.biting = False

    def on_event_bite(self):
        websocket.send_data('bite', 1)

    def on_event_blink(self):
        websocket.send_data('blink', 1, eyes='both')

    def plot(self):
        # instead of ax.hold(False)
        self.figure.clear()
        # create an axis
        ax = self.figure.add_subplot(111)
        # discards the old graph
        # ax.hold(False) # deprecated, see above
        # plot data
        if self.signals is not None:
            for ch in range(EEG_CHANNELS):
                # sig = self.signals[2000:, ch]
                # TODO: add real time filtering
                sig = tl_data.filter_signal(self.signals[:, ch], bands=[1, 120])
                # sig = sig - np.mean(sig)
                ax.plot(sig[PLOT_OFFSET:],
                        label=str(ch + 1))
            #ax.set_xlim([min(self.timestamps), max(self.timestamps)])
            ax.legend(loc=2)
        ax.set_ylim(SIGNAL_RANGE)
        ax.grid()
        # refresh canvas
        self.canvas.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
