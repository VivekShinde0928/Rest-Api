from app_using_RESTful-Flask_JWT import app
from db import db

db.init_app(app)

# by using this our table get created by name data.db & no need to make create_table.py
@app.before_first_request
def create_table():
    db.create_all()
