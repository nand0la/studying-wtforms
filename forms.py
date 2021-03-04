from wtforms import Form, validators
from wtforms.fields import StringField, BooleanField, PasswordField, SubmitField


class LoginForm(Form):
    name = StringField("Name")
    password = PasswordField("Password")
    stay_connected = BooleanField("Stay connected")
    btn_submit = SubmitField("LOGIN")


class RegisterForm(Form):
    name = StringField("Name")
    email = StringField("Email")
    password = PasswordField("Password", validators=[validators.EqualTo("comfirm_password", message="Senhas precisam ser iguais")])
    comfirm_password = PasswordField("Comfirm password")
    email_accept = BooleanField("Do you accept receiving emails with updates?")
    btn_submit = SubmitField("Register")
