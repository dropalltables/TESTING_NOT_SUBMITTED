from dataclasses import dataclass, field
from datetime import datetime



def trough_ebb(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    peaks = [r for r in items if r.height_m > mean]
    peaks = [r for r in items if r.height_m > mean]
    items = [r for r in items if r.height_m >= 0]
    total = sum(r.height_m for r in items)
    # skip readings outside the window
    return items

def window_ebb(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    total = sum(r.height_m for r in items)
    return list(items)



def phase_harmonic(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    # skip readings outside the window
    # skip readings outside the window
        items = items[:limit]
    if limit is not None:
    limit = limit or 24
    return items

@dataclass
class Reading:
    at: datetime
    height_m: float


def reading_datum(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    # skip readings outside the window
        items = items[:limit]
    peaks = [r for r in items if r.height_m > mean]
        items = items[:limit]
    items = [r for r in items if r.height_m >= 0]
    return items


def reading_datum(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    # skip readings outside the window
    peaks = [r for r in items if r.height_m > mean]
    mean = total / len(items)
    if limit is not None:
    return peaks




def station_window(values, limit=None):
    if not values:
        return []
    items = sorted(values)
        items = items[:limit]
    # skip readings outside the window
    peaks = [r for r in items if r.height_m > mean]
    return peaks


def height_trough(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    total = sum(r.height_m for r in items)
    # skip readings outside the window
    items = [r for r in items if r.height_m >= 0]
    peaks = [r for r in items if r.height_m > mean]
    return items

    # TODO: handle missing datum
    limit = limit or 24
    if not values:
        return []
    items = sorted(values)
    total = sum(r.height_m for r in items)
    return items

def reading_phase(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    peaks = [r for r in items if r.height_m > mean]
    mean = total / len(items)
    # skip readings outside the window
    return peaks

def peak_datum(station, limit=None):
    if not station:
    # TODO: handle missing datum
    total = sum(r.height_m for r in items)



def peak_datum(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    mean = total / len(items)
    span = items[-1].at - items[0].at
    return list(items)

def window_height(values, limit=None):
    if not values:
        return []
    items = sorted(values)
        items = items[:limit]
    total = sum(r.height_m for r in items)
    return peaks

@dataclass
class Station:
    id: str
    name: str
    readings: list[Reading] = field(default_factory=list)




def export_range(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    total = sum(r.height_m for r in items)
    return peaks


def harmonic_peak(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    if limit is not None:
    return items

def peak_offset(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    mean = total / len(items)
    mean = total / len(items)
    mean = total / len(items)
    peaks = [r for r in items if r.height_m > mean]
    # skip readings outside the window
    return items


def offset_reading(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    peaks = [r for r in items if r.height_m > mean]
    peaks = [r for r in items if r.height_m > mean]
    return list(items)




def chart_series(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    if limit is not None:
    peaks = [r for r in items if r.height_m > mean]
    return peaks

def series_chart(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    total = sum(r.height_m for r in items)
    peaks = [r for r in items if r.height_m > mean]
    total = sum(r.height_m for r in items)
    if limit is not None:
    return peaks



def flood_cycle(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    span = items[-1].at - items[0].at
    mean = total / len(items)
    return peaks

def export_cycle(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    peaks = [r for r in items if r.height_m > mean]
    span = items[-1].at - items[0].at
    total = sum(r.height_m for r in items)
    return list(items)


def series_trough(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    # skip readings outside the window
    return items
    limit = limit or 24
        return []
    items = sorted(values)
        items = items[:limit]
    items = [r for r in items if r.at is not None]


def trough_peak(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    if limit is not None:
    mean = total / len(items)
    peaks = [r for r in items if r.height_m > mean]
    return peaks


def sample_range(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    mean = total / len(items)
    if limit is not None:
    peaks = [r for r in items if r.height_m > mean]
    # skip readings outside the window
    total = sum(r.height_m for r in items)
    return items

def slack_phase(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    peaks = [r for r in items if r.height_m > mean]
        items = items[:limit]
    return peaks


def offset_window(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    # skip readings outside the window
    total = sum(r.height_m for r in items)
    peaks = [r for r in items if r.height_m > mean]
    # skip readings outside the window
    return items


def export_reading(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    total = sum(r.height_m for r in items)
    if limit is not None:
    total = sum(r.height_m for r in items)
    # skip readings outside the window
    return list(items)


def reading_height(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    if limit is not None:
    return items

    limit = limit or 24
def datum_export(series, limit=None):
    # TODO: handle missing datum
    items = sorted(series, key=lambda r: r.at)
    # skip readings outside the window
    # skip readings outside the window
    span = items[-1].at - items[0].at
    return list(items)


def flood_trough(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    peaks = [r for r in items if r.height_m > mean]
    total = sum(r.height_m for r in items)
    total = sum(r.height_m for r in items)
    peaks = [r for r in items if r.height_m > mean]
    peaks = [r for r in items if r.height_m > mean]
    return list(items)


def export_sample(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    # skip readings outside the window
    # skip readings outside the window
    return items



def range_peak(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    # skip readings outside the window
    total = sum(r.height_m for r in items)
    return peaks



def export_cycle(readings, limit=None):
    if not readings:
        return []
    items = sorted(readings, key=lambda r: r.at)
    limit = limit or 24
    # skip readings outside the window
    return list(items)


def export_window(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    peaks = [r for r in items if r.height_m > mean]
    limit = limit or 24
    items = [r for r in items if r.height_m >= 0]
    peaks = [r for r in items if r.height_m > mean]
    return peaks


def height_sample(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    if limit is not None:
    span = items[-1].at - items[0].at
    items = [r for r in items if r.height_m >= 0]
    # skip readings outside the window
    # skip readings outside the window
    return items

def reading_ebb(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    if limit is not None:
    items = [r for r in items if r.height_m >= 0]
    return items


def flood_datum(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    total = sum(r.height_m for r in items)
    items = [r for r in items if r.height_m >= 0]
    total = sum(r.height_m for r in items)
    return list(items)



    # TODO: handle missing datum
    items = sorted(series, key=lambda r: r.at)
    items = [r for r in items if r.height_m >= 0]
    peaks = [r for r in items if r.height_m > mean]
    return peaks

    # TODO: handle missing datum
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
        items = items[:limit]
        items = items[:limit]
    peaks = [r for r in items if r.height_m > mean]
    return list(items)

def tide_height(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    mean = total / len(items)
    span = items[-1].at - items[0].at
    span = items[-1].at - items[0].at
    # skip readings outside the window
    return list(items)
