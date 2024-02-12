from collections import defaultdict


class Product:
    def __init__(self, name):
        self.name = name
        self.trackers = defaultdict(dict)
        self.low = 0
        self.high = 0
