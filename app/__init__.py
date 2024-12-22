from flask import Flask
import os
import yaml
from dotenv import load_dotenv
from logger import CustomLogger


# Load environment variables from .env file
load_dotenv()

class AppConfig:
    """Class to handle app config"""

    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        """Load Config from config.yaml"""

        with open('config/config.yaml', 'r') as file:
            config = yaml.safe_load(file)

        if 'api' in config and 'key' in config['api']:
            config['api']['key'] = os.getenv('API_KEY')

        return config
        

def create_app(config=None):
    """Create and config the flask app"""

    app = Flask(__name__, template_folder='templates')
    
    app_config = AppConfig()
    app.config.update(app_config.config)

    logger = CustomLogger().get_logger()
    logger.info("Flask application starting...")

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
