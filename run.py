from app import GeneiAppSelenium
from config import config, user_config


config.update(user_config)
g_app = GeneiAppSelenium(**config)
g_app.run()
