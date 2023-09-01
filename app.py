from flask import Flask , render_template , jsonify
app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru , India',
        'salary': 'Rs . 1000000',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Bengaluru , India',
        'salary': 'Rs . 2500000'
    },
    {
        'id': 3,
        'title': 'Frontend Dev',
        'location': 'Remote',
        'salary': 'Rs . 1300000'
    },
    {
        'id': 4,
        'title': 'Backend Dev',
        'location': 'New Delhi , India',
        'salary': 'Rs . 1800000'
    },
]
@app.route("/")
def hello_world():
    return render_template('home.html',
                           jobs = JOBS,
                           company_name = "Alpha Careers" )


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__" :
    print("Im inside the if")
    app.run("0.0.0.0", debug=True)
