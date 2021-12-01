import pandas as pd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# process_file() takes a string with a path to the .csv


def process_file(pathname):
    res = pd.read_csv(pathname, sep=',', header=0, index_col=None, names=[
                      'time', 'seconds', 'z', 'y', 'x'])
    return res

# butterworth() takes a dataframe with our accelerometer data and applies the Butterworth filter to it.
# The columns of the DF is overwritten by the filtered values.
# Sources: https://scipy-cookbook.readthedocs.io/items/ButterworthBandpass.html
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html


def butterworth(df):
    nyquist_frequency = 0.5 * 50

    low = 0.5 / nyquist_frequency
    high = 3.0 / nyquist_frequency

    b, a = signal.butter(3, Wn=[low, high], btype='bandpass')

    df['x'] = signal.filtfilt(b, a, df['x'])
    df['y'] = signal.filtfilt(b, a, df['y'])
    df['z'] = signal.filtfilt(b, a, df['z'])

    return df


def main():

    # read the preocessed file to get the trimed data
    dlp_5min = process_file('processed_data/dlp_5min.csv')
    drp_5min = process_file('processed_data/drp_5min.csv')
    mrp_5min = process_file('processed_data/mrp_5min.csv')
    slp_5min = process_file('processed_data/slp_5min.csv')
    srp_5min = process_file('processed_data/srp_5min.csv')

    # use butterworth() to filter the data
    dlp_5min_bw = butterworth(dlp_5min)
    drp_5min_bw = butterworth(drp_5min)
    mrp_5min_bw = butterworth(mrp_5min)
    slp_5min_bw = butterworth(slp_5min)
    srp_5min_bw = butterworth(srp_5min)

    # write out the filtered data
    dlp_5min_bw.to_csv('processed_data/dlp_5min_bw.csv', index=False)
    drp_5min_bw.to_csv('processed_data/drp_5min_bw.csv', index=False)
    mrp_5min_bw.to_csv('processed_data/mrp_5min_bw.csv', index=False)
    slp_5min_bw.to_csv('processed_data/slp_5min_bw.csv', index=False)
    srp_5min_bw.to_csv('processed_data/srp_5min_bw.csv', index=False)


if __name__ == "__main__":
    main()