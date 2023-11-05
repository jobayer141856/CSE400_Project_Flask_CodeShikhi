from app import *
@app.route('/change_pass')
def change_pass():
    if "email" in session:
        email = session["email"]
        name = session["name"]
        email_true = True

        if request.method == 'POST':
            password = request.form["oldpass"]
            password1 = request.form["newpass"]
            password2 = request.form["newconfpass"]

        if password1 != password2:
            return "both new password should be same"
        
        id_x = db_user_problem_solved.find_one({'email': email})

        if id_x:
            passcheck = id_x['password']
        if bcrypt.checkpw(password.encode('utf-8'), passcheck):
            hashed = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
            db_user_profile.update_one({'_id': id_x['_id']}, {
                                "$set": {"password": hashed}})
            return redirect("/login")
        else:
            return "Old password don't match"

    return render_template("change_pass.html", **locals())