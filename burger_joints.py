from util.helper import Person


class BurgerJoint:
    def buy_burger(self, people: list[Person]):
        self.wait_in_line(people)
        self.order_burger(people)
        self.wait_order(people)

    def wait_in_line(self, people: list[Person]):
        for person in people:
            person.wait(20)
        print("The line was too long and we had to wait 20 minutes in line since people were",
              "not given an order ticket and were afraid their food would be stolen")

    def order_burger(self, people: list[Person]):
        for person in people:
            person.wait(5)
        print("We thought about which fancy burger we had to eat that day and talked to the kind cashier")

    def wait_order(self, people: list[Person]):
        # TODO block cook
        for person in people:
            person.wait(25)


class ConcurrentBurgerJoint(BurgerJoint):
    def buy_burger(self, people: list[Person]):
        self.wait_in_line(people)
        self.order_burger(people)
        self.wait_order(people)

    def wait_in_line(self, people: list[Person]):
        for person in people:
            person.wait(3)
        print("The order lines were relatively empty since everyone just had to give their",
              "order and receive an order ticket to later pickup their food")

    def wait_order(self, people: list[Person]):
        print("We never had to wait on foot in line to make sure our food is not stolen and just admired how",
              "how beautiful our outfits on that day")
