from flask import Flask, render_template, json, request
#from flask.ext.mysql import MySQL

# Create a flask app
app = Flask(__name__)

# Define route and request handler
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/showSignup")
def showSignup():
    return render_template("signup.html")

@app.route("/home")
def home():
    return main()

@app.route("/signUp", methods=["POST"])
def signUp():
    # read posted values from UI
    _name = request.get_json()["fname"]
    _email = request.get_json()["femail"]
    _password = request.get_json()["fpassword"]
    # validation of recived values
    if _name and _email and _password:
        return json.dumps({"html":"<span>Everything went ok!</span>"})
    else:
        return json.dumps({"html":"<span>You must complete all information to sign up.</span>"})


if __name__ == "__main__":
    app.run()
