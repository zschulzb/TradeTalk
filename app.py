from flask import Flask, render_template



app = Flask(__name__) #instantiate a flask app object

#routing blocks;
#   all routing blocks use @app

@app.route('/')
def landpage():
    return render_template("home.html")

@app.route("/Sign In")
def signin():
    return render_template("signin.html")

#done routing blocks

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    # the combination of host and port are where we look for it in our browser
    # e.g. http://0.0.0.0:8080/
    # setting debug=True to see error messages - wouldn't do this on a final deployed app