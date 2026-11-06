import shutil

import chess
import pytest
import torch

from chessbot.smoke import pick_device


def test_python_chess_start_position() -> None:
    assert chess.Board().legal_moves.count() == 20


def test_device_runs_tensor_ops() -> None:
    x = torch.ones(4, 4, device=pick_device())
    assert float((x @ x).sum()) == 64.0


@pytest.mark.skipif(shutil.which("stockfish") is None, reason="Stockfish not installed")
def test_stockfish_responds() -> None:
    import chess.engine

    path = shutil.which("stockfish")
    assert path is not None
    with chess.engine.SimpleEngine.popen_uci(path) as engine:
        result = engine.play(chess.Board(), chess.engine.Limit(depth=5))
    assert result.move is not None
