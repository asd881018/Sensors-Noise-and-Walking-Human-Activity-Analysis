import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## process_file() takes a string with a path to the .csv
def process_file(pathname):
    res = pd.read_csv(pathname, sep = ',', header = 0, index_col = None, names = ['time', 'seconds', 'z', 'y', 'x'])
    return res
    
# 5 minutes waking data- Diego
def read_dlp_data():
    # Left pocket
    dlp_5min = process_file('data/5minlp.csv')
    dlp_5min = dlp_5min[(dlp_5min['seconds'] >= 30) & (dlp_5min['seconds'] <= 330)]
    dlp_5min['seconds'] = dlp_5min['seconds'] - 30
    dlp_5min = dlp_5min.iloc[0:14000, :]
    return dlp_5min

def read_drp_data():
    # Right pocket
    drp_5min = process_file('data/5minrp.csv')
    drp_5min = drp_5min[(drp_5min['seconds'] >= 30) & (drp_5min['seconds'] <= 330)]
    drp_5min['seconds'] = drp_5min['seconds'] - 30
    drp_5min = drp_5min.iloc[0:14000, :]
    return drp_5min

# 5 minutes waking data- Matt
def read_mrp_data():  
    # Right pocket
    mrp_5min = process_file('data/matt_rp50_5mins_screeon.csv')
    mrp_5min = mrp_5min[(mrp_5min['seconds'] >= 10) & (mrp_5min['seconds'] <= 310)]
    mrp_5min = mrp_5min.iloc[0:14000, :]
    return mrp_5min

# 5 minutes waking data- Sidak 
def read_srp_data():  
    # Right pocket
    srp_5min = process_file('data/sam_rp50_5mins.csv')
    srp_5min = srp_5min[(srp_5min['seconds'] >= 30) & (srp_5min['seconds'] <= 330)]
    srp_5min = srp_5min.iloc[0:14000, :]
    return srp_5min

def read_slp_data():  
    # Left pocket
    slp_5min = process_file('data/sam_lp50_5mins.csv')
    slp_5min = slp_5min[(slp_5min['seconds'] >= 30) & (slp_5min['seconds'] <= 330)]
    slp_5min = slp_5min.iloc[0:14000, :]
    return slp_5min


def main():

    dlp_5min = read_dlp_data()
    drp_5min = read_dlp_data()

    mrp_5min = read_mrp_data()

    slp_5min = read_slp_data()
    srp_5min = read_srp_data()

    dlp_5min.to_csv('processed_data/dlp_5min.csv')
    drp_5min.to_csv('processed_data/drp_5min.csv')


    mrp_5min.to_csv('processed_data/mrp_5min.csv')

    slp_5min.to_csv('processed_data/slp_5min.csv')
    srp_5min.to_csv('processed_data/srp_5min.csv')

if __name__ == "__main__":
    main()