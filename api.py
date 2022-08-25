from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1> API with FLASK </h1>"

app.run(debug=True)

