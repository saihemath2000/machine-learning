#!/usr/bin/env python
# coding: utf-8

# In[64]:


#write a python script to concatenate the following dictionaries to create a new one
dict1={'1':10,'2':20}
dict2={'3':30,'4':40}
dict3={'5':50,'6':60}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)


# In[65]:


#write a python script to check if a given key already exists in a dictionary
dict1.__contains__('1')


# In[66]:


#write a  python script to print a dictionary where the keys are numbers between 1 and 15(both included) and the values are square of keys.
dict4={}
for i in range(1,16):
    dict4[i]=i*i
print(dict4)    


# In[70]:


#write a python program to remove duplicates from dictionary
temp=[]
res=dict()
for key,val in dict4.items():
    if val not in temp:
        temp.append(val)
        res[key]=val
print(dict4)        
           
        


# In[72]:


#write a python program to create nd display all combination of letters,selecting each letter from a different key in a dictionary.
import itertools      
d ={'1':['a','b'], '2':['c','d']}
for i in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(i))
	


# In[77]:


#write a python program to create a dictionary from a string.
dict5={}
samplestring='w3resource'
list1=list(samplestring)
#print(len(list1))
n = len(samplestring)
for i in samplestring:
    dict5[i]=list1.count(i)
print(dict5)    
    
    


# In[88]:


#write a python program to sort counter by value
dict6={'Math':81,'Physics':83,'Chemistry':87}
print(sorted([(k,v) for k,v in dict6.items()]))

