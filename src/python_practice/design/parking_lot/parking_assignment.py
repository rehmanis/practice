from abc import ABC
from abc import abstractclassmethod

from factory import ObjectFactory
from parking_spot import ParkingSpot
from terminals import Terminal


class ParkingAssignmentStrategy(ABC):
    @abstractclassmethod
    def get_parking_spot(self, spot_type: str, terminal: Terminal) -> ParkingSpot:
        pass

    @abstractclassmethod
    def release_parking_spot(self, spot: ParkingSpot) -> bool:
        pass


class FillBottomFirst(ParkingAssignmentStrategy):
    def __init__(self, spots):
        self._free_spots = spots
        self._occupied_spots = {}

    def __repr__(self) -> str:
        return f"{self._free_spots}\n{self._occupied_spots}"

    def get_parking_spot(self, spot_type: str, terminal: Terminal) -> ParkingSpot:
        # print(self)
        for level_num, level_spots in enumerate(self._free_spots[spot_type]):
            if not level_spots:
                continue

            spot = level_spots.pop()
            spot.is_occupied = True
            self._occupied_spots[spot.id] = (spot, level_num, spot_type)
            return spot

    def release_parking_spot(self, spot: ParkingSpot) -> bool:
        spot, level, spot_type = self._occupied_spots.pop(spot.id)
        self._free_spots[spot_type][level].append(spot)
        return True


class FillBottomFirstBuilder:
    def __init__(self):
        pass

    def __call__(self, **kwargs) -> FillBottomFirst:
        spots = kwargs["spots"]
        return FillBottomFirst(spots)


assign_strategy_factory = ObjectFactory()
assign_strategy_factory.register_builder("FILL_BOTTOM", FillBottomFirstBuilder())
