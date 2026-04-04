#!/usr/bin/env python3
from ..ex0.creature import Creature
from .capabilities import TransformCapability


class Gatomon(Creature, TransformCapability):

    def __init__(self) -> None:
        super().__init__("Gatomon", "Normal")

    def attack(self) -> str:
        """Return Gatomon's attack message."""
        return f"{self.name} uses Cat Punch!"

    def transform(self, target) -> str:
        return f"{self.name} transformed"

    def revert(self) -> str:
        return f"{self.name} reverted"


class Betsumon(Creature, TransformCapability):

    def __init__(self) -> None:
        super().__init__("BEtsumon", "Normal/Puppet")

    def attack(self) -> str:
        """Return Betsumon's attack message."""
        return f"{self.name} uses Tsukkomi Punch!"

    def transform(self, target) -> str:
        return f"{self.name} transformed"

    def revert(self) -> str:
        return f"{self.name} reverted"
