import json
from collections import defaultdict

from events import VehicleEntryEvent
from parking_spot import ParkingSpot
from parking_spot import spot_factory
from ticket import ParkingTicket

from src.python_practice.design.parking_lot.billing import BillingStrategy
from src.python_practice.design.parking_lot.billing import Receipt
from src.python_practice.design.parking_lot.events import VehicleExitEvent


class ParkingLot:
    def __init__(self, zip, **config):
        self._zip = zip
        self._billing_strategy = None
        self._assignment_strategy = None
        self._spots = defaultdict(list)
        self._int_objects(**config)
        # print(self._parking_spots)

    def _int_objects(self, **config):

        for level in config["levels"]:
            # print(level["parking_spots"])
            for spot_type, freq in level["parking_spots"].items():
                # print(spot_type, freq)
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

    def get_free_spot(self, spot_type: str) -> ParkingSpot:
        return self._assignment_strategy.get_parking_spot(spot_type)

    def release_spot(self, spot: ParkingSpot) -> bool:
        return self._assignment_strategy.release_parking_spot(spot)

    def get_billing_strategy(self) -> BillingStrategy:
        return self._billing_strategy


with open("config.json") as f:
    config = json.load(f)

p = ParkingLot("V5G4N7", **config)
