from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes import prime_bp
    app.register_blueprint(prime_bp)

    return app
