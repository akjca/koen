#!/usr/bin/python
USER_AGENT = 'koenkrawl - crawling for fun'
import urllib, urllib2, htmllib, formatter, re, sys, os, socket
print '<!---    koenkrawl spider    ---!>'
print 'made by gnomes out of discarded snake skin.'
url = raw_input("enter site to krawl: ")
print 'be patient...'
f = open('otp.txt','wb')
w = urllib.urlopen("http://"+url)
data = w.read()
w.close()
format = formatter.AbstractFormatter(formatter.NullWriter())
t = htmllib.HTMLParser(format)
t.feed(data)
link = []
links = t.anchorlist
for link in links:
	if re.search('http', link) != None:		
		f.write(link) 
		f.write('\n')
		w2 = urllib.urlopen(link)
		data2 = w2.read()
		w2.close()
		t = htmllib.HTMLParser(format)
		t.feed(data2)
		alink = []
		blinks = t.anchorlist
		for alink in blinks:
			if re.search('http', link) != None:
				links.append(alink)
				f.write(alink) 
				f.write('\n')

f.close()
print 'The site returned no links'
print 'probably...'
