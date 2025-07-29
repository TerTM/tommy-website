from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title':'Learner',
        'location':'Tangerang',
        'salary':'0'
    },
    {
        'id': 2,
        'title':'Backend Engineer',
        'location':'San Francisco, USA',
        'salary':'$120,000'
    },
    {
        'id':3,
        'title':'Analyst',
        'location':'Remote',
    }
]

@app.route("/")
def home():
    return render_template('home.html', jobs=JOBS) 

@app.route("/api/jobs")
def job():
    return jsonify(JOBS)

@app.route("/another")
def another():
    return render_template('another.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)