# Step 8: Rigorous evaluation

## What it means
This step is what makes the project credible. You measure every stage with the same protocol and report uncertainty, instead of saying "it seems stronger".

## What you need to do

1. **Build the Stockfish match harness.** Using `chess.engine`, play your bot against Stockfish with `UCI_LimitStrength=true` and `UCI_Elo` at several levels (for example 1320, 1500, 1700, 1900).
2. **Match rules** (from the Step 0 protocol):
   - at least **100 games per level**
   - colours alternated
   - a varied opening book (a list of short opening lines or positions) so games are not identical
   - fixed simulations or time per move
3. **Estimate Elo with confidence intervals.** Convert score fraction against each opponent into an Elo estimate with the logistic formula, then fit across opponent levels (BayesElo, or a simple logistic fit of score vs opponent Elo). Report a 95% interval.
4. **Evaluate each stage:** random, greedy, alpha-beta (Step 3), supervised only (Step 5), supervised + MCTS (Step 6), then each promoted RL iteration (Step 7).
5. **Produce the headline figure:** Elo (with error bars) against stage or training iteration. Save results as CSV/JSON in `results/` so charts are reproducible.
6. **Keep head-to-head matches too** between consecutive versions for gating and ablations.
7. **Calibration note:** Stockfish `UCI_Elo` is calibrated to its own scale, not Lichess. Treat this as your internal measure and let Step 9 supply the Lichess number.

## Key terms
- **Confidence interval:** the range the true Elo likely lies in.
- **Opening book:** varied start positions for fairness and diversity.
- **Logistic Elo model:** expected score = 1 / (1 + 10^(-diff/400)).

## What this step leads to
The evidence for the entire project: the Elo-vs-stage chart, the ablation table, and the numbers placed in your Step 10 README and resume bullet.

## How you know it's done
- [ ] One command reproduces the evaluation for any checkpoint
- [ ] Each stage has an Elo with a confidence interval
- [ ] Chart and raw results are committed (small files only)

## Common pitfalls
- Too few games, so intervals overlap and tell you nothing.
- Using the same opening every game.
- Mixing time budgets between stages.
- Playing at levels far from your strength; choose opponents within a few hundred Elo of you.

## Resume angle
Error bars and a reproducible protocol separate this from a hobby script.
