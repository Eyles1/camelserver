from flask import Flask

app = Flask("app")

@app.route("/")
def app():
    return "Test"
