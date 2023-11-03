from app import *
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        print(request.form)
        username = request.form["username"]
        password = request.form["password"]
        name_found = db_user_profile.find_one({'username':username})
        name_found2 = db_user_profile.find_one({'username': username})
        if name_found:
            name = name_found['username']
            passcheck = name_found['password']
            if bcrypt.checkpw(password.encode('utf-8'), passcheck):
                session["username"] = name
                return redirect(url_for("home"))
            else:
                return "Wrong Password"
        elif name_found2:
            name = name_found2['username']
            passcheck = name_found2['password']

            if bcrypt.checkpw(password.encode('utf-8'), passcheck):
                session["username"] = name
                return redirect(url_for("home"))
            else:
                return "Wrong Password"

        return "Username not found"
    return render_template("login.html", **locals())