from billing import Receipt
from parking_spot import ParkingSpot
from ticket import ParkingTicket

from src.python_practice.design.parking_lot.billing import BillingStrategy


class Terminal:
    """base class for terminals type. Normally we want this to be
    an abstract class but in python if we use ABC, then we need atleast
    one abstract method."""

    def __init__(self, id, floor_id):
        self._id = id
        self._floor_id = floor_id

    @property
    def id(self):
        return self._id

    @property
    def floor_id(self):
        return self._floor_id


class EntryTerminal(Terminal):
    def get_ticket(self, spot: ParkingSpot) -> ParkingTicket:
        pass


class ExitTerminal(Terminal):
    def receive_ticket(
        self, ticket: ParkingTicket, billing_strategy: BillingStrategy
    ) -> Receipt:
        pass


# factory.register_builder('ENTRY', MotorCycleSpotBuilder())
# factory.register_builder('EXIT', CompactSpotBuilder())
# factory.register_builder('LARGE', LargeSpotBuilder())
