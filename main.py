from util.helper import Person
from burger_joints import BurgerJoint
import time


class ABeautifulDay:
    def __init__(self):
        self.me = Person()
        self.my_date = Person()

    def burger_date(self, joint: BurgerJoint):
        joint.buy_burger([self.me, self.my_date])

        print("My mood have become", self.me.mood.value)
        print("and my dates mood has become", self.me.mood.value)
        print("since we waited for", self.me.wait_time, "minutes each")








