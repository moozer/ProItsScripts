#!/bin/sh

# files...
WebLog="$HOME/web.log"
FtpLog="$HOME/ftp.log"

cd $(dirname $(realpath $0))

date >> $FtpLog
./PushAll.py >> $FtpLog

date >> $WebLog
./ReadAllBase.py >> $WebLog

