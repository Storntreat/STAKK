from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
database = {}

@app.route("/teacher")
def home():
    return render_template("teacher.html")

@app.route('/submitform', methods=['POST'])
def submitform():
    fullname = request.form['preferredname-input']
    pronouns = request.form['pronouns-input']
    markgoal = request.form['markgoal-input']
    job = request.form['job-input']
    hobbies = request.form['hobbies-input']
    personality = request.form['personality-input']
    strengths = request.form['strengths-input']
    weaknesses = request.form['weaknesses-input']
    learningneeds = request.form['learningneeds-input']
    othercomments = request.form['othercomments-input']
    database[fullname] = {fullname, pronouns, markgoal, job, hobbies, personality, strengths, weaknesses,learningneeds, othercomments}
    return render_template(
        "student.html",
        fullname = fullname

    ) 
