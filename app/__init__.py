from flask import Flask
from app import connection

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "secret_key"

from app import views

connected = connection.getConnection(app)