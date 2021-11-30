import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## process_file() takes a string with a path to the .csv
def process_file(pathname):
    res = pd.read_csv(pathname, sep = ',', header = 0, index_col = None, names = ['time', 'seconds', 'z', 'y', 'x'])
    return res
    
def main():

    # 5 minutes waking data- Diego
    # Left pocket
    dlp_5min = process_file('data/5minlp.csv')
    # Right pocket
    drp_5min = process_file('data/5minrp.csv')

    # Trim data to 300 seconds from 30 to 330 seconds.
    dlp_5min = dlp_5min[(dlp_5min['seconds'] >= 30) & (dlp_5min['seconds'] <= 330)]
    drp_5min = drp_5min[(drp_5min['seconds'] >= 30) & (drp_5min['seconds'] <= 330)]

    dlp_5min.to_csv('processed_data/dlp_5min.csv')
    drp_5min.to_csv('processed_data/drp_5min.csv')


    # 5 minutes waking data- Matt
    # Right pocket
    mrp_5min = process_file('data/matt_rp50_5mins.csv')
    mlp_5min = process_file('data/matt_lp50_5mins.csv')
    mrp_5min = mrp_5min[(mrp_5min['seconds'] >= 10) & (mrp_5min['seconds'] <= 310)]
    mlp_5min = mlp_5min[(mlp_5min['seconds'] >= 30) & (mlp_5min['seconds'] <= 330)]

    mlp_5min.to_csv('processed_data/mlp_5min.csv')
    mrp_5min.to_csv('processed_data/mrp_5min.csv')


    # 5 minutes waking data- Sidak 
    # Right pocket
    srp_5min = process_file('data/sam_rp50_5mins.csv')
    slp_5min = process_file('data/sam_lp50_5mins.csv')
    srp_5min = srp_5min[(srp_5min['seconds'] >= 30) & (srp_5min['seconds'] <= 330)]
    slp_5min = slp_5min[(slp_5min['seconds'] >= 30) & (slp_5min['seconds'] <= 330)]

    slp_5min.to_csv('processed_data/slp_5min.csv')
    srp_5min.to_csv('processed_data/srp_5min.csv')


if __name__ == "__main__":
    main()