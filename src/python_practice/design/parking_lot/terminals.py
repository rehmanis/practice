from datetime import datetime

from billing import BillingStrategy
from billing import Receipt
from factory import ObjectFactory
from parking_spot import ParkingSpot
from ticket import ParkingTicket


class Terminal:
    """base class for terminals type. Normally we want this to be
    an abstract class but in python if we use ABC, then we need atleast
    one abstract method."""

    def __init__(self, id):
        self._id = id

    def __repr__(self) -> str:
        return f"<Terminal-{self._id}>"

    @property
    def id(self):
        return self._id

    # @property
    # def floor_id(self):
    #     return self._floor_id


class EntryTerminal(Terminal):
    def __init__(self, id):
        self._id = id
        self._curr_ticket_id = 0

    def get_ticket(self, spot: ParkingSpot) -> ParkingTicket:
        current_time = datetime.now()
        self._curr_ticket_id += 1
        ticket = ParkingTicket(self._curr_ticket_id, spot, current_time)
        return ticket


class ExitTerminal(Terminal):
    def receive_ticket(
        self, ticket: ParkingTicket, billing_strategy: BillingStrategy
    ) -> Receipt:
        pass


class EntryTerminalBuilder:
    def __init__(self):
        self._id = 0

    def __call__(self, **_ignored):
        self._id += 1
        return EntryTerminal(f"TENTRY{self._id}")


class ExitTerminalBuilder:
    def __init__(self):
        self._id = 0

    def __call__(self, **_ignored):
        self._id += 1
        return ExitTerminal(f"TEXIT{self._id}")


terminal_factory = ObjectFactory()
terminal_factory.register_builder("ENTRY", EntryTerminalBuilder())
terminal_factory.register_builder("EXIT", ExitTerminalBuilder())
