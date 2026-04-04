#!/usr/bin/env python3
from abc import ABC, abstractmethod


class HealCapability(ABC):

    @abstractmethod
    def heal(self, target) -> str:
        return f"{self.name} healed"


class TransformCapability(ABC):

    def __init__(self, state: str) -> None:
        self.state = state

    @abstractmethod
    def transform(self) -> str:
        return f"{self.name} transformed"

    @abstractmethod
    def revert(self) -> str:
        return f"{self.name} reverted"
