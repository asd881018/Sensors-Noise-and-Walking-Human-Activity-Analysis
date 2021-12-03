import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy import signal
from numpy.fft import fft

# process_file() takes a string with a path to the .csv


def process_file(pathname):
    res = pd.read_csv(pathname, sep=',', header=0, index_col=None, names=[
                      'time', 'seconds', 'z', 'y', 'x'])
    return res

# fourier() takes a dataframe with our filtered accelerometer data and produces a new dataframe with x, y pairs.
# This produces the Fourier-transformed data. (I assume)
# Sources: https://stackoverflow.com/questions/66675657/fast-fourier-transform-for-an-accelerometer-in-python


def fourier(df):
    yf = np.abs(fft(df['x'] + df['y'] + df['z']))
    xf = np.linspace(0, df.shape[0] / 60, len(yf))

    return pd.DataFrame(zip(xf, yf), columns=['x', 'y'])


def main():
    # read trimed raw data
    dlp_5min = process_file('processed_data/dlp_5min.csv')
    drp_5min = process_file('processed_data/drp_5min.csv')

    mrp_5min = process_file('processed_data/mrp_5min.csv')
    mrp_1min_screenon = process_file('data/matt_rp50_1min_screenon.csv')
    mrp_1min_screenoff = process_file('data/matt_rp50_1min_screenoff.csv')

    slp_5min = process_file('processed_data/slp_5min.csv')
    srp_5min = process_file('processed_data/srp_5min.csv')

    # read butter worth filter data
    dlp_5min_bw = process_file('processed_data/dlp_5min_bw.csv')
    drp_5min_bw = process_file('processed_data/drp_5min_bw.csv')

    mrp_5min_bw = process_file('processed_data/mrp_5min_bw.csv')
    mrp_1min_screenon_bw = process_file(
        'processed_data/mrp_1min_screenon_bw.csv')
    mrp_1min_screenoff_bw = process_file(
        'processed_data/mrp_1min_screenoff_bw.csv')

    slp_5min_bw = process_file('processed_data/slp_5min_bw.csv')
    srp_5min_bw = process_file('processed_data/srp_5min_bw.csv')

    # using fourier transform for trimed raw data
    dlp_5min_fft = fourier(dlp_5min)
    drp_5min_fft = fourier(drp_5min)

    mrp_5min_fft = fourier(mrp_5min)
    mrp_1min_screenon_fft = fourier(mrp_1min_screenon)
    mrp_1min_screenoff_fft = fourier(mrp_1min_screenoff)

    slp_5min_fft = fourier(slp_5min)
    srp_5min_fft = fourier(srp_5min)

    # using fourier transform for butter worth filter data
    dlp_5min_bw_fft = fourier(dlp_5min_bw)
    drp_5min_bw_fft = fourier(drp_5min_bw)

    mrp_5min_bw_fft = fourier(mrp_5min_bw)
    mrp_1min_screenon_bw_fft = fourier(mrp_1min_screenon_bw)
    mrp_1min_screenoff_bw_fft = fourier(mrp_1min_screenoff_bw)

    slp_5min_bw_fft = fourier(slp_5min_bw)
    srp_5min_bw_fft = fourier(srp_5min_bw)

    # write out fourier transform for trimed raw data
    dlp_5min_fft.to_csv('processed_data/dlp_5min_fft.csv', index=False)
    drp_5min_fft.to_csv('processed_data/drp_5min_fft.csv', index=False)

    mrp_5min_fft.to_csv('processed_data/dlp_5min_fft.csv', index=False)
    mrp_1min_screenon_fft.to_csv(
        'processed_data/mrp_1min_screenon_fft.csv', index=False)
    mrp_1min_screenoff_fft.to_csv(
        'processed_data/mrp_1min_screenoff_fft.csv', index=False)

    slp_5min_fft.to_csv('processed_data/slp_5min_fft.csv', index=False)
    srp_5min_fft.to_csv('processed_data/srp_5min_fft.csv', index=False)

    # write out fourier transform for butter worth filter data
    dlp_5min_bw_fft.to_csv('processed_data/dlp_5min_bw_fft.csv', index=False)
    drp_5min_bw_fft.to_csv('processed_data/drp_5min_bw_fft.csv', index=False)

    mrp_5min_bw_fft.to_csv('processed_data/mrp_5min_bw_fft.csv', index=False)
    mrp_1min_screenon_bw_fft.to_csv(
        'processed_data/mrp50_1min_screenon_bw_fft.csv', index=False)
    mrp_1min_screenoff_bw_fft.to_csv(
        'processed_data/mrp50_1min_screenoff_bw_fft.csv', index=False)

    slp_5min_bw_fft.to_csv('processed_data/slp_5min_bw_fft.csv', index=False)
    srp_5min_bw_fft.to_csv('processed_data/srp_5min_bw_fft.csv', index=False)


if __name__ == "__main__":
    main()
