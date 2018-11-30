#!/bin/bash

API_KEY=***REMOVED***
REDIRECT_URI=https://0c07cec7.ngrok.io
AUTH_URI="https://api.sonos.com/auth/v3/oauth?client_id=$API_KEY&response_type=code&state=1&scope=playback-control-all&redirect_uri=$REDIRECT_URI"

echo $AUTH_URI
open $AUTH_URI
