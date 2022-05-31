import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  plt.figure(1, figsize = (10, 10))
  plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color = 'blue', linewidths=1)

  # Create first line of best fit
  regression = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  years = range(df['Year'].min(), 2051)
  plt.plot(years, regression.intercept + regression.slope * years, color = 'red')

  # Create second line of best fit
  regression = linregress(df[df['Year'] >= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
  years = range(2000, 2051)
  plt.plot(years, regression.intercept + regression.slope * years, color = 'green')

  # Add labels and title
  plt.title('Rise in Sea Level')
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
    
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()