#!/usr/bin/env python3
from typing import TypeAlias

from ex0 import FlameFactory, AquaFactory
from ex0.factory_0 import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy as Normal
from ex2 import AggressiveStrategy as Aggressive
from ex2 import DefensiveStrategy as Defensive
from ex2.strategies import BattleStrategy


Opponent: TypeAlias = tuple[CreatureFactory, BattleStrategy]


def battle(opponent1: Opponent, opponent2: Opponent) -> None:
    """Make two opponents fight using their associated strategies."""

    factory1, strategy1 = opponent1
    factory2, strategy2 = opponent2

    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print("\n* Battle *")
    print(creature1.describe())
    print(" vs.")
    print(creature2.describe())
    print(" now fight!")

    strategy1.act(creature1)
    strategy2.act(creature2)


def run_tournament(opponents: list[Opponent]) -> None:
    """Run a round-robin tournament."""

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for i in range(0, len(opponents)):
            for j in range(i+1, len(opponents)):
                battle(opponents[i], opponents[j])
    except ValueError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    """Run all test tournaments."""

    tournament_0 = [
        (FlameFactory(), Normal()),
        (HealingCreatureFactory(), Defensive())
        ]

    tournament_1 = [
        (FlameFactory(), Aggressive()),
        (HealingCreatureFactory(), Defensive())
    ]

    tournament_2 = [
        (AquaFactory(), Normal()),
        (HealingCreatureFactory(), Defensive()),
        (TransformCreatureFactory(), Aggressive()),
        (FlameFactory(), Normal())
    ]

    print("Tournament 0 (basic)")
    print("[ (Biyomon+Normal), (Patamon+Defensive) ]")
    run_tournament(tournament_0)

    print("\nTournament 1 (error)")
    print("[ (Biyomon+Aggressive), (Patamon+Defensive) ]")
    run_tournament(tournament_1)

    print("\nTournament 2 (multiple)")
    print("[ (Syakomon+Normal), (Patamon+Defensive),"
          " (Gatomon+Aggressive), (Biyomon+Normal)]")
    run_tournament(tournament_2)


if __name__ == "__main__":
    main()
