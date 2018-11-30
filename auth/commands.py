import webbrowser
from http import HTTPStatus
from http.server import HTTPServer, BaseHTTPRequestHandler
from os import path
from urllib.parse import parse_qs

import requests
from requests.auth import HTTPBasicAuth

from config import CLIENT_ID, CLIENT_SECRET

PORT_NO = 5000
CREATE_AUTH_CODE_REDIRECT_URL = 'https://haa5mxcg4k.execute-api.eu-west-1.amazonaws.com/default/authorized'
SONOS_API_BASE_URL = 'https://api.sonos.com'
AUTH_CODE_URL = f'{SONOS_API_BASE_URL}/login/v3/oauth?client_id={CLIENT_ID}&response_type=code&state=1&scope=playback-control-all&redirect_uri={CREATE_AUTH_CODE_REDIRECT_URL}'
CREATE_TOKEN_URL = f'{SONOS_API_BASE_URL}/login/v3/oauth/access'


def _create_token(code):
    data = {'grant_type': 'authorization_code', 'code': code, 'redirect_uri': CREATE_AUTH_CODE_REDIRECT_URL}
    response = requests.post(CREATE_TOKEN_URL, data=data,
                             auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
    print(response.json())


def _get_authorization_code():
    class ClientRedirectServer(HTTPServer):
        query_params = {}

    class ClientRedirectHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            query_string = self.path.split('?', 1)[-1]
            self.server.query_params = parse_qs(query_string)

            print(self.server.query_params)

            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            html_file = path.join(path.dirname(path.realpath(
                __file__)), 'templates', 'ok.html' if 'code' in query_string else 'fail.html')
            with open(html_file, 'rb') as html_view:
                self.wfile.write(html_view.read())

    port = 5000
    server = ClientRedirectServer(('', port), ClientRedirectHandler)
    while True:
        server.handle_request()
        if 'code' in server.query_params:
            return server.query_params['code'][0]


def login():
    webbrowser.open_new(AUTH_CODE_URL)
    code = _get_authorization_code()
    _create_token(code)
