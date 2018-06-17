import app.payment.models
from flask import Flask
from .database import db


def create_app(settings_path):
    app = Flask(__name__)
    app.config.from_pyfile(settings_path)

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    import app.payment.controllers as payment

    app.register_blueprint(payment.module)

    return app
