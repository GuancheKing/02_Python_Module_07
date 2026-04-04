#!/usr/bin/env python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_factory(factory: HealingCreatureFactory) -> None:
    """Test the healing creature factory."""

    print("Testing Creature with healing capability")
    print(" base:")

    healing_base = factory.create_base()
    print(healing_base.describe())
    print(healing_base.attack())
    print(healing_base.heal("itself"))

    print(" evolved:")

    healing_evolved = factory.create_evolved()
    print(healing_evolved.describe())
    print(healing_evolved.attack())
    print(healing_evolved.heal("itself and others"))


def test_transform_factory(factory: TransformCreatureFactory) -> None:
    """Test the transform creature factory."""

    print("Testing Creature with transform capability")
    print(" base:")

    transform_base = factory.create_base()
    print(transform_base.describe())
    print(transform_base.attack())
    print(transform_base.transform())
    print(transform_base.attack())
    print(transform_base.revert())

    print(" evolved:")

    transform_evolved = factory.create_evolved()
    print(transform_evolved.describe())
    print(transform_evolved.attack())
    print(transform_evolved.transform())
    print(transform_evolved.attack())
    print(transform_evolved.revert())


def main() -> None:
    """Run the exercise 1 test scenario."""
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    test_healing_factory(healing)
    print()
    test_transform_factory(transform)


if __name__ == "__main__":
    main()
