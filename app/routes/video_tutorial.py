from app import *
@app.route('/video_tutorial')
def video_tutorial():
    if "email" in session:
        email = session["email"]
        name = session["name"]
        email_true = True
    return render_template("video_tutorial.html", **locals())