# import all required libraries and modules from read_pandas.py
from read_pandas import read_my_csv
from read_pandas import make_plot_ecg, make_plot_power
import pandas as pd
import numpy as np

t_w = [1,2,5,10,20,30,60,120,300,600,1200,1800] #Daten nicht länge vorhanden

def find_best_effort(df):
    power_curve = []
    df_clean = df.dropna (subset=['PowerOriginal'])

    for interval in t_w:
        rolling_mean = df_clean['PowerOriginal'].rolling (window=interval).mean ()
        max_average_power = rolling_mean.max ()
        power_curve.append(max_average_power)


    #power_curve_df = pd.DataFrame (list (power_curve.items()), columns=['Interval (s)', 'Max Average Power'])

    return t_w, power_curve

