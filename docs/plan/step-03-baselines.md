# Step 3: Baselines

## What it means
Baselines are weak reference bots. They give you a floor to beat and, later, show how much the RL part really adds. If a simple search with a hand-written evaluation already reaches your target, the neural network has to justify itself.

## What you need to do

1. **Random mover.** Picks a uniformly random legal move. Strength is roughly the bottom of the scale; it checks your game loop works.
2. **Greedy material bot.** Picks the move that maximises material after one move (pawn 1, knight 3, bishop 3, rook 5, queen 9). Add a tiny random tie-break so games vary.
3. **Alpha-beta bot.** Minimax search with alpha-beta pruning, using material plus piece-square tables (bonuses for well-placed pieces). Add move ordering (captures first), iterative deepening and a fixed depth or node budget.
4. **Common interface.** Every bot exposes `choose_move(board) -> move`, so the same match runner plays any bot against any other, and later against Stockfish.
5. **Match runner.** Play N games with alternating colours and varied openings; record wins, draws, losses and PGNs.
6. **Measure them.** Run each baseline against Stockfish at several `UCI_Elo` levels using the Step 0 protocol and record an Elo estimate.

## Key terms
- **Minimax:** assume both sides pick their best move; search the tree of replies.
- **Alpha-beta pruning:** skip branches that cannot change the result; same answer, far faster.
- **Piece-square table:** a small grid giving each piece a bonus or penalty per square.

## What this step leads to
- The shared match runner is reused by Step 6 (gating) and Step 8 (evaluation).
- Baseline Elo values are the leftmost points on your Elo-vs-stage chart.
- A decent alpha-beta bot can reach about 1400-1800 alone, so the later RL results must be compared against it honestly.

## How you know it's done
- [ ] All three bots play full legal games without crashing
- [ ] Ranking is sensible: alpha-beta > greedy > random
- [ ] Each has a measured Elo with a confidence interval

## Common pitfalls
- Unlimited depth causing unfair, inconsistent time use; fix the budget.
- Forgetting draws by repetition, 50 moves and stalemate.
- Evaluating from the wrong side's perspective in minimax.

## Resume angle
"Beats a tuned alpha-beta baseline by X Elo" is far stronger than "plays chess".
