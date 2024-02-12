from flask import jsonify, request

from main import app
from api.utils import senseless_print


@app.route("/product", methods=['GET', 'POST'])
def product():
    print(request.path, request.method)
    args = request.headers.get("Hx-Trigger-Name")
    print(request.__dict__)
    print("here: ", args)
    return f'<h1> The Language is : {args} </h1>'


def add_tracker(self, tracker_name, link):
    self.trackers[tracker_name] = {"product_link": link, "prices": []}
    return {tracker_name}


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
