from app import *
@app.route('/animation_tutorial')
def animation_tutorial():
    if "email" in session:
        email = session["email"]
        name = session["name"]
        email_true = True
    return render_template("animation_tutorial.html", **locals())