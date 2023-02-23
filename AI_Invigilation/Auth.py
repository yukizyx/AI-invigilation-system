from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/auth-supervisor',methods = ['POST', 'GET'])
def sup_login():
    if request.method == 'POST':
        user_id = request.form['id']
        code = request.form['code']
        
        if (user_id in ["sup1", "sup2", "sup3"]) and (code == "11223344"):
            return redirect('http://localhost:3000/supervisor-home')

@app.route('/auth-staff',methods = ['POST', 'GET'])
def stf_login():
    if request.method == 'POST':
        user_id = request.form['id']
        code = request.form['code']
        
        if (user_id in ["stf1", "stf2", "stf3"]) and (code == "11223344"):
            return redirect('http://localhost:3000/staff-home')

if __name__ == '__main__':
    app.run(debug = True)