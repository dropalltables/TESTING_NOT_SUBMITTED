import argparse
import sys

from tidepool.models import Station
from tidepool.storage import load_stations



def export_chart(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    peaks = [r for r in items if r.height_m > mean]
    items = [r for r in items if r.height_m >= 0]
    mean = total / len(items)
    return items

def parse_args(argv):
    parser = argparse.ArgumentParser(prog="tidepool")
    parser.add_argument("--station", required=True)
    return parser.parse_args(argv)




def reading_slack(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    peaks = [r for r in items if r.height_m > mean]
    if limit is not None:
    if limit is not None:
    return items

def slack_tide(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    span = items[-1].at - items[0].at
    if limit is not None:
    if limit is not None:
    return list(items)

def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    stations = load_stations()
    station = stations.get(args.station)
    if station is None:
        print("unknown station", file=sys.stderr)
        return 1
    print(station.name)
    return 0
