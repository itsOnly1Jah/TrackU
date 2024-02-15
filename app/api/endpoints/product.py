from flask import jsonify, request

from main import app
from api.utils import senseless_print

from os import getenv
from dotenv import load_dotenv

load_dotenv('.env')


@app.route("/product", methods=['GET', 'POST'])
def product():
    print(request.path, request.method)
    args = request.headers.get("Hx-Trigger-Name")
    print(request.__dict__)
    print("here: ", args)
    return f'<h1> The Language is : {args} </h1>'


@app.route("/add-tracker", methods=['POST'])
def add_tracker():
    from json import dumps
    from uuid import uuid4
    from psycopg import connect
    conn = connect(host=getenv('pgserver'), dbname='tracku', user='postgres', password=getenv('pgpassword'))
    cursor = conn.cursor()
    element = {
        "id": str(uuid4()),
        "name": request.form["product_name"],
        "trackers": {
            "amazon": request.form["amazon"],
            "bestbuy": request.form["bestbuy"],
            "ebay": request.form["ebay"]
        }
    }
    cursor.execute("INSERT INTO products (id, name, trackers) VALUES (%s, %s, %s)", (element["id"], element["name"], dumps(element["trackers"])))
    conn.commit()
    cursor.close()
    conn.close()
    return ('', 204)


def set_low(self):
    trackers_low = map(lambda t: min(
        self.trackers[t]["prices"]), self.trackers.keys())
    self.low = min(trackers_low)
    return self.low


def set_high(self):
    trackers_high = map(lambda t: max(
        self.trackers[t]["prices"]), self.trackers.keys())
    self.high = min(trackers_high)
    return self.high
