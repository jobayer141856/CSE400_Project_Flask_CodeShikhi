from app import *
@app.route("/admin_SignOut", methods=["POST", "GET"])
def admin_SignOut():
    if "email" in session:
        session.clear()
    return redirect("/")