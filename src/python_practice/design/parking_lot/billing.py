from abc import ABC
from abc import abstractclassmethod

from ticket import ParkingTicket


class Receipt:
    def __init__(self, invoice_id, amount_due) -> None:
        pass


class BillingStrategy(ABC):
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def calculate(self, ticket: ParkingTicket):
        pass


class FlatBilling(BillingStrategy):
    def __init__(self, hourly_rate: float) -> None:
        self._hourly_rate = hourly_rate

    def calculate(self, ticket: ParkingTicket) -> Receipt:
        # current time - ticket issue time * hourly rate
        pass
