#!/usr/bin/env python3
"""Deterministic test-fixture checks for finite Veyra resource patches.

This is a small balance prototype, not the game runtime and not a calibrated
planetary ecology simulation. Numeric values below are synthetic test fixtures,
not canonical resource quantities or growth rates.
"""
from __future__ import annotations

import unittest
from dataclasses import dataclass


@dataclass
class Patch:
    stock: float
    capacity: float
    renewal_rate: float

    def consume(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("consumption cannot be negative")
        taken = min(self.stock, amount)
        self.stock -= taken
        return taken

    def renew(self, *, conditions_suitable: bool) -> None:
        if conditions_suitable:
            self.stock = min(self.capacity, self.stock + self.renewal_rate)

    def flood_redistribute(self, destination: "Patch", amount: float) -> float:
        """Move finite stock between patches; never create stock."""
        if amount < 0:
            raise ValueError("transfer cannot be negative")
        moved = min(self.stock, amount, destination.capacity - destination.stock)
        self.stock -= moved
        destination.stock += moved
        return moved


class ResourceBalanceTests(unittest.TestCase):
    def test_overharvest_stops_at_zero(self) -> None:
        patch = Patch(stock=4, capacity=10, renewal_rate=1)
        taken = patch.consume(100)
        self.assertEqual(taken, 4)
        self.assertEqual(patch.stock, 0)
        self.assertGreaterEqual(patch.stock, 0)

    def test_drought_pauses_renewal(self) -> None:
        patch = Patch(stock=3, capacity=10, renewal_rate=2)
        patch.renew(conditions_suitable=False)
        self.assertEqual(patch.stock, 3)
        patch.renew(conditions_suitable=True)
        self.assertEqual(patch.stock, 5)

    def test_renewal_never_exceeds_capacity(self) -> None:
        patch = Patch(stock=9, capacity=10, renewal_rate=5)
        patch.renew(conditions_suitable=True)
        self.assertEqual(patch.stock, 10)

    def test_flood_redistributes_without_creating_stock(self) -> None:
        upstream = Patch(stock=8, capacity=10, renewal_rate=0)
        downstream = Patch(stock=1, capacity=10, renewal_rate=0)
        before = upstream.stock + downstream.stock
        moved = upstream.flood_redistribute(downstream, 4)
        after = upstream.stock + downstream.stock
        self.assertEqual(moved, 4)
        self.assertEqual(after, before)
        self.assertEqual((upstream.stock, downstream.stock), (4, 5))

    def test_transfer_cannot_move_more_than_source_has(self) -> None:
        source = Patch(stock=2, capacity=5, renewal_rate=0)
        destination = Patch(stock=0, capacity=5, renewal_rate=0)
        moved = source.flood_redistribute(destination, 20)
        self.assertEqual(moved, 2)
        self.assertEqual(source.stock, 0)
        self.assertEqual(destination.stock, 2)

    def test_consumption_rejects_negative_amount(self) -> None:
        with self.assertRaises(ValueError):
            Patch(stock=1, capacity=2, renewal_rate=0).consume(-1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
