from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

LOGGED_IN = False


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

@app.route("/Sign_In", methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    user = {}
    post = [{},{}]
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={})'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template("signin.html", user=user, post=post, form=form)

@app.route("/About_Us")
def aboutus():
    user = {}
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