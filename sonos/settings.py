import os

from sonos.config import config_store

cfg = config_store.get_config() or {}

SONOS_CLIENT_ID = os.getenv("SONOS_CLIENT_ID") or cfg.get("client_id")
SONOS_CLIENT_SECRET = os.getenv("SONOS_CLIENT_SECRET") or cfg.get("client_secret")

SONOS_AUTH_API_BASE_URL = "https://api.sonos.com"
SONOS_CONTROL_API_BASE_URL = "https://api.ws.sonos.com/control/api/v1"

CLIENT_REDIRECT_PORT_NO = 5000
CLIENT_REDIRECT_URL = f"http://localhost:{CLIENT_REDIRECT_PORT_NO}"
CLIENT_SCOPE = ["playback-control-all"]
AUTH_URL = f"{SONOS_AUTH_API_BASE_URL}/login/v3/oauth"
ACCESS_TOKEN_URL = f"{SONOS_AUTH_API_BASE_URL}/login/v3/oauth/access"
REFRESH_TOKEN_URL = ACCESS_TOKEN_URL
