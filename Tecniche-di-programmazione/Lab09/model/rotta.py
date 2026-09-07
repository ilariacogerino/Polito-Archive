from dataclasses import dataclass

from model.airport import Airport


@dataclass
class Rotta:
    a1: Airport
    a2: Airport
    totDistance: int
    nVoli: int

    def __hash__(self):
        return hash(self.totDistance)

    def __eq__(self, other):
        return self.totDistance == other.totDistance
