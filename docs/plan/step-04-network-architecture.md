# Step 4: Network architecture

## What it means
The network is the model that looks at a position and outputs two things: which moves look good (policy) and who is winning (value). It plays the role of the bot's intuition.

## What you need to do

1. **Build a residual CNN (ResNet) in PyTorch.**
   - Input convolution: takes the Step 2 planes and expands to N filters.
   - A tower of residual blocks: each block is conv, batch norm, ReLU, conv, batch norm, plus a skip connection that adds the block's input to its output. Skips make deeper nets trainable.
2. **Policy head.** A small conv layer then a linear layer outputting 4,672 scores (one per move slot). Softmax over legal moves only (using the mask) gives probabilities.
3. **Value head.** A small conv, then linear layers ending in `tanh`, giving one number from -1 (loss) to +1 (win), with 0 for draw.
4. **Keep it small for your Mac.** Start with **6 residual blocks and 64 filters**; try up to 8 blocks and 96-128 filters only if speed allows. The network is called thousands of times per game by search, so speed matters more than size.
5. **Make sizes configurable** in a YAML file (`configs/model.yaml`: blocks, filters, head sizes).
6. **Benchmark inference.** Measure positions per second on MPS at batch sizes 1, 16, 64, 256. Larger batches are far more efficient, which drives the batched-search design in Step 6.
7. **Save/load checkpoints** with the config embedded, so a checkpoint can be rebuilt with no guesswork.
8. **Tests:** output shapes, masking yields valid probabilities, value in [-1, 1], loading a checkpoint reproduces outputs.

## Key terms
- **Convolution:** a small filter slid across the board to detect patterns.
- **Residual block / skip connection:** lets information bypass layers, making training stable.
- **Policy head / value head:** the two outputs sharing one body.
- **tanh:** squashes numbers into -1 to 1.

## What this step leads to
An untrained model object. Step 5 trains it on human games; Step 6 wraps it in search; Step 7 improves it through self-play. Its inference speed sets how many simulations per second you can afford.

## How you know it's done
- [ ] Forward pass works on MPS and CPU
- [ ] Throughput table recorded for several batch sizes
- [ ] Parameter count and model size documented

## Common pitfalls
- Choosing a big network that makes search unusably slow.
- Computing softmax over all 4,672 slots instead of legal moves only.
- MPS-specific numeric differences; compare outputs against CPU.

## Resume angle
Architecture diagram plus a "size vs speed vs strength" justification shows design reasoning.
