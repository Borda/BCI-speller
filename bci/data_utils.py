"""
Basic hadling data

"""

import numpy as np
from scipy import signal
from mne import filter

SAMPLE_FREQ = 250.


def load_data(file_name, float_mean=5):
    """ loading data from a file

    :param str file_name: file name
    :param float float_mean: floating mean in seconds
    :return:

    """
    ft_mean_samples = int(float_mean * SAMPLE_FREQ)
    data = np.fromfile(file_name, dtype='float32')
    data = data.reshape(-1, 17)
    eeg = data[:, :8]
    means = np.array([np.mean(eeg[i:ft_mean_samples+i], axis=0)
                      for i in range(len(eeg) - ft_mean_samples)])
    print (means.shape)
    eeg = eeg[ft_mean_samples:] - means
    for i in range(eeg.shape[1]):
        eeg[:, i] = filter.notch_filter(x=eeg[:, i].astype(np.float64),
                                        Fs=SAMPLE_FREQ,
                                        freqs=[50],
                                        trans_bandwidth=2)
        b, a = signal.butter(5, Wn=np.array([0.5, 30]) / (0.5 * SAMPLE_FREQ),
                             btype='band')
        eeg[:, i] = signal.lfilter(b, a, eeg[:, i])
    return eeg
