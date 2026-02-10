from flask import Flask
from flask_dummyimage import DummyImage

app = Flask(__name__)
DummyImage(app)

if __name__ == "__main__":
    app.run(debug=True)
