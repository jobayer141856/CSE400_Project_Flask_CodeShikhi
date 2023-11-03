from app import*
@app.route('/SignUp', methods=['GET','POST'])
def SignUp():
    if request.method=='POST':
        name = request.form["name"]
        email = request.form["email"]
        password1 = request.form["password"]
        password2 = request.form["confirm-password"]
        print(request.form)
 
        email_found = db_user_profile.find_one({"email": email})
        if email_found:
            message = 'This email already exists in database'
            return message
           
        elif password1 != password2:
            message = 'Passwords should match!'
            return message
        else:
            hashed = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
            # print(session[username])
            session["name"] = name
            session["email"] = email
            session["password"] = hashed
            return redirect(url_for("verify"))
    return render_template("SignUp.html", **locals())