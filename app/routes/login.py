from app import *
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        print(request.form)
        email = request.form["email"]
        password = request.form["password"]
        email_found = db_user_profile.find_one({'email':email})

        if email_found:
            email_f = email_found['email']
            passcheck = email_found['password']
            if bcrypt.checkpw(password.encode('utf-8'), passcheck):
                session["email"] = email_f
                session["name"] = email_found['name']
                return redirect(url_for("index"))
            else:
                return "Wrong Password"
        return "Username not found"
    return render_template("login.html", **locals())