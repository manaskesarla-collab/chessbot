# chess-rl

A small AlphaZero-inspired chess engine, built incrementally: starting with
supervised learning on human games, and eventually transitioning to
reinforcement learning via self-play.

## Project Description

This project is being built step-by-step, one focused session at a time.
The end goal is a chess bot that:

1. Learns an initial policy from real human games (supervised learning).
2. Improves itself through self-play reinforcement learning, in the spirit
   of AlphaZero — but scoped down to run on a MacBook Air M3 with 16GB RAM.

## Today's Progress (Day 1)

- Set up the full project folder structure.
- Installed and verified `python-chess` and PyTorch (with MPS backend).
- Learned the `python-chess` API in depth: creating boards, printing
  boards, FEN, legal move generation, playing/undoing moves, detecting
  game-over states, and checking whose turn it is.
- Built a simple interactive CLI (`play.py`) to manually play chess against
  yourself and observe the rules engine in action.
- Confirmed PyTorch can run tensor operations on the Apple Silicon GPU via
  MPS.
- No neural networks, datasets, or training loops were built yet —
  those come later.

## Folder Structure

```
chess-rl/
│
├── data/
│   ├── raw/            # Untouched source data (e.g. downloaded PGN files) — Day 2+
│   └── processed/      # Cleaned/encoded data ready for training — Day 3+
│
├── logs/                # Training logs, metrics, TensorBoard files — later days
│
├── models/               # Saved model checkpoints — Day 5+
│
├── src/
│   ├── environment.py    # python-chess fundamentals (no AI)
│   ├── play.py           # Interactive CLI to play chess manually
│   └── test_mps.py       # Verifies PyTorch + Apple MPS backend works
│
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Install

```bash
# From inside the chess-rl/ directory
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to Run

Verify PyTorch + MPS:

```bash
python src/test_mps.py
```

Explore the python-chess fundamentals demo:

```bash
python src/environment.py
```

Play chess interactively from the command line:

```bash
python src/play.py
```

## Future Roadmap

- ✔ **Day 1** — Learn python-chess, set up project structure, verify MPS.
- **Day 2** — Read and parse PGN files of real human games.
- **Day 3** — Encode chess boards into tensors (input representation for a
  neural network).
- **Day 4** — Build a PyTorch `Dataset` / `DataLoader` for supervised
  training.
- **Day 5** — Train the first neural network (supervised policy/value
  network).
- **Day 6** — Evaluate the trained model.
- **Day 7+** — Begin reinforcement learning: self-play, MCTS, and
  iterative policy improvement.
