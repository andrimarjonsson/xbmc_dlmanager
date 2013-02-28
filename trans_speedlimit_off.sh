#!/bin/bash
 
HOST=localhost
PORT=9091
USER=username_for_transmission_rpc
PASS=password_for_transmission_rpc
 
SESSID=$(curl --silent --anyauth --user $USER:$PASS "http://$HOST:$PORT/transmission/rpc" | sed 's/.*<code>//g;s/<\/code>.*//g')
curl --silent --anyauth --user $USER:$PASS --header "$SESSID" "http://$HOST:$PORT/transmission/rpc" -d "{\"method\":\"session-set\",\"arguments\":{\"alt-speed-enabled\":false}}"
