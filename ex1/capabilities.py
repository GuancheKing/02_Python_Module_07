#!/usr/bin/env python3
from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Abstract capability for healing actions."""

    @abstractmethod
    def heal(self, target: str) -> str:
        """Heal a target and return the corresponding message."""
        raise NotImplementedError


class TransformCapability(ABC):
    """Abstract capability for transformation actions."""

    @abstractmethod
    def transform(self) -> str:
        """Transform the creature and return the corresponding message."""
        raise NotImplementedError

    @abstractmethod
    def revert(self) -> str:
        """Revert the creature and return the corresponding message."""
        raise NotImplementedError
