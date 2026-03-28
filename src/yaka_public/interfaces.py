"""Public interface skeleton for the YAKA automation stack.

This file exposes the high-level components of the public method without
shipping the private implementation details.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class ScannerOutput:
    clickables: list[dict[str, Any]]
    win_condition: dict[str, Any]
    transitions: list[dict[str, Any]]
    levels: list[dict[str, Any]]


@dataclass
class InvariantSet:
    hubs: list[str]
    gate_sequence: list[str]
    capacity_constraints: dict[str, Any]
    subgoals: list[dict[str, Any]]


class GameSourceScanner:
    """Extract structural mechanics from a game description."""

    def scan(self, source_text: str) -> ScannerOutput:
        raise NotImplementedError


class InvariantInterpreter:
    """Compress gameplay traces into reusable structural invariants."""

    def infer(self, scanner_output: ScannerOutput, traces: list[dict[str, Any]]) -> InvariantSet:
        raise NotImplementedError


class TargetedTraceGenerator:
    """Generate probes that confirm or reject candidate invariants."""

    def generate(self, scanner_output: ScannerOutput, invariants: InvariantSet) -> list[dict[str, Any]]:
        raise NotImplementedError


class HypothesisConditionedProbePlanner:
    """Plan narrow hypothesis-first probes instead of blind sweeps."""

    def plan(self, scanner_output: ScannerOutput, invariants: InvariantSet) -> list[dict[str, Any]]:
        raise NotImplementedError


class WorldModelBuilder:
    """Build a deterministic solver from extracted mechanics and invariants."""

    def build(self, scanner_output: ScannerOutput, invariants: InvariantSet) -> Any:
        raise NotImplementedError
