"""Environment smoke test: PyTorch device, python-chess, and Stockfish."""

from __future__ import annotations

import shutil

import chess
import chess.engine
import torch


def pick_device() -> torch.device:
    """MPS on Apple Silicon, otherwise CPU."""
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def main() -> None:
    device = pick_device()
    x = torch.randn(64, 64, device=device)
    print(f"torch {torch.__version__}, device: {device}, matmul ok: {(x @ x).shape}")

    board = chess.Board()
    print(f"python-chess: {board.legal_moves.count()} legal moves at the start position")

    path = shutil.which("stockfish")
    if path is None:
        raise SystemExit("Stockfish not found on PATH (brew install stockfish)")
    with chess.engine.SimpleEngine.popen_uci(path) as engine:
        info = engine.analyse(board, chess.engine.Limit(depth=10))
        print(f"Stockfish ({engine.id.get('name')}): start position score {info['score']}")


if __name__ == "__main__":
    main()
