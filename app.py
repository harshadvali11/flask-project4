from flask import Flask,render_template,request

from flask_wtf import Form

from wtforms import StringField,SubmitField



AI=Flask(__name__)
AI.config['SECRET_KEY']='csrfToken'

@AI.route('/firsthtml',methods=['GET','POST'])
def firsthtml():
    if request.method=='POST':
        form_data=request.form
        return form_data['name']

    return render_template('firsthtml.html')


class NameForm(Form):
    name=StringField()
    submit=SubmitField()

@AI.route('/flaskWTF',methods=['GET','POST'])
def flaskWTF():
    form=NameForm()
    if request.method=='POST':
        fd=NameForm(request.form)
        if fd.validate():
            return fd.name.data



    return render_template('flaskWTF.html',form=form)











if __name__=='__main__':
    AI.run(debug=True)














