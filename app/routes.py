from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Henry'}
    posts = [
        {
            'author':{'username':'Nicholas'}, 
            'body':'There exist infinitely many prime natural numbers'
        },
        {
            'author':{'username':'Sophie'}, 
            'body':'The LAST Averngers movie was..aight'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    