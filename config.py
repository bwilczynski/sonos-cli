import os

from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

SONOS_AUTH_API_BASE_URL = 'https://api.sonos.com'
SONOS_CONTROL_API_BASE_URL = 'https://api.ws.sonos.com/control/api/v1'
