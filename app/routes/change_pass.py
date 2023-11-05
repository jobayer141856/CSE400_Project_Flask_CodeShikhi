from app import *
@app.route('/change_pass', methods=['GET', "POST"])
def change_pass():
    if "email" in session:
        email = session["email"]
        name = session["name"]
        email_true = True

        if request.method == 'POST':
            old_password = request.form["old_pass"]
            password = request.form["new_password"]
            conf_password = request.form["confirm_password"]
            print(password)

            if password != conf_password:
                return "both new password should be same"
            
            id_x = db_user_profile.find_one({'email': email})
            passcheck = id_x['password']
            if bcrypt.checkpw(old_password.encode('utf-8'), passcheck):
                hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                db_user_profile.update_one({'_id': id_x['_id']}, {
                                    "$set": {"password": hashed}})
                return redirect("/login")
            else:
                return "Old password don't match"

    return render_template("change_pass.html", **locals())