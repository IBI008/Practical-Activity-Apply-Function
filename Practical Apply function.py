#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Pandas and Numpy.
import pandas as pd
import numpy as np


# In[2]:


# Load the excel data using the pd.read_excel
movies = pd.read_excel('movies_merge.xlsx')

# Load the csv data using the pd.read_csv
ott = pd.read_csv('ott_merge.csv')

# Data imported correctly?
print(movies.columns)
print(movies.shape)
print(ott.columns)
print(ott.shape)


# In[3]:


# Merge the two DataFrame.
mov_ott = pd.merge(movies, ott, how='left', on='ID')

# View the DataFrame
print(mov_ott.columns)
print(mov_ott.shape)


# In[5]:


# What is the effect of adding 60seconds to each movie
# Determine the runtime of each movie
mov_ott_runtime = mov_ott[['ID','Runtime','Genres']]

# View the DataFrame
mov_ott_runtime


# In[6]:


# Add seconds or 1min to the runtime.
mov_ott_runtime['Runtime'].add(1)


# In[7]:


# Question two
# Which movies were documentaries

mov_ott_runtime['Gen_doc'] = np.where(mov_ott_runtime['Genres'].str.contains('Documentary'), 'Documentary', 'Not Documentary' )

# View the DataFrame
mov_ott_runtime


# In[8]:


# Use the applymap (determine the length of string).
mov_ott_runtime.Gen_doc.apply(len)


# In[9]:


# Challenge
# Determine the original runtime
mov_ott_runtime[['ID','Runtime']]


# In[10]:


# Subtract 0.01 from the runtime
mov_ott_runtime['Runtime'].subtract(0.01)


# In[11]:


# Try lambda function.
mov_ott['Runtime'] = mov_ott['Runtime'].apply(lambda x: x + 1)

# View output
mov_ott['Runtime']


# In[ ]:




