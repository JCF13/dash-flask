from flask import Flask
from flask_app.app.Config import Config

def init_app():
    app = Flask(__name__.split('.')[1])
    app.config.from_object(Config)

    from flask_app.app.routes import routes
    app.register_blueprint(routes)

    from flask_app.app.dash.dashboard import init_dasboard
    init_dasboard(app)

    return app

app = init_app()