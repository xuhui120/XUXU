#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np


# In[21]:


from numpy import float64


# In[57]:


import random


# In[61]:


import matplotlib.pyplot as plot


# In[62]:


arr1=np.array(([1,2],[3,4]),dtype= np.float)


# In[63]:


print(arr1)


# In[64]:


arr2 = np.zeros((6,6))


# In[65]:


print(arr2)


# In[66]:


arr3=np.ones((6,6))


# In[67]:


print(arr3)


# In[68]:


arr4= np.eye((6))


# In[69]:


print(arr4)


# In[70]:


arr5=np.arange(0,10,2)


# In[71]:


print(arr5)


# In[72]:


arr6=np.linspace(0,10,6)


# In[73]:


print(arr6)


# In[74]:


a=np.arange(0,10,1)


# In[75]:


print(a)


# In[76]:


print(type(a))


# In[77]:


b=np.argmax(a,axis=0)


# In[78]:


print(b)


# In[51]:


a[b]=0


# In[52]:


print(a)


# In[53]:


x=np.array([1,2,3,2,3,4,3,4,5,6])


# In[54]:


y=np.array([7,2,10,2,7,4,9,4,9,8])


# In[55]:


dist=np.sqrt(np.sum(np.square(x-y)))


# In[56]:


print(dist)


# In[58]:


np.random.seed(1)


# In[89]:


values=np.random.randn(1000).cumsum()


# In[90]:


print(values)


# In[91]:


plot.plot(values)


# In[87]:


pl


# In[ ]:




