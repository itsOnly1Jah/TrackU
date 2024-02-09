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


def tracker_color(tracker_name):
    match tracker_name:
        case "Amazon":
            return "bg-cyan-500"
        case "Ebay":
            return "bg-violet-500"
        case "Best Buy":
            return "bg-amber-400"
        case _:
            return "bg-zinc-400"


def map_items(fn, items):
    return map(fn, items)


def wrap(el, item, options=""):
    return f'<{el} {options}">{item}</{el}>'


def tracker_button(tracker):
    return wrap('button', tracker, f'class="{tracker_color(tracker)} py-1 px-3 text-white text-sm font-semibold rounded-full shadow focus:outline-none')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/table")
def table():
    return render_template('table.html', map_items=map_items, items=db_entries, tracker_button=tracker_button)


@app.route("/chart")
def chart():
    return render_template('chart.html', item=db_entries[0])
