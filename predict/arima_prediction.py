
# coding: utf-8

# In[204]:


##load data
import prepare
import importlib
path = 'data/business.xls'
business = prepare.loadDataSet(path)


# In[202]:


test = pd.read_excel(path)


# In[203]:


test.head()


# In[276]:


business.tail(7)


# In[207]:


##get daylist
importlib.reload(prepare)
datelist = prepare.get_datelist('2015-09-28','2017-10-16')


# In[208]:


len(datelist)-len(business)


# In[209]:


import pandas as pd
new_business = pd.merge(datelist,business,how='outer')
new_business.fillna(0,inplace = 'true')
print(new_business[new_business['rentNumber']==0])


# In[210]:


new_business[new_business['rentNumber']==0]


# In[215]:


##get daylist
importlib.reload(prepare)
df = prepare.month_data(business)
prepare.plot_monthdata(df)


# In[216]:


prepare.plot_daydata(business)


# In[222]:


##generate data
data_list =  [1,3,4,5,3,1,3,6,7,5,4,2,3,5,7,8,9]
gen = pd.DataFrame({'rentNumber':data_list})
prepare.plot_monthdata(gen)


# In[223]:


import numpy as np
business_copy = business.copy()
business_copy['rentNumber'] = np.log(business_copy.rentNumber)


# In[224]:


##stationarity test,测试样本7
prepare.stationarity_test(business_copy,7)


# In[225]:


##whitenoise_test
prepare.whitenoise_test(business_copy,7)


# In[264]:


##acf、pacf
importlib.reload(prepare)
prepare.plot_acfandpacf(business_copy)


# In[291]:


##predict
importlib.reload(prepare)
import numpy as np
pred, RMSE=prepare.arma_predict(business_copy,21)


# In[292]:


np.exp(pred).astype(int)


# In[293]:


RMSE

