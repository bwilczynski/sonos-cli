import webbrowser
from http import HTTPStatus
from http.server import HTTPServer, BaseHTTPRequestHandler
from os import path
from urllib.parse import parse_qs

import click

from api import auth
from config.creds_store import save_access_token
from settings import CLIENT_REDIRECT_PORT_NO


def _get_access_token(code):
    return auth.get_access_token(code)


def _get_authorization_code(state):
    class AuthenticationError(Exception):
        pass

    class ClientRedirectServer(HTTPServer):
        query_params = {}

    class ClientRedirectHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            print(self.headers.get('Referer'))
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

    server = ClientRedirectServer(('', CLIENT_REDIRECT_PORT_NO), ClientRedirectHandler)
    while True:
        server.handle_request()
        if 'code' and 'state' in server.query_params:
            state_param = server.query_params['state'][0]
            code_param = server.query_params['code'][0]
            if state == state_param:
                return code_param
            else:
                raise AuthenticationError()


@click.command()
def login():
    url, state = auth.login()
    webbrowser.open_new(url)
    code = _get_authorization_code(state)
    data = _get_access_token(code)
    save_access_token(data)
