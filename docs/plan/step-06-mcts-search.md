# Step 6: Search (MCTS)

## What it means
The network alone is intuition. Search is calculation: the bot imagines sequences of moves ahead, using the network to judge each imagined position. Monte Carlo Tree Search (MCTS) builds a tree of positions, spending more effort on promising lines. Search typically adds several hundred Elo over the raw network. This is where most of your engineering effort goes.

## What you need to do

1. **Tree nodes.** Each node stores, per move, the network prior `P`, visit count `N`, total value `W` and mean value `Q = W/N`.
2. **One simulation has four parts:**
   - *Select:* from the root, repeatedly pick the move maximising the **PUCT** score: `Q + c_puct * P * sqrt(sum of N) / (1 + N)`. High `Q` favours moves that worked; high `P` favours moves the net likes; the bonus term favours moves rarely tried.
   - *Expand:* on reaching an unvisited position, ask the network for its policy and value.
   - *Evaluate:* the network's value replaces any random rollout.
   - *Back up:* pass the value back up the path, flipping sign at each level (my gain is your loss).
3. **Handle terminal positions** (checkmate, stalemate, draws) with exact values, not the network.
4. **Use 100-400 simulations per move** for play. On a Mac, start near 100 and measure.
5. **Batch network calls.** Evaluating positions one at a time wastes the GPU. Collect many leaves (using a "virtual loss" so different simulations explore different leaves) and evaluate them together.
6. **Transposition cache.** Different move orders reach the same position; cache network outputs by position hash so you evaluate it once.
7. **Move selection.** After the simulations, play the most-visited root move (greedy) or sample proportionally to visits with a temperature (used in self-play, Step 7).
8. **Exploration tools for self-play:** Dirichlet noise added to the root priors, and a temperature parameter.
9. **Expose it as a UCI engine** (`scripts/uci_engine.py`) so Stockfish matches and Lichess (Step 9) can use it.
10. **Test and profile.** Check search finds mate-in-1 and mate-in-2 puzzles, never plays illegal moves, and visit counts sum correctly. Profile to find whether time goes to the network, to board copying, or to Python overhead.

## Key terms
- **PUCT:** the formula balancing the net's opinion, results so far, and curiosity.
- **Simulation / playout:** one trip from root to leaf and back.
- **Virtual loss:** a temporary penalty letting parallel simulations diverge.
- **Transposition:** the same position reached by different move orders.

## What this step leads to
A stronger player than the raw net, and the engine that generates Step 7's training data: the visit counts it produces are better than the raw policy, which is exactly what the net learns to match.

## How you know it's done
- [ ] Solves tactical puzzles the raw net misses
- [ ] Simulations per second measured and acceptable
- [ ] "Supervised + MCTS" Elo exceeds "supervised only" in a measured match

## Common pitfalls
- Slow Python MCTS making self-play too expensive; this is the project's main risk. Batch, cache and avoid copying boards needlessly.
- Sign errors in value backup.
- Not distinguishing "side to move" value perspectives.

## Resume angle
"Implemented batched PUCT MCTS with transposition caching; search added +X Elo over the raw network at N simulations."
