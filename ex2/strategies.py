#!/usr/bin/env python3
from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability

valid_classes = [Creature, HealCapability, TransformCapability]

class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> None:
        raise NotImplementedError

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        raise NotImplementedError


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True
    
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature) == True:
            print(creature.attack())
        return


class AggressiveStrategy(BattleStrategy):
    
    def is_valid(self, creature: (Creature | TransformCapability)) -> bool:
        if cre