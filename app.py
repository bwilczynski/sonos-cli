from flask import Flask, request, render_template
from http import HTTPStatus
import webbrowser
import requests
from requests.auth import HTTPBasicAuth

from config import AUTH_CODE_URL, PORT_NO, SONOS_ACCOUNT_URL, CREATE_TOKEN_URL, CLIENT_ID, CLIENT_SECRET, CREATE_AUTH_CODE_REDIRECT_URL

app = Flask(__name__)


def create_token(code):
    data = dict(grant_type='authorization_code',
                code=code, redirect_uri=CREATE_AUTH_CODE_REDIRECT_URL)
    response = requests.post(CREATE_TOKEN_URL, data=data,
                             auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
    print(response.json())


@app.route('/authorized', methods=['GET'])
def authorized():
    code = request.args['code']
    print(code)
    create_token(code)
    return render_template('authorized.html', redirect_url=SONOS_ACCOUNT_URL)


if __name__ == '__main__':
    webbrowser.open_new(AUTH_CODE_URL)
    app.run(port=PORT_NO)
