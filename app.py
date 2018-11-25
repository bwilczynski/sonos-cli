from flask import Flask, request, render_template
from http import HTTPStatus
import webbrowser

from config import AUTH_CODE_URI, PORT_NO, SONOS_ACCOUNT_URI

app = Flask(__name__)


@app.route('/authorized', methods=['GET'])
def authorized():
    print(request.query_string)
    return render_template('authorized.html', redirect_url=SONOS_ACCOUNT_URI)


if __name__ == '__main__':
    webbrowser.open_new(AUTH_CODE_URI)
    app.run(port=PORT_NO)
