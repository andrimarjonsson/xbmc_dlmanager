#!/bin/bash

if [ $# -eq "0" ] # should check for no arguments
then
	echo "Usage: transmission_limit.sh <on|off> <port> <username> <password>"
else

	HOST=localhost
	PORT=$2
	USER=$3
	PASS=$4
	 
	SESSID=$(curl --silent --anyauth --user $USER:$PASS "http://$HOST:$PORT/transmission/rpc" | sed 's/.*<code>//g;s/<\/code>.*//g')

	if [ $1 == "on" ] # lets enable speedlimit
	then
		 curl --silent --anyauth --user $USER:$PASS --header "$SESSID" "http://$HOST:$PORT/transmission/rpc" -d "{\"method\":\"session-set\",\"arguments\":{\"alt-speed-enabled\":true}}"
	fi

	if [ $1 == "off" ] # lets enable speedlimit
	then
		 curl --silent --anyauth --user $USER:$PASS --header "$SESSID" "http://$HOST:$PORT/transmission/rpc" -d "{\"method\":\"session-set\",\"arguments\":{\"alt-speed-enabled\":false}}"
	fi
fi
	
