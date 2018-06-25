"""
THe basic app for listening BCI and sending singals do BackEnd

"""

import sys
import time
import logging
import numpy as np
from PyQt5 import QtCore, QtWidgets

import matplotlib.pyplot as plt

import bci.data_utils as tl_data
from apps.websocket_client import WebSocketClient
from apps.simple_viewer import WaveViewer

SOCKET_LINK = 'ws://192.168.7.14:8000/ws/bci/U123/'

class PeakDetect(WaveViewer):

    MEASURE_FRAME = int(0.1 * WaveViewer.SAMPLING_FREQ)
    DOUBLE_DELAY = 0.5
    BITING_THRESHOLD = 10000

    def __init__(self, parent=None):
        super(PeakDetect, self).__init__(parent)

        # data
        self.biting = False
        self.bite_last = -np.inf
        self.bite_wait = 0

        self.websocket = WebSocketClient(SOCKET_LINK)

    def update(self):
        """ plot some random stuff """
        super(PeakDetect, self).update()
        self.detection()

    def detection(self):
        if self.signals is None or len(self.signals) < self.RECORD_HISTORY:
            return
        sig = tl_data.filter_signal(self.signals[:, 0], bands=[1, 120])
        measure = np.mean(sig[-self.MEASURE_FRAME:] ** 2)
        # print (measure)
        if measure > self.BITING_THRESHOLD and not self.biting:
            logging.debug('biting')
            self.biting = True
            self.bite_wait += 1
            self.bite_last = time.time()
        else:
            self.biting = False

        # logic for double bites within 0.5s
        delay = time.time() - self.bite_last
        if self.biting and self.bite_wait > 1 and delay <+ self.DOUBLE_DELAY:
            self.on_event_bite_double()
            self.bite_wait = 0
        elif not self.biting and self.bite_wait == 1 and  delay > self.DOUBLE_DELAY:
            self.on_event_bite_single()
            self.bite_wait = 0

    def on_event_bite_double(self):
        logging.info('Bite Double! t:%f', time.time())
        self.websocket.send_data('bite', 2)

    def on_event_bite_single(self):
        logging.info('Bite! t:%f', time.time())
        self.websocket.send_data('bite', 1)

    def on_event_blink(self):
        logging.info('Blink!')
        self.websocket.send_data('blink', 1, eyes='both')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app = QtWidgets.QApplication(sys.argv)

    main = PeakDetect()
    main.show()

    sys.exit(app.exec_())
