
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:


data_input = './PeopleCountData.txt'
data_output = './PeopleCountData_wide.txt'


# In[3]:


def reshape_toWide(data_input, data_output):

    column_names = ['date','time','ip','entrypoint','incoming','outgoing']
    data_raw = pd.read_csv(data_input,names=column_names)
    
    data = data_raw.copy()
    data['timestamp'] = pd.to_datetime(data.date+' '+data.time)

    columns_values = ['incoming', 'outgoing']

    data_wide = data.pivot_table(values = columns_values,
                                 index = ['timestamp'],
                                 columns = 'entrypoint',
                                 aggfunc = 'mean').diff()

    data_wide.columns = ['_'.join(t) for t in data_wide.columns]
    data_wide.fillna(0,inplace=True)
    
    return(data_wide)


# In[4]:


data_wide = reshape_toWide(data_input,data_output)


# In[5]:


data_wide.head(5)


# In[6]:


data_wide.to_csv(path_or_buf=data_output, sep='|')