from unittest import TestCase
from main import ABeautifulDay
from util.helper import Mood
from burger_joints import BurgerJoint, ConcurrentBurgerJoint


class TestBurgerJoints(TestCase):
    def test_burger_joint(self):
        day = ABeautifulDay()
        day.burger_date(BurgerJoint())

        self.assertEqual(Mood.ANGRY, day.me.mood)
        self.assertEqual(Mood.ANGRY, day.my_date.mood)

    def test_concurrent_burger_joint(self):
        print("The next day...")
        day = ABeautifulDay()
        day.burger_date(ConcurrentBurgerJoint())

        self.assertEqual(Mood.EXCITED, day.me.mood)
        self.assertEqual(Mood.EXCITED, day.my_date.mood)
