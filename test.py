# -*- coding: utf-8 -*-
import urllib2
import urllib

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
url = 'http://www.stat-nba.com/player/12.html'
headers = { 'User-Agent' : user_agent }
request = urllib2.Request(url,None,headers) 
response = urllib2.urlopen(request)
page = response.read()
print page