# YAKA

Public proof-and-materials repository for the YAKA ARC-AGI-3 submission.

This repo exists to support the public scorecards and community leaderboard
submission. It is intentionally narrow: it documents the method, links the
official results, and exposes a small public interface layer for the automation
stack. It does not contain the full private implementation used to produce the
runs.

## Official Public Scorecards

| Game | Outcome | Actions | Scorecard |
| --- | --- | ---: | --- |
| `ls20` | `WIN`, `7/7` | `378` | https://arcprize.org/scorecards/a721e6be-3654-4463-aea4-2000c818c99d |
| `ft09` | `WIN`, `6/6` | `75` | https://arcprize.org/scorecards/ebe3d845-68ed-4147-88c4-ddc14e2132b1 |
| `vc33` | `WIN`, `7/7` | `221` | https://arcprize.org/scorecards/f8f98c2d-3de1-4bc9-9a5d-854283f05455 |

All three runs were:
- provider-free
- backend-free
- `$0.00` cost
- tagged `agent:yaka`, `runtime:hive`, `agent_family:hive_world_model`

## Method

YAKA is a deterministic world-model method built on the Oppositional Vector
Strategy framework and Hive reasoning engine.

The working loop for these public ARC-AGI-3 games was:
1. Read exact game structure.
2. Extract irreducible mechanics through recursive compression.
3. Build the minimum deterministic world model for that game.
4. Verify offline on an exact or source-faithful path.
5. Run the live ARC scorecard only after the offline and live paths matched.

This was applied successfully to three different game classes:
- `ls20`: movement, transforms, movers, recharges, pushers
- `ft09`: click-state constraint solving
- `vc33`: structural rail routing, transfer gates, and late-level phase constraints

## What This Public Repo Contains

- official public scorecard links
- community leaderboard submission materials
- short method and results notes
- a small public source skeleton for the automation stack

## What This Public Repo Does Not Contain

- the full private implementation
- internal runtime infrastructure
- private training data
- deeper solver internals beyond the public interface layer

## Repository Layout

- [`community/submission.yaml`](community/submission.yaml)
- [`community/README.md`](community/README.md)
- [`docs/METHOD.md`](docs/METHOD.md)
- [`docs/RESULTS.md`](docs/RESULTS.md)
- [`docs/PUBLIC_SCOPE.md`](docs/PUBLIC_SCOPE.md)
- [`src/yaka_public/interfaces.py`](src/yaka_public/interfaces.py)

## Honest Limitations

The public ARC-AGI-3 wins were achieved with a source-grounded world-model
workflow. The source-free automation path is under active development.

This repository should be read as an honest public proof/materials repo, not as
a claim that the entire private system has been open-sourced.
