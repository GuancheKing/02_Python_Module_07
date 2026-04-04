#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base class for all creatures."""

    def __init__(self, name: str, creature_type: str) -> None:
        """Initialize a creature with a name and a type."""
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        """Return the attack message of the creature."""
        raise NotImplementedError

    def describe(self) -> str:
        """Return the standard description of the creature."""
        return f"{self.name} is a {self.creature_type} type Digimon"
