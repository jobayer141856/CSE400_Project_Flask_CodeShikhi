import webbrowser
from bson import ObjectId
import requests
import stdin
import json
from app import *
import os
import sys
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain. llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "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"

loader = TextLoader('app/routes/data.txt', encoding = 'UTF-8')

index = VectorstoreIndexCreator().from_loaders([loader])

def process_user_query(user_query):
    try:
        # Call your langchain code with the user's query
        response = index.query(user_query, ChatOpenAI())
        return response
    except Exception as e:
        return f"Error: {str(e)}"

dict_for_solved_by_user = {}
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
            prob_list[i] = [prob_title["_id"], str(prob_title["problem_title"]), str(prob_title["problem_details"]),str(prob_title["input"]),str(prob_title["output"]), str(len(prob_title["total_solved"]))]
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
        session["count"] = c
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
    viewprob.append(ed["total_solved"])
    viewprob.append(ed["source_code"])

    if "email" in session:
        email = session["email"]
        name = session["name"]
        email_true = True
        c = session["count"]
    code = request.form['code']  # Get the user's code from the request
    url = 'https://api.jdoodle.com/v1/execute'  # Replace 'API_URL' with the actual API endpoint
    print(code)
    if request.form['submit_button'] == "Submit":
        submit = True
        StdIn = viewprob[3]
        c+=1
        session["count"] = c
        # Create a payload with the code
        payload = {
            'clientId': 'b5976d432804e8b418c899eb84f0725a',
            'clientSecret': '4791c13dc4e6a1bde497a1a484bbed0c9e29881dcc145d8b4231f11336b869c',
            'script': code,
            'stdin': StdIn,
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
            if str(result) == str(viewprob[4]):
                Output = "Right answer and submitted"
                print(Output)
                db_user = db_user_profile.find_one({"email": email})
                dict_for_solved_by_user = dict(viewprob[5])
                print(dict_for_solved_by_user)
                if email in dict_for_solved_by_user.keys():
                    dict_for_solved_by_user.update({email: code})
                    print("if er moddhe", dict_for_solved_by_user)
                else:
                    dict_for_solved_by_user[email] = code
                    print("else er moddhe" , dict_for_solved_by_user)
                db_admin_problemset.update_one({'_id':ed['_id']}, {"$set" : {"total_solved" :dict_for_solved_by_user}})
            else:
                Output = "Wrong answer and not submitted"  
        else:
            result = 'Error: Failed to retrieve output.'
            Output = "Wrong answer and not submitted"
            print(response.content)
        return render_template('problem_solve.html', **locals())
    
    elif request.form['submit_button'] == "Hints":
        hints = True
        # print(request.form['hints_button'])
        c+=1
        session["count"] = c
        hints_for_code = viewprob[2] + 'For this Problem suggest the logic of this problem not source code for c progamming language and only suggest code of logic not full code'
        response = process_user_query(hints_for_code)
        print(response)
        return render_template('problem_solve.html', **locals())
    
    elif request.form['submit_button'] == "Source Code":
        source = True
        source_code =  viewprob[6]
        print(source_code)
        return render_template('problem_solve.html', **locals())