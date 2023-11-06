from app import *
@app.route('/contact_us')
def contact_us():
    if "email" in session:
        email = session["email"]
        name = session["name"]
        email_true = True
    return render_template("contact.html", **locals())