from app import *
@app.route('/')
def index():
    if "email" in session:
        email = session["email"]
        name = session["name"]
        email_true = True
    return render_template("index.html", **locals())