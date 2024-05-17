# import all required libraries and modules from read_pandas.py
import streamlit as st
from read_pandas import read_my_csv
from read_pandas import make_plot_ecg, make_plot_power
import pandas as pd
import numpy as np

# Read the EKG data
df1 = pd.read_csv("data/ekg_data/01_Ruhe.txt", sep="\t", header=None)

# Read the Power data
df2 = pd.read_csv("data/activities/activity.csv")

# Add a time column to the Power data
t_end = len(df2["PowerOriginal"])
df2["Time in s"] = np.arange(0, t_end)

# Create a list of paths to the EKG data
path1 = "data/ekg_data/01_Ruhe.txt"
path2 = "data/ekg_data/02_Ruhe.txt"
path3 = "data/ekg_data/03_Ruhe.txt"
path4 = "data/ekg_data/04_Belastung.txt"
path5 = "data/ekg_data/05_Belastung.txt"
paths = [path1, path2, path3, path4, path5]

tab1, tab2 = st.tabs(["EKG-Data", "Power-Data"])

with tab1:
    st.header("EKG-Data")
    st.write("# My Plot")
    path = st.selectbox('Choose your File:', paths)  # Select the file to display
    df = read_my_csv(path)
    fig = make_plot_ecg(df)
    st.plotly_chart(fig)

with tab2:
    st.subheader("Interaktiver Plot")
    st.header("Power- & Heart-Data")
    hr_max = st.number_input('Please enter the maximum heartrate (0 = no Input -> max_hr generated from data):',
                             min_value=0, max_value=300, value=0, step=1)  # Input for the maximum heartrate
    if hr_max == 0:
        hr_max = df2["HeartRate"].max() # Set the maximum heartrate to the maximum heartrate from the data
    elif hr_max < df2["HeartRate"].max(): #Warn the user if the input is lower than the maximum heartrate from the data
        st.markdown("The maximum heartrate from data is:", df2["HeartRate"].max())
        st.markdown("Are you sure you want to use a lower value?")

    fig, zone_counts = make_plot_power(df2, hr_max)

    # Calculate Power statistics
    st.write("Maximum power:", round(df2["PowerOriginal"].max()), "watts")
    st.write("Average power:", round(df2["PowerOriginal"].mean()), "watts")

    st.plotly_chart(fig)

    col1, col2 = st.columns(2)
    with col1:
        # Calculate time in each zone
        st.write("Time in Zone 1:", zone_counts["Zone1"], "s")
        st.write("Time in Zone 2:", zone_counts["Zone2"], "s")
        st.write("Time in Zone 3:", zone_counts["Zone3"], "s")
        st.write("Time in Zone 4:", zone_counts["Zone4"], "s")
        st.write("Time in Zone 5:", zone_counts["Zone5"], "s")

    with col2:
        # Calculate average power in each zone
        zones = ['Zone1', 'Zone2', 'Zone3', 'Zone4', 'Zone5']
        for zone in zones:
            if zone in df2.columns and df2[zone].any():
                average_power = round(df2[df2[zone]]['PowerOriginal'].mean())
                st.write(f"Average power in {zone}:", average_power, "watts")
