from abc import ABC
from abc import abstractclassmethod
from dataclasses import dataclass

from ticket import ParkingTicket


@dataclass
class Receipt:
    invoice_id: str
    amount_due: str


class BillingStrategy(ABC):
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def calculate(self, ticket: ParkingTicket) -> Receipt:
        pass


class FlatBilling(BillingStrategy):
    def __init__(self, hourly_rate: float) -> None:
        self._hourly_rate = hourly_rate

    def calculate(self, ticket: ParkingTicket) -> Receipt:
        # current time - ticket issue time * hourly rate
        pass
