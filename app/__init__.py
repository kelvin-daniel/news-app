from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootsrap = Bootstrap()
def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    # Initializing Flask Extensions
    bootstrap.init_app(app)
    # registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    #setting up config
    from .request import configure_request
    configure_request(app)

    return app