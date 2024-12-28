from flask import Flask
from routes import all_routes
from os import environ

app = Flask(__name__)

for route in all_routes:
    app.register_blueprint(route)

if __name__ == "__main__":
    app.run(port=int(environ["PORT"]), debug=True)
