#!/usr/bin/env python
# coding: utf-8

# # US Accidents Exploratory Data Analysis

# ### Downloading the Data

# In[1]:


# downloading opendatasets
# creating new API key on Kaggle to access dataset
get_ipython().system('pip install opendatasets')
import opendatasets as od
od.download("https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents")


# In[2]:


data_filename = './us-accidents/US_Accidents_Dec21_updated.csv'


# ### Data Preparation / Cleaning

# In[3]:


# Steps I will be doing: 
# Load file
# Explore dataset by investigating columns
# Fix data discrepancies / incorrect values


# In[4]:


# importing modules
import pandas as pd
import numpy as np
import seaborn as sns
sns.set_style("darkgrid") # setting style of grid
cm = sns.light_palette("purple",as_cmap=True)
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv(data_filename)


# In[6]:


df


# In[7]:


# exploring what columns represent in our dataset
df.columns


# In[8]:


df.info()
# total 2845342 records
# 47 columns - boolean and numerical


# In[9]:


# quick overview of aggregated statistics of dataframe
df.describe()


# In[11]:


# Wanted to know how much numeric data I would work with
numerics = ['int16','int32','float16','float32','float64']
numeric_df = df.select_dtypes(include=numerics)
len(numeric_df.columns)


# In[12]:


# Counting number of missing values per column
df.isna().sum()


# In[13]:


isnull = df.isnull().sum().sort_values(ascending=False).to_frame()
isnull.columns = ['Counts']
isnull['percentage'] = np.around(((isnull / len(df) * 100)[(isnull / len(df) * 100) != 0]), decimals = 2)
isnull[isnull.Counts > 0].style.background_gradient(cmap=cm)


# ### Let's investigate states!

# In[14]:


State = df.State.value_counts().reset_index()
State.columns = ['State','Accidents']
State.head()


# In[15]:


State['Percentage'] = round(State['Accidents'] * 100 / State['Accidents'].sum() , 2)
State.head()


# In[16]:


# top ten states with the most occurring accidents from 2016 to 2021
# the most accident prone state is California!
plt.figure(figsize=(18,9))
graph = plt.bar(State.State.head(10),State.Accidents.head(10),
               color=('#C09ADB','#825B97','#825B97','#825B97','#825B97',
                      '#825B97','#825B97','#825B97','#825B97','#825B97'))
plt.title('Percentage of Accidents Across Top 10 States',ha='center',weight='bold')
plt.xlabel("State",ha='center',weight='bold')
plt.ylabel("Number of Accidents",ha='center',weight='bold')
 
i = 0
for p in graph:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    plt.text(x+width/2,
             y+height*1.01,
             str(State.Percentage[i])+'%',
             ha='center',
             weight='bold')
    i+=1
plt.show()


# In[17]:


# plotting chloropleth map to showcase accidents per state across the country
import plotly.express as px
fig = px.choropleth(State, locationmode= 'USA-states',locations='State', color='Accidents',
                           color_continuous_scale="Viridis",
                           range_color=(0, 800000),
                           scope="usa",
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# ### Let's investigate some timestamps!

# In[18]:


# investigating start time column
df.Start_Time


# In[19]:


import warnings
warnings.filterwarnings('ignore')


# In[20]:


# converting string to datetime type
df.Start_Time = pd.to_datetime(df.Start_Time)
df.Start_Time


# In[21]:


# checking value output of column after conversion
df.Start_Time[0]


# In[22]:


# What time of day are accidents most frequently occurring?
# Which days of the week have the most accidents?
# Which months have the most accidents?
# What is trend of accidents over the years?


# In[23]:


# plotting accidental frequencies per hour from 2016 to 2021
# highest count of accidents around rush hour --> most likely when people are commuting back from work
# bimodal distribution with two peaks both at rush hours or commuting hours to and from work
sns.histplot(pd.to_datetime(df.Start_Time).dt.hour, bins=24)


# In[24]:


# plotting accidental frequencies as percentages per hour from 2016 to 2021
sns.distplot(pd.to_datetime(df.Start_Time).dt.hour, norm_hist=True)


# In[25]:


# investigating day of the week accidents occurred the most
# note that monday = 0 and sunday = 6
sns.distplot(pd.to_datetime(df.Start_Time).dt.day_of_week, norm_hist=True)

# interestingly, seems that the most accidents occur on Fridays
# there are a lot less accidents on Sat and Sundays


# In[26]:


# is the distribution of accidents per hour similar to the distribution on the weekends? 
weekend_hours = df.Start_Time[(df.Start_Time.dt.day_of_week == 5) | (df.Start_Time.dt.day_of_week == 6)].dt.hour
weekend_hours


# In[27]:


# plotting accidents per hour on saturdays and sundays
# on the weekend, there were more accidents during the afternoon and midnight
sns.distplot(weekend_hours,norm_hist=True)


# In[28]:


# distribution of accidents per hour over the weekdays, not weekend
weekday_hours = df.Start_Time[(df.Start_Time.dt.day_of_week != 5) & (df.Start_Time.dt.day_of_week != 6)].dt.hour
weekday_hours


# In[29]:


# plotting accidents per hour on weekdays
# accidents were more likely to occur in the late afternoon hours (~3pm to evening)
# this can most likely be attributed to commuting hours from work to home
sns.distplot(weekday_hours,norm_hist=True)

# compared to the weekends, there are more accidents during the morning commuting hours (~6AM - 8AM)


# In[30]:


# are there more accidents in certain months?
# more accidents occurred toward the end of the year
# the most = december
sns.distplot(df.Start_Time.dt.month,norm_hist=True)


# In[31]:


# which year had the most accidents? 
sns.histplot(df.Start_Time.dt.year)

# 2021 had the most accidents
# surprisingly, 2020 had a lot of accidents given that the pandemic took over the states and caused lockdowns
# should look into 2020 more


# In[33]:


# separating data into subsets of 2020 + 2021 when COVID hit the states
df['Year'] = df['Start_Time'].dt.year
df['Month'] = df['Start_Time'].dt.month
data_2020 = df[(df['Year'] == 2020)]
data_2021 = df[(df['Year'] == 2021)]


# In[34]:


Year = df.Year.value_counts().reset_index()
Year.columns = ['Year','Accidents']
Year.head()


# In[35]:


# plotting to see the distribution of accidental frequencies from 2020
fig, ax = plt.subplots(figsize = (10,5))
c = sns.countplot(x="Month", data=data_2020, orient = 'v', palette = "flare")
c.set_title("No. of Accidents in 2020")
plt.show()


# In[36]:


# plotting to see the distribution of accidental frequencies from 2021
fig, ax = plt.subplots(figsize = (10,5))
c = sns.countplot(x="Month", data=data_2021, orient = 'v', palette = "flare")
c.set_title("No. of Accidents in 2021")
plt.show()


# In[37]:


# plotting accidents to see freqencies as detailed overview from 2020
fig, ax = plt.subplots(figsize = (15,5))
c = sns.countplot(x=data_2020.Start_Time.dt.isocalendar().week, data=data_2020, orient = 'v', palette = "flare")
c.set_title("No. of Accidents in 2020")
plt.show()


# ### Let's investigate cities!

# In[38]:


# investigating city column
cities = df.City.unique()
len(cities) # 11,682 unique cities included in data set!


# In[39]:


cities_by_accident = df.City.value_counts()
cities_by_accident[:20] # looking at top 20 cities with most accidents


# In[40]:


# plotting barchart of top 20 cities with the most accidents
cities_by_accident[:20].plot(kind='barh')


# In[41]:


sns.distplot(cities_by_accident)


# In[42]:


# separating cities into high and low buckets in terms of # of accidents
high_accident_cities = cities_by_accident[cities_by_accident >= 1000]
low_accident_cities = cities_by_accident[cities_by_accident <= 1000]


# In[43]:


# there are a little over 4% of cities that have more than 1,000 yearly accidents
len(high_accident_cities) / len(cities)


# In[44]:


# cities with high number of yearly accidents
sns.distplot(high_accident_cities)


# In[45]:


# cities with low number of yearly accidents
sns.distplot(low_accident_cities)


# In[46]:


# number of accidents per city seems to decrease/increase exponentially
# will have to shift to log scale
sns.histplot(cities_by_accident, log_scale=True) # enabling log scale

# about 1000+ cities have reported 1 accident only


# In[47]:


# checking values with graph above
cities_by_accident[cities_by_accident == 5]


# In[ ]:




