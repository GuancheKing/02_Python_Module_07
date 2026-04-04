#!/usr/bin/env python3
from .creature import Creature


class Syakomon(Creature):
    """Base creature of the aqua family."""

    def __init__(self) -> None:
        """Initialize Syakomon with fixed attributes."""
        super().__init__("Syakomon", "Water")

    def attack(self) -> str:
        """Return Syakomon's attack message."""
        return f"{self.name} uses Black Pearls!"


class Seadramon(Creature):
    """Digi Evolved creature of the aqua family."""

    def __init__(self) -> None:
        """Initialize Seadramon with fixed attributes."""
        super().__init__("Seadramon", "Water")

    def attack(self) -> str:
        """Return Seadramon's attack message."""
        return f"{self.name} uses Ice Blast!"
