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

    mrp_1min_screenon = process_file('data/matt_rp50_1min_screenon.csv')
    mrp_1min_screenoff = process_file('data/matt_rp50_1min_screenoff.csv')

    m_up24_1 = process_file('processed_data\m_up24_1.csv')
    m_up24_2 = process_file('processed_data\m_up24_2.csv')
    m_up24_3 = process_file('processed_data\m_up24_3.csv')
    m_up24_4 = process_file('processed_data\m_up24_4.csv')
    m_up24_5 = process_file('processed_data\m_up24_5.csv')

    m_down24_1 = process_file('processed_data\m_down24_1.csv')
    m_down24_2 = process_file('processed_data\m_down24_2.csv')
    m_down24_3 = process_file('processed_data\m_down24_3.csv')
    m_down24_4 = process_file('processed_data\m_down24_4.csv')
    m_down24_5 = process_file('processed_data\m_down24_5.csv')

    d_up_1 = process_file('processed_data\d_up_1.csv')
    d_up_2 = process_file('processed_data\d_up_2.csv')
    d_up_3 = process_file('processed_data\d_up_3.csv')
    d_up_4 = process_file('processed_data\d_up_4.csv')

    d_down_1 = process_file('processed_data\d_down_1.csv')
    d_down_2 = process_file('processed_data\d_down_2.csv')
    d_down_3 = process_file('processed_data\d_down_3.csv')
    d_down_4 = process_file('processed_data\d_down_4.csv')

    d_run = process_file('processed_data\d_run_4min.csv')

    # use butterworth() to filter the data
    dlp_5min_bw = butterworth(dlp_5min)
    drp_5min_bw = butterworth(drp_5min)
    mrp_5min_bw = butterworth(mrp_5min)
    mrp_1min_screenon_bw = butterworth(mrp_1min_screenon)
    mrp_1min_screenoff_bw = butterworth(mrp_1min_screenoff)
    slp_5min_bw = butterworth(slp_5min)
    srp_5min_bw = butterworth(srp_5min)

    # use butterworth() to filter the activity data
    m_up24_1_bw = butterworth(m_up24_1)
    m_up24_2_bw = butterworth(m_up24_2)
    m_up24_3_bw = butterworth(m_up24_3)
    m_up24_4_bw = butterworth(m_up24_4)
    m_up24_5_bw = butterworth(m_up24_5)

    m_down24_1_bw = butterworth(m_down24_1)
    m_down24_2_bw = butterworth(m_down24_2)
    m_down24_3_bw = butterworth(m_down24_3)
    m_down24_4_bw = butterworth(m_down24_4)
    m_down24_5_bw = butterworth(m_down24_5)

    d_up_1_bw = butterworth(d_up_1)
    d_up_2_bw = butterworth(d_up_2)
    d_up_3_bw = butterworth(d_up_3)
    d_up_4_bw = butterworth(d_up_4)

    d_down_1_bw = butterworth(d_down_1)
    d_down_2_bw = butterworth(d_down_2)
    d_down_3_bw = butterworth(d_down_3)
    d_down_4_bw = butterworth(d_down_4)

    d_run_bw = butterworth(d_run)

    # write out the filtered data
    dlp_5min_bw.to_csv('processed_data/dlp_5min_bw.csv', index=False)
    drp_5min_bw.to_csv('processed_data/drp_5min_bw.csv', index=False)

    mrp_5min_bw.to_csv('processed_data/mrp_5min_bw.csv', index=False)
    mrp_1min_screenon_bw.to_csv(
        'processed_data/mrp_1min_screenon_bw.csv', index=False)
    mrp_1min_screenoff_bw.to_csv(
        'processed_data/mrp_1min_screenoff_bw.csv', index=False)

    slp_5min_bw.to_csv('processed_data/slp_5min_bw.csv', index=False)
    srp_5min_bw.to_csv('processed_data/srp_5min_bw.csv', index=False)

    m_up24_1_bw.to_csv('processed_data/m_up24_1_bw.csv', index=False)
    m_up24_2_bw.to_csv('processed_data/m_up24_2_bw.csv', index=False)
    m_up24_3_bw.to_csv('processed_data/m_up24_3_bw.csv', index=False)
    m_up24_4_bw.to_csv('processed_data/m_up24_4_bw.csv', index=False)
    m_up24_5_bw.to_csv('processed_data/m_up24_5_bw.csv', index=False)

    m_down24_1_bw.to_csv('processed_data/m_down24_1_bw.csv', index=False)
    m_down24_2_bw.to_csv('processed_data/m_down24_2_bw.csv', index=False)
    m_down24_3_bw.to_csv('processed_data/m_down24_3_bw.csv', index=False)
    m_down24_4_bw.to_csv('processed_data/m_down24_4_bw.csv', index=False)
    m_down24_5_bw.to_csv('processed_data/m_down24_5_bw.csv', index=False)

    d_up_1_bw.to_csv('processed_data/d_up_1_bw.csv', index=False)
    d_up_2_bw.to_csv('processed_data/d_up_2_bw.csv', index=False)
    d_up_3_bw.to_csv('processed_data/d_up_3_bw.csv', index=False)
    d_up_4_bw.to_csv('processed_data/d_up_4_bw.csv', index=False)

    d_down_1_bw.to_csv('processed_data/d_down_1_bw.csv', index=False)
    d_down_2_bw.to_csv('processed_data/d_down_2_bw.csv', index=False)
    d_down_3_bw.to_csv('processed_data/d_down_3_bw.csv', index=False)
    d_down_4_bw.to_csv('processed_data/d_down_4_bw.csv', index=False)

    d_run_bw.to_csv('processed_data/d_run_4min_bw.csv', index=False)


if __name__ == "__main__":
    main()
