from enum import Enum


class Mood(Enum):
    EXCITED = "excited"
    INDIFFERENT = "indifferent"
    FRUSTRATED = "frustrated"
    ANGRY = "angry"


class Person:
    def __init__(self, mood: Mood = Mood.EXCITED):
        self.mood: Mood = mood
        self.wait_time: int = 0

    def wait(self, time: int):
        self.wait_time += time
        self.update_mood()

    def update_mood(self):
        if self.wait_time > 40:
            self.mood = Mood.ANGRY
        elif self.wait_time > 30:
            self.mood = Mood.FRUSTRATED
        elif self.wait_time > 20:
            self.mood = Mood.INDIFFERENT


class ImitateTime:
    def __init__(self):
        self.hour = 10
        self.min = 0
        self.time = (self.hour, self.min)

    def time_pass(self, minutes: int):
        self.min += minutes
        if self.min > 60:
            self.hour += int(self.min / 60)
            self.min %= 60


