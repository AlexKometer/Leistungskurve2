# Description: This file contains the functions to read the data from the csv file and create the plots.
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def read_my_csv(path):
    df = pd.read_csv(path, sep="\t", header=None)
    df.columns = ["Messwerte in mV", "Zeit in ms"]

    return df


def make_plot_ecg(df):
    # Creating a line plot using Plotly Express
    fig = px.line(df, x="Zeit in ms", y="Messwerte in mV")

    # Configuring the layout to include a range slider
    fig.update_layout(xaxis=dict(rangeslider=dict(visible=True, thickness=0.1), type='linear', fixedrange=False),
                      yaxis=dict(fixedrange=True))
    return fig


def make_plot_power(df2, hr_max):
    # Create a plot with two y-axes
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(x=df2["Time in s"], y=df2["PowerOriginal"], name="PowerOriginal", line=dict(color="lightgray")),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=df2["Time in s"], y=df2["HeartRate"], name="HeartRate", line=dict(color="royalblue")),
        secondary_y=True,
    )
    fig.update_xaxes(title_text="Time in s")

    fig.update_yaxes(title_text="Power (watts)", title_font=dict(color="lightgray"), tickfont=dict(color="lightgray"),
                     secondary_y=False)
    fig.update_yaxes(title_text="Heart Rate (bpm)", title_font=dict(color="royalblue"),
                     tickfont=dict(color="royalblue"), secondary_y=True)

    max_value = max(df2["PowerOriginal"].max(), df2["HeartRate"].max())

    fig.update_yaxes(range=[0, max_value], secondary_y=False)
    fig.update_yaxes(range=[0, max_value], secondary_y=True)

    # Define the heart rate zones
    zone1 = hr_max * 0.6
    zone2 = hr_max * 0.7
    zone3 = hr_max * 0.8
    zone4 = hr_max * 0.9

    # Create a column for each heart rate zone
    df2["Zone1"] = df2["HeartRate"] < zone1
    df2["Zone2"] = (df2["HeartRate"] >= zone1) & (df2["HeartRate"] < zone2)
    df2["Zone3"] = (df2["HeartRate"] >= zone2) & (df2["HeartRate"] < zone3)
    df2["Zone4"] = (df2["HeartRate"] >= zone3) & (df2["HeartRate"] < zone4)
    df2["Zone5"] = (df2["HeartRate"] >= zone4) & (df2["HeartRate"] < hr_max)

    # Calculate the time in each zone
    zone_counts = {
        "Zone1": df2["Zone1"].sum(),
        "Zone2": df2["Zone2"].sum(),
        "Zone3": df2["Zone3"].sum(),
        "Zone4": df2["Zone4"].sum(),
        "Zone5": df2["Zone5"].sum(),
    }
    # Add the heart rate zones to the plot
    fig.add_hrect(y0=0, y1=zone1, fillcolor="lightgreen", opacity=0.5, layer="below", line_width=0)
    fig.add_hrect(y0=zone1, y1=zone2, fillcolor="green", opacity=0.5, layer="below", line_width=0)
    fig.add_hrect(y0=zone2, y1=zone3, fillcolor="yellow", opacity=0.5, layer="below", line_width=0)
    fig.add_hrect(y0=zone3, y1=zone4, fillcolor="orange", opacity=0.5, layer="below", line_width=0)
    fig.add_hrect(y0=zone4, y1=hr_max, fillcolor="red", opacity=0.5, layer="below", line_width=0)

    return fig, zone_counts
