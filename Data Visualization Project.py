#!/usr/bin/env python
# coding: utf-8

# In[28]:


import matplotlib.pyplot as plt
plt.style.available


# In[29]:


input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
x_values = range(1,10001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.scatter(x_values,y_values, c=y_values, cmap=plt.cm.Blues,s=10)


#Set chart title and label axes.
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 24)
ax.set_ylabel("square of Value", fontsize = 14)
ax.tick_params(labelsize=14)

#Set the range for each axis
ax.axis([0,1100,0,1_100_000])
ax.ticklabel_format(style='plain')

plt.savefig('squares_plot.png',bbox_inches = 'tight')

