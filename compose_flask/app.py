#!/usr/bin/env python

# compose_flask/app.py

from flask import Flask
from redis import Redis

app = Flask(__name__)

# Do not set host to localhost
redis = Redis(host="redis", port=6379)

@app.route("/")
def hello():
    redis.incr("hits")
    #return "<H1>Hello Frank</h1>"
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
