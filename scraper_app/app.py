from flask import Flask
import uuid
import os


def create_app():
    """
    Register routes within Flask app and returns app instance
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = uuid.uuid4().hex

    from routes import (endpoint_blueprint)
    app.register_blueprint(endpoint_blueprint)

    return app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8084))
    create_app().run(host="0.0.0.0", port=port, debug=True)