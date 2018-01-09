from flask import Flask, request, render_template
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__name__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def index():
    template = jinja_env.get_template('user-signup.html')
    return template.render()

@app.route('/', methods = ['POST'])
def check_input():
    return '<h1>under_construction</h1>'

@app.route('/alt', methods = ['GET'])
def index2():
    
    return render_template('user-signup.html')

@app.route('/registration', methods = ['POST'])
def checkPW():
    username = request.form['username']
    if len(username) < 3 or len(username)>20 or username.isalnum() == False:
        return render_template('user-signup.html',username = 'Alpha and Numeric only!/ Must be more than 3 character')
    
    first = request.form['First']
    if len(first) == 0 or username.isalpha() == False:
        return render_template('user-signup.html',first = 'Alpha only!',u = username)
    
    last = request.form['Last']
    if len(last) == 0 or username.isalpha() == False:
        return render_template('user-signup.html',last = 'Alpha only!', k = first, u = username)
    
    email = request.form['email']
    if len(email) < 3 or len(email) > 20:
        return render_template('user-signup.html',
        email = 'Must be between 3 to 20 character long including domain.', u = username,k = first, l = last)
    atNdot = 0
    for char in email:
        if char == '@' or char =='.':
            atNdot +=1
    if atNdot != 2:
        return render_template('user-signup.html',email = 'Invalid Email.',u = username, k = first, l = last)
    


    password = request.form['password1']

    p1 = request.form['password1']
    p2 = request.form['password2']
    if len(p1)<3 or len(p1) >20:
        return render_template('user-signup.html', password = '3-6 Character Only!',k = first, l = last, u = username, e = email)

    #    return '''<h1>Please make your Password longer than 6 character. <br>
    #Click <a href = 'http://localhost:5000/' > here</a> to return.<h1>'''
    if p1 == p2:
        template = jinja_env.get_template('confirmation.html')
        return template.render(username = username)
    else:
        return render_template('user-signup.html', password = 'Password does not match.',k = first, l = last, u = username, e = email)
    #    return '''<h1>Password do not match! 
    #<a href = 'http://localhost:5000/' > Return</a> </h1>'''


if __name__ == '__main__':
    app.run()