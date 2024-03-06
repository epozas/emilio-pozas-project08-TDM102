import pandas as pd
myDF = pd.read_parquet('/anvil/projects/tdm/data/whin/weather.parquet')
pd.set_option('display.max_columns', None)
myDF.head()
myDF['observation_time'] = pd.to_datetime(myDF['observation_time'])
myDF['year'] = myDF['observation_time'].dt.year
myDF['month'] = myDF['observation_time'].dt.month
myDF['day'] = myDF['observation_time'].dt.day
myDF.head()
myDF['station_id'].value_counts()
my_station_id = 1
myDF[myDF['station_id'] == my_station_id].groupby(['year','month'])['temperature'].mean()
my_station_id = 3
myDF[myDF['station_id'] == my_station_id].groupby(['year','month'])['temperature'].mean()
my_station_id = 5
myDF[myDF['station_id'] == my_station_id].groupby(['year','month'])['temperature'].mean()
def get_avg_temp(station_id = int): 
    return(myDF[myDF['station_id'] == station_id].groupby(['year','month'])['temperature'].mean())

get_avg_temp(5)
get_avg_temp(129)
get_avg_temp(3)

import matplotlib.pyplot as plt

get_avg_temp(1).unstack(0).plot(kind ='line', marker='o')
plt.title(f'Average monthly temperatures for given station_id and all month-and-year pairs')
plt.xlabel('Month')
plt.ylabel('Average Temperatures')
plt.xticks(range(1,13), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.legend(title= 'Year')
plt.grid(True)
plt.show

def plot_avg_temp_per_year(station_id): 
    get_avg_temp(station_id).unstack(0).plot(kind ='line', marker='o')
    plt.title(f'Average monthly temperatures for given station_id and all month-and-year pairs')
    plt.xlabel('Month')
    plt.ylabel('Average Temperatures')
    plt.xticks(range(1,13), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    plt.legend(title= 'Year')
    plt.grid(True)
    plt.show
plot_avg_temp_per_year(1)

myDF[myDF['station_id'] == 1].groupby(['year','month'])['temperature'].max()
myDF[myDF['station_id'] == 5].groupby(['year','month'])['temperature'].max()

def get_max_temp(station_id = int): 
    return(myDF[myDF['station_id'] == station_id].groupby(['year','month'])['temperature'].max())
get_max_temp(1)
get_max_temp(5)

def plot_max_temp_per_year(station_id): 
    get_max_temp(station_id).unstack(0).plot(kind ='bar')
    plt.title(f'Maximum monthly temperatures for given station_id and all month-and-year pairs')
    plt.xlabel('Month')
    plt.ylabel('Maximum Temperatures')
    plt.xticks(range(0,12), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    plt.legend(title= 'Year')
    plt.grid(True)
    plt.show

plot_max_temp_per_year(1)
plot_max_temp_per_year(5)

myDF[(myDF['station_id'] == 1)&(myDF['year']==2020)].shape
myDF[(myDF['station_id'] == 1)&(myDF['year']==2020)].boxplot(column = 'wind_speed_mph',by = 'month')
myDF[(myDF['station_id'] == 5)&(myDF['year']==2020)].boxplot(column = 'wind_speed_mph',by = 'month')
def boxplot_windspeeds_by_month(station_id=int,year=int):
    myDF[(myDF['station_id'] == station_id)&(myDF['year']==year)].boxplot(column = 'wind_speed_mph',by = 'month')
    plt.title(f'Monthly Wind Speeds at the station {station_id} and {year}')
    plt.xlabel('Month')
    plt.ylabel('Wind Speed (in mph)')
    plt.show()

boxplot_windspeeds_by_month(1,2021)
boxplot_windspeeds_by_month(1,2020)

myDF.head()
myDF[myDF['station_id'] == 5].groupby(['year','month'])['humidity'].max()
def get_max_humidity(station_id = int): 
    return(myDF[myDF['station_id'] == station_id].groupby(['year','month'])['humidity'].max())
  
get_max_humidity(5).unstack(0).plot(kind ='bar')
plt.title(f'Maximum monthly humidity for given station_id and all month-and-year pairs')
plt.xlabel('Month')
plt.ylabel('Maximum Humidity')
plt.xticks(range(0,12), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.legend(title= 'Year')
plt.grid(True)
plt.show

def plot_max_humidity_per_year(station_id): 
    get_max_humidity(station_id).unstack(0).plot(kind ='bar')
    plt.title(f'Maximum monthly humidity for given station_id and all month-and-year pairs')
    plt.xlabel('Month')
    plt.ylabel('Maximum Humidity')
    plt.xticks(range(0,12), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    plt.legend(title= 'Year')
    plt.grid(True)
    plt.show
    
plot_max_humidity_per_year(5)

def get_avg_humidity(station_id = int): 
    return(myDF[myDF['station_id'] == station_id].groupby(['year','month'])['humidity'].mean())
  
get_avg_humidity(5).unstack(0).plot(kind ='line', marker='o')
plt.title(f'Average monthly humididty for given station_id and all month-and-year pairs')
plt.xlabel('Month')
plt.ylabel('Average Humidity')
plt.xticks(range(1,13), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.legend(title= 'Year')
plt.grid(True)
plt.show

def plot_avg_humidity_per_year(station_id): 
    get_avg_humidity(station_id).unstack(0).plot(kind ='line', marker='o')
    plt.title(f'Average monthly humididty for given station_id and all month-and-year pairs')
    plt.xlabel('Month')
    plt.ylabel('Average Humidity')
    plt.xticks(range(1,13), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    plt.legend(title= 'Year')
    plt.grid(True)
    plt.show

plot_avg_humidity_per_year(5)