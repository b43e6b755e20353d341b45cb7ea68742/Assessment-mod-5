import os
from flask import Flask
import requests
app = Flask(__name__)


@app.route("/")
def hello_world():
   
    a = {"message": "Assessment time!!!!"}
    return a['message']


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(port=port, host="0.0.0.0",debug=True)