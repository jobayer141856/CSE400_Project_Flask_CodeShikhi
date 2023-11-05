import webbrowser
from bson import ObjectId
import requests
import stdin
import json
from app import *
@app.route('/problems' , methods=['GET', "POST"])

def problems():

    if "email" in session:
        email = session["email"]
        name = session["name"]
        email_true = True
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
        return render_template("problems.html", **locals())
    else:
       return redirect(url_for("login")) 

@app.route('/view/<string:s>', methods=['GET', "POST"])
def view(s):
    s =str(s)
    p = 2
    c=0
    viewprob = []
    if "email" in session:
        email = session["email"]
        name = session["name"]
        email_true = True
    ed = db_admin_problemset.find_one({"_id": ObjectId(s)})
    viewprob.append(ed["_id"])
    viewprob.append(ed["problem_title"])
    viewprob.append(ed["problem_details"])
    viewprob.append(ed["input"])
    viewprob.append(ed["output"])
    return render_template("problem_solve.html", **locals())

@app.route('/compile/<string:s>', methods=['POST'])
def compile_code(s):
    s =str(s)
    viewprob = []
    ed = db_admin_problemset.find_one({"_id": ObjectId(s)})
    viewprob.append(ed["_id"])
    viewprob.append(ed["problem_title"])
    viewprob.append(ed["problem_details"])
    viewprob.append(ed["input"])
    viewprob.append(ed["output"])

    if "email" in session:
        email = session["email"]
        name = session["name"]
        email_true = True
    code = request.form['code']  # Get the user's code from the request
    url = 'https://api.jdoodle.com/v1/execute'  # Replace 'API_URL' with the actual API endpoint
    print(code)
    if request.form['submit_button'] == "Submit":
        submit = True
    # Create a payload with the code
        payload = {
            'clientId': 'b5976d432804e8b418c899eb84f0725a',
            'clientSecret': '4791c13dc4e6a1bde497a1a484bbed0c9e29881dcc145d8b4231f11336b869c',
            'script': code,
            'language': 'c',
            'versionIndex': '0',
            'compileOnly': 'false'
        }
        # Make a request to the online compiler API
        response = requests.post(url, json=payload)
        response_data = response.json()
        print(response_data)
        if 'output' in response_data:
            result = response_data['output']
            if result == viewprob[4]:
                Output = "Right answer and submitted"
                print(Output)
                db_user = db_user_profile.find_one({"email": email})
                print(email)
                print(db_user)
                if db_user:
                    db_user_problem_solved.update_one({'_id':db_user['_id']},{"$set" : {"problem_id" :viewprob[0]}})
                    db_user_problem_solved.update_one({'_id':db_user['_id']},{"$set" : {"problem_title" :viewprob[1]}})
                    db_user_problem_solved.update_one({'_id':db_user['_id']},{"$set" : {"problem_details" :viewprob[2]}})
                    db_user_problem_solved.update_one({'_id':db_user['_id']},{"$set" : {"input" :viewprob[3]}})
                    db_user_problem_solved.update_one({'_id':db_user['_id']},{"$set" : {"output" :viewprob[4]}})
                    db_user_problem_solved.update_one({'_id':db_user['_id']},{"$set" : {"source_code_solved_by_user" :code}})
        else:
            result = 'Error: Failed to retrieve output.'
            print(response.content)
        return render_template('problem_solve.html', **locals())
    
    if request.form['Hints_button'] == "Hints":
        hints = True

        return render_template('problem_solve.html', **locals())
