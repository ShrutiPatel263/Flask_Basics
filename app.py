from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/MyProducts")
def my_products():
    return "<p>My Products Page</p>"

if __name__ == "__main__":
    app.run(debug=True,port=8000)