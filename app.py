import webbrowser
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path
from urllib.parse import parse_qs

import requests
from requests.auth import HTTPBasicAuth

from config import CREATE_TOKEN_URL, CLIENT_ID, CLIENT_SECRET, \
    CREATE_AUTH_CODE_REDIRECT_URL, AUTH_CODE_URL


def create_token(code):
    data = {'grant_type': 'authorization_code', 'code': code, 'redirect_uri': CREATE_AUTH_CODE_REDIRECT_URL}
    response = requests.post(CREATE_TOKEN_URL, data=data,
                             auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
    print(response.json())


def get_authorization_code(callback):
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
            callback(server.query_params['code'][0])
            break


if __name__ == '__main__':
    webbrowser.open_new(AUTH_CODE_URL)

    get_authorization_code(create_token)
