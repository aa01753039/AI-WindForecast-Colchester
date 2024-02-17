# Wind Power Forecasting in Colchester

## Overview
This project aims to model and forecast wind power production in Colchester using historical weather data. The script incorporates data cleaning, visualization, and time series analysis to predict wind power generation and identify periods of energy surplus. This analysis is critical for optimizing the use of renewable energy resources and planning for energy distribution.

## Author
- **Lesly Carolina Guerrero Vélez**
- University of Essex, Colchester
- Date: February 17, 2024

## Features
- Data cleaning and preprocessing of Colchester weather data.
- Visualization of historical wind power production.
- Decomposition of time series data to identify trends, seasonality, and residuals.
- Implementation of wind power modeling using the `windpowerlib` library.
- Forecasting of wind power production to identify surplus periods.
- Analysis based on historical data spanning several years, focusing on hourly, daily, and monthly trends.

## Data
The dataset consists of historical weather data for Colchester, including wind speed, temperature, and atmospheric pressure. This data is used to model wind power production using the `windpowerlib` library. The analysis focuses on the Earls Hall wind farm's performance, which has Senvion MM92 turbines.

## Libraries Used
- pandas
- matplotlib
- plotly
- seaborn
- statsmodels
- numpy
- windpowerlib

## Installation
Ensure you have Python installed on your system. You will need to install the following packages:
```
pip install pandas matplotlib plotly seaborn statsmodels numpy windpowerlib
```

## Usage
The script is organized into multiple sections, each responsible for a step in the analysis:
1. **Data Cleaning:** Cleans the raw data for analysis.
2. **Data Visualization:** Visualizes the cleaned data to identify patterns and trends.
3. **Wind Power Modeling:** Models the wind power production using weather data and the `windpowerlib`.
4. **Forecasting:** Uses time series analysis to forecast future wind power production.

To run the script, navigate to the directory containing the script and execute it in a Jupyter notebook environment or any Python interpreter that supports the necessary libraries.
