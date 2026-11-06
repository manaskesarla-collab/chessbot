# Risks and timeline

## Realistic budget
- **Time:** about 8-12 weeks part-time. Search, evaluation and debugging take longer than the training code.
- **Compute:** Apple Silicon Mac only, $0 cloud. Steps 1-6 are comfortable. Steps 5 and 7 run in the background for hours or days at reduced scale.

## Schedule

| Weeks | Steps | Milestone |
|---|---|---|
| 1 | 0, 1 | Protocol written, repo and tests running, Stockfish callable |
| 2 | 2 | Encoders pass exhaustive tests |
| 3 | 3 | Baselines and match runner; first Elo numbers |
| 4 | 4, start 5 | Network built and benchmarked; data pipeline producing shards |
| 5-6 | 5 | Pretraining done; raw-net Elo measured |
| 7-8 | 6 | MCTS working, batched, profiled; UCI engine |
| 9-11 | 7 | Self-play iterations with gating |
| 11-12 | 8, 9, 10 | Full evaluation, Lichess deployment, write-up |

Run Step 8 measurements at the end of every milestone, not only at the end.

## Biggest risks

| Risk | Where | Mitigation |
|---|---|---|
| Encoding bugs (silent) | Step 2 | Round-trip tests over thousands of positions; hand-checked special moves |
| Slow MCTS makes self-play too expensive | Step 6 | Batch network calls, cache positions, profile early, cut sims per move |
| Unstable self-play training | Step 7 | Mix in human data, gate at 55%, small learning rate, monitor draw rate and entropy |
| Data pipeline too slow | Step 5 | Preprocess once into shards; stream from disk |
| MPS quirks | Step 1, 4 | CPU fallback, compare outputs |
| Lichess bot upgrade lost | Step 9 | Never play on the account before upgrading |

## Fallback ladder (if 1750 is out of reach on a Mac)
1. Reduce network size or simulations to keep iterations fast.
2. Spend more on supervised training (it gives the largest gain per hour).
3. Lower the RL scope: fewer iterations, but keep gating and honest measurement.
4. Claim what you measured: for example "~1500 Lichess rapid, with +X Elo from MCTS and +Y from RL".
5. If you later want to push further, a short cloud-GPU rental for Steps 5 and 7 is the cheapest route.

## Go / no-go checks
- After Step 2: tests green, or stop and fix.
- After Step 5: raw net beats the greedy baseline, or revisit data and labels.
- After Step 6: MCTS beats the raw net, or fix the search before any self-play.
- After the first RL iteration: loss decreasing and the gate runs, or fix before scaling.
