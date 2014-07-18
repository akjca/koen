#!/usr/bin/env python
import urllib, urllib2, htmllib, formatter, re, sys, os, socket
print '<!---    koenkrawl spider    ---!> \n made by gnomes out of discarded snake skin.'
url = raw_input("enter site to krawl: ")
print 'be patient...'
f = open('otp','wb')
w = urllib.urlopen("http://"+url)
w.addheaders = [('User-agent', 'KoenKrawler/0.5')]
d = w.read()
w.close()
format = formatter.AbstractFormatter(formatter.NullWriter())
t = htmllib.HTMLParser(format)
t.feed(d)
link = []
links = t.anchorlist
for link in links:
	if re.search('http', link) != None:		
		f.write(link+'\n') 
		w2 = urllib.urlopen(link)
		d2 = w2.read()
		w2.close()
		format = formatter.AbstractFormatter(formatter.NullWriter())
		t = htmllib.HTMLParser(format)
		t.feed(d2)
		alink = []
		blinks = t.anchorlist
		for alink in blinks:
			if re.search('http', link) != None:
				links.append(alink)
				f.write(alink+'\n') 
			
f.close()
print 'The site returned no links \n probably...'
