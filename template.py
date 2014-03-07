from flask import Flask, render_template, url_for
app = Flask(__name__, static_url_path='')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    #url_for('static/css', filename='bootstrap.css')
    #url_for('static/js', filename='jquery-1.10.2.js')
    #url_for('static/js', filename='bootstrap.js')
    return render_template('landing.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)