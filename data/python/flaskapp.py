import json
from flask import Flask
from flask import Response
from flask_cors import CORS

from proxy import get_flight_radar_data


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route('/flightradar')
def flightradar():
    return Response(
        response=json.dumps(get_flight_radar_data()),
        status=200,
        mimetype='application/json'
    )
if __name__=='__main__':
    app.run()
