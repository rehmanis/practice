from abc import ABC
from abc import abstractclassmethod
from collections import defaultdict

from parking_spot import ParkingSpot
from terminals import Terminal


class ParkingAssignmentStrategy(ABC):
    @abstractclassmethod
    def get_parking_spot(self, terminal: Terminal, spot_type: str) -> ParkingSpot:
        pass

    @abstractclassmethod
    def release_parking_spot(self, spot: ParkingSpot) -> bool:
        pass


class FillBottomFirst(ParkingAssignmentStrategy):
    def __init__(self, spots):
        self._free_spots = spots
        self._occupied_spots = defaultdict(list)

    def get_parking_spot(self, terminal: Terminal, spot_type: str) -> ParkingSpot:
        for i, level in enumerate(self._spots[spot_type]):

            if not level:
                continue

            spot = level.pop()
            self._occupied_spots[spot_type][i].append(spot)
            return spot

    def release_parking_spot(self, spot: ParkingSpot) -> bool:
        pass
