from datetime import datetime
from flask import Flask, flash, render_template, redirect, url_for
from forms import ContactMeForm
from markdown import markdown
from pathlib import Path
from time import sleep
import os
import smtplib
import requests


current_year = datetime.now().year

github_projects_url = "https://api.github.com/users/ssourang/repos"

github_response = requests.get(github_projects_url).json()


gif_urls = []
repos = []
blog_posts = []

with os.scandir("blog") as blog_folder:
    for file in blog_folder:
        if file.name.endswith(".md") and file.is_file():
            raw_post_date, _ = file.name.split("_")
            post_date = datetime.strptime(raw_post_date, "%Y-%m-%d").strftime(
                "%B-%d, %Y"
            )
            post_name = _.split(".")[0]
            post_data = markdown(
                Path(file.path).read_text(),
                extensions=[
                    "fenced_code",
                    "codehilite",
                    "nl2br",
                    "markdown_captions",
                    "md_in_html",
                ],
            )
            blog_posts.append({"name": post_name, "date": post_date, "data": post_data})


ordered_blog_posts = sorted(blog_posts, key=lambda t: int(t['name'].split('-')[0]))

with open("gif_urls.txt") as gif_file:
    for line in gif_file:
        if line == "\n":
            break
        gif_url = line.strip().split("=")[1]
        gif_urls.append({"gif_url": gif_url})


for i, project in enumerate(github_response):
    name = project["name"]
    desc = project["description"]
    url = project["html_url"]

    repos.append(
        {"name": name, "desc": desc, "url": url, "gif_url": gif_urls[i]["gif_url"]}
    )


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
    return render_template("home.html", form=form, current_year=current_year)


@app.route("/projects", methods=["GET", "POST"])
def projects():

    form = ContactMeForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        msg = form.content.data
        send_mail(name, email, msg)
        flash(
            "Thank you, your message has been sent successfully ✔️ I will get back to you shortly.",
            "success",
        )
    return render_template(
        "projects.html", form=form, current_year=current_year, repos=repos
    )


@app.route("/about", methods=["GET", "POST"])
def about():

    form = ContactMeForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        msg = form.content.data
        send_mail(name, email, msg)
        flash(
            "Thank you, your message has been sent successfully ✔️ I will get back to you shortly.",
            "success",
        )
    return render_template("about.html", form=form, current_year=current_year)


@app.route("/blog/<post_name>")
def blog_listing(post_name):
    for post in blog_posts:
        if post_name == post["name"]:
            return render_template(
                "blog_entry.html",
                current_year=current_year,
                post=post,
                blog_posts=ordered_blog_posts,
            )
    return "<h1>Oops! Sorry, Blog Post Not Found</h1>"


@app.route("/blog")
def blog():
    return render_template(
        "blog_listing.html",
        current_year=current_year,
        blog_posts=ordered_blog_posts,
    )


if __name__ == "__main__":
    app.run(debug=True)
