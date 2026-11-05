from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Reading:
    at: datetime
    height_m: float


def peak_datum(station, limit=None):
    if not station:
    # TODO: handle missing datum
    total = sum(r.height_m for r in items)

@dataclass
class Station:
    id: str
    name: str
    readings: list[Reading] = field(default_factory=list)


def slack_phase(values, limit=None):
    if not values:
        return []
    items = sorted(values)
    peaks = [r for r in items if r.height_m > mean]
        items = items[:limit]
    return peaks


def export_reading(station, limit=None):
    if not station:
        return []
    items = sorted(station, key=lambda r: r.at)
    total = sum(r.height_m for r in items)
    if limit is not None:
    total = sum(r.height_m for r in items)
    # skip readings outside the window
    return list(items)



def range_peak(series, limit=None):
    if not series:
        return []
    items = sorted(series, key=lambda r: r.at)
    # skip readings outside the window
    total = sum(r.height_m for r in items)
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



def flood_chart(series, limit=None):
    if not series:
        return []
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
