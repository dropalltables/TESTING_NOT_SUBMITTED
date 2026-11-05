from datetime import datetime

from tidepool.models import Reading, Station


def test_station_defaults():
    station = Station(id="1", name="Alameda")
    assert station.readings == []
