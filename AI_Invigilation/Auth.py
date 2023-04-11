from flask import Flask, redirect, url_for, request, jsonify
from src.action_queue import *
app = Flask(__name__)

ac = ActionQueue()

@app.route('/auth-supervisor',methods = ['POST', 'GET'])
def sup_login():
    if request.method == 'POST':
        user_id = request.form['id']
        code = request.form['code']  
        pass_supervisor = hash(user_id)
        print(pass_supervisor)
        
        if (user_id in ["sup1", "sup2", "sup3"]) and (code == "11223344"):
            return redirect('http://localhost:3000/supervisor-home')
        else:
            return redirect('http://localhost:3000/auth-supervisor')
        

@app.route('/auth-staff',methods = ['POST', 'GET'])
def stf_login():
    if request.method == 'POST':
        user_id = request.form['id']
        code = request.form['code']
        pass_staff = hash(user_id)
        print(pass_staff)
        
        if (user_id in ["stf1", "stf2", "stf3"]) and (code == "11223344"):
            return redirect('http://localhost:3000/staff-home')
        else:
            return redirect('http://localhost:3000/auth-staff')

@app.route('/supervisor-home', methods=['POST'])
def triggers():
    data = request.json
    
    status = [False] * 3
    selectedRows = [row['id'] for row in data.get('selectedRows')]
    for checked_id in selectedRows:
        status[checked_id - 1] = True
    
    # send trigger status to backend
    ac.add_action(SET_TRIGER, status)
    # print(f'Trigger Request: {status}')
    return {'success': True}

@app.route('/supervisor-home/setup-cams', methods=['POST'])
def cams():
    data = request.json
    
    status = [False] * 2
    ac.add_action(SET_CAMERA, status)
    selectedRows = [row['id'] for row in data.get('selectedRows')]
    for checked_id in selectedRows:
        status[checked_id - 1] = True
    
    # send cam status to backend
    # print(f'Cam Status: {status}')
    return {'success': True}

data = {
    1: {'date': '2022/01/01', 'name': 'MATH 1A03 Final Exam'},
    2: {'date': '2021/11/20', 'name': 'MATH 1A03 Midterm Exam'},
    3: {'date': '2021/07/26', 'name': 'MATH 1B03 Midterm Exam'},
}

@app.route('/Auth/data', methods=['GET'])
def get_data():
    return jsonify(data)


def start_flask():
    app.run(debug = False)

if __name__ == '__main__':
    app.run(debug = True) 