from flask import Flask

import api

characters = api.characters

app = Flask(__name__)

from views import *

if __name__ == "__main__":
    app.run(debug = True)