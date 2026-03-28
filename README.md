# YAKA / ARCAGI

Public proof-and-materials repository for the YAKA ARC-AGI-3 submission.

This repository is intentionally narrow. It documents the method, links the
official public scorecards, and exposes a small public source skeleton for the
automation stack. It does not contain the full private implementation used to
produce the runs.

## Official Public Scorecards

| Game | Outcome | Actions | Scorecard |
| --- | --- | ---: | --- |
| `ls20` | `WIN`, `7/7` | `378` | https://arcprize.org/scorecards/a721e6be-3654-4463-aea4-2000c818c99d |
| `ft09` | `WIN`, `6/6` | `75` | https://arcprize.org/scorecards/ebe3d845-68ed-4147-88c4-ddc14e2132b1 |
| `vc33` | `WIN`, `7/7` | `221` | https://arcprize.org/scorecards/f8f98c2d-3de1-4bc9-9a5d-854283f05455 |

All three scorecards were produced with:
- `agent:yaka`
- `runtime:hive`
- `provider:none`
- `backend:none`
- `$0.00` cost

## Method Summary

YAKA is a provider-free deterministic world-model method built on the
Oppositional Vector Strategy (OVS) framework and Hive reasoning engine.

The working loop used for the public ARC-AGI-3 games was:
1. Read exact game structure.
2. Extract irreducible mechanics through recursive compression.
3. Build the minimum deterministic world model for that game.
4. Verify offline on an exact or source-faithful path.
5. Run the live ARC scorecard only after the offline/live path matched.

## What Is In This Public Repo

- public scorecard links
- community leaderboard submission files
- short architecture and method notes
- small public source interfaces for the automation stack

## What Is Not In This Public Repo

- the full private implementation
- private runtime infrastructure
- internal training data
- private solver details beyond the public interface layer

## Repository Layout

- [community/submission.yaml](/home/simon/ARCAGI/community/submission.yaml)
- [community/README.md](/home/simon/ARCAGI/community/README.md)
- [docs/METHOD.md](/home/simon/ARCAGI/docs/METHOD.md)
- [docs/RESULTS.md](/home/simon/ARCAGI/docs/RESULTS.md)
- [docs/PUBLIC_SCOPE.md](/home/simon/ARCAGI/docs/PUBLIC_SCOPE.md)
- [src/yaka_public/interfaces.py](/home/simon/ARCAGI/src/yaka_public/interfaces.py)

## Honest Limitations

The current public ARC-AGI-3 wins were achieved with a source-grounded world
model workflow. The source-free automation path is under active development.
This public repo should be read as an honest proof/materials repo, not a claim
that the entire private system has been open-sourced.
