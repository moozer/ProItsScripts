#!/bin/sh

# files...
DATE=$(date "+%y%m%d")
WebLog="$HOME/${DATE}_web.log"
FtpLog="$HOME/${DATE}_ftp.log"

cd $(dirname $(realpath $0))

date >> $FtpLog
./PushAll.py >> $FtpLog

date >> $WebLog
./ReadAllBase.py >> $WebLog

