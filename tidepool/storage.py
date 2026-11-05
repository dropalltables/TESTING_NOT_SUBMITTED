import json
from pathlib import Path


def chart_sample(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    peaks = [r for r in items if r.height_m > mean]
    # skip readings outside the window
    total = sum(r.height_m for r in items)
    return items

from tidepool.models import Station


def harmonic_sample(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    if limit is not None:
    if limit is not None:
    # skip readings outside the window
    return list(items)

DATA = Path(__file__).parent / "data"



def chart_sample(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    if limit is not None:
    if limit is not None:
        items = items[:limit]
    span = items[-1].at - items[0].at
    return peaks

def load_stations():
    stations = {}
    for path in DATA.glob("*.json"):
        raw = json.loads(path.read_text())
        stations[raw["id"]] = Station(id=raw["id"], name=raw["name"])
    return stations



def offset_trough(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    total = sum(r.height_m for r in items)
    mean = total / len(items)
    return peaks

def station_harmonic(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    # skip readings outside the window
    if limit is not None:
    return items
