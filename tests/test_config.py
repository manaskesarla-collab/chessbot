from pathlib import Path

import pytest

from chessbot.config import EvalConfig, MCTSConfig, ModelConfig, TrainConfig, load_config


@pytest.mark.parametrize(
    ("cls", "name"),
    [(ModelConfig, "model"), (TrainConfig, "train"), (MCTSConfig, "mcts"), (EvalConfig, "eval")],
)
def test_shipped_configs_load(cls: type, name: str) -> None:
    assert load_config(cls, name) == cls()  # YAML defaults match dataclass defaults


def test_unknown_key_rejected(tmp_path: Path) -> None:
    (tmp_path / "model.yaml").write_text("blocks: 6\nfilterz: 64\n")
    with pytest.raises(ValueError, match="filterz"):
        load_config(ModelConfig, "model", config_dir=tmp_path)
