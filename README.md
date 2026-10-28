# what-works-repo

Active-learning screening pipeline: sample → import to NACSOS → human annotation
→ DEET auto-annotation → resolve → stopping criterion.

## Quick start
uv sync
uv run nacsos-login       # store your personal NACSOS API token (first run per token lifetime)
uv run snakemake          # runs until a manual step is needed, then stops

## Layout
| Path            | What it holds                                            |
|-----------------|----------------------------------------------------------|
| `Snakefile`     | Pipeline definition (the entry point)                    |
| `src/`          | Python package (`what_works_repo`) — all real logic      |
| `config/`       | Run configuration (`snakemake.yaml`)                     |
| `profiles/`     | Snakemake command-line defaults (auto-loaded)            |
| `data/`         | Inputs & outputs — DVC-tracked, not in git (`data.dvc`)  |
| `deet_projects/`| Per-batch DEET extraction configs & runs                 |
| `docs/`         | mkdocs site (`mkdocs.yml`); see `docs/workflow.md`       |

## NACSOS API access
All data exchange with NACSOS goes through the nacsos-core REST API.

**Login** — each user runs `uv run nacsos-login`.
The command prints the URL of your NACSOS profile page, where the token is shown once
you are signed in; copy it there and paste it into the terminal.
The token is validated against the server before being stored at
`~/.config/nacsos/token` (mode 600), shared by all checkouts of that user.
Tokens expire after ~8 days; re-running the command then just asks for a fresh paste.
For cluster jobs, set the `NACSOS_API__API_TOKEN` environment variable instead
(it takes precedence over the file).
The deployment URL is group config: `nacsos_api.base_url` in `config/snakemake.yaml`.

**The client** is generated code, committed (vendored) under
`src/what_works_repo/nacsos_api/generated/`, so a checkout needs no codegen step.
Hand-written code sits beside it: `client.py` (token auth, with re-login and replay
on expiry for runs longer than the token lifetime), `ops.py` (shared higher-level
operations), `login.py` (the login command).

**After a nacsos-core server update**, refresh the spec snapshot
(`curl <base-url>/openapi.json -o api/openapi.json`; other options in the script
header), add any new endpoints the pipeline needs to `api/endpoint_allowlist.yaml`,
then run `scripts/regen_nacsos_client.sh` and commit the regenerated tree.
The generator version is pinned in that script; the generated tree is excluded from
our ruff/ty config.
Keeping this here rather than in a shared package is deliberate: the vendored tree
is a build artifact of spec + allowlist, and the allowlist encodes what this
pipeline may touch.
A second consumer of the API would be the cue to extract a group package.

## Manual steps
The workflow pauses and prints "MANUAL STEP REQUIRED" when it needs a human
(create scope, finalise DEET run, assign docs). Do the step, write the ID to the
named file, and re-run