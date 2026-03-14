from flask import Flask
from config import Config
import os

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Create necessary folders
    os.makedirs(app.config['DATA_FOLDER'], exist_ok=True)
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Register blueprints
    from routes.main import main
    from routes.articles import articles
    from routes.api import api
    
    app.register_blueprint(main)
    app.register_blueprint(articles, url_prefix='/articles')
    app.register_blueprint(api, url_prefix='/api')
    
    return app
