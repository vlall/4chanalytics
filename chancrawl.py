import urllib2
import re
import time;
from datetime import datetime
import json
from HTMLParser import HTMLParser
import htmlentitydefs

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def html_to_text(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

board = 'biz'
    
url = 'http://a.4cdn.org/'+ board +'/catalog.json'

response = urllib2.urlopen(url)
data = json.load(response)

# len(data) is the number of pages. data[x] where x is the page number on the board.

front = data[0]
space = '\n\n\t'

#List>Dictionary with 'Page:','Threads' dictionarys
contentList = front.get('threads')

for i in range (len(contentList)):
    #Move later
    print space + 'Thread #: ' + str(i)     
    threadTags = contentList[i] # this is the 'i'th post of the first page
    time = threadTags.get('now') # when the thread was made
    sub = threadTags.get('sub') 
    com = threadTags.get('com') #First post of the thread that shows up on the main page
    no = threadTags.get('no') #Number
    closed = threadTags.get('closed', 0) # 1 - Yes, 0 - No
    last_replies = threadTags.get('last_replies') # last replies that appear on front page
    replies = threadTags.get('replies') # Number of replies
    last_modified = threadTags.get('last_modified') # last post

    # This is where we extract data from the home page to get each individual thread number
    # From each thread number we do "http://a.4cdn.org/biz/res/"THREADNUMBER".json"

    threadNum = str(no)
    threadUrl = 'http://a.4cdn.org/' + board + '/res/'+ threadNum +'.json'
    threadResponse = urllib2.urlopen(threadUrl)
    threadData = json.load(threadResponse)
    
    # This will prevent us trying to access closed threads.
    if (int(closed) == 1):
        continue;  
    posts = threadData.get('posts') 
    for j in range (len(posts)):
        comDict = posts[j]
        
        comment = unicode(comDict.get('com'))
        comment = comment.replace('<br>', '\n\t')
        if '</a>' in comment:
            words = comment.split('</a>')
            for n in range (len(words)-1):
                quote = words[n]
                strippedQuote = html_to_text(quote)
                print '>> ' + strippedQuote
            reply = words[n+1]    
            strippedReply = html_to_text(reply)    
            print space + strippedReply
        else:
            print space + 'Reply #' + str(j) + space +(comment)

'''Current bugs:
1) If theres more than one quote it doesn't get the reply. 
^ loop through list of </a> values to get all the reply 
2) Doesn't delete tripcodes
3) if you direct to a different thread, it messes up and places that as part of the reply.
4) treat <br> as breaks---Check
5) FORMAT INTO FUNCTIONS'''
