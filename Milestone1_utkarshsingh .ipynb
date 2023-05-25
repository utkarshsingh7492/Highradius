#!/usr/bin/env python
# coding: utf-8

# # Utkarsh Singh

# # Milestone 1 - Data Sanity(by using Numpy and Pandas

# In[1]:


import numpy as np
import pandas as pd


# # Use the PRS dataset to create a dataframe

# In[3]:


df=pd.read_csv("Final.csv")


# # Check the description of the dataframe

# In[41]:


df.describe()


# # check the shape of the dataframe

# In[7]:


df.shape


# # check the dataframe informations

# In[9]:


df.info


# # check for the null values in the dataframe

# In[11]:


df.isnull().sum()


# # Replace all the null values with "NaN"

# In[14]:


df.fillna("NaN",inplace=True)


# # Change the format of date columns - "ORDER_CREATION_DATE" to datetime[64] with the format as "%Y%m%d"

# In[16]:


df["ORDER_CREATION_DATE"] = pd.to_datetime(df["ORDER_CREATION_DATE"], format="%Y%m%d")
df[:5]


# # Do the same activity for the other date field i.e. "REQUESTED_DELIVERY_DATE" to datetime[64] with the format as "%Y%m%d"
# 

# In[18]:


df["REQUESTED_DELIVERY_DATE"] = pd.to_datetime(df["REQUESTED_DELIVERY_DATE"], format="%Y%m%d")
df[:5]


# # Sanity check - Check how many records are having order date greater than the delivery date

# In[20]:


(df["ORDER_CREATION_DATE"]>df["REQUESTED_DELIVERY_DATE"]).sum()


# # Remove those records where order date is greater than the delivery date

# In[22]:


df.drop(df[df['ORDER_CREATION_DATE'] > df['REQUESTED_DELIVERY_DATE']].index,inplace=True)
df.shape


# # Check the number of records where the “ORDER_AMOUNT” field is having “-” in it.

# In[24]:


df["ORDER_AMOUNT"].str.contains("-").sum()


# # Replace “-” with “” from the “ORDER_AMOUNT” field.

# In[26]:


df["ORDER_AMOUNT"] = df["ORDER_AMOUNT"].str.replace("-", "")


# # Check the number of records where the “ORDER_AMOUNT” field is having “,” in it.

# In[28]:


df["ORDER_AMOUNT"].str.contains(",").sum()


# # Replace “,” with “.” from the “ORDER_AMOUNT” field.

# In[30]:


df["ORDER_AMOUNT"] = df["ORDER_AMOUNT"].str.replace(",", ".")


# # Count the number of records where the order date and the delivery date are same

# In[32]:


(df["ORDER_CREATION_DATE"]==df["REQUESTED_DELIVERY_DATE"]).sum()


# # Count the number of records for each currency type by using the field “'ORDER_CURRENCY'”

# In[34]:


df['ORDER_CURRENCY'].value_counts()


# # Create a new column in the existing dataframe as “'amount_in_usd'” and convert all the non-USD currencies in USD and store them in the same column. 

# In[36]:


conversion_rates = {
    'USD': 1.0,
    'EUR': 1.08,
    'AUD': 0.66,
    'CAD': 0.74,
    'GBP': 1.24,
    'MYR': 0.22,
    'PLN': 0.24,
    'AED': 0.27,
    'HKD': 0.13,
    'CHF': 1.11,
    'RON': 0.22,
    'SGD': 0.74,
    'CZK': 0.046,
    'HU1': 0.0028,
    'NZD': 0.61,
    'BHD': 2.65,
    'SAR': 0.27,
    'QAR': 0.27,
    'KWD': 3.25,
    'SEK': 0.094
}
df['amount_in_usd'] = df.apply(lambda row: float(row['ORDER_AMOUNT'])*conversion_rates.get(row['ORDER_CURRENCY']), axis=1)
df[:5]


# # Check for values “0” in the “'amount_in_usd” column. 
# 

# In[38]:


(df["amount_in_usd"]==0).sum()


# # Create a new column in the existing dataframe “unique_cust_id” by adding 'CUSTOMER_NUMBER' and 'COMPANY_CODE'
# 

# In[40]:


df['unique_cust_id'] = df.groupby(['CUSTOMER_NUMBER', 'COMPANY_CODE']).ngroup()
df


# In[ ]:




