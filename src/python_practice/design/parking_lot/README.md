# Design a parking lot system

## What type of question is this?

* Do you want me to come up with a system design, or class diagram/hierarchy or just write methods class etch

## Clarify requirements/Scope

* How is the parking lot designed? Is it an open space? Is there an accessibility requirements? (i.e are some parking lots only available after the other ones get filled)

    Assume for now it is open space and no order to park the car

* How many spots are we talking about? (In case you are doing system design)?

    Assume for now that we have 1000 spots etc.

* Does each parking lot have a unique number ?

    Yes

* Do we have multiple types of spots or just one?

    let say for now you have three types of spots. Large, compact and small/Motorcycle

* Do we have one level or multiple

    Yes you have multiple levels

* How many entry and exits do the lot have ?

    For now lets say we have 1 entries and 1 exits. (follow-up how do you design for more entries and exits?
    Concurrency issues?)

* How are we charging for the parking? Is it a flat rate for all types based on per hour rate or are
the costs different for different type of spot?

    Charge flat rate of $5 per hour for now

* What is the pricing strategy? Do we allow cash, creditcards etc.?

    You can pay wit either credit card or cash

* Do we allow small vehicle to park on medium or large spot?

    yes small(motorcycle) size can be parked in medium or large if small is not available.  Medium(compact car) can be parked
    in large spot but large(Bus) can only be parked in large spot

* Any premium parking spots (for example handicaps, or reserved etc)?

    For now no.

* What happens if no spots available a vehicle?

    Send it back

## determine use cases

* Vehicle enters at the entry terminal. This triggers the vehicle entry event (for example, the driver pushes a button
to get a ticket or some sensors triggers this event). The system finds the appropriate spot for the vehicle (for example, the
user was required to select the vehicle type or some sensors can pick up the vehicle size). The system outputs a ticket
with the spot id, level, and issue time. The vehicle then goes to this spot and parks.

* Vehicles enters the exit terminal and inserts the ticket or enters the ticket id. This triggers the vehicle exit event. From the ticket id, it has all the information about the issue time and spot type etc and the system calculates the total amount to be paid. The terminal then prints a billing receipt and waits for the driver to pay. Once payment is successful, the vehicle can exit the lot and the parking spot linked to this ticket is marked free

## identify key objects/classes

* ParkingSpot (Abstract class)

    Extended by MotorcycleParkingSpot, CompactParkingSpot, LargeParkingSpot

* ParkingAssignmentStrategy (Abstract class)

    Extended by FillBottomLevelFirst, FillNearestToTerminalFirst, etc

* Terminal (Abstract Class)

    Extended by EntryTerminal, ExitTerminal

* Ticket (dataclass)

    contains id, spot, maybe vehicle licence plate etc

* ObjectFactory

    Used to register builders and then use these builders to instantiate objects

* Builders

    Several Builder classes for Terminals, Spots, Assignment Strategies etc

* ParkingLot

    Use factory pattern to initialize objects. Can have multiple Parking lots with id being the zip for example.

Note I have omitted Vehicles from the design but we can also have these and link them to parking spot in case we want
to store various data related to vehicles for example, their make, year etc

## Class diagram

![class diagram](./class_diagram.png)
