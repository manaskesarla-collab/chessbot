# Step 7: Self-play reinforcement learning loop

## What it means
The bot plays itself, learns from the results, and repeats. The key idea: MCTS acts as a **policy improvement operator**. Search produces better moves than the raw network, and the network is trained to match them. That is the reinforcement learning.

## What you need to do

1. **Generate games.** The current best network plays itself using MCTS.
   - Add **Dirichlet noise** at the root so games are varied.
   - Use a **temperature** for roughly the first 30 moves (sample moves in proportion to visit counts), then play the most-visited move.
   - Resign or adjudicate obviously decided games to save time.
2. **Store.** For every position save the encoded planes, the MCTS **visit distribution** (policy target) and the **final game result** from that side's view (value target) in a replay buffer, a rolling window of the most recent games.
3. **Train.** Fit the network to those targets:
   - Policy loss: cross-entropy against the MCTS visit distribution.
   - Value loss: MSE against the game result.
   - Mix in some of the human data from Step 5 to stabilise training.
4. **Gate.** Play the new network against the previous best (fixed simulations, colours alternated). Promote it only if it wins at least about 55% of games. Otherwise keep the old one.
5. **Repeat.** Each cycle is an "iteration". Keep a log of iteration, games generated, loss, gate result.
6. **Size for a Mac, $0:** a few hundred to a couple of thousand games per iteration, 5-15 iterations, 50-100 simulations per self-play move. Expect each iteration to take hours. Run in the background, resumable from checkpoints.
7. **Parallelise self-play** across CPU processes if search is CPU-bound, with a shared inference queue to the GPU.
8. **Monitor health:** loss curves, average game length, draw rate, policy entropy, and the Elo of each promoted net (Step 8).

## Key terms
- **Replay buffer:** recent training positions to sample from.
- **Dirichlet noise:** random perturbation of root priors to force exploration.
- **Temperature:** controls how random move sampling is.
- **Gating:** only accept a new network if it beats the old one.

## What this step leads to
The final engine: the best gated checkpoint, plus a per-iteration Elo curve, which is your headline chart and the "+X Elo from RL" in your resume bullet.

## How you know it's done
- [ ] Loop runs end to end unattended and resumes after interruption
- [ ] At least some iterations promote
- [ ] Measured Elo of the final net exceeds supervised + MCTS alone

## Common pitfalls
- Unstable self-play training: collapsing draw rates, forgetting, value head overfitting. Mitigate with the human-data mix, small learning rates, a large enough buffer, and gating.
- Too few simulations, making the "improved" targets barely better than the raw policy.
- Drawing too much from stale games.

## Resume angle
"Improved via self-play RL for N iterations (M games), gated at 55%, gaining +X Elo on a single laptop."
