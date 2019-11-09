from flask_sqlalchemy import SQLAlchemy
from config import *
from app import *


app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)
from models.Goods import *


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

