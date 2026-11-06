# Chess Bot Plan: an AlphaZero-style engine targeting ~1750 on Lichess

Goal: build a chess bot that learns with reinforcement learning (RL) and reaches roughly **1750 Lichess rapid**, in a way that is verifiable and resume-worthy.

## Is 1750 possible?

Yes, but how you get there matters.

| Approach | Reaches 1750? | Cost |
|---|---|---|
| Pure AlphaZero from scratch (random weights, only self-play) | Probably not on a laptop. DeepMind and Leela used thousands of GPU-hours. | Very high |
| **Hybrid:** supervised pretraining, then MCTS and self-play RL fine-tuning | Realistic on bigger hardware; a stretch on a Mac alone | Laptop only (your setting) |

We follow the **hybrid**. It is also the better resume story, because you can show each stage's contribution with numbers.

## Your decisions

| Topic | Choice | What it means |
|---|---|---|
| ML library | PyTorch | The toolkit that builds and trains the neural network. Uses your Mac GPU through `mps`. |
| Compute | Apple Silicon Mac only, $0 cloud | Smaller network, fewer training games, slower self-play. See "Honest budget" below. |
| Rating target | Lichess rapid bot account | A public, third-party rating a recruiter can check. Backed by Stockfish limited-strength matches. |
| Tooling | `pyproject.toml` + `uv` + YAML configs | Modern Python packaging, fast installs, and settings kept in files instead of code. |

## Honest budget (Mac only, $0)

The original plan assumed about $50-150 of rented GPU for steps 5 and 7. Without it:

- Use a small network (about 6 blocks, 64-96 filters) so search stays fast.
- Train on a subset of human games (about 0.5-2M games), not the whole database.
- Run fewer self-play games per iteration, and fewer iterations.
- **1750 becomes a stretch goal.** The ladder in [risks-and-timeline.md](risks-and-timeline.md) says what to claim if you land lower. A measured ~1400-1600 with clean ablations is still a strong project.

## Steps

| # | Step | Output |
|---|---|---|
| [ ] 0 | [Success and measurement](step-00-success-and-measurement.md) | Written definition of "1750" and an evaluation protocol |
| [ ] 1 | [Environment and tooling](step-01-environment-and-tooling.md) | Working repo, dependencies, tests, Stockfish |
| [ ] 2 | [State and move representation](step-02-state-and-move-representation.md) | Board-to-tensor and move-to-index encoders, fully tested |
| [ ] 3 | [Baselines](step-03-baselines.md) | Random, greedy and alpha-beta bots with measured strength |
| [ ] 4 | [Network architecture](step-04-network-architecture.md) | Two-headed ResNet that runs fast on your Mac |
| [ ] 5 | [Supervised pretraining](step-05-supervised-pretraining.md) | A net that already plays sensible chess |
| [ ] 6 | [MCTS search](step-06-mcts-search.md) | A search engine on top of the net |
| [ ] 7 | [Self-play RL loop](step-07-self-play-rl-loop.md) | Net improved by playing itself |
| [ ] 8 | [Rigorous evaluation](step-08-rigorous-evaluation.md) | Elo estimates with confidence intervals, per stage |
| [ ] 9 | [Lichess deployment](step-09-lichess-deployment.md) | A live bot with a public rating |
| [ ] 10 | [Resume packaging](step-10-resume-packaging.md) | README, charts, ablations, write-up |
| | [Risks and timeline](risks-and-timeline.md) | Schedule, risks, fallback ladder |

## How the pieces connect

```
Step 2 encoder ──► Step 4 network ──► Step 5 pretrained weights
                                          │
                       Step 6 MCTS ◄──────┤
                          │               │
                          ▼               ▼
                    Step 7 self-play RL (net + search generate and learn from games)
                          │
                          ▼
        Step 8 evaluation ──► Step 9 Lichess ──► Step 10 resume
        (Step 3 baselines and Step 0 metrics feed every evaluation)
```

Evaluate after every step, not only at the end. That is how you catch the three biggest risks early.
