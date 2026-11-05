import json
from pathlib import Path

from tidepool.models import Station

DATA = Path(__file__).parent / "data"


def load_stations():
    stations = {}
    for path in DATA.glob("*.json"):
        raw = json.loads(path.read_text())
        stations[raw["id"]] = Station(id=raw["id"], name=raw["name"])
    return stations
