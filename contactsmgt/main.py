from flask import flash,redirect,Flask, render_template, url_for
from datetime import datetime
from form import New,Box
from flask_bootstrap import Bootstrap4

Allcontacts=[]
year=datetime.now().year
app=Flask(__name__)
bootsrap=Bootstrap4(app)
app.secret_key='christian'
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home',year=year)
@app.route('/Add', methods=['POST', 'GET'])
def add():
    my_form=New()
    form=my_form
    if form.validate_on_submit():
        
        username=form.name.data
        usercontacts=form.contacts.data
        flash (f'contact {username} succefully created')
        li={'username':username,'contacts':usercontacts}
        Allcontacts.append(li)
        return redirect(url_for('all'))
    return render_template('user.html', title='Add contact',year=year, form=form)
@app.route('/All')
def all():
    return render_template('all.html', title='All Contacts',year=year,contacts=Allcontacts)

    

if __name__=='__main__':
    app.run(debug=True)