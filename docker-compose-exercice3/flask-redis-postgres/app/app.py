from flask import Flask
import redis
import psycopg2
import os

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

@app.route("/")
def home():
    visits = redis_client.incr("visits")

    return f"""
        <h1>Bienvenue sur mon application Flask !</h1>
        <p>Nombre de visites : {visits}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)