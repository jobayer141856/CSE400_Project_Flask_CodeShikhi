from app import *
@app.route('/admin_login', methods=['GET','POST'])
def admin_login():
    if request.method=='POST':
        print(request.form)
        email = request.form["email"]
        password = request.form["password"]
        email_found = db_admin_profile.find_one({'email':email})
        if email_found:
            email_f = email_found['email']
            passcheck = email_found['password']
            if passcheck == password:
                session["email"] = email_f
                return redirect(url_for("admin"))
            else:
                return "Wrong Password"
        return "Username not found"
    return render_template("admin_login.html", **locals())