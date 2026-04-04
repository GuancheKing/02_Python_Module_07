#!/usr/bin/env python3
from ex0.creature import Creature
from .capabilities import HealCapability


class Patamon(Creature, HealCapability):
    """Base creature with healing capability."""

    def __init__(self) -> None:
        """Initialize Patamon with fixed attributes."""
        super().__init__("Patamon", "Holy/Flying")

    def attack(self) -> str:
        """Return Patamon's attack message."""
        return f"{self.name} uses Air Shot!"

    def heal(self, target: str) -> str:
        """Heal a target with a small healing effect."""
        return f"{self.name} heals {target} for a small amount."


class Angemon(Creature, HealCapability):
    """Evolved creature with healing capability."""

    def __init__(self) -> None:
        """Initialize Angemon with fixed attributes."""
        super().__init__("Angemon", "Holy/Flying")

    def attack(self) -> str:
        """Return Angemon's attack message."""
        return f"{self.name} uses Heaven's Knuckle!"

    def heal(self, target: str) -> str:
        """Heal a target with a large healing effect."""
        return f"{self.name} heals {target} for a large amount."
