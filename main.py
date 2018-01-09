from flask import Flask, request
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__name__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def user():
    template = jinja_env.get_template('user-signup.html')
    return template.render()

@app.route('/registration', methods = ['POST'])
def sucess():
    name = request.form['First']
    p1 = request.form['password1']
    p2 = request.form['password2']
    if len(p1)<6:
        return '''<h1>Please make your Password longer than 6 character. <br>
    Click <a href = 'http://localhost:5000/' > here</a> to return.<h1>'''
    if p1 == p2:
        template = jinja_env.get_template('confirmation.html')
        return template.render(name = name)
    else:
        return '''<h1>Password do not match! 
    <a href = 'http://localhost:5000/' > Return</a> </h1>'''


if __name__ == '__main__':
    app.run()