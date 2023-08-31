#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df_tracks = pd.read_csv("C:/Users/maria/OneDrive/Desktop/Portfolio Project/Python Project/tracks.csv")
df_tracks.head() ## Display few rows


# In[5]:


pd.isnull(df_tracks).sum()
## diplay the null values


# In[6]:


df_tracks.info()

## information about the data


# In[7]:


sorted_df = df_tracks.sort_values('popularity', ascending = True).head(10)
sorted_df

## least 10 popularity songs ordered by popularity


# In[8]:


df_tracks.describe().transpose()

## numercial data for the table


# In[9]:


most_popular = df_tracks.query('popularity>90', inplace = False).sort_values('popularity', ascending = False)
most_popular[:10]

## Sort by most popular by popularity more than 90 in Desc order


# In[10]:


df_tracks.set_index("release_date", inplace = True)
df_tracks.index=pd.to_datetime(df_tracks.index)
df_tracks.head()

## Changing the format of release date into date time format


# In[11]:


df_tracks[["artists"]].iloc[18]

## To find the artist located at 18th row


# In[17]:


df_tracks["duration"]= df_tracks["duration_ms"].apply(lambda x: round(x/1000))
df_tracks.drop("duration_ms", inplace=True, axis=1)

##  convert the duration into from milliseconds to seconds and change the original dataset


# In[18]:


df_tracks.duration.head()


# In[19]:


corr_df=df_tracks.drop(["key","mode","explicit"],axis=1).corr(method="pearson")
plt.figure(figsize=(14,6))
heatmap=sns.heatmap(corr_df,annot=True,fmt=".1g", vmin=-1, vmax=1, center=0, cmap="inferno",linewidths=1, linecolor="Black")
heatmap.set_title("Correlation Heatmap between variable")
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=90)

## Creating a correlation heat map using Seaborn library


# In[20]:


sample_df = df_tracks.sample(int(0.004*len(df_tracks)))
print(len(sample_df))


# In[21]:


plt.figure(figsize=(10,6))
sns.regplot(data = sample_df, y = "loudness", x = "energy", color = "c").set(title = "Loudness vs Energy Correlation")


# In[22]:


plt.figure(figsize=(10,6))
sns.regplot(data = sample_df, y = "popularity", x = "acousticness", color = "b").set(title = "Popularity vs Acousticness Correlation")


# In[23]:


df_tracks['dates']=df_tracks.index.get_level_values('release_date')
df_tracks.dates=pd.to_datetime(df_tracks.dates)
years=df_tracks.dates.dt.year


# In[24]:


#pip install --userseaborn==0.11.0


# In[25]:


sns.displot(years,discrete=True,aspect=2,height=5,kind="hist").set(title="Number of songs per year")


# In[ ]:


# total_dr = df_tracks.duration
fig_dims = (18,7)
figs, ax = plt.subplots(figsize = fig_dims)
fig = sns.barplot(x = years, y = total_dr, ax = ax, errwidth = False).set(title="Year vs Duration")
plt.xticks(rotation=90)


# In[27]:


total_dr=df_tracks.duration
sns.set_style(style="whitegrid")
fig_dims = (10,5)
fig, ax = plt.subplots(figsize=fig_dims)
fig=sns.lineplot(x=years, y=total_dr, ax=ax).set(title="Year vs Duration")
plt.xticks(rotation=60)


# In[29]:


df_genre=pd.read_csv("C:/Users/maria/OneDrive/Desktop/Portfolio Project/Python Project/SpotifyFeatures.csv")


# In[30]:


df_genre.head()


# In[33]:


plt.figure(figsize=(10, 8))
plt.title("Duration of the Songs in different Genres")
sns.set_palette("rocket")
sns.barplot(y='genre', x='duration_ms', data=df_genre)
plt.xlabel("Duration in milliseconds")
plt.ylabel("Genres")
plt.show()


# In[34]:


sns.set_style(style="darkgrid")
plt.figure(figsize=(10,5))
famous = df_genre.sort_values("popularity", ascending=False).head(10)
sns.barplot(y='genre', x='popularity', data=famous).set(title="Top 5 Genres by Popularity")


# In[ ]:




