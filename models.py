# contains much of the database models. Uses Flask, SQLAlchemy
# Building of the API Happens here.

# This db variable will give us an access to SQLAlchemy
from config import db

#db model represented in a python class and now in Python code we can define what different fields the db is gonna have.
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(70), unique=False, nullable=False)
    last_name = db.Column(db.String(80),unique = False, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique = True)

#Takes the different fields we have and convert them into a python dictionary then convert it to json.
#From json then we caan pass it as an API. JSON file is in form of a dictionary.
#The API will return json and we will send json to the API to create our different objects.(Returning json back and fourth.)
#JSON file is in form of a dictionary but written in Javascript.(camelCase)
    def to_json(self):
        return{
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }