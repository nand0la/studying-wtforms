from flask import Flask, render_template, request, jsonify
from forms import LoginForm, RegisterForm
from db import db


app = Flask(__name__)


@app.route("/login", methods=["POST", "GET"])
def login():
    form_login = LoginForm(request.form)

    if request.method == "POST":
        return jsonify({
            "name": form_login.name.data,
            "password": form_login.password.data,
            "stay connect": form_login.stay_connected.data,
        })

    return render_template("login.jinja2", form=form_login)


@app.route("/register", methods=["POST", "GET"])
def register():
    form_register = RegisterForm(request.form)
    
    if request.method == "POST":
        return jsonify({
            "name": form_register.name.data,
            "email": form_register.email.data,
            "password": form_register.password.data,
            "comfirm_password": form_register.comfirm_password.data,
            "email accept": form_register.email_accept.data
        })


    return render_template("register.jinja2", form=form_register)


if __name__ == "__main__":
	app.run(debug=True)
