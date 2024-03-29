from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks_flask.db"
app.secret_key = '123456789'

login_manager = LoginManager(app)
db = SQLAlchemy(app)



from views import *
from models import *

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)