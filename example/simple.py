"""
Flask-DummyImage example application.

Run with:
    uv run flask --app example.simple run --debug

Then open http://localhost:5000/ in your browser.
"""

from flask import Flask, render_template

from flask_dummyimage import DummyImage

app = Flask(__name__)

# Custom configuration: url_prefix, endpoint, route can be customized.
# Default values are url_prefix="/dummyimage", endpoint="dummyimage", route="dummyimage"
dummyimage = DummyImage(app, url_prefix="/dm", endpoint="images", route="img")


@app.route("/")
def index():
    return render_template("index.html")
