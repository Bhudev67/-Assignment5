#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Import Python Libraries
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


df = pd.read_csv('./youtube_dataset.csv', encoding='latin-1')
df


# In[7]:


#show data from dataset
df.head()


# In[8]:


#get dataset information
df.info()


# In[9]:


#Creating a function to calculate the distribution of top 1000 records and loading dataset to new CSV

df['channeltype'] = df['channeltype'].astype('|S')
df1=df.head(1000)
df_count= df1['channeltype'].value_counts()
def histogram_function():
    print(df_count)
    fig=plt.figure(figsize=(20,20))
   
    plt.hist(df1['channeltype'],bins=15)
    plt.gca().set(title='Frequency Histogram of Channel Type', ylabel='Frequency')


# In[10]:


histogram_function()


# In[11]:


#exporting 1000 records to a new csv file
df1.to_csv('1000_records.csv')


# In[ ]:




