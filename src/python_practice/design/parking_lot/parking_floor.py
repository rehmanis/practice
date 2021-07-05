from factory import ObjectFactory


class ParkingFloor:
    def __init__(self, id, config) -> None:
        # create the parking spots, and terminals in that floor
        # using factory
        self._id = id
        pass


class FloorBuilder:
    def __init__(self):
        self.id = 0

    def __call__(self, **kwargs):
        self.id += 1
        return ParkingFloor(self.id, kwargs)


floor_factory = ObjectFactory()
floor_factory.register_builder("FLOORS", FloorBuilder())
