from flask import Flask, request
from http import HTTPStatus
import webbrowser

from config import AUTH_CODE_URI, PORT_NO

app = Flask(__name__)


@app.route('/authorized', methods=['GET'])
def callback():
    print(request.query_string)
    return ('', HTTPStatus.NO_CONTENT)


if __name__ == '__main__':
    webbrowser.open_new(AUTH_CODE_URI)
    app.run(port=PORT_NO)
