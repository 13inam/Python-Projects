#!/usr/bin/env python
# coding: utf-8

# PYHTON PROGRAMS PT 1

# # GRADING SYSTEM

# In[3]:


##Assigning variable for user to input any number
a=float(input('enter a number'))
##first condition
if a>90:
    print('A+')    
##elif for multiple conditions
elif a>=80:
    print('A1')
elif a>=70:
    print('A')
elif a>=60:
    print('B')
elif a>=50:
    print('C')    
else:
    print('FAIL')


# # MATHEMATICAL TABLE

# In[5]:


##Assigning variable for user to input any number
a=int(input('enter a number'))
##using FOR LOOPS to generate table
for i in range(1,13):
    print(f'{a}*{i}={a*i}')
    


# In[ ]:





# In[ ]:




