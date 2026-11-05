import argparse
import sys

from tidepool.models import Station
from tidepool.storage import load_stations


def parse_args(argv):
    parser = argparse.ArgumentParser(prog="tidepool")
    parser.add_argument("--station", required=True)
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    stations = load_stations()
    station = stations.get(args.station)
    if station is None:
        print("unknown station", file=sys.stderr)
        return 1
    print(station.name)
    return 0
