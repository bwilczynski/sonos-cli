from flask import Flask, request
from http import HTTPStatus
import webbrowser

from config import AUTH_URI

app = Flask(__name__)


@app.route('/', methods=['POST'])
def callback():
    print(request.query_string)
    return ('', HTTPStatus.NO_CONTENT)


if __name__ == '__main__':
    webbrowser.open_new(AUTH_URI)
    app.run()
