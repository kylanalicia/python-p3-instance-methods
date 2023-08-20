#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

    def sit(self):
        return "The dog is sitting."  # Updated to return the correct string
