#!/usr/bin/env python
# coding: utf-8

# # Identifying Patient Cohorts in [MIMIC-II](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3124312/)
# 

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import pymysql
import pandas as pd
import getpass
import pandas as pd
import seaborn as sns
import datetime
import time
import matplotlib.pyplot as plt


# In[3]:


conn = pymysql.connect(host="mysql",
                       port=3306,user="jovyan",
                       passwd=getpass.getpass("Enter MySQL passwd for jovyan"),db='mimic2')
cursor = conn.cursor()


# In[4]:


mimic2Adm = pd.read_sql("""SELECT * FROM admissions LIMIT 100""", conn)


# In[5]:


mimic2Adm.head()


# ## Exercise: Create a Histogram of the length of stay for subjects in the database

# In[6]:


mimic2Adm["LOS"] = mimic2Adm.apply(lambda row: (row["disch_dt"] - row["admit_dt"]).days, axis = 1)
mimic2Adm.head()


# In[7]:


mimic2Adm.LOS.plot.hist()


# In[8]:


mimic2Adm.LOS.describe()


# ## Exercise: Create a histogram of the day of the week when patients are admitted

# In[18]:


mimic2Adm["AdmDaysOnWeek"] = mimic2Adm.apply(lambda row: int(time.strftime("%w", row["admit_dt"].timetuple())), axis = 1)


# In[19]:


mimic2Adm.head()


# In[22]:


mimic2Adm.AdmDaysOnWeek.plot.hist()


# In[23]:


mimic2Adm.AdmDaysOnWeek.describe()

