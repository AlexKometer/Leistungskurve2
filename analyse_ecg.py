#import all required libraries and modules from read_pandas.py
import scipy
from read_pandas import read_my_csv
import numpy as np

# Function to detect peaks in the ECG data, Output is an array of heart rates
def peak_detection(path):
    df = read_my_csv(path)
    peaks = scipy.signal.find_peaks(df["Messwerte in mV"], height=350)
    print("Peaks:", peaks)
    peak_interval = np.diff(peaks[0])
    peak_interval_seconds = peak_interval / 1000
    hr = np.round(60 / peak_interval_seconds, 2)

    return hr



# Function to calculate heart rate statistics
def calculate_hr_data(hr):
    hr_max = hr.max()
    hr_min = hr.min()
    hr_mean = hr.mean()

    return hr_max, hr_min, hr_mean
