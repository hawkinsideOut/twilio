from app import app, db
from flask import redirect, render_template, url_for, flash, request
from app.twilio import client
from app.forms import MessageForm, RegistrationForm, AddContactForm
import twilio
from twilio.twiml.messaging_response import MessagingResponse
from flask_login import login_required
from app.models import User, Contact

@login_required
@app.route('/', methods=['GET'])
def index():
  sorted_messages = []
  [sorted_messages.append(i) for i in client.messages.list()]
  print([i.to for i in sorted_messages])
  for i in sorted_messages:
    for j in Contact.query.all():
      if i.to[2:] == j.phone:
        number = i.to
        number = j.name
        print(number)
  sorted_messages.reverse()
  
  context = {
    'title': 'Site Name',
    'messageForm': MessageForm(),
    'messages': sorted_messages,
    'my_number': app.config['TWILIO_NUMBER'],
    'contactForm': AddContactForm(),
    'contacts': Contact.query.all()
  }
  return render_template('index.html', **context)


@app.route('/send_message', methods=['POST'])
def send_message():
  try:
    if MessageForm().validate_on_submit():
      client.messages.create(
        body = MessageForm().message.data,
        from_ = str(app.config['TWILIO_NUMBER']),
        to = f"+1{MessageForm().send_to.data}"
      )
      flash("Message sent")
      return redirect(url_for('index'))
  except twilio.base.exceptions.TwilioRestException:
    flash("There seems to be an error. Try again later!")
    return redirect(url_for('index'))
  return redirect(url_for('index'))


@app.route('/contacts', methods=['POST'])
def contacts():
  contactForm = AddContactForm()
  if contactForm.validate_on_submit():
    contact = Contact(name=contactForm.name.data, phone=contactForm.phone.data)
    db.session.add(contact)
    db.session.commit()
    flash("Added a new contact")
  return redirect(url_for('index'))


@app.route('/sms', methods=['GET', 'POST'])
def incoming_sms():
  resp = MessagingResponse()
  resp.message(request.values.get('Body', None))
  return redirect(url_for('index'))

@app.route('/registration', methods=['GET', 'POST'])
def registration():
  form = RegistrationForm()
  if form.validate_on_submit():
    u = User(name=form.name.data, email=form.email.data)
    u.password_hash = u.set_password(form.password.data)
    db.session.add(u)
    db.session.commit()
    flash("You are registered")
    return redirect(url_for('login'))
  context = {
    'form': form
  }
  return render_template('registration.html', **context)

@app.route('/login')
def login():
  return render_template('login.html')
