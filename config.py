# OBJECT RELATIONAL MAPPING.
# Pip install Flask-SQLAlchemy
# pip install cors for Cross Origin Request.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS # Allows to send sn origin to the backend through a different URL.
# Our server is protected so it cant be hit from a different url.
#Remeber our backend has a different server from our frontend and we need to access it, so the CORS enables our backend and Frontend to Interact.

app = Flask(__name__)
CORS(app) # Prevention of the error between the interaction of our backend and our frontend.

# Initialization of the database. 
#Also specification of the local db we are gonna be storing on our machine.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

#For now it's not gonna track the modifications of the database.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Creates a database instance which makes it possible to use the db we just initialized.
db = SQLAlchemy(app)