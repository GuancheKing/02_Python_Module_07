#!/usr/bin/env python3
from abc import ABC, abstractmethod
from .creature import Creature
from .creatures import Biyomon, Birdramon, Syakomon, Seadramon


class CreatureFactory(ABC):
    """Abstract factory for related creature families."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create and return the base creature of a family."""
        raise NotImplementedError

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create and return the evolved creature of a family."""
        raise NotImplementedError


class FlameFactory(CreatureFactory):
    """Factory for the flame creature family."""

    def create_base(self) -> Creature:
        """Create and return the base flame creature."""
        return Biyomon()

    def create_evolved(self) -> Creature:
        """Create and return the evolved flame creature."""
        return Birdramon()


class AquaFactory(CreatureFactory):
    """Factory for the aqua creature family."""

    def create_base(self) -> Creature:
        """Create and return the base aqua creature."""
        return Syakomon()

    def create_evolved(self) -> Creature:
        """Create and return the evolved aqua creature."""
        return Seadramon()
