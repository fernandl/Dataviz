#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Libreries
import pandas as pd
import folium

# Load data 
df = pd.read_csv('C:/Users/lisbe/OneDrive/@PA/DATA VISUALIZATION/5. Lab 1 - Conduction Data Analysis/divvy_trip_history_201909-202108.csv')

print(df.columns)
print(df.shape)
print(df.head(5))

# Dataframe Divvy_trimmed
df_map = df.loc[: , ['ride_id', 'start_lat', 'start_lng','end_lat', 'end_lng', 'member_casual']]
df_map_member = df_map[df_map['member_casual']=='member']
df_map_casual = df_map.loc[df_map['member_casual']=='casual']

# df_map2 = df.loc[: , ['start_lat', 'start_lng']]

# Even after dropping unnecessary columns, this dataset is HUGE. And while that makes for a very robust map of the most common 
# combinations of start and end stations, throwing the entire dataframe through the visualization steps we will take next will bring
# (most) computers to their knees. You will want to take a random sample of the data at this point, just for expediency sake. 
# To do that, you can use thte sample_n() command below. Note that the number is the size of the sample, so you can change that depending 
# on your needs. You can always comment-out this line by adding a hashtag to it (#) later on should you want the full tortuous experience
# of visualizing what will eventually be 17 million Divvy datapoints. (Nota de Kevin)

df_map_sample = df_map.sample(n=1000)
df_map_member_sample = df_map.sample(n=1000)
df_map_casual_sample = df_map.sample(n=1000)


# In[ ]:


# df_map2_sample['start_lat'] = df_map2_sample.start_lat.astype(float)
# df_map2_sample['start_lng'] = df_map2_sample.start_lng.astype(float)


# In[9]:


map = folium.Map([41.9482, -87.6639], zoom_start=10)       


# In[4]:


cas = folium.map.FeatureGroup()
    


# In[7]:


for lat, long in zip(df_map_sample.start_lat, df_map_sample.start_lng):
    folium.CircleMarker(
    [lat, long],
    radius = 0.2,
    color = ('blue'),
    fill = True
    ).add_to(map)
    
map


# In[8]:


for lat, long in zip(df_map_sample.end_lat, df_map_sample.end_lng):
    folium.CircleMarker(
    [lat, long],
    radius = 0.2,
    color = ('magenta'),
    fill = True
    ).add_to(map)
    
map


# In[ ]:





# In[ ]:




