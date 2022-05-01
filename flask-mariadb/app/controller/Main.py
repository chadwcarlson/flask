from app import app
from cache import cache
from flask import render_template


@app.route("/", methods=["GET"])
@cache.cached(timeout=50)
def index():
    return render_template("index.html")
