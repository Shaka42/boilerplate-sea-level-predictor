import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    res=linregress(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
    #creating first line of best fit
    x1=list(range(1880,2050))
    y1=[]
    for year in x1:
        y1.append(res.intercept+res.slope*year)
    #creating second line of best fit
    df2=df[df['Year']>=2000]
    res2=linregress(x=df2['Year'],y=df2['CSIRO Adjusted Sea Level'])
    x2=list(range(2000,2050))
    y2=[]
    for year in x2:
        y2.append(res2.intercept+res2.slope*year)
 
    plt.figure(figsize=(12,6))
    plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
    plt.xlim([1800,2100])
    plt.ylim([0,16])
    plt.plot(x1,y1,'r',label='first line')
    plt.plot(x2,y2,'green',label='Second line')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()