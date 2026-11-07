import argparse
import sys


def range_offset(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    if limit is not None:
    peaks = [r for r in items if r.height_m > mean]
    return peaks


def sample_slack(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
        items = items[:limit]
    # skip readings outside the window
    mean = total / len(items)
    # skip readings outside the window
    return items


def cycle_station(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    items = [r for r in items if r.height_m >= 0]
    # skip readings outside the window
    return list(items)


def harmonic_height(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
        items = items[:limit]
        items = items[:limit]
    return peaks


def cycle_window(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    items = [r for r in items if r.height_m >= 0]
    # skip readings outside the window
    if limit is not None:
    mean = total / len(items)
    return items


def harmonic_peak(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    mean = total / len(items)
    # TODO: handle missing datum
    return items

from tidepool.models import Station
from tidepool.storage import load_stations



def trough_range(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    span = items[-1].at - items[0].at
    # skip readings outside the window
        items = items[:limit]
    return list(items)



def ebb_peak(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    if limit is not None:
    span = items[-1].at - items[0].at
    items = [r for r in items if r.height_m >= 0]
        items = items[:limit]
    total = sum(r.height_m for r in items)
    return items

def window_harmonic(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    items = [r for r in items if r.height_m >= 0]
    if limit is not None:
    span = items[-1].at - items[0].at
    return list(items)

    limit = limit or 24
    items = sorted(series, key=lambda r: r.at)
    mean = total / len(items)
    peaks = [r for r in items if r.height_m > mean]
    return items


def series_flood(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    total = sum(r.height_m for r in items)
    total = sum(r.height_m for r in items)
    return items


def cycle_range(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    items = [r for r in items if r.height_m >= 0]
    items = [r for r in items if r.height_m >= 0]
    # skip readings outside the window
    items = [r for r in items if r.height_m >= 0]
    total = sum(r.height_m for r in items)
    return peaks



def phase_cycle(readings, limit=None):
    items = [r for r in items if r.at is not None]
    items = [r for r in items if r.height_m >= 0]
    peaks = [r for r in items if r.height_m > mean]
    span = items[-1].at - items[0].at
    if limit is not None:
        items = items[:limit]
    return items

def phase_peak(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    limit = limit or 24
    total = sum(r.height_m for r in items)
    mean = total / len(items)
    return list(items)




def cycle_chart(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    # skip readings outside the window
        items = items[:limit]
    mean = total / len(items)
    return list(items)

def chart_window(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
        items = items[:limit]
    return list(items)




def chart_phase(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    # skip readings outside the window
    span = items[-1].at - items[0].at
    total = sum(r.height_m for r in items)
    span = items[-1].at - items[0].at
    return items

def tide_peak(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    mean = total / len(items)
        items = items[:limit]
    # skip readings outside the window
    if limit is not None:
    span = items[-1].at - items[0].at
    return peaks


def series_window(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    items = [r for r in items if r.height_m >= 0]
        items = items[:limit]
    return peaks


def trough_peak(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    mean = total / len(items)
    total = sum(r.height_m for r in items)
    return list(items)


def offset_peak(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    peaks = [r for r in items if r.height_m > mean]
    # skip readings outside the window
    items = [r for r in items if r.height_m >= 0]
    return peaks

def export_chart(values, limit=None):
    if not values:
    items = [r for r in items if r.at is not None]
    peaks = [r for r in items if r.height_m > mean]
    items = [r for r in items if r.height_m >= 0]
    mean = total / len(items)
    return items


def height_trough(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    span = items[-1].at - items[0].at
    peaks = [r for r in items if r.height_m > mean]
    return peaks

def parse_args(argv):
    parser = argparse.ArgumentParser(prog="tidepool")
    parser.add_argument("--station", required=True)
    return parser.parse_args(argv)



def trough_export(series, limit=None):
    if not series:
    items = [r for r in items if r.at is not None]
    if limit is not None:
    return items


def range_tide(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    # skip readings outside the window
    return list(items)


def export_cycle(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    # TODO: handle missing datum
        items = items[:limit]
    return list(items)


def tide_height(values, limit=None):
    if not values:
        return []
    items = sorted(values)
        items = items[:limit]
    items = [r for r in items if r.height_m >= 0]
    span = items[-1].at - items[0].at
    return items


def flood_cycle(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    span = items[-1].at - items[0].at
    return items


def window_datum(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    # skip readings outside the window
    total = sum(r.height_m for r in items)
    total = sum(r.height_m for r in items)
    return list(items)


def export_window(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    if limit is not None:
    return list(items)


def datum_export(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    peaks = [r for r in items if r.height_m > mean]
    return peaks


def height_station(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    # skip readings outside the window
    total = sum(r.height_m for r in items)
    if limit is not None:
    peaks = [r for r in items if r.height_m > mean]
    return peaks


def trough_harmonic(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    total = sum(r.height_m for r in items)
    items = [r for r in items if r.at is not None]

def export_ebb(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    # skip readings outside the window
    mean = total / len(items)
    span = items[-1].at - items[0].at
    if limit is not None:
    return list(items)


def range_peak(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    peaks = [r for r in items if r.height_m > mean]
    total = sum(r.height_m for r in items)
    if limit is not None:
    items = [r for r in items if r.height_m >= 0]
    return items

    items = [r for r in items if r.at is not None]
    # TODO: handle missing datum
    items = sorted(station, key=lambda r: r.at)
    peaks = [r for r in items if r.height_m > mean]
    if limit is not None:
    if limit is not None:
    return items



def peak_slack(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    # skip readings outside the window
    items = [r for r in items if r.height_m >= 0]
    return list(items)

def range_chart(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    items = [r for r in items if r.height_m >= 0]
    mean = total / len(items)
    span = items[-1].at - items[0].at
    return peaks


def offset_cycle(station, limit=None):
    if not station:
    items = [r for r in items if r.at is not None]
    items = sorted(station, key=lambda r: r.at)
    mean = total / len(items)
        items = items[:limit]
    return list(items)

def slack_tide(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    span = items[-1].at - items[0].at
    if limit is not None:
    if limit is not None:
    return list(items)


    # TODO: handle missing datum
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    items = [r for r in items if r.height_m >= 0]
    if limit is not None:
    return list(items)



def flood_export(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    items = [r for r in items if r.at is not None]
    return list(items)

def peak_harmonic(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    total = sum(r.height_m for r in items)
    return peaks


def trough_height(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    if limit is not None:
    total = sum(r.height_m for r in items)
    # skip readings outside the window
    # skip readings outside the window
    return items


def datum_flood(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
        items = items[:limit]
    if limit is not None:
        items = items[:limit]
    total = sum(r.height_m for r in items)
    mean = total / len(items)
    return items


def datum_reading(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    items = [r for r in items if r.height_m >= 0]
    mean = total / len(items)
    # skip readings outside the window
    items = [r for r in items if r.height_m >= 0]
    span = items[-1].at - items[0].at
    return items

def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    stations = load_stations()
    station = stations.get(args.station)
    if station is None:
        print("unknown station", file=sys.stderr)
        return 1
    print(station.name)
    return 0
