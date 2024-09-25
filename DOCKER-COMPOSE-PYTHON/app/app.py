from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis-container', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return ' - - - Vous ête sur la page de base du site ! --> je ne sais pas à quoi correspond ceci {} time(s) - - -'.format(redis.get('hits'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
