#!/usr/bin/env python3
"""Validate the Veyra Reedwater ecology seed dataset using Python's standard library.

This checks structural and cross-record references; it does not run an ecology simulation
or claim that any proposed food-web relationship has been experimentally validated.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "veyra" / "reedwater-basin-ecology.json"
SCHEMA_PATH = ROOT / "data" / "schemas" / "veyra-ecology.schema.json"

PATTERNS = {
    "habitat": re.compile(r"^VEY-START-[0-9]{2}$"),
    "species": re.compile(r"^LA-PLN-[A-Z]{3}-[0-9]{3}$"),
    "resource": re.compile(r"^VEY-RES-[A-Z]{3}-[0-9]{3}$"),
    "interaction": re.compile(r"^VEY-EDGE-[0-9]{3}$"),
}


def fail(errors: list[str]) -> int:
    for error in errors:
        print(f"ERROR: {error}")
    print(f"FAILED: {len(errors)} validation error(s)")
    return 1


def main() -> int:
    errors: list[str] = []
    try:
        data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return fail([f"Could not read or parse dataset/schema: {exc}"])

    for field in ("habitats", "species", "resources", "interactions", "seasonal_scenarios"):
        if not isinstance(data.get(field), list):
            errors.append(f"'{field}' must be an array")
    if errors:
        return fail(errors)

    habitats = data["habitats"]
    species = data["species"]
    resources = data["resources"]
    interactions = data["interactions"]

    def unique_index(records: list[dict], label: str, pattern: re.Pattern[str]) -> dict[str, dict]:
        result: dict[str, dict] = {}
        for index, record in enumerate(records):
            item_id = record.get("id")
            if not isinstance(item_id, str) or not pattern.fullmatch(item_id):
                errors.append(f"{label}[{index}] has invalid ID: {item_id!r}")
                continue
            if item_id in result:
                errors.append(f"duplicate {label} ID: {item_id}")
            result[item_id] = record
        return result

    habitat_by_id = unique_index(habitats, "habitat", PATTERNS["habitat"])
    species_by_id = unique_index(species, "species", PATTERNS["species"])
    resource_by_id = unique_index(resources, "resource", PATTERNS["resource"])
    unique_index(interactions, "interaction", PATTERNS["interaction"])

    if "resources" not in schema.get("required", []):
        errors.append("schema must require the resources array")
    if "resources" not in schema.get("properties", {}):
        errors.append("schema must define resources")

    for label, records in (("species", species), ("resource", resources)):
        for record in records:
            for habitat_id in record.get("habitat_ids", []):
                if habitat_id not in habitat_by_id:
                    errors.append(f"{label} {record.get('id')} references unknown habitat {habitat_id}")

    for resource in resources:
        rid = resource.get("id", "<missing-id>")
        if resource.get("finite_stock") is not True:
            errors.append(f"resource {rid} must declare finite_stock=true")
        if resource.get("stock_model") not in {
            "unbalanced_provisional", "fixed_test_fixture", "runtime"
        }:
            errors.append(f"resource {rid} has invalid stock_model")
        if resource.get("evidence_status") not in {
            "design_only", "implementation_evidence", "test_evidence"
        }:
            errors.append(f"resource {rid} has invalid evidence_status")
        for consumer in resource.get("consumers", []):
            if consumer not in species_by_id:
                errors.append(f"resource {rid} references unknown consumer {consumer}")

    valid_endpoints = set(habitat_by_id) | set(species_by_id) | set(resource_by_id)
    for interaction in interactions:
        edge_id = interaction.get("id", "<missing-id>")
        for endpoint in ("source_id", "target_id"):
            value = interaction.get(endpoint)
            # resource: prefix deliberately allows unresolved resource placeholders.
            if value not in valid_endpoints and not (
                isinstance(value, str) and value.startswith("resource:")
            ):
                errors.append(f"interaction {edge_id} has unknown {endpoint}: {value!r}")
        status = interaction.get("status")
        evidence = interaction.get("evidence", [])
        if status == "implemented" and not evidence:
            errors.append(f"implemented interaction {edge_id} lacks evidence")
        if status == "tested" and not evidence:
            errors.append(f"tested interaction {edge_id} lacks evidence")

    aquatic_edge = next((item for item in interactions if item.get("id") == "VEY-EDGE-013"), None)
    if not aquatic_edge or aquatic_edge.get("status") != "rejected":
        errors.append("VEY-EDGE-013 must remain rejected until aquatic capture is validated")

    counts = data.get("counts", {})
    for key, actual in (
        ("habitats", len(habitats)),
        ("species", len(species)),
        ("resources", len(resources)),
        ("interactions", len(interactions)),
        ("seasonal_scenarios", len(data["seasonal_scenarios"])),
    ):
        if counts.get(key) != actual:
            errors.append(f"counts.{key} is {counts.get(key)!r}; expected {actual}")

    if errors:
        return fail(errors)
    print(
        "PASS: JSON parsed; IDs unique and patterned; habitat, consumer, and interaction "
        "references resolve; resources are finite; evidence/status checks pass."
    )
    print(
        f"Counts: {len(habitats)} habitats, {len(species)} species, {len(resources)} resources, "
        f"{len(interactions)} interactions, {len(data['seasonal_scenarios'])} seasonal scenarios."
    )
    print("Scope: structural validation only; no JSON Schema engine or ecology simulation run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
