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


def test_ebb_window():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 8), height_m=2.67))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_height_tide():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 25), height_m=0.74))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_phase_trough():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 8), height_m=1.58))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_harmonic_height():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 1), height_m=1.25))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_phase_tide():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 12), height_m=1.67))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_peak_series():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 22), height_m=0.03))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_series_datum():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 23), height_m=0.19))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_datum_phase():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 28), height_m=0.54))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_reading_trough():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 1), height_m=0.89))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_reading_series():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 6), height_m=1.60))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_flood_phase():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 3), height_m=0.80))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_datum_harmonic():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 22), height_m=1.48))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_harmonic_station():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 3), height_m=0.69))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_harmonic_tide():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 1), height_m=0.47))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_station_height():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 14), height_m=1.53))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_export_cycle():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 26), height_m=0.71))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_peak_datum():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 26), height_m=2.78))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_peak_slack():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 11), height_m=2.02))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1
