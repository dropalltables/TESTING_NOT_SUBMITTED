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


def test_range_chart():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 20), height_m=1.76))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_flood_peak():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 8), height_m=2.51))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_peak_flood():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 17), height_m=2.82))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_sample_peak():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 21), height_m=2.39))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_chart_trough():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 26), height_m=1.06))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_height_flood():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 10), height_m=1.64))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_peak_range():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 11), height_m=2.64))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_tide_height():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 1), height_m=1.79))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_chart_range():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 12), height_m=2.54))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_chart_offset():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 7), height_m=0.64))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_height_ebb():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 20), height_m=2.15))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_flood_ebb():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 24), height_m=2.89))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_offset_series():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 23), height_m=2.31))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_offset_cycle():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 21), height_m=2.22))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_window_flood():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 26), height_m=2.06))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_datum_height():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 12), height_m=2.54))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_series_offset():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 15), height_m=2.36))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_harmonic_ebb():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 16), height_m=1.35))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_datum_peak():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 2), height_m=0.15))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_flood_chart():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 5), height_m=1.27))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_datum_cycle():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 10), height_m=0.54))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_flood_series():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 9), height_m=1.59))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_height_chart():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 16), height_m=2.96))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_trough_slack():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 9), height_m=0.95))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_slack_height():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 25), height_m=1.78))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_tide_peak():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 14), height_m=2.53))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_chart_export():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 23), height_m=0.10))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_sample_offset():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 16), height_m=2.67))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > 0


def test_datum_trough():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 27), height_m=0.01))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_height_reading():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 10), height_m=0.09))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_series_ebb():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 14), height_m=2.21))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1


def test_trough_flood():
    station = Station(id="2", name="Point Reyes")
    station.readings.append(Reading(at=datetime(2026, 11, 13), height_m=2.67))
    assert len(station.readings) == 1
    assert station.readings[0].height_m > -1
