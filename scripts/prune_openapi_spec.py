"""Restrict an OpenAPI spec to an allowlist of paths plus transitively
referenced components."""

import argparse
import json
from pathlib import Path

import yaml


def referenced_names(node, found: set[tuple[str, str]]) -> None:
    """Collect (section, name) pairs from $ref pointers in `node`."""
    if isinstance(node, dict):
        for key, value in node.items():
            if (
                key == "$ref"
                and isinstance(value, str)
                and value.startswith("#/components/")
            ):
                section, name = value.removeprefix("#/components/").split("/")
                if (section, name) not in found:
                    found.add((section, name))
                    referenced_names(components[section].get(name), found)
            else:
                referenced_names(value, found)
    elif isinstance(node, list):
        for item in node:
            referenced_names(item, found)


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--spec", type=Path, required=True)
parser.add_argument("--allowlist", type=Path, required=True)
parser.add_argument("--out", type=Path, required=True)
args = parser.parse_args()

spec = json.loads(args.spec.read_text())
allow = yaml.safe_load(args.allowlist.read_text())["paths"]

missing = [path for path in allow if path not in spec["paths"]]
if missing:
    raise SystemExit(f"Allowlist paths not in spec: {missing}")

spec["paths"] = {path: spec["paths"][path] for path in allow}

components = spec.get("components", {})
kept: set[tuple[str, str]] = set()
referenced_names(spec["paths"], kept)
for section, values in components.items():
    if section == "securitySchemes":
        continue  # referenced by name, not $ref; keep whole
    components[section] = {
        name: value for name, value in values.items() if (section, name) in kept
    }

args.out.parent.mkdir(parents=True, exist_ok=True)
args.out.write_text(json.dumps(spec, indent=1))
print(f"Pruned to {len(spec['paths'])} paths")
