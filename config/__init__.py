import os
import yaml
from dotenv import load_dotenv

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
        
app_config = AppConfig()
config = app_config.config