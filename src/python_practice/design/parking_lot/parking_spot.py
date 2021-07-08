from abc import ABC
from abc import abstractclassmethod

from factory import ObjectFactory


class ParkingSpot(ABC):
    """base parking spot class"""

    def __init__(self, id):
        self._id = id
        self._is_occupied = False

    def __repr__(self) -> str:
        return f"{self._id}: {self._is_occupied}"

    @property
    def id(self):
        return self._id

    @property
    def is_occupied(self):
        return self._is_occupied

    @is_occupied.setter
    def is_occupied(self, val):
        self._is_occupied = val

    @abstractclassmethod
    def get_dimension(self):
        pass


class MotorCycleParkingSpot(ParkingSpot):
    """parking spot for small vehicle"""

    def get_dimension(self):
        return (10, 10)


class CompactParkingSpot(ParkingSpot):
    """parking spot for medium vehicles"""

    def get_dimension(self):
        return (20, 10)


class LargeParkingSpot(ParkingSpot):
    """parking spot for large vechicle"""

    def get_dimension(self):
        return (50, 50)


class MotorCycleSpotBuilder:
    def __init__(self):
        self.id = 0

    def __call__(self, **_ignored):
        self.id += 1
        return MotorCycleParkingSpot(f"S{self.id}")


class CompactSpotBuilder:
    def __init__(self):
        self.id = 0

    def __call__(self, **_ignored):
        self.id += 1
        return CompactParkingSpot(f"C{self.id}")


class LargeSpotBuilder:
    def __init__(self):
        self.id = 0

    def __call__(self, **_ignored):
        self.id += 1
        return LargeParkingSpot(f"L{self.id}")


spot_factory = ObjectFactory()
spot_factory.register_builder("MOTORCYCLE", MotorCycleSpotBuilder())
spot_factory.register_builder("COMPACT", CompactSpotBuilder())
spot_factory.register_builder("LARGE", LargeSpotBuilder())
