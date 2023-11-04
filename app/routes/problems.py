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
    viewprob = []
    ed = db_admin_problemset.find_one({"_id": ObjectId(s)})
    viewprob.append(ed["problem_title"])
    viewprob.append(ed["problem_details"])
    viewprob.append(ed["input"])
    viewprob.append(ed["output"])
    viewprob.append(ed["_id"])
    return render_template("problem_solve.html", **locals())


@app.route('/compile', methods=['POST'])
def compile_code():
    code = request.form['code']  # Get the user's code from the request
    url = 'https://api.jdoodle.com/v1/execute'  # Replace 'API_URL' with the actual API endpoint
    print(code)
    # Create a payload with the code
    payload = {
        'clientId': 'b5976d432804e8b418c899eb84f0725a',
        'clientSecret': '3d6d9dae1a9be42f9595d6b7a171b1280d1537157d91c406a06fbee046e4f630',
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
    else:
        result = 'Error: Failed to retrieve output.'
        print(response.content)
    return render_template('result.html', **locals())