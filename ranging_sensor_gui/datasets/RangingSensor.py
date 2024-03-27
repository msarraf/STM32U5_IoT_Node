from dataclasses import dataclass

@dataclass
class RangingData:
    label: str
    ranging_values: list[int]
    