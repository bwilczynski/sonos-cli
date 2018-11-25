# from urllib import parse

PORT_NO = 5000
CREATE_AUTH_CODE_REDIRECT_URL = 'https://haa5mxcg4k.execute-api.eu-west-1.amazonaws.com/default/authorized'

CLIENT_ID = '***REMOVED***'
CLIENT_SECRET = '***REMOVED***'

SONOS_ACCOUNT_URL = 'https://www.sonos.com/myaccount/'
SONOS_API_BASE_URL = 'https://api.sonos.com'
AUTH_CODE_URL = f'{SONOS_API_BASE_URL}/login/v3/oauth?client_id={CLIENT_ID}&response_type=code&state=1&scope=playback-control-all&redirect_uri={CREATE_AUTH_CODE_REDIRECT_URL}'
CREATE_TOKEN_URL = f'{SONOS_API_BASE_URL}/login/v3/oauth/access'
