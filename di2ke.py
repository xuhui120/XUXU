#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[36]:


import csv


# In[37]:


p=r"C:\Users\Administrator\Desktop\iris.csv"


# In[38]:


with open(p,encoding="utf-8") as f:
    iris=np.loadtxt(f,delimiter=",")  #如果CSV里有字符，最好是F.STR
    print(iris[:])


# In[39]:


max=np.argmax(iris)
print(max)


# In[40]:


min=np.argmin(iris)
print(min)


# In[41]:


iris.sort()
print(iris)


# In[42]:


a=np.unique(iris)
print(a)


# In[43]:


c=np.mean(b)
print(b)
print(c)


# In[44]:


var=np.var(b)
print(var)


# In[45]:


std=np.std(b)
print(std)


# In[46]:


sm=sum(b)
print(sm)


# In[47]:


ljsm=np.cumsum(b)
print(ljsm)


# In[48]:


tj=(b>5.84).sum()
print(tj)

