#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install ipython-sql')
import pandas as pd


# In[3]:


import sqlalchemy


# In[4]:


from sqlalchemy import create_engine
engine = create_engine('postgresql://himanshu:dudi@localhost:5432/mydatabase')


# In[5]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[6]:


get_ipython().run_line_magic('sql', 'sqlite://')


# In[7]:


get_ipython().run_line_magic('sql', 'sqlite:////Users\\him91\\Downloads\\data.sqlite')


# In[8]:


get_ipython().run_line_magic('sql', 'select * from international_debt limit 10;')


# In[9]:


get_ipython().run_cell_magic('sql', '', 'SELECT\nCount(DISTINCT country_name) AS total_distinct_countries\nFROM international_debt;')


# In[10]:


SELECT
Count(DISTINCT country_name) AS total_distinct_countries
FROM international_debt;


# In[ ]:


get_ipython().run_cell_magic('sql', '', 'SELECT\nCount(DISTINCT indicator_name) AS distinct_indicators\nFROM international_debt\nORDER BY distinct_indicators')


# In[ ]:


get_ipython().run_cell_magic('sql', '', 'SELECT ROUND(SUM(debt)/1000000, 2) AS total_debt \n \nFROM international_debt;')


# In[11]:


get_ipython().run_cell_magic('sql', '', 'SELECT country_name, SUM(debt) AS total_debt\nFROM international_debt\nGROUP BY country_name\nORDER BY total_debt DESC\nLIMIT 1;')


# In[12]:


get_ipython().run_cell_magic('sql', '', 'SELECT \n indicator_code AS debt_indicator,\n indicator_name,\n AVG(debt) AS average_debt\nFROM international_debt\nGROUP BY debt_indicator, indicator_name\nORDER BY average_debt DESC\nLIMIT 10;')


# In[18]:


get_ipython().run_cell_magic('sql', '', "SELECT country_name, indicator_name, debt\nFROM international_debt\nWHERE debt= (SELECT MAX(debt)\n FROM international_debt\n WHERE indicator_code ='DT.AMT.DLXF.CD'\n GROUP BY country_name, indicator_code \n ORDER BY MAX(debt) DESC\n LIMIT 1\n            )  ")


# In[21]:


get_ipython().run_cell_magic('sql', '', 'SELECT indicator_code, COUNT(indicator_code) AS indicator_count\nFROM international_debt\nGROUP BY indicator_code\nORDER BY indicator_count DESC')


# In[20]:


get_ipython().run_cell_magic('sql', '', 'SELECT country_name, indicator_code, MAX(debt) as maximum_debt\nFROM international_debt\nGROUP by country_name, indicator_code\nORDER BY maximum_debt DESC\nLIMIT 10;')


# In[ ]:




