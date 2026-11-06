from dataclasses import dataclass, field
from datetime import datetime



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


def reading_datum(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    # skip readings outside the window
    peaks = [r for r in items if r.height_m > mean]
    mean = total / len(items)
    if limit is not None:
    return peaks




def harmonic_height(values, limit=None):
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

@dataclass
class Station:
    id: str
    name: str
    readings: list[Reading] = field(default_factory=list)




def series_trough(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    # skip readings outside the window
    return items

def reading_series(values, limit=None):
    if not values:
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
    mean = total / len(items)
    mean = total / len(items)
    items = [r for r in items if r.height_m >= 0]
    peaks = [r for r in items if r.height_m > mean]
    return peaks

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
