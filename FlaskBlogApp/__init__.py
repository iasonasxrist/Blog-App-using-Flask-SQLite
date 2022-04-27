
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt

from flask_login import LoginManager

app = Flask(__name__)

app.config["SECRET_KEY"] = '5c1ac729d042a22a17a39666e776d381'
app.config["WTF_CSRF_SECRET_KEY"] = '3o2vb320f042a22a17a39666e776d098'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///FlaskCourse_database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = "login"

login_manager.login_message_category = "warning"

login_manager.login_message = "Παρακαλούμε κάντε login για να μπορέσετε να δείτε αυτή τη σελίδα."

from FlaskBlogApp import routes,models