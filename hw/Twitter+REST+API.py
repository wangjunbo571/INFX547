
# coding: utf-8

# In[1]:

import pandas as pd
pd.__version__


# In[1]:

# REST API
import sys
import json
import pandas as pd

#Fill in your twitter dev info.
consumer_key = '9qfh9E7NytEJir0x8DPhA0Wo3'
consumer_secret = 'KXrazhottbw0htNyaz8ghC7JiPvmbuunqmDToqp1fGoqX2Cwa0'

access_token ='775111751108923392-0i4ZTsWb11OgIBSI9ZoA7noTLdUwSQI'
access_token_secret = 'prMoEZkGgvgOaWwI9WOlHuaNr4D6jkQPhZkWkh8ZPuxJo'

import twitter
api = twitter.Api(consumer_key, consumer_secret, access_token, access_token_secret)
# print api.VerifyCredentials()

import time
now = time.strftime("%c")

query = "q=University%20of%20Washington&result_type=recent&count=100"

data = api.GetSearch(raw_query= query)

print data


# In[7]:

# save data
with open('REST data['+now+'].json', 'w') as outfile:
    status = {}
    array = []
    for item in data:
        array.append(json.loads(item.AsJsonString()))
    status["status"] = array
    json.dump(json.dumps(status), outfile)
#         outfile.write(item.AsJsonString())
    
print "successfully save data into local file: 'data["+now+"].json'"


# In[ ]:



