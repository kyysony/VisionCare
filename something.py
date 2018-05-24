import yaml
from subprocess  import call
from flask import Flask, request


app = Flask(__name__)


config = {
    'server_address': "0.0.0.0",
    'server_port': 9988
}


@app.route('/')
def root_get():
    return 'OK'


@app.route("/github-feed", methods=["POST"])
def gitlab_feed():
    print("[NEW EVENT]")
    call(["bash", "/home/ubuntu/something.sh"])
    return "OK"


if __name__ == '__main__':
    app.run(host=config['server_address'], port=config['server_port'])