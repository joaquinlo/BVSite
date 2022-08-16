from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('dbc.DatabaseConfig')
db = SQLAlchemy(app)

import application.routes.home
import application.routes.reports

with app.app_context():
    db.create_all()