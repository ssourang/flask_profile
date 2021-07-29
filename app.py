from flask import Flask, render_template, request, flash
from forms import ContactMeForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "willchangelater"


@app.route("/", methods=["GET", "POST"])
def home():

    form = ContactMeForm()
    if form.validate_on_submit():
        flash(
            "Thank you, your message has been sent! I will get back to you shortly.",
            "success",
        )
    return render_template("home.html", form=form)


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
