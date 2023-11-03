from app import *

otp = randint(000000,999999)
@app.route('/verify', methods=['GET','POST'])
def verify():
    msg_otp = ""
    name = session["name"] 
    email = session["email"] 
    hashed = session["password"]

    msg = Message('Verify Email-OTP',sender='meetyourmentor150@gmail.com',recipients=[email])
    msg.body = str(otp)
    mail.send(msg)
    if request.method=='POST':
        userotp = request.form["otp"]
        if otp==int(userotp):
            msg_otp = "OTP Verified Successfully!"
            user_input = {'name': name,  'email': email, 'password': hashed }
            db_user_profile.insert_one(user_input)
            session.clear()
            return redirect(url_for("login"))
        else:
            return "Wrong OTP"

    return render_template("verify.html")