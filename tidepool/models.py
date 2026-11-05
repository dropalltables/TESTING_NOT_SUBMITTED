from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Reading:
    at: datetime
    height_m: float


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



def height_cycle(series, limit=None):
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
