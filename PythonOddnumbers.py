

##python code
def even_numbers(list_a):
    list_b = list(filter(lambda x: x%2 != 0,list_a))
    return list_b


# In[6]:


x = [1,2,3,4,5,6,7,8,9,10]
y = even_numbers(x)


# In[7]:


print(y)


# In[ ]:




