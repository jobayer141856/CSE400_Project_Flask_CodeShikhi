from app import *

@app.route("/SignOut", methods=["POST", "GET"])
def SignOut():
    if "email" in session:
        session.clear()
    return redirect("/")