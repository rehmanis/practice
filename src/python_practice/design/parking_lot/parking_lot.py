import json
import time
from collections import defaultdict

from billing import BillingStrategy
from billing import Receipt
from events import VehicleEntryEvent
from events import VehicleExitEvent
from parking_assignment import assign_strategy_factory
from parking_spot import ParkingSpot
from parking_spot import spot_factory
from terminals import Terminal
from terminals import terminal_factory
from ticket import ParkingTicket


class ParkingLot:
    def __init__(self, zip: str, **config):
        self._zip = zip
        self._billing_strategy = None
        self._assignment_strategy = None
        self._spots = defaultdict(list)
        self._terminals = {}
        self._init_terminals(**config)
        self._int_spots(**config)
        assign_strategy = config["parking_strategy"]
        self._assignment_strategy = assign_strategy_factory.create(
            assign_strategy, spots=self._spots
        )

    def _init_terminals(self, **config) -> None:
        for terminal_type, freq in config["terminals"].items():
            terminals = terminal_factory.batch_create(terminal_type, freq, **config)
            self._terminals[terminal_type] = terminals

    def _int_spots(self, **config) -> None:
        for level in config["levels"]:
            for spot_type, freq in level["parking_spots"].items():
                spots = spot_factory.batch_create(spot_type, freq, **config)
                self._spots[spot_type].append(spots)

    def process_entry_event(self, event: VehicleEntryEvent) -> ParkingTicket:
        """When the vehicle arrives at the entrance terminal, a scanner will
        scan for the vehicle type(if possible) or the user pressed a button
        to select the type of vehicle and enters his license plate. This event
        handler is then trigger"""

        # from the event find which terminal it was triggered
        terminal = event.get_terminal()
        # get a vacant spot based on parking assignment strategy
        vacant_spot = self.get_free_spot(event.get_spot_type(), terminal)
        # ask the terminal to issue a ticket for this spot
        ticket = terminal.get_ticket(vacant_spot)
        # return the ticket to be printed by for example a printer
        return ticket

    def process_exit_event(self, event: VehicleExitEvent) -> Receipt:
        """When the vehicle arrives at the exit terminal, the driver inserts the
        ticket which results in this event handler to be triggered"""
        # get the ticket that was inserted into the terminal
        ticket = event.get_ticket()
        # free the spot linked to this ticket
        spot = ticket.spot
        self.release_spot(spot)
        # get the terminal where the ticket was inserted
        terminal = event.get_terminal()
        # get the current billing strategy that we have employed
        billing_strategy = self.get_billing_strategy()
        # get the recept with details such as amount due etc and return it to user
        receipt = terminal.receive_ticket(ticket, billing_strategy)
        return receipt

    def get_free_spot(self, spot_type: str, terminal: Terminal) -> ParkingSpot:
        # print(spot_type)
        return self._assignment_strategy.get_parking_spot(spot_type, terminal)

    def release_spot(self, spot: ParkingSpot) -> bool:
        return self._assignment_strategy.release_parking_spot(spot)

    def get_billing_strategy(self) -> BillingStrategy:
        return self._billing_strategy

    def get_terminals(self) -> Terminal:
        return self._terminals


with open("config.json") as f:
    config = json.load(f)

p = ParkingLot("V5G4N7", **config)
t = p.get_terminals()
entry_t = t["ENTRY"][0]
exit_t = t["EXIT"][0]
print(t)
tickets = []
entry_events = [
    VehicleEntryEvent(entry_t, "COMPACT", "1"),
    VehicleEntryEvent(entry_t, "COMPACT", "2"),
    VehicleEntryEvent(entry_t, "LARGE", "3"),
    VehicleEntryEvent(entry_t, "MOTORCYCLE", "4"),
    VehicleEntryEvent(entry_t, "MOTORCYCLE", "5"),
    VehicleEntryEvent(entry_t, "MOTORCYCLE", "6"),
    VehicleEntryEvent(entry_t, "MOTORCYCLE", "7"),
]

for event in entry_events:
    tickets.append(p.process_entry_event(event))
    time.sleep(0.5)

exit_events = []

for ticket in tickets:
    exit_events.append(VehicleExitEvent(ticket, exit_t))

print(tickets)

p.process_exit_event(exit_events[2])
p.process_exit_event(exit_events[5])
