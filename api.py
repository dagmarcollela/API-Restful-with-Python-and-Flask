from flask import Flask, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

users_data = {
    1: {
        "id": 1,
        "name": "Mark"
    },
    2: {
        "id": 2,
        "name": "Chloe"
    }
}

def response_users():
    return {"users": list(users_data.values())}

@app.route("/")
def root():
    return "<h1> API with FLASK </h1>"

@app.route("/users")
def list_users():
    return response_users()

@app.route("/users", methods=["POST"])
def create_user():
    body = request.json

    ids = list(users_data.keys())

    if ids:
        new_id = ids[-1] + 1
    else:
        new_id = 1
    
    users_data[new_id] = {
        "id": new_id,
        "name": body["name"]
    }
    return response_users()


app.run(debug=True)

