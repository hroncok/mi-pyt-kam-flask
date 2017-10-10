from flask import Flask, render_template

app = Flask(__name__)

if app.config.get('DEBUG'):
    app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
