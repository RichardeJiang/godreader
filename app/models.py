from app import db
from app import login
from flask_login import UserMixin

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password = db.Column(db.String(128))
	documents = db.relationship('Document', backref='holder', lazy='dynamic')

	def __repr__(self):
		return '<User {}>'.format(self.username)

class Document(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	original_text = db.Column(db.Text())
	title = db.Column(db.String(64))
	summary = db.Column(db.Text())

	def __repr__(self):
		return '<Document {}>'.format(self.title)
