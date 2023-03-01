from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru,India',
    'salary':'Rs. 10,000,000'
  },
    {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi,India',
    'salary':'Rs. 15,000,000'
  },
    {
    'id':3,
    'title':'Frontend Engineer',
    'location':'remote'
  },
    {
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco,USA',
    'salary':'Rs. 120,000'
  }
]

@app.route('/') 
def hello_world():
  return render_template('home.html',jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

@app.route('/login', methods=['POST', 'GET'])
def login():
   
    return render_template('login.html',)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
   
    return render_template('signup.html',)

if __name__==__name__:
   app.run(host='0.0.0',debug=True)
  
  
