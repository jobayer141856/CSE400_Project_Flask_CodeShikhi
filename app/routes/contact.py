from app import *
@app.route('/contact_us', methods=['GET','POST'])
def contact_us():
    if "email" in session:
        email = session["email"]
        name = session["name"]
        email_true = True
    if request.method=='POST':
        send_msg = True
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        send_message = {'email': email, 'subject': subject, 'message' :message }
        technical_issue_face.insert_one(send_message)
        return render_template("contact.html", **locals())

    return render_template("contact.html", **locals())