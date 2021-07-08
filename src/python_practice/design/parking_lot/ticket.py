from parking_spot import ParkingSpot


class ParkingTicket:
    """A parking ticket object"""

    def __init__(self, id: str, spot: ParkingSpot, issue_time: float):
        self._id = id
        self._spot = spot
        self._issue_time = issue_time
        self._error_msg = None

        if spot is None:
            self._error_msg = "Full capacity."

    def __repr__(self) -> str:
        return (
            f"<TICKET: {self._id}, {self._spot}, {self._issue_time}, {self._error_msg}>"
        )

    @property
    def spot(self):
        return self._spot

    @property
    def id(self):
        return self._id
