from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
    txt = TextAreaField('txt', default = '')

class PostForm(Form):
    post = TextField('post', validators = [Required()])

class CmntForm(Form):
    cmnt = TextField('post', validators = [Required()])
