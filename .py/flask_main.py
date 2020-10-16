from flask import Flask; from flask import render_template, request

app = Flask(__name__, template_folder="../templates") # we put 2 dots to search in one directory before /templates

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def loginPage():
    return render_template("login.html")

@app.route("/login/page2")
def page2():
    return render_template("page2.html")

if __name__ == "__main__":
    app.run()