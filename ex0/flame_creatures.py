#!/usr/bin/env python3
from .creature import Creature


class Biyomon(Creature):
    """Base creature of the flame family."""

    def __init__(self) -> None:
        """Initialize Biyomon with fixed attributes."""
        super().__init__("Biyomon", "Fire/Flying")

    def attack(self) -> str:
        """Return Biyomon's attack message."""
        return f"{self.name} uses Spiral Twister!"


class Birdramon(Creature):
    """Digi Evolved creature of the flame family."""

    def __init__(self) -> None:
        """Initialize Birdramon with fixed attributes."""
        super().__init__("Birdramon", "Flying/Fire")

    def attack(self) -> str:
        """Return Birdramon's attack message."""
        return f"{self.name} uses Meteor Wing!"
