from bson import ObjectId
from app import *
@app.route('/admin' , methods=['GET', "POST"])
def admin():
     if "email" in session:
        email = session["email"]
        email_true = True
     return render_template("admin.html", **locals())

@app.route('/admin_problemset', methods=['GET', "POST"])
def admin_problemset():
    title_list = []
    title_id = []
    len_list = []
    prob_list = {}
    i=0
    for prob_title in db_admin_problemset.find():
        title_list.append(prob_title["problem_title"])
        title_id.append(prob_title["_id"])
        prob_list[i] = [prob_title["_id"], str(prob_title["problem_title"]), str(prob_title["problem_details"]),str(prob_title["input"]),str(prob_title["output"])]
        i+=1
    len_list = len(title_list) 
    is_post = False
    is_prob = False
    view_prob = []
    if request.method == 'POST':
        is_post = True
        form_data = dict(request.form)
        id = form_data["id"]  
        id = str(id)
        probs = []
        for prob_view in db_admin_problemset.find({"_id": ObjectId(id)}):
            probs.append(prob_view["problem_title"])
            probs.append(prob_view["problem_details"])
            probs.append(prob_view["input"])
            probs.append(prob_view["output"])
            probs.append(prob_view["source_code"])
            is_prob = True
    return render_template("admin_problemset.html", **locals())

@app.route('/add_problem', methods=['GET', "POST"])
def admin_add_problem():
    if request.method == "POST":
        form_data = dict(request.form)
        form_title = form_data["title"]
        form_textarea = form_data["details"]
        form_input = form_data["input"]
        form_output = form_data["output"]
        form_source_code = form_data["source_code"]
        print(form_data)
        db_admin_problemset.insert_one(
            {"problem_title": form_title, "problem_details": form_textarea , "input":form_input,  "output":form_output, "source_code":form_source_code})
        return redirect(url_for('admin_problemset'))
    return render_template("admin_add_problem.html", **locals())


@app.route('/update/<string:s>', methods=['GET', "POST"])
def edit(s):
    s =str(s)
    p = 2
    edprob = []
    ed = db_admin_problemset.find_one({"_id": ObjectId(s)})
    edprob.append(ed["problem_title"])
    edprob.append(ed["problem_details"])
    edprob.append(ed["input"])
    edprob.append(ed["output"])
    edprob.append(ed["source_code"])
    edprob.append(ed["_id"])
    if request.method=='POST':
        print("blog")
        print(request.form["prob"])
        db_admin_problemset.update_one({"_id": ObjectId(s)},  {"$set" : {"problem_details" :request.form["prob"]}})
        db_admin_problemset.update_one({"_id": ObjectId(s)}, {"$set" : {"problem_title" :request.form["title"]}})
        db_admin_problemset.update_one({"_id": ObjectId(s)}, {"$set" : {"input" :request.form["input"]}})
        db_admin_problemset.update_one({"_id": ObjectId(s)}, {"$set" : {"output" :request.form["output"]}})
        db_admin_problemset.update_one({"_id": ObjectId(s)}, {"$set" : {"source_code" :request.form["source_code"]}})
        print("Updated")
        return redirect(url_for('admin_problemset'))

    return render_template("admin_update_problem.html", **locals())

@app.route('/delete/<string:s>', methods=['GET', "POST"])
def delete(s):
    s =str(s)
    if db_admin_problemset.delete_many({'_id': ObjectId(s)}):
        return redirect(url_for('admin_problemset'))

    return render_template("admin_problemset.html")
