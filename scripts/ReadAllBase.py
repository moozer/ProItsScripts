#!/usr/bin/env python

# reads config and pushes data

import ConfigParser
from CheckBaseData import FetchBaseData 

Grouplist = "../grouplist.txt"
GroupNames = ["Group01", "Group02", "Group03", "Group04", "Group05", "Group06", "Group07", "Group08" ]


if __name__ == "__main__":
	#config = ConfigParser.ConfigParser()
	config = ConfigParser.SafeConfigParser()
	config.read( Grouplist )

	for group in GroupNames:
		print "Group: %s"%group
		try:
			WebUrl = config.get(group, 'weburl' )
			FetchBaseData( WebUrl+'basedata.php')
		except Exception, e:
			print "Something went wrong: %s"%e

