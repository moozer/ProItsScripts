#!/usr/bin/env python

# reads config and pushes data

import ConfigParser
from PushToFtp import Push

Grouplist = "../grouplist.txt"
GroupNames = ["Group01", "Group02", "Group03", "Group04", "Group05", "Group06", "Group07", "Group08" ]


if __name__ == "__main__":
	#config = ConfigParser.ConfigParser()
	config = ConfigParser.SafeConfigParser( {'port': '21', 'passive': False, 'sftp': False })
	config.read( Grouplist )

	for group in GroupNames:
		print "Group: %s"%group
		try:
			Username = config.get(group, 'user' )
			FtpServer = config.get(group, 'ip' )
			Passwd = config.get(group, 'pass' )
			WebUrl = config.get(group, 'weburl' )
			port = config.get(group, 'port' )
			passive = config.get(group, 'passive' )
			sftp = config.get(group, 'sftp')
			Push( FtpServer, Username, Passwd, port=port, 
				passive=True if passive == 'True' else False,
				Sftp=True if sftp == 'True' else False)
		except Exception, e:
			print "Something went wrong: %s"%e

