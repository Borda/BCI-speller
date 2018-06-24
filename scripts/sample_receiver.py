import sys
import numpy as np
import pylsl
from PyQt5 import QtCore, QtWidgets
# from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import bci.data_utils as tl_data

PLOT_DURATION = 3.0
EEG_CHANNELS = 14
SIGNAL_RANGE = [-1000, 1000]
FRAME_REFRESH = 100

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = pylsl.resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = pylsl.StreamInlet(streams[0])


class Window(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure(figsize=(20, 5))
        # data
        self.timestamps = None
        self.signals = None

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
        chunk, tstamps = inlet.pull_chunk(timeout=0.0, max_samples=128)
        if tstamps:
            tstamps = np.asarray(tstamps)
            ys = np.asarray(chunk)
            t0 = np.max(tstamps) - PLOT_DURATION

            if self.timestamps is None:
                self.signals = ys.copy()
                self.timestamps = tstamps.copy()
            else:
                mask = self.timestamps > t0
                self.timestamps = np.hstack([self.timestamps[mask], tstamps])
                self.signals = np.vstack([self.signals[mask], ys])
        self.plot()

    def plot(self):
        # instead of ax.hold(False)
        self.figure.clear()
        # create an axis
        ax = self.figure.add_subplot(111)
        # discards the old graph
        # ax.hold(False) # deprecated, see above
        # plot data
        if self.timestamps is not None:
            for ch in range(EEG_CHANNELS):
                sig = tl_data.filter_signal(self.signals[:, ch])
                # sig = self.signals[:, ch] - np.mean(self.signals[:, ch])
                ax.plot(self.timestamps, sig,
                        label=str(ch + 1))
            ax.set_xlim([min(self.timestamps), max(self.timestamps)])
            ax.legend()
        # ax.set_ylim(SIGNAL_RANGE)
        ax.grid()
        # refresh canvas
        self.canvas.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
