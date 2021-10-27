from flask import Flask, request
from flask_cors import CORS
from steam_find_api import API

#App Logging
app = Flask(__name__)
CORS(app)
app.logger.disabled = True

#GUI
@app.route('/steamApp', methods=['GET'])
def gui():
    return API.get_steam_app_info(request.args.get('appID'))

if (__name__ == "__main__"):
    app.run(app, port = 5000,debug = False)