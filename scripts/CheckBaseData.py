#!/usr/bin/env python


import sys
import urllib2
import json


def FetchBaseData( URL ):
	
	print 'Fetching basedata from %s :'%(URL,)

	# fetch data
	req = urllib2.Request(URL)
	response = urllib2.urlopen(req)
	jsondata = response.read() 
	response.close()

	# parsing json
	data = json.loads( jsondata )

	print 'Data fetched: hostname: %s, php version: %s, timestamp: %s'%(data['hostname'], data['version'], data['date'])

	return data

if __name__ == '__main__':

	# command line args.
	if len(sys.argv) < 3:
	    print "usage %s <id> <URL>"%sys.argv[0]
	    exit( 1 )

	GroupId = sys.argv[1]
	URL = sys.argv[2]


	# parsing json
	data = FetchBaseData( URL )





