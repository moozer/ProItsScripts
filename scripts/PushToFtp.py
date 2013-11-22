#!/usr/bin/env python

# pushes data to a given server

from ftplib import FTP, FTP_TLS
import sys
import os

FilesToPut = ['../php/basedata.php']

def Push( FtpServer, Username, Password, uploadlist = FilesToPut, port = 21, passive = False, StartTls = False ):
	print "Login to %s:%s using %s:%s (%s%s)"%(FtpServer, port, Username, 'xxx', 
				'passive' if passive else 'active', 
				'/tls' if StartTls else '')

	if StartTls:
		ftp = FTP_TLS()
	else:
		ftp = FTP()
	
	#ftp.set_debuglevel(2)

	ftp.connect( FtpServer, port )
	ftp.login( Username, Password )                     # user anonymous, passwd anonymous@
	ftp.set_pasv( passive )

	if StartTls:
		ftp.prot_p()	    

	for f in uploadlist:
		print "uploading %s"%f		
		fp = open( f, 'rb')
		ftp.storbinary('STOR %s'%os.path.basename(f), fp)     # send the file

	ftp.quit()

if __name__ == "__main__":
	if len(sys.argv) < 5:
		print >> sys.stderr, "usage %s <server> <port> <username> <password>"%sys.argv[0]
		exit( 1 )

	FtpServer = sys.argv[1]
	Port = sys.argv[2]
	Username = sys.argv[3]
	Passwd = sys.argv[4]

	Push( FtpServer, Username, Passwd, port = Port )
	print >> sys.stderr, "Done"
