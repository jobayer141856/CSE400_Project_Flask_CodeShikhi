from app import *
@app.route('/c_tutorial')
def c_tutorial():
    return render_template("c_tutorial.html", **locals())

@app.route('/variable')
def variable():
    return render_template("variable.html", **locals())

@app.route('/datatype')
def datatype():
    return render_template("datatype.html", **locals())

@app.route('/operations')
def operations():
    return render_template("operations.html", **locals())

@app.route('/booleans')
def booleans():
    return render_template("bool.html", **locals())

@app.route('/if_else')
def if_else():
    return render_template("if_else.html", **locals())

@app.route('/while_loop')
def while_loop():
    return render_template("while.html", **locals())

@app.route('/for_loop')
def for_loop():
    return render_template("For_loops.html", **locals())

@app.route('/array')
def array():
    return render_template("Array.html", **locals())

@app.route('/string')
def string():
    return render_template("String.html", **locals())

@app.route('/user_input')
def user_input():
    return render_template("User_Input.html", **locals())

