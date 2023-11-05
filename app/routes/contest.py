from app import *
@app.route('/contest', methods=['GET', "POST"])
def contest():
    if "email" in session:
        email = session["email"]
        name = session["name"]
        email_true = True
    return render_template("contest.html", **locals())