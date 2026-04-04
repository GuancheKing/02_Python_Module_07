#!/usr/bin/env python3
from ex0.factory_0 import CreatureFactory
from .healing_creatures import Patamon, Angemon
from .transform_creatures import Gatomon, Betsumon


class HealingCreatureFactory(CreatureFactory):
    """Factory for creatures with healing capability."""

    def create_base(self) -> Patamon:
        """Create and return the base healing creature."""
        return Patamon()

    def create_evolved(self) -> Angemon:
        """Create and return the evolved healing creature."""
        return Angemon()


class TransformCreatureFactory(CreatureFactory):
    """Factory for creatures with transform capability."""

    def create_base(self) -> Gatomon:
        """Create and return the base transform creature."""
        return Gatomon()

    def create_evolved(self) -> Betsumon:
        """Create and return the evolved transform creature."""
        return Betsumon()
