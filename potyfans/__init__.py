from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '503d9da0a2295b54fea4796867e41ff8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///potyfans.db'

database = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'
login_manager.login_message = 'Faça login para prosseguir.'


from potyfans import routes
