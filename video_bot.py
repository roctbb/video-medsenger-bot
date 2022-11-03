import base64
from flask import Flask, jsonify
from medsenger_api import AgentApiClient
from config import *
from helpers import *

medsenger_api = AgentApiClient(API_KEY, MAIN_HOST, AGENT_ID, API_DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
    return "Waiting for the thunder"


# settings and views
@app.route('/settings', methods=['GET'])
@verify_args
def get_settings(args, form):
    return "Этот интеллектуальный агент не требует настройки."

@app.route('/video', methods=['GET'])
@verify_args
def get_video(args, form):
    return render_template('video.html')

if __name__ == "__main__":
    app.run(HOST, PORT, debug=API_DEBUG)
