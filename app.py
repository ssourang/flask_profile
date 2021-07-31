from datetime import datetime
from flask import Flask, flash, render_template, redirect, url_for
from forms import ContactMeForm
import os
import smtplib
import requests

github_projects_url = "https://api.github.com/users/ssourang/repos"

github_response = requests.get(github_projects_url).json()

repos = []

for project in github_response:
    name = project["name"]
    desc = project["description"]
    url = project["html_url"]

    repos.append({"name": name, "desc": desc, "url": url})


# print(github_response)


app = Flask(__name__)
app.config["SECRET_KEY"] = "willchangelater"


YAHOO_EMAIL = os.environ.get("YAHOO_EMAIL")
YAHOO_PASSWORD = os.environ.get("YAHOO_PASSWORD")
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")


def send_mail(name, email, msg):
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=YAHOO_EMAIL, password=YAHOO_PASSWORD)
        connection.sendmail(
            from_addr=YAHOO_EMAIL,
            to_addrs=MAIL_USERNAME,
            msg=f"""Subject: Get In Touch\n\nFrom your portfolio Website:\n\nName: {name}
\nEmail: {email}\n\nMessage: {msg}""",
        )


def current_year():
    year = datetime.now().year
    return year


@app.route("/", methods=["GET", "POST"])
def home():

    form = ContactMeForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        msg = form.content.data
        send_mail(name, email, msg)
        flash(
            "Thank you, your message has been sent successfully ✔️ I will get back to you shortly.",
            category="success",
        )
        return redirect(url_for("home"))
    return render_template("home.html", form=form, current_year=current_year())


@app.route("/projects")
def projects():

    form = ContactMeForm()
    if form.validate_on_submit():
        flash(
            "Thank you, your message has been sent successfully ✔️ I will get back to you shortly.",
            "success",
        )
    return render_template(
        "projects.html", form=form, current_year=current_year(), repos=repos
    )


@app.route("/about")
def about():

    form = ContactMeForm()
    if form.validate_on_submit():
        flash(
            "Thank you, your message has been sent successfully ✔️ I will get back to you shortly.",
            "success",
        )
    return render_template("about.html", form=form, current_year=current_year())


if __name__ == "__main__":
    app.run(debug=True)
