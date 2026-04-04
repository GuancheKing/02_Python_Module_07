#!/usr/bin/env python3
from ex0.creature import Creature
from .capabilities import TransformCapability


class Gatomon(Creature, TransformCapability):
    """Base creature with transform capability."""

    def __init__(self) -> None:
        """Initialize Gatomon with its default state."""
        super().__init__("Gatomon", "Normal")
        self.state: str = "normal"

    def attack(self) -> str:
        """Return Gatomon's attack message based on its state."""
        if self.state == "transformed":
            return f"{self.name} uses boosted FAST Cat Punch!"
        return f"{self.name} uses Cat Punch!"

    def transform(self) -> str:
        """Transform Gatomon into its enhanced form."""
        self.state = "transformed"
        return f"{self.name} shifts into a quicker form!"

    def revert(self) -> str:
        """Revert Gatomon to its normal form."""
        self.state = "normal"
        return f"{self.name} returns to normal"


class Betsumon(Creature, TransformCapability):
    """Evolved creature with transform capability."""

    def __init__(self) -> None:
        """Initialize Betsumon with its default state."""
        super().__init__("Betsumon", "Normal/Puppet")
        self.state: str = "normal"

    def attack(self) -> str:
        """Return Betsumon's attack message based on its state."""
        if self.state == "transformed":
            return f"{self.name} unleashes an ULTRA Tsukkomi Punch"
        return f"{self.name} uses Tsukkomi Punch!"

    def transform(self) -> str:
        """Transform Betsumon into its enhanced form."""
        self.state = "transformed"
        return f"{self.name} morphs into its opponent!"

    def revert(self) -> str:
        """Revert Betsumon to its normal form."""
        self.state = "normal"
        return f"{self.name} stabilizes its form."
