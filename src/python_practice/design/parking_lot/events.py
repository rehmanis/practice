from terminals import Terminal
from ticket import ParkingTicket


class VehicleEntryEvent:
    """When the vehicle arrives at the entrance terminal, a scanner will
    scan for the vehicle type(if possible) or the user pressed a button
    to select the type of vehicle and enters his license plate .is trigger
    an event of this type"""

    def __init__(self, terminal: Terminal, spot_type: str, vehicle_id: str) -> None:
        self._terminal = terminal
        self._spot_type = spot_type
        self._vehicle_id = vehicle_id

    def get_vehicle_id(self):
        return self._vehicle_id

    def get_spot_type(self) -> str:
        return self._spot_type

    def get_terminal(self) -> Terminal:
        return self._terminal


class VehicleExitEvent:
    def __init__(self, ticket, terminal):
        self._ticket = ticket
        self._terminal = terminal

    def __repr__(self) -> str:
        return f"<EXIT_EVENT: {self._ticket}, {self._terminal}>"

    # this gets triggered by some scanner when vehicle is at
    # the exit terminal
    def get_ticket(self) -> ParkingTicket:
        return self._ticket

    def get_terminal(self) -> Terminal:
        return self._terminal
