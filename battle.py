#!/usr/bin/env python3
from ex0 import CreatureFactory, FlameFactory, AquaFactory


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

    print(f"{base1.describe()}")
    print(" vs.")
    print(f"{base2.describe()}")
    print(" fight!")
    print(f"{base1.attack()}")
    print(f"{base2.attack()}")


def main() -> None:
    """Run the test scenario for both factories and their battle."""
    flame = FlameFactory()
    aqua = AquaFactory()

    test_factory(flame)
    test_factory(aqua)
    battle(flame, aqua)


if __name__ == "__main__":
    main()
