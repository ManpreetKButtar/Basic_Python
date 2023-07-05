#!/usr/bin/env python
# coding: utf-8

# ---
# ---
# 
# <center><h1>📍 📍 String Manipulation 📍 📍</h1></center>
# 
# ---

# ***Define a string***
# 
# ---

# In[2]:


my_string = "Analytics Vidhya creating next generation data science eco-system"


# ***Length of the string***
# 
# ---

# In[3]:


len(my_string)


# ***Access characters in a string***
# 
# ---

# In[4]:


my_string[0]


# In[5]:


my_string[3]


# ***Access characters with negative indexing***
# 
# ---

# In[6]:


my_string[-1]


# ***String Slicing***
# 
# ---

# In[7]:


my_string[1:3]


# In[8]:


my_string[10:-10]


# In[8]:


# reverse a string

my_string[::-1]


# ***Count of a particular `character` or a `sub-string` in a string.***
# 
# ---

# In[9]:


my_string


# In[10]:


my_string.count('a')


# In[11]:


my_string.count('A')


# In[12]:


my_string[10:-10]


# In[13]:


my_string[10:-10].count('a')


# In[14]:


my_string.count('en')


# ***Find a substring in the string using `find` and `index` function.***
# 
# **`find`**
# 
# * If present it will return the starting index.
# * If not found, then it will return -1
# 
# ---

# In[15]:


my_string.find('next')


# In[16]:


my_string.find('python')


# **`index`**
# 
# * If present it will return the starting index.
# * If not found, then it will give error

# In[17]:


my_string.index('next')


# In[18]:


my_string.index('python')


# ***Check whether if the string `startswith` or `endswith` a particular substring or not.***
# 
# ---

# In[19]:


my_string


# In[20]:


my_string.endswith('python')


# In[21]:


my_string.endswith('system')


# In[22]:


my_string.startswith('python')


# In[23]:


my_string.startswith('analytics')


# ***Convert the string to the upper case.***
# 
# ---

# In[24]:


my_string


# In[25]:


my_string.upper()


# ***Capitalize: Update the first character of the string to upper case***
# 
# 
# ---

# In[26]:


my_string.capitalize()


# In[27]:


# proper case


# ***Check if the string is in lower case or upper case.***
# 
# ---

# In[28]:


my_string.islower()


# In[29]:


my_string.isupper()


# ***Check if the string is digit, alpabetic, alpha-numeric.***
# 
# ---

# In[30]:


"10".isnumeric()


# In[31]:


"1213as".isnumeric()


# In[32]:


"python".isalpha()


# In[33]:


"1212as".isalpha()


# In[34]:


"1212as".isalnum()


# In[35]:


string = "AnalyticsVidhya"


# In[36]:


string.isalpha()


# In[37]:


string = "Analytics Vidhya"


# In[38]:


string.isalpha()


# ***Replace substrings***
# 
# ---

# In[39]:


"java is easy to learn.".replace('java', 'python')


# ***Split function***
# 
# ---

# In[40]:


"python is easy to learn".split(' ')


# In[41]:


"python is easy to learn".split('easy')

