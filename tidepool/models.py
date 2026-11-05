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
