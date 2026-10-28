from flask import Flask, render_template

app = Flask(__name__, static_folder="assets", static_url_path="/assets")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/story")
def story():
    return render_template("story.html")


if __name__ == "__main__":
    app.run(debug=True)