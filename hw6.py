from flask import Flask, render_template, url_for
from flask_db import User
app = Flask(__name__, static_url_path='')

class nav:
    def __init__(self, href, caption):
        self.href = href
        self.caption = caption
    

@app.route('/home/')
def hello(name=None): 
    navigation = [nav('http://www.reddit.com/', 'Reddit'), nav('http://www.dogevault.com/', 'Dogevault'), nav('http://www.gmail.com/','GMail')]
    return render_template('template.html', navigation=navigation)

@app.route('/users/')
def users(userList=None):
    ulist = User.query.all()
    return render_template('template.html', userList=ulist)

if __name__ == '__main__':
    app.run(debug=True)