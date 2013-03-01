#!/bin/bash
 
NO_ARGS=0

if [ $# -eq "$NO_ARGS" ] # should check for no arguments
then
	echo "Usage: `transmission_limit.sh <on|off> <port> <username> <password>"
else

	HOST=localhost
	PORT=$2
	USER=$3
	PASS=$4
	 
	SESSID=$(curl --silent --anyauth --user $USER:$PASS "http://$HOST:$PORT/transmission/rpc" | sed 's/.*<code>//g;s/<\/code>.*//g')
	curl --silent --anyauth --user $USER:$PASS --header "$SESSID" "http://$HOST:$PORT/transmission/rpc" -d 

	if [ $1 -eq "on" ] # lets enable speedlimit
	then
		"{\"method\":\"session-set\",\"arguments\":{\"alt-speed-enabled\":true}}"
	fi

	if [ $1 -eq "off" ] # lets enable speedlimit
	then
		"{\"method\":\"session-set\",\"arguments\":{\"alt-speed-enabled\":false}}"
	fi
fi
	
