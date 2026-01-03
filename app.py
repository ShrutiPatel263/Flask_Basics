from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskTopics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Todo(db.column):
    srNo=db.comumn(db.integer,primary_key=True)
    title=db.comumn(db.string(200),nullable=False)
    desc=db.comumn(db.string(500),nullable=False)
    data_created=db.column(db.DateTime,default=datetime.utcnow)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/MyProducts")
def my_products():
    return "<p>My Products Page</p>"

if __name__ == "__main__":
    app.run(debug=True,port=8000)