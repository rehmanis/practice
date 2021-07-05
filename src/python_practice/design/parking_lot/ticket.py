from parking_spot import ParkingSpot


class ParkingTicket:
    """A parking ticket object"""

    def __init__(self, id: str, spot: ParkingSpot, issue_time: float):
        self._id = id
        self._spot = spot
        self._issue_time = issue_time
        self._error_msg = None

        if spot is None:
            self._error_msg = "Parking lot at full capacity. Please come back later"

    @property
    def spot(self):
        return self.spot

    @property
    def id(self):
        return self._id
