from flask import Flask

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

app.run(debug=True)

