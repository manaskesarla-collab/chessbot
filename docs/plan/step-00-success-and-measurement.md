# Step 0: Define success and how you'll measure it

## What it means
Before writing any model, decide what "1750" means and how you will prove it. Chess ratings from different systems are not comparable: Lichess ratings run well above FIDE and are usually somewhat above Chess.com. If you skip this, you end up with a number nobody can interpret.

## What you need to do

1. **Pick the primary metric.** Your bot's rating on Lichess, from a bot account playing rated rapid games (for example 10+0 or 15+10). This is public and checkable.
2. **Pick the secondary metric.** Match results against Stockfish with `UCI_LimitStrength` on and `UCI_Elo` set (the minimum is about 1320). Convert the score into an Elo estimate (see Step 8). This lets you measure strength long before the Lichess bot exists.
3. **Set the fairness rule.** Every comparison uses a fixed budget per move: a fixed number of MCTS simulations or a fixed time. Otherwise a "stronger" bot may just be thinking longer.
4. **Write a one-page evaluation protocol** at `docs/evaluation-protocol.md`:
   - time or node budget per move
   - which Stockfish `UCI_Elo` levels (for example 1320, 1500, 1700, 1900)
   - games per level (at least 100, colours alternated)
   - opening book (a short list of varied starting positions)
   - how Elo and its confidence interval are computed
5. **Decide your fallback claim in advance.** If you reach 1500 instead of 1750, you will state it honestly. Writing this down now stops you from moving the goalposts later.

## Key terms
- **Elo / rating:** a number estimating playing strength from game results.
- **Stockfish:** the strongest open-source chess engine; it can be weakened on purpose to act as a calibrated opponent.
- **UCI:** the standard text protocol engines use to talk to chess programs.
- **Node/simulation budget:** how much thinking the bot may do per move.

## What this step leads to
A fixed yardstick. Step 3 baselines, Step 5 and Step 7 networks, and the Step 9 Lichess bot are all measured with it, so the Elo-vs-stage chart in Step 10 is meaningful.

## How you know it's done
- [ ] `docs/evaluation-protocol.md` exists with every parameter above
- [ ] The scale ("Lichess rapid") is stated in one sentence
- [ ] A fallback claim is written down

## Common pitfalls
- Comparing Lichess numbers to FIDE numbers.
- Changing the time or node budget between experiments.
- Evaluating with too few games (under 100 per level gives huge error bars).

## Resume angle
"Measured against calibrated Stockfish opponents and a live Lichess account" signals rigor.
