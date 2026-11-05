#!/usr/bin/env bash
# Regenerate the vendored nacsos-core API client (src/what_works_repo/nacsos_api/generated).
#
# Refresh the spec snapshot from the deployed core first:
#   curl -fsS "<core-base-url>/openapi.json" -o api/openapi.json
# Offline, dump it from a nacsos-core checkout with its own venv:
#   .venv/bin/python -c "import json; from main import app; \
#     json.dump(app.openapi(), open('.../api/openapi.json','w'), indent=1)"
# Endpoints to adopt: add them to api/endpoint_allowlist.yaml and re-run.
set -euo pipefail
cd "$(dirname "$0")/.."

VERSION=0.29.1 # openapi-python-client; bump deliberately

uv run --no-project --with pyyaml python scripts/prune_openapi_spec.py \
	--spec api/openapi.json \
	--allowlist api/endpoint_allowlist.yaml \
	--out api/.openapi_pruned.json

uv run --no-project --with openapi-python-client=="${VERSION}" openapi-python-client generate \
	--path api/.openapi_pruned.json \
	--config api/client-config.yaml \
	--meta none \
	--output-path src/what_works_repo/nacsos_api/generated \
	--overwrite

rm api/.openapi_pruned.json
echo "Client regenerated in src/what_works_repo/nacsos_api/generated"
