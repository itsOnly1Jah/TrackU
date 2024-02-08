from flask import Flask, render_template
from flask_assets import Bundle, Environment


app = Flask(__name__)


assets = Environment(app)
css = Bundle("css/styles.css", output="css/tailwind.css")

assets.register("css", css)
css.build()

trackers = {
    "Amazon": [34, 55, 70, 91, 65, 55, 40],
    "EBay": [56, 55, 40, 81, 65, 59, 80],
    "Best Buy": [65, 59, 80, 81, 56, 55, 40]
}

db_entries = [
    {"name": "4060", "tracker": trackers},
    {"name": "XBOX", "tracker": trackers},
    {"name": "PS5", "tracker": trackers}
]


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/table")
def table():
    return render_template('table.html', items=db_entries)


@app.route("/chart")
def chart():
    return render_template('chart.html', item=db_entries[0])
