# Step 1: Environment and tooling

## What it means
Install the software the project depends on and lay out the repo so that tests, configs and commands exist from day one. Reviewers notice a clean setup.

## What you need to do

1. **Install Python and `uv`.** `uv` is a fast tool that creates the virtual environment and installs packages from `pyproject.toml`.
2. **Create `pyproject.toml`** listing dependencies: `torch`, `python-chess`, `numpy`, `pyyaml`, `zstandard` (reading Lichess files), `tqdm`, and dev tools `pytest`, `ruff` (linting), `mypy` (type checking), `matplotlib` (charts).
3. **Verify PyTorch uses your Mac GPU.** Check `torch.backends.mps.is_available()` is `True`. MPS is Apple's GPU backend. Some operations are missing or slower there, so keep a CPU fallback.
4. **Install Stockfish** (`brew install stockfish`) and confirm you can launch it from Python through `chess.engine`.
5. **Use `python-chess`** for legal moves, board state and PGN parsing. You never write chess rules yourself.
6. **Lay out the repo:**
   ```
   src/chessbot/{encoding,baselines,model,data,mcts,selfplay,eval}/
   tests/
   configs/        # YAML files: model size, training, MCTS, eval
   scripts/        # train, selfplay, evaluate, play entry points
   docs/plan/
   ```
7. **Config system.** Put hyperparameters (learning rate, blocks, filters, simulations) in YAML files under `configs/`, loaded into typed dataclasses. Changing an experiment then means editing a file, not code.
8. **Update `.gitignore`** for `.venv/`, `data/`, `checkpoints/`, `logs/`, `*.pt`, `*.pgn*`.
9. **Add one-command entry points**: `uv run train`, `uv run play`, `uv run evaluate`, and `uv run pytest`.
10. **Commit early**, with small commits per step.

## Key terms
- **Virtual environment:** an isolated set of packages for this project only.
- **MPS:** Metal Performance Shaders, PyTorch's Apple GPU backend.
- **Type hints / mypy:** annotations that let a tool catch type mistakes.

## What this step leads to
A project where `uv sync && uv run pytest` works on any machine. Every later step adds modules and tests into this layout.

## How you know it's done
- [ ] `uv sync` succeeds from a clean clone
- [ ] A smoke test prints the MPS device and a Stockfish evaluation of the start position
- [ ] `uv run pytest` and `ruff check` pass

## Common pitfalls
- Committing large data or model files to git.
- Assuming every PyTorch op works on MPS; test early.
- Hard-coding hyperparameters in code.

## Resume angle
Tests, type hints, configs and one-command workflows show engineering discipline.
