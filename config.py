import os

from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

SONOS_AUTH_API_BASE_URL = 'https://api.sonos.com'
SONOS_CONTROL_API_BASE_URL = 'https://api.ws.sonos.com/control/api/v1'

CLIENT_REDIRECT_PORT_NO = 5000
REDIRECT_URL = f'http://localhost:{CLIENT_REDIRECT_PORT_NO}'
AUTH_URL = f'{SONOS_AUTH_API_BASE_URL}/login/v3/oauth'
CLIENT_SCOPES = ['playback-control-all']
ACCESS_TOKEN_URL = f'{SONOS_AUTH_API_BASE_URL}/login/v3/oauth/access'
REFRESH_TOKEN_URL = ACCESS_TOKEN_URL
