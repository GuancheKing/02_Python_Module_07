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


class Biyomon(Creature):
    """Base creature of the flame family."""

    def __init__(self) -> None:
        """Initialize Biyomon with fixed attributes."""
        super().__init__("Biyomon", "Flying")

    def attack(self) -> str:
        """Return Biyomon's attack message."""
        return f"{self.name} uses Spiral Twister!"


class Birdramon(Creature):
    """Digi Evolved creature of the flame family."""

    def __init__(self) -> None:
        """Initialize Birdramon with fixed attributes."""
        super().__init__("Birdramon", "Flying/Fire")

    def attack(self) -> str:
        """Return Birdramon's attack message."""
        return f"{self.name} uses Meteor Wing!"


class Syakomon(Creature):
    """Base creature of the aqua family."""

    def __init__(self) -> None:
        """Initialize Syakomon with fixed attributes."""
        super().__init__("Syakomon", "Water")

    def attack(self) -> str:
        """Return Syakomon's attack message."""
        return f"{self.name} uses Black Pearls!"


class Seadramon(Creature):
    """Digi Evolved creature of the aqua family."""

    def __init__(self) -> None:
        """Initialize Seadramon with fixed attributes."""
        super().__init__("Seadramon", "Water")

    def attack(self) -> str:
        """Return Seadramon's attack message."""
        return f"{self.name} uses Ice Blast!"


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


def test_factory(factory: CreatureFactory) -> None:
    """Test a factory by creating and using both family creatures."""

    print("Testing factory")

    base1 = factory.create_base()
    print(base1.describe())
    print(base1.attack())

    evolved1 = factory.create_evolved()
    print(evolved1.describe())
    print(evolved1.attack())
    print()


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    """Make the base creatures of two factories fight."""
    print("Testing battle")

    base1 = factory1.create_base()
    base2 = factory2.create_base()

    print(f"{base1.describe()}\n vs.\n{base2.describe()}\n fight!")
    print(f"{base1.attack()}\n{base2.attack()}")


def main() -> None:
    """Run the test scenario for both factories and their battle."""
    flame = FlameFactory()
    aqua = AquaFactory()

    test_factory(flame)
    test_factory(aqua)
    battle(flame, aqua)


if __name__ == "__main__":
    main()
