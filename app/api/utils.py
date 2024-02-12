def senseless_print():
    # Print something, just to demonstrate how to import modules
    print("Senseless print")


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
