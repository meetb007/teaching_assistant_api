from datetime import timedelta

import settings
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URL
app.config['JWT_SECRET_KEY'] = settings.JWT_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
db = SQLAlchemy(app)

app.app_context().push()

import models, views
