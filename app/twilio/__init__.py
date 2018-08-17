# Download the helper library from https://www.twilio.com/docs/python/install
from app import app
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = app.config['TWILIO_ACCOUNT_SID']
auth_token = app.config['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
