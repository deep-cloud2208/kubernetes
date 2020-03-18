from flask import Flask
import os

app = Flask(__name__)

name = os.environ['NAME']

@app.route("/kubernetes")

def awsecs():
    return "Hi " + name + " ... Welcome to K8S session. (shommo.com)"


if (__name__) == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
