from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/auth-supervisor", methods=['POST'])
def get_dates():
    #Try this code
    email = request.json['email']
    print(email)
    return email
    # return jsonify({"email":email})

if __name__ == '__main__':
    app.run(debug = True)