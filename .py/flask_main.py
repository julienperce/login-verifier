from flask import Flask; from flask import render_template

app = Flask(__name__, template_folder="../templates") # we put 2 dots to search in one directory before /templates

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/login")
def loginPage():
    return render_template("login.html")

if __name__ == "__main__":
    app.run()