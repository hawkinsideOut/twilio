from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  email = db.Column(db.String, index=True, unique=True)
  password_hash = db.Column(db.String)

  def set_password(self, password):
    self.password_hash = generate_password_hash(self.password_hash)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  def __repr__(self):
    return f"User({self.email})"


class Contact(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  phone = db.Column(db.String, index=True, unique=True)

  def __repr__(self):
    return f"Contact({self.phone}: {self.name})"