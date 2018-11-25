# from urllib import parse

PORT_NO = 5000
CLIENT_ID = '***REMOVED***'
CREATE_AUTH_CODE_REDIRECT_URI = f'https://haa5mxcg4k.execute-api.eu-west-1.amazonaws.com/default/authorized'
AUTH_CODE_URI = f'https://api.sonos.com/login/v3/oauth?client_id={CLIENT_ID}&response_type=code&state=1&scope=playback-control-all&redirect_uri={CREATE_AUTH_CODE_REDIRECT_URI}'
