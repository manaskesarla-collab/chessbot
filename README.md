# chessbot

An AlphaZero-style chess engine: a ResNet policy/value network, PUCT Monte Carlo Tree Search, supervised pretraining on Lichess games, then self-play reinforcement learning. Target: ~1750 Lichess rapid, measured on a live bot account. Runs on an Apple Silicon Mac (PyTorch MPS).

The full step-by-step plan is in [docs/plan/](docs/plan/README.md).

## Setup

Requires [uv](https://docs.astral.sh/uv/) and Stockfish (`brew install stockfish`).

```bash
uv sync                # create .venv and install dependencies
uv run smoke           # check PyTorch device, python-chess and Stockfish
uv run pytest          # run the tests
uv run ruff check .    # lint
uv run mypy src        # type check
```

## Layout

```
src/chessbot/   encoding, baselines, model, data, mcts, selfplay, eval, config
configs/        YAML hyperparameters (model, train, mcts, eval)
scripts/        standalone entry scripts
tests/          pytest suite
docs/plan/      project plan, one file per step
```

## Commands

| Command | Status |
|---|---|
| `uv run smoke` | working |
| `uv run train` | planned (Step 5) |
| `uv run play` | planned (Step 6) |
| `uv run evaluate` | planned (Step 8) |

## Progress

- [x] Step 1: environment and tooling
- [ ] Steps 0 and 2-10: see [docs/plan/](docs/plan/README.md)
