# Power curve II
#### Autors: Georg Sagmeister, Kometer Alexander

## Description

This Streamlit application allows users to visualize and analyze EKG and power data. The app provides three main functionalities:
1. **EKG Data Visualization**: Select and plot EKG data from different files.
2. **Power Data Analysis**: Input maximum heart rate, visualize power and heart rate data, and analyze time spent in different heart rate zones.
3. **Power Curve Analysis**: Generate and visualize the power curve, which shows the maximum average power over various time intervals.

## Installation

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/ekg-power-analysis.git
   cd ekg-power-analysis
   
2. **Install Required Packages**
   Install the necessary Python packages using pip:
   ```sh
   pip install -r requirements.txt
   
## How to use

1. **Run the streamlit app**

   ```sh
   streamlit run main.py

2. **Navigate Through the Tabs**

   The application has three tabs:

### EKG-Data
**Description**: This tab allows you to visualize EKG data.  
**Usage**: Select an EKG file from the dropdown menu to plot the EKG data. The plot includes an interactive range slider for detailed examination.

### Power-Data
**Description**: This tab provides an interactive plot of power and heart rate data, along with a summary of power statistics and heart rate zone analysis.  
**Usage**:
- Enter the maximum heart rate in the input field. If no input is provided, the app uses the maximum heart rate from the data.
- View the power and heart rate plot. The time spent in each heart rate zone and the average power in each zone are displayed in columns.

### Power Curve
**Description**: This tab analyzes and visualizes the power curve, which represents the best average power over various time intervals.  
**Usage**:
- The power curve is automatically generated and plotted based on the power data.
- The x-axis is log-scaled, showing intervals from 1 second to 30 minutes. The y-axis represents the power in watts.
- The plot includes a shaded area under the curve for better visualization.

## Detailed Description of the Power Curve Analysis

The power curve provides insights into the best average power an individual can sustain over different time durations. Here's how it's calculated and visualized:

### Data Cleaning
The data is cleaned by removing any rows with NaN values in the `PowerOriginal` column.

### Rolling Mean Calculation
For each predefined time interval (ranging from 1 second to 30 minutes), the rolling mean of the power data is calculated. This rolling mean represents the average power over the specified interval.

### Maximum Average Power
The maximum value of the rolling mean for each interval is determined, representing the best effort for that duration.

### Plotting the Power Curve
The power curve is plotted using Plotly, with the x-axis representing the time intervals and the y-axis representing the average power. The x-axis is log-scaled to accommodate the wide range of intervals. The plot includes a shaded area under the curve to highlight the power values.

This detailed analysis allows athletes and trainers to understand performance capabilities over different timeframes, which can be crucial for training and performance optimization.
