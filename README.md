# CMPT353 Project: Sensors, Noise and Walking: Human Activity Analysis


## Project Scope
This project explores human activity prediction by using Data Science and Machine Learning tools to analyze and predict a person’s current activity. We use our smartphones to record simple human movements, such as walking, running, and climbing stairs, and build a Machine Learning model that accurately predicts these activities. This project is inspired by Guillaume Chevalier’s LSTM Human Activity Recognition Project (https://github.com/guillaume-chevalier/LSTM-Human-Activity-Recognition).

## Python version and libraries
- We use python version 3.7.0
- Library installed: pandas, numpy, matplotlib, scipy, sklearn

## Main topic
- Data gathering and cleaning
- Machine Learning

## Files
1. `src.ipynb`
  - include all the library, functions
  - Small demostration of the implements
      - Screen on/off test
      - Butterworth Filter
      - Fourier Transform
(Note: machine learning implement is in `machinelearning.ipynb`)

2. `read_raw_data.py`
  - read the raw data
  - trim the useless data
  - write out new CSV file to processed_data folder
 
3. `bw_filter_data`
  - read raw or trimmed data
  - use Butterworth filter to filter the noise the out
  - write out new CSV file with tag( _bw ) to processed_data folder

4. `fft_data`
  - read raw or trimmed data or filtered data
  - use Fast Fourier Transform to transform the sigal to frequency
  - write out new CSV file with tag( _fft ) to processed_data folder

5. `machinelearning.ipynb`
  - read 5 mins walking data and up/downstairs walking data
  - make data fit int the Machine Leanring Model format
  - mark down each movement and trim each movement with same size
  - Run different Machine Learning Model, print out the score and report
  - Use different Machine Learning Model to predict the activity
6. `screen_onoff.ipynb`
  - read screen on/off data
  - plot two raw data to compare the difference
  - Use Butterworth Filter and Fourier Transfrom
  - Plot screen off raw data, screen on raw data, Butterwoth Filter screen off bw filtered data, Butterwoth Filter screen on bw filtered data
  - Plot screen off raw data with Fourier Tansform, screen on raw data with Fourier Tansform, Butterwoth Filter screen off bw filtered data with Fourier Tansform, Butterwoth   Filter screen on bw filtered data with Fourier Tansform
