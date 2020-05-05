from flask import Flask, redirect, url_for

app = Flask(__name__)

admin_access = False

@app.route("/")
@app.route("/home")
def index():
    return  "Hello ! This my first Web App. <h2> - Akash Patel</hr> "

@app.route("/admin_page")
def admin_page():
    return  "Hello ! This an Admin page. "


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    if admin_access:
        return redirect(url_for("admin_page"))
    else :
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()

