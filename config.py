import os
from pathlib import Path
# base_dir = Path(__file__).parent.resolve()
# base_dir = os.path.abspath(os.path.dirname(__file__))
base_dir = Path(__file__).parent


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or "you-can't-guess"

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        'sqlite:///' + os.path.join(base_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False