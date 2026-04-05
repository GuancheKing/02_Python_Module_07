#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import cast

from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability
from ex1.healing_creatures import Patamon, Angemon
from ex1.transform_creatures import Gatomon, Betsumon
from .exceptions import InvalidStrategyCreatureError


class BattleStrategy(ABC):
    """Base class for all battle strategies."""

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Apply the strategy to the creature."""
        raise NotImplementedError

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Check if the creature can use this strategy."""
        raise NotImplementedError


class NormalStrategy(BattleStrategy):
    """Basic attack strategy."""

    def is_valid(self, creature: Creature) -> bool:
        """Works with any creature."""
        return True

    def act(self, creature: Creature) -> None:
        """Just perform a normal attack."""
        if self.is_valid(creature):
            print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """Strategy for creatures that can transform."""

    def is_valid(self, creature: Creature) -> bool:
        """Only valid for transformable creatures."""
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        """Transform, attack, then revert."""
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid creature '{creature.name}' for aggressive strategy"
                )
        fighting_creature = cast(Gatomon | Betsumon, creature)
        print(fighting_creature.transform())
        print(fighting_creature.attack())
        print(fighting_creature.revert())


class DefensiveStrategy(BattleStrategy):
    """Strategy for creatures that can heal."""

    def is_valid(self, creature: Creature) -> bool:
        """Only valid for healing creatures."""
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        """Attack and then heal."""
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid creature '{creature.name}' for defensive strategy"
                )
        fighting_creature = cast(Patamon | Angemon, creature)
        print(fighting_creature.attack())
        print(fighting_creature.heal("itself"))
