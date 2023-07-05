from app import *
@app.route('/c_tutorial')
def c_tutorial():
    return render_template("c_tutorial.html", **locals())