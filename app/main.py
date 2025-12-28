#getting dependencies
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
database = SQLAlchemy(app)



class Event(database.Model):
    id = database.Column(database.Integer, primary_key = True)

    user = database.Column(
        database.String(100),
        database.ForeignKey("user.user_name"),
        nullable = False
    )

    event_name = database.Column(database.String(100), nullable = False)
    event_date = database.Column(database.String(80), nullable = False)
    event_time = database.Column(database.Integer)
    event_description = database.Column(database.String(300))

class User(database.Model):
    user_name = database.Column(database.String(100), nullable = False, primary_key = True)
    user_events = database.relationship(
        "Event", 
        backref = 'user', 
        lazy = True
        )




#this is like our main page, we want to be able to create users here
@app.route('/')
def index():
    return "..."

"""
@app.route('/<user_name>')
def index(user_name):
    user = User.query.get_or_404(user_name)
"""
