# Method

## Core Idea

YAKA does not try to force one generic policy across unrelated games.

Instead, it compiles a small deterministic solver per game:
- identify the actual state variables
- identify the real action surface
- model the game mechanics directly
- choose the right solver family for that mechanic set

## Public ARC-AGI-3 Patterns

### `ls20`

World-model problem over:
- movement
- transforms
- movers
- recharges
- pushers

### `ft09`

Constraint-satisfaction problem over:
- click targets
- palette cycling
- local kernel effects
- target constraint tiles

### `vc33`

Structural routing problem over:
- rail resizing
- gate activation
- payload transfer
- late-level phase constraints

## Automation Direction

The public automation stack developed during the sprint has four layers:
- scanner
- interpreter
- targeted trace generator
- hypothesis-conditioned probe planner

Those layers are represented in the public source skeleton under
`src/yaka_public/`.
