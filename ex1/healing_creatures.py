#!/usr/bin/env python3
from ..ex0.creature import Creature
from .capabilities import HealCapability


class Patamon(Creature, HealCapability):

    def __init__(self) -> None:
        super().__init__("Patamon", "Holy/Flying")

    def attack(self) -> str:
        """Return Patamon's attack message."""
        return f"{self.name} uses Air Shot!"

    def heal(self, target) -> str:
        return f"{self.name} healed"


class Angemon(Creature, HealCapability):

    def __init__(self) -> None:
        super().__init__("Angemon", "Holy/Flying")

    def attack(self) -> str:
        """Return Angemon's attack message."""
        return f"{self.name} uses Heaven's Knuckle!"

    def heal(self, target) -> str:
        return f"{self.name} healed"
