from flask import Flask, render_template


app = Flask(__name__)

db_entries = ["4060", "XBOX", "PS5"]

trackers = [
    {"name": "EBay", "value": [56, 55, 40, 81, 65, 59, 80]},
    {"name": "Best Buy", "value": [65, 59, 80, 81, 56, 55, 40]},
    {"name": "Amazon", "value": [34, 55, 70, 91, 65, 55, 40]}
]


@app.route("/list")
def item():
    return render_template('list.html', items=db_entries)


@app.route("/chart")
def chart():
    return render_template('chart.html', items=trackers)
