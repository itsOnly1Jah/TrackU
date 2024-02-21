from api import api
from main import app

from flask import render_template
from flask_assets import Bundle, Environment

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


def int_db():
    from os import getenv
    from dotenv import load_dotenv
    from psycopg import connect
    load_dotenv('.env')
    conn = connect(host=getenv('pgserver'), dbname='tracku', user='postgres', password=getenv('pgpassword'))
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS api (name text PRIMARY KEY, key text)")
    cursor.execute("CREATE TABLE IF NOT EXISTS products (id uuid PRIMARY KEY, name text, trackers jsonb)")
    conn.commit()
    cursor.close()
    conn.close()


def tracker_color(tracker_name):
    match tracker_name:
        case "amazon":
            return "bg-cyan-500"
        case "ebay":
            return "bg-rose-700"
        case "bestbuy":
            return "bg-amber-400"
        case _:
            return "bg-zinc-400"


def map_items(fn, items):
    return map(fn, items)


def wrap(el, item, options=""):
    return f'<{el} {options}">{item}</{el}>'


def tracker_button(tracker):
    return wrap('button', tracker, f'class="{tracker_color(tracker)} py-1 px-3 text-white text-sm font-semibold rounded-full shadow focus:outline-none')


int_db()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/table")
def table():
    from os import getenv
    from dotenv import load_dotenv
    from psycopg import connect
    load_dotenv('.env')
    conn = connect(host=getenv('pgserver'), dbname='tracku', user='postgres', password=getenv('pgpassword'))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = []
    for product in cursor.fetchall():
        products.append({"id": product[0], "name": product[1], "trackers": product[2]})
    cursor.close()
    conn.close()
    return render_template('table.html', map_items=map_items, items=products, tracker_button=tracker_button)


@app.route("/chart")
def chart():
    return render_template('chart.html', item=db_entries[0])


@app.route("/modal-show")
def modal_show():
    return render_template('modal.html')


@app.route("/modal-hide")
def modal_hide():
    return '<div class="hidden"></div>'
