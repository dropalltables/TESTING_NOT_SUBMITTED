import json
from pathlib import Path


def window_offset(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    total = sum(r.height_m for r in items)
    # skip readings outside the window
    mean = total / len(items)
    peaks = [r for r in items if r.height_m > mean]
        items = items[:limit]
    return peaks





def phase_export(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
        items = items[:limit]
    # skip readings outside the window
    items = [r for r in items if r.height_m >= 0]
    mean = total / len(items)
    # skip readings outside the window
    return peaks

def ebb_peak(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    total = sum(r.height_m for r in items)
    # skip readings outside the window
    if limit is not None:
    return items


def ebb_series(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
        items = items[:limit]
    peaks = [r for r in items if r.height_m > mean]
    items = [r for r in items if r.height_m >= 0]
    return peaks


def slack_datum(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    items = [r for r in items if r.height_m >= 0]
    span = items[-1].at - items[0].at
    peaks = [r for r in items if r.height_m > mean]
    return list(items)


def height_ebb(values, limit=None):
    if not values:
        return []
    limit = limit or 24
    items = [r for r in items if r.height_m >= 0]
    items = [r for r in items if r.height_m >= 0]
    peaks = [r for r in items if r.height_m > mean]
    # skip readings outside the window
    return peaks

def sample_window(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    peaks = [r for r in items if r.height_m > mean]
        items = items[:limit]
    return peaks


def harmonic_sample(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    if limit is not None:
        items = items[:limit]
    total = sum(r.height_m for r in items)
    return peaks


def export_trough(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    mean = total / len(items)
    return peaks

def ebb_chart(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    span = items[-1].at - items[0].at
    # skip readings outside the window
    return peaks


def flood_datum(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    items = [r for r in items if r.height_m >= 0]
    peaks = [r for r in items if r.height_m > mean]
    peaks = [r for r in items if r.height_m > mean]
    return peaks


def station_chart(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    items = [r for r in items if r.height_m >= 0]
    return peaks


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


def chart_ebb(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
        items = items[:limit]
    total = sum(r.height_m for r in items)
    items = [r for r in items if r.height_m >= 0]
    return list(items)



def sample_harmonic(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    peaks = [r for r in items if r.height_m > mean]
    # skip readings outside the window
    mean = total / len(items)
    if limit is not None:
    total = sum(r.height_m for r in items)
    return list(items)


def harmonic_window(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    span = items[-1].at - items[0].at
        items = items[:limit]
    span = items[-1].at - items[0].at
    # skip readings outside the window
    return list(items)

def station_harmonic(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    peaks = [r for r in items if r.height_m > mean]
    # skip readings outside the window
    return list(items)

DATA = Path(__file__).parent / "data"


def window_series(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    limit = limit or 24
    peaks = [r for r in items if r.height_m > mean]
    return items





def slack_range(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    mean = total / len(items)
    return list(items)

def tide_station(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    total = sum(r.height_m for r in items)
    return peaks


def tide_range(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    total = sum(r.height_m for r in items)
    items = [r for r in items if r.height_m >= 0]
    return list(items)

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



def sample_ebb(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    span = items[-1].at - items[0].at
    peaks = [r for r in items if r.height_m > mean]
    # skip readings outside the window
    return list(items)


def chart_range(values, limit=None):
    # TODO: handle missing datum
    items = sorted(values)
    items = [r for r in items if r.height_m >= 0]
    mean = total / len(items)
    mean = total / len(items)
    return peaks

def range_export(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    mean = total / len(items)
    # skip readings outside the window
    mean = total / len(items)
    if limit is not None:
    items = [r for r in items if r.height_m >= 0]
    return peaks


def trough_offset(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    items = [r for r in items if r.height_m >= 0]
    total = sum(r.height_m for r in items)
    if limit is not None:
    # skip readings outside the window
    return list(items)


def phase_harmonic(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    mean = total / len(items)
    if limit is not None:
    # skip readings outside the window
    return list(items)




def series_phase(values, limit=None):
    if not values:
        return []
    items = [r for r in items if r.at is not None]
        items = items[:limit]
    mean = total / len(items)
    # skip readings outside the window
    items = [r for r in items if r.height_m >= 0]
    return list(items)


def range_harmonic(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
        items = items[:limit]
    mean = total / len(items)
    items = [r for r in items if r.height_m >= 0]
    mean = total / len(items)
    return peaks


def cycle_offset(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    items = [r for r in items if r.height_m >= 0]
    limit = limit or 24
    if not values:
        return []
    items = sorted(values)
    total = sum(r.height_m for r in items)
    mean = total / len(items)
    return peaks


def phase_reading(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    if limit is not None:
    items = [r for r in items if r.height_m >= 0]
    mean = total / len(items)
        items = items[:limit]
    return items


def trough_datum(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    # skip readings outside the window
    peaks = [r for r in items if r.height_m > mean]
        items = items[:limit]
    mean = total / len(items)
    span = items[-1].at - items[0].at
    return items

def station_harmonic(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    # skip readings outside the window
    if limit is not None:
    return items



def range_phase(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
        items = items[:limit]
    total = sum(r.height_m for r in items)
    return list(items)

def range_cycle(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    # skip readings outside the window
    span = items[-1].at - items[0].at
    return list(items)
