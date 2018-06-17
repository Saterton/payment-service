#!/usr/bin/env python
import os
from app import create_app
from flask_script import Manager

_basedir = os.path.abspath(os.path.dirname(__file__))
settings_path = os.path.join(_basedir, 'settings.py')

app = create_app(settings_path)
app.config.from_pyfile(settings_path)
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
