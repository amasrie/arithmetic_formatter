import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Clean data
df = df.drop(df[(df['value'] < df['value'].quantile(0.025)) | (df['value'] > df['value'].quantile(0.975))].index)


def draw_line_plot():
  # Draw line plot
  fig, ax = plt.subplots(figsize=(12, 8))
  plt.plot(df)
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  plt.xlabel('Date')
  plt.ylabel('Page Views')

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar["year"] = df_bar.index.year
  df_bar["month"] = df_bar.index.month_name()  
  df_bar = df_bar.groupby(by=["year", "month"], sort=False).value.mean()
  df_bar = df_bar.reset_index()
  for month in ['April', 'March', 'February', 'January']:
    df_bar = pd.concat([pd.DataFrame({'year': [2016], 'month': [month], 'value': [0]}), df_bar])  

  # Draw bar plot
  fig, ax = plt.subplots(figsize=(10, 10))
  sns.barplot(data=df_bar, x="year", y="value", hue="month").set(xlabel='Years', ylabel='Average Page Views')
  plt.legend(title='Months')

    # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))
  sns.boxplot(x='year', y='value', data=df_box, ax=ax1).set(title='Year-wise Box Plot (Trend)', xlabel='Year', ylabel='Page Views')
  sns.boxplot(x='month', y='value', data=df_box, ax=ax2, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']).set(title='Month-wise Box Plot (Seasonality)', xlabel='Month', ylabel='Page Views')

  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
