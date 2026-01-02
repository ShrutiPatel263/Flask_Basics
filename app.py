from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/MyProducts")
def my_products():
    return "<p>My Products Page</p>"

if __name__ == "__main__":
    app.run(debug=True,port=8000)