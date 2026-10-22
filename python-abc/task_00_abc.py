#!/usr/bin/python3
"""Define a function
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal class"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Dog class inherited from Animal"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class inherited from Animal"""
    def sound(self):
        return "Meow"
