# Step 2: State and move representation

## What it means
A neural network needs numbers, not a chess board. You need (a) a way to turn any position into a fixed-size grid of numbers, and (b) a fixed list of all possible moves so the network can output one score per move.

## What you need to do

1. **Input encoding.** Turn a position into a stack of 8x8 planes:
   - 12 planes: one per piece type and colour (a 1 where that piece stands, else 0)
   - side to move
   - 4 castling-right planes
   - en passant target square
   - optionally the last few positions (history) and a repetition/halfmove counter
   - typical size: 8x8x19 or more
   - **Orient from the side to move's point of view** (flip the board for Black) so the network learns one perspective.
2. **Move encoding.** Use the AlphaZero 8x8x73 scheme: for each of the 64 from-squares, 73 move types (56 "queen-like" moves of up to 7 squares in 8 directions, 8 knight moves, 9 underpromotions). That is 4,672 slots. The network outputs a score per slot.
3. **Legal-move mask.** Build a vector with 1 for legal moves and 0 otherwise. Set illegal scores to minus infinity before the softmax so the bot can never pick an illegal move.
4. **Implement both directions:** `encode_board(board) -> tensor`, `move_to_index(move, board) -> int`, `index_to_move(i, board) -> move`, `legal_mask(board)`.
5. **Test thoroughly:**
   - round-trip every legal move: `index_to_move(move_to_index(m)) == m`
   - run over thousands of positions (random playouts plus positions from real games)
   - special cases: castling, en passant, promotions (queen and underpromotions), Black's perspective flip
   - no two legal moves map to the same index
   - plane contents on hand-checked positions

## Key terms
- **Plane:** an 8x8 layer of numbers; a stack of planes is the network input.
- **Action space:** the fixed list of all moves the network can output.
- **Masking:** forcing illegal moves to zero probability.

## What this step leads to
The Step 4 network is built to consume exactly this tensor shape and output exactly this move vector. Step 5 turns human moves into these indices as training labels, and Step 6 search uses the mask and indices at every node.

## How you know it's done
- [ ] Round-trip test passes on at least 10,000 positions
- [ ] Hand-verified examples for castling, en passant, promotions and flips
- [ ] Encoding speed is measured (it runs thousands of times per move in search)

## Common pitfalls
- **Encoding bugs are the most common silent failure** in these projects: the net trains fine but learns nonsense.
- Forgetting to flip moves as well as the board for Black.
- Mismatched index conventions between encoder and decoder.

## Resume angle
A tested, documented encoding is something interviewers can probe and you can defend.
