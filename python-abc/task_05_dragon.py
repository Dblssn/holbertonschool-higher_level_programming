#!/usr/bin/python3
"""Module containing mixins and the Dragon class"""


class SwimMixin:
    """Give a creature the ability to swim"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Give a creature the ability to fly"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon that can swim and fly"""

    def roar(self):
        print("The dragon roars!")
