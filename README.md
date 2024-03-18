# Wind Power Forecasting in Colchester

## Overview
This project aims to model and forecast wind power production in Colchester using historical weather data. The script incorporates data cleaning, visualization, and time series analysis to analyse wind power generation and identify periods of energy surplus. This analysis is critical for optimizing the use of renewable energy resources and planning for free energy distribution.

## Author
- **Lesly Carolina Guerrero Vélez**
- University of Essex, Colchester
- Date: February 17, 2024


---

## Assumptions
For our wind power modeling, we focus on utilizing wind energy due to its significance as the largest source of renewable energy in the UK, as outlined on [Wikipedia](https://en.wikipedia.org/wiki/Wind_power_in_the_United_Kingdom#:~:text=Wind%20power%20is%20the%20largest,amount%20of%20thermal%20primary%20energy.). Given the incomplete data regarding solar variables, our analysis emphasizes wind power, leveraging the `windpowerlib` for modeling. 

The roughness length assumption is based on guidelines from the University of Wyoming's atmospheric science department, which can be found [here](http://www-das.uwyo.edu/~geerts/cwx/notes/chap14/roughness.html#:~:text=The%20'roughness%20length'%20zo,temperature%20times%20the%20roughness%20length.).

Our analysis is primarily based on the Earls Hall wind farm, located near Colchester. This farm operates five MM92 turbines, with a maximum energy production capacity of 10,275,000 W per hour. With a capacity factor of 30%, the farm's output is sufficient for approximately 10,000 homes, assuming a continuous operation model.

To be considered a surplus, the farm must generate over 3,082,500 W. We estimate the average household energy consumption at 308.25 W per hour. During hours of free energy, we anticipate a 20% increase in consumption, leading to an estimated usage of 370 W per hour. Peak hours are considered to be between 8 am and 10 pm, during which this increased consumption rate will apply, while non-peak hours will observe normal energy usage rates.

### Sources:
- [Earls Hall Wind Farm Overview](https://www.newenergyhub.com/earls-hall-wind-farm)
- [The Wind Power - Earls Hall Farm](https://www.thewindpower.net/windfarm_en_19254_earls-hall-farm.php)
- [BayWa r.e. - Earls Hall Farm Case](https://www.baywa-re.co.uk/en/cases-in-the-uk-and-ireland/earls-hall-farm)
- [Wind Power in the United Kingdom - Wikipedia](https://en.wikipedia.org/wiki/Wind_power_in_the_United_Kingdom)
- [Electricity Costs by Time of Day - MoneySuperMarket](https://www.moneysupermarket.com/gas-and-electricity/is-electricity-cheaper-at-night/#:~:text=When%20is%20peak%20time%20for,during%20the%20daytime%20and%20evening.)


## Preparing the Dataset

Before beginning the wind power forecasting analysis, it's essential to consolidate the raw weather data from multiple CSV files into two main files, one each for Colchester and Brighton. This preprocessing step is facilitated by the `load_data.py` script, which automates the combination of CSV files with the same prefix into a single CSV file for each location.

### Using the `load_data.py` Script

The `load_data.py` script is designed to merge several CSV files, each containing weather data for Colchester or Brighton, into two comprehensive CSV files. Here's a brief overview of how the script operates:

1. **Identify CSV Files**: The script searches the specified directory for CSV files with prefixes "brighton" and "colchester", segregating them based on their respective prefixes.

2. **Merge Logic**:
    - The script ensures the first row (usually headers) of the first file for each prefix is retained.
    - For subsequent files, it skips the first row if it's numeric and not the first file processed, preventing header duplication.
    - It handles special cases for files named "brighton_0001.csv" and "colchester_0001.csv" by not skipping any rows, assuming they're the initial files with necessary headers.

3. **Output**:
    - After processing, the script outputs two files: `brighton.csv` and `colchester.csv`, each containing combined data from their respective CSV files.

### Steps to Run the Script

1. **Prepare Your Environment**:
    - Ensure Python is installed on your system and you have access to the command line or terminal.
    - Place the `load_data.py` script in a directory that also contains a subdirectory named `data` with the raw CSV files.

2. **Execute the Script**:
    - Navigate to the directory containing the `load_data.py` script.
    - Run the script using the command:
      ```
      python load_data.py
      ```
    - The script will process the CSV files in the `data` folder and output the consolidated files `brighton.csv` and `colchester.csv` in the same folder.

### Requirements

- Python 3.x
- Access to a command-line interface

This script is the first step in preparing your data for the subsequent wind power forecasting analysis. After running this script, proceed with the main analysis script to clean, visualize, and model the wind power data as detailed in the sections above.

---

## Notebook Features
- Data cleaning and preprocessing of Colchester weather data.
- Visualization of historical wind power production.
- Decomposition of time series data to identify trends, seasonality, and residuals.
- Implementation of wind power modeling using the `windpowerlib` library.
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
2. **Wind Power Modeling:** Models the wind power production using weather data and the `windpowerlib`.
3. **Data Exploration:** Visualizes the cleaned data to identify patterns and trends.



To run the script, navigate to the directory containing the script and execute it in a Jupyter notebook environment or any Python interpreter that supports the necessary libraries.
