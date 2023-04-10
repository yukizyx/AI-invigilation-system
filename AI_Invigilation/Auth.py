from flask import Flask, redirect, url_for, request

app = Flask(__name__)

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
def table():
    data = request.json
    
    status = [False] * 3
    selectedRows = [row['id'] for row in data.get('selectedRows')]
    for checked_id in selectedRows:
        status[checked_id - 1] = True
    
    # send trigger status to backend
    print(f'Trigger Status: {status}')
    return {'success': True}

if __name__ == '__main__':
    app.run(debug = True) 