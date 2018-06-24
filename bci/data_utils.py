"""
Basic handling data

"""

import os

import numpy as np
from scipy import signal
# from mne import filter

SAMPLE_FREQ = 250.


def update_path(path, max_up=5):
    """ update the path by bobble up

    :param str path:
    :param int max_up:
    :return str:

    >>> os.path.isdir(update_path('bci'))
    True
    """
    path = os.path.expanduser(path)
    for _ in range(max_up):
        if os.path.exists(path):
            break
        path = os.path.join('..', path)
    return path


def load_data(file_name, bands=(0.5, 120), eeg_channels=8):
    """ loading data from a binary (raw) file

    :param str file_name: file name
    :param float float_mean: floating mean in seconds
    :return:

    >>> p_data = os.path.join(update_path('data_samples'), 'blinking', 'both.bin')
    >>> eeg = load_data(p_data)  # doctest: +ELLIPSIS
    ...
    >>> len(eeg) > 0
    True
    """
    data = np.fromfile(file_name, dtype='float32')
    data = data.reshape(-1, 17)
    eeg = data[:, :eeg_channels]
    for i in range(eeg.shape[1]):
        eeg[:, i] = filter_signal(eeg[:, i], bands)
    return eeg


def filter_signal(sig, bands=(0.5, 120)):
    freq = 50 / (0.5 * SAMPLE_FREQ)
    b, a = signal.iirnotch(freq, Q=freq / 2.)
    sig = signal.lfilter(b, a, sig)
    if bands is not None:
        b, a = signal.butter(5, Wn=np.array(bands) / (0.5 * SAMPLE_FREQ),
                             btype='band')
        sig = signal.lfilter(b, a, sig)
    return sig


# TODO: online data filtering
