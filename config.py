import os
from dotenv import load_dotenv

# setting a path for this particular file
basedir = os.path.abspath(os.path.dirname(__file__))

#Give access to the project in ANY OS where find ourselves in
# all outside files/folders to be added to the project
# from the base directory

load_dotenv(os.path.join(basedir, '.env'))

class Config():
    """
    Set configuration variables for the flask app
    Using environment variables where available
    otherwise creates the config variable if not done
    already
    """
    """
    GitIgnore will not upload certain sensitive information

    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get("SECRET_KEY") or "nana nana boo boo youll never guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # turns of messages from sqlalchemy regarding updates to our db