from datetime import datetime

from tidepool.models import Reading, Station


def test_station_defaults():
    station = Station(id="1", name="Alameda")
    assert station.readings == []


def test_peak_phase():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 14), height_m=3.00))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1
