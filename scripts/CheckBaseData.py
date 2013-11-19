#!/usr/bin/env python


import sys
import urllib2
import json


# command line args.
if len(sys.argv) < 3:
    print "usage %s <id> <URL>"%sys.argv[0]
    exit( 1 )

GroupId = sys.argv[1]
URL = sys.argv[2]

print '%s: 0: Fetching basedata from %s :'%(GroupId, URL)

# fetch data
req = urllib2.Request(URL)
response = urllib2.urlopen(req)
jsondata = response.read() 
response.close()

# parsing json
data = json.loads( jsondata )

print '%s: 10: Data fetched: hostname: %s, php version: %s, timestamp: %s'%(GroupId, data['hostname'], data['version'], data['date'])




