from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index_multiple_Values.html", username = name, email= "abc@myemail.com" )

if __name__ == "__main__":
    app.run()