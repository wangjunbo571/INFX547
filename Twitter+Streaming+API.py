
# coding: utf-8

# In[1]:

# Streaming API
import sys
import time
import datetime
import pandas as pd

from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

#Fill in your twitter dev info.
consumer_key = '9qfh9E7NytEJir0x8DPhA0Wo3'
consumer_secret = 'KXrazhottbw0htNyaz8ghC7JiPvmbuunqmDToqp1fGoqX2Cwa0'

access_token ='775111751108923392-0i4ZTsWb11OgIBSI9ZoA7noTLdUwSQI'
access_token_secret = 'prMoEZkGgvgOaWwI9WOlHuaNr4D6jkQPhZkWkh8ZPuxJo'

#This handles Twitter authetification and the connection to Twitter Streaming API
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth)

#Print received tweets to stdout

class StreamParser(StreamListener):
    """ Controls how streaming data is parsed. Pass an outfile, or data will be writting to 
    sys.stdout (eg the screen)
    """
    def __init__(self, outfile=None, max_tweets=5, max_seconds=30):
        self.counter = 0
        self.start_time = time.time()
        # Set upper limits on maximum tweets or seconds before timeout
        self.max_tweets = max_tweets
        self.max_seconds = max_seconds
        if outfile:
            self.stdout = open(outfile, 'w')
        else:
            self.stdout = sys.stdout
    
    def on_data(self, data):
        """ Data is a string, but formatted for json. Parses it"""
        self.counter += 1
        # time data is all timestamps.
        current_time = time.time()
        run_time = current_time - self.start_time
                
        # If we want to read time, easiest way is to convert from timestamp using datetime
        formatted_time = datetime.datetime.now()
            
        # Technically, might not be the best place to put kill statements, but works well enough
        if self.max_tweets:
            if self.counter > self.max_tweets:
                self._kill_stdout()
                raise SystemExit('Max tweets of %s exceeded.  Killing stream... see %s'                              % (self.max_tweets, self.stdout))
  
        if self.max_seconds:
            if run_time > self.max_seconds:
                self._kill_stdout()
                raise SystemExit('Max time of %s seconds exceeded.  Killing stream... see %s'                                  % (self.max_seconds, self.stdout))

        print ('Tweet %s at %s.\nEllapsed: %.2f seconds\n' %(self.counter, formatted_time, run_time))

        # Write to file, return True causes stream to continue I guess...
        self.stdout.write(data)
        return True

    def _kill_stdout(self):
        """ If self.stdout is a file, close it.  If sys.stdout, pass"""
        if self.stdout is not sys.stdout:
            self.stdout.close() 
    
    def on_error(self, status):
        print (status)

import time
now = time.strftime("%c")

# Stream 10 tweets, no matter the time it takes!
listener = StreamParser(outfile='Streaming data[' + now + '].json', max_tweets=10, max_seconds=None)
stream = Stream(auth, listener)

#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.filter(track=['University of Washington','uw'])


# In[ ]:

# data = pd.read_json('infx547d4.json', lines=True)
# data

