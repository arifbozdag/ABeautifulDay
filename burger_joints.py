from typing import List
import time
from util.helper import clock

from util.helper import Person


class BurgerJoint:
    def __init__(self, customer_queue: List[Person]):
        self.queue = customer_queue
        self.service_time = 0

    def start_day(self):
        start_service = time.time()
        for person in self.queue:
            person.wait(self.service_time)  # wait for previous in queue
            person.order = self.get_order(person)
            self.prepare_meal(person)
            self.service_time += person.wait_time
        end_service = time.time()
        print("everyone served in ", time.ctime(end_service - start_service))

    def get_order(self, person: Person):
        duration = 3
        time.sleep(duration / 10)
        person.wait(duration)
        order = time.time()
        print("new order at", clock(order))
        return order

    def prepare_meal(self, person):
        duration = 9
        time.sleep(duration / 10)
        person.wait(duration)
        print(clock(person.order), "order served at", clock(time.time()))

    def buy_burger(self, people: List[Person]):
        self.wait_in_line(people)
        self.order_burger(people)
        self.wait_order(people)

    def wait_in_line(self, people: List[Person]):
        for person in people:
            person.wait(20)
        print("The line was too long and we had to wait 20 minutes in line since people were",
              "not given an order ticket and were afraid their food would be stolen")

    def order_burger(self, people: List[Person]):
        for person in people:
            person.wait(5)
        print("We thought about which fancy burger we had to eat that day and talked to the kind cashier")

    def wait_order(self, people: List[Person]):
        # TODO block cook
        for person in people:
            person.wait(25)


class ConcurrentBurgerJoint(BurgerJoint):
    def __init__(self):
        super().__init__()

    def buy_burger(self, people: List[Person]):
        self.wait_in_line(people)
        self.order_burger(people)
        self.wait_order(people)

    def wait_in_line(self, people: List[Person]):
        for person in people:
            person.wait(3)
        print("The order lines were relatively empty since everyone just had to give their",
              "order and receive an order ticket to later pickup their food")

    def wait_order(self, people: List[Person]):
        print("We never had to wait on foot in line to make sure our food is not stolen and just admired how",
              "how beautiful our outfits on that day")
