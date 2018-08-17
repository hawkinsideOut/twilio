import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
  SECRET_KEY = os.urandom(24)
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  TWILIO_ACCOUNT_SID = os.getenv('ACCOUNT_SID')
  TWILIO_AUTH_TOKEN = os.getenv('AUTH_TOKEN')
  TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')
