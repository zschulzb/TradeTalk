from flask import render_template
from app import app

LOGGED_IN = False

@app.route('/')

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Zach'}
    post = [
        {},
        {}
    ]
    return render_template('index.html', user=user, post=post)

@app.route('/Home_Page')
def userpage():
    user = {'username':'Zach'}
    post = [
        {
            'author': {'username': 'Andrew'},
            'body': 'Beautiful Craftsmanship!'
        },
        {
            'author': {'username': 'Munish'},
            'body': 'Best handyman experience!'
        }
    ]
    return render_template("userpage.html", user=user, post=post)

@app.route("/Sign_In")
def signin():
    user = {'username':'Zach'}
    post = [
        {},
        {}
    ]
    return render_template("signin.html", user=user, post=post)

@app.route("/About_Us")
def aboutus():
    user = {'username':'Zach'}
    post = [
        {},
        {}
    ]
    return render_template("aboutus.html", user=user, post=post)

#end block routes

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    # the combination of host and port are where we look for it in our browser
    # e.g. http://0.0.0.0:8080/
    # setting debug=True to see error messages - wouldn't do this on a final deployed app