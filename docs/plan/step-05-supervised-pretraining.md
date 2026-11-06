# Step 5: Supervised pretraining (the bootstrap)

## What it means
Teach the network basic chess by imitating strong human players before any reinforcement learning. Without this, self-play RL spends days relearning how pieces move. This is "learning from examples": for each position the label is the move a human actually played and the final result of that game.

## What you need to do

1. **Download the Lichess open database** (monthly `.pgn.zst` files from database.lichess.org). They are compressed and huge, so stream them; never load a whole file.
2. **Filter** to games where both players are rated 2000 or higher, with a normal time control (exclude bullet if you want quality), finished normally, and skip the first few opening moves if you want less memorisation.
3. **Convert to training shards.** Parse games with `python-chess`, and for each position store the encoded planes (Step 2), the played move's index, and the game result from the side to move's view (+1 / 0 / -1). Save as compact `.npy` shards on disk.
4. **Choose a data size that fits a Mac:** about 0.5-2M games' worth of positions, sampled across months. Keep a held-out validation set of whole games so positions from one game never appear in both train and validation.
5. **Train both heads together.**
   - Policy loss: cross-entropy against the human move.
   - Value loss: mean squared error against the game result.
   - Total loss: policy loss plus a weighted value loss.
   - Use AdamW, a learning-rate schedule, and checkpoint regularly.
6. **Track validation metrics:** top-1 and top-5 move accuracy, value error. Policy-only networks like Maia reach about 50% top-1 and play at roughly 1500+ level without any search.
7. **Measure strength.** Play the raw network (pick the highest-probability legal move, no search) against baselines and Stockfish levels from the Step 0 protocol.

## Key terms
- **Supervised learning:** learning from labelled examples.
- **Cross-entropy:** a loss that rewards putting probability on the correct move.
- **MSE:** mean squared error, penalises wrong outcome predictions.
- **PGN / `.zst`:** the chess game text format and its compression.

## What this step leads to
A checkpoint that already plays sensibly. It is the starting weights for Step 7 and the "supervised only" bar in your ablation chart. Its value head also makes Step 6 search meaningful from the first run.

## How you know it's done
- [ ] Validation top-1 accuracy is clearly above chance and plateaus
- [ ] Network beats the greedy baseline and ideally approaches the alpha-beta baseline
- [ ] Raw-net Elo measured and logged

## Common pitfalls
- Leaking positions from the same game into train and validation.
- Value labels from the wrong side's perspective.
- Training on too many near-duplicate opening positions.
- Data pipeline being the bottleneck; preprocess once, then reuse the shards.

## Resume angle
"Pretrained on N million positions from Lichess 2000+ games; X% top-1 accuracy; raw net reaches ~Y Elo."
