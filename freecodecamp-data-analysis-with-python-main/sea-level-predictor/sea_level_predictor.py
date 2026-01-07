import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
  # Read data from file
  df = pd.read_csv('.\sea-level-predictor\epa-sea-level.csv')

  # Create scatter plot
  # Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
  plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

  # Create first line of best fit
  # Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
  line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  x = np.arange(df['Year'].min(), 2051, 1)
  y = line.slope * x + line.intercept
  plt.plot(x, y)

  # Create second line of best fit
  # Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
  df_from2000 = df[df['Year'] >= 2000]
  line = linregress(df_from2000['Year'],
                    df_from2000['CSIRO Adjusted Sea Level'])
  x = np.arange(df_from2000['Year'].min(), 2051, 1)
  y = line.slope * x + line.intercept
  plt.plot(x, y)

  # Add labels and title
  # The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.
  plt.title('Rise in Sea Level')
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
