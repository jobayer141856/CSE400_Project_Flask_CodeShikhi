from app import *
@app.route('/')
def index():
    email = session["email"]
    name = session["name"]
    return render_template("index.html", **locals())