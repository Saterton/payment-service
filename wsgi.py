import os
from app import create_app

_basedir = os.path.abspath(os.path.dirname(__file__))
settings_path = os.path.join(_basedir, 'settings.py')

application = create_app(settings_path)
application.config.from_pyfile(settings_path)
