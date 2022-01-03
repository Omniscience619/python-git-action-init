import logging
from flask import Flask
from flask import json

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("Just accessed init method successfully")
    return "Hey there!"

@app.route("/status")
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info("Just accessed status successfully")
    return response

@app.route("/metrics")
def metricpull():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info("Just accessed metrics successfully")
    return response



if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
