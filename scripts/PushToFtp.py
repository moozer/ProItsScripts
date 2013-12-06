#!/usr/bin/env python

# pushes data to a given server

from ftplib import FTP, FTP_TLS
import sys
import os
import paramiko

FilesToPut = ['../php/basedata.php']

def Push( FtpServer, Username, Password, uploadlist = FilesToPut, port = 21, passive = False, Sftp = False ):
        print "Login to %s:%s using %s:%s (%s)"%(FtpServer, port, Username, 'xxx', 
				'passive' if passive else 'active')
                
        if Sftp:
            paramiko.util.log_to_file('/tmp/paramiko.log')
            transport = paramiko.Transport((FtpServer,int(port)))
            transport.connect(username = Username, password = Password)
            sftp = paramiko.SFTPClient.from_transport(transport)
            
            for f in uploadlist:
		    print "uploading %s"%f		
		    sftp.put(f, os.path.basename(f))
            sftp.close()
            transport.close()

        else:
            ftp = FTP()
            ftp.connect( FtpServer, port )
            ftp.login( Username, Password ) 
	    ftp.set_pasv( passive )
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
