import os
from flask import Flask

from teaspoon.routes import home

def create_app():
    app = Flask(__name__)
    app.config["PORT"] = os.environ.get("PORT", 5001)

    with app.app_context():
        # register blueprints
        app.register_blueprint(home.blueprint)

        @app.route("/ping")
        def ping():
            return "pong"
        return app
