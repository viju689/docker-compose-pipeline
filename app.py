from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379, db=0)

@app.route('/')
def index():
    try:
        count = redis.incr('hits')
    except Exception:
        # graceful fallback if redis not available
        count = 0
    return f'Hello — this page has been viewed {int(count)} times.\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
