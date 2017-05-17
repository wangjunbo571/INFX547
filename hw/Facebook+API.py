
# coding: utf-8

# In[4]:

import facebook

# prompt for credentials on the command-line,
# get access to one or more pages
#pages = fi.authenticate()
# alternatively, pass an existing page token

token = 'EAADGURIfP60BAAfLymQuB3sWkWvWrw5aCQVhCeWf51klK6BZA5UHBs3NuZCT3Pc12HD61r6Bovmq5e6gmnhnpwUdfn10itgZBv05E1Vntje963qsZCE3PpR3uKLAEtBLDdqmPiZAefRTV1TiYEaZABcIfIhbfAcsUOXeJbvameaZAt3Vt9xod3OnY5cugB1nykZD'
app_token = '218051498688429|EzhgMbT74dvlpQ21EGLUip4NdxQ'
graph = facebook.GraphAPI(access_token = token, version='2.8')

data = graph.request('/search?q=University%20of%20Washington&type=page')


# In[8]:

import json

with open('Facebook API Data.json', 'w') as outfile:
    json.dump(data, outfile)
print "successfully save data"


# In[5]:

data


# In[ ]:



