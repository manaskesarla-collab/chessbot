"""
play.py

Purpose
-------
A small interactive command-line demo that lets YOU play chess against
yourself (no AI yet) by typing moves in UCI notation. This exists purely
so you can feel, hands-on, how `chess.Board` behaves: legal move
validation, turn switching, and game-over detection.

This is intentionally simple. It reuses the functions we built and
explained in environment.py rather than re-implementing chess logic here.

Run it with:
    python src/play.py
"""

import chess

from environment import (
    create_board,
    is_game_over,
    play_move,
    print_board,
    whose_turn,
)


def _prompt_for_move(board: chess.Board) -> str:
    """Ask the user for a move and return their raw input.

    Why: Keeping input-gathering in its own tiny function makes main()
    easier to read, and makes it trivial later to swap this out (e.g. for
    an AI move generator) without touching the game loop structure.

    Args:
        board: The current board, used only to display whose turn it is
            in the prompt text.

    Returns:
        str: The raw text the user typed, stripped of whitespace.
    """
    color_name = "White" if board.turn == chess.WHITE else "Black"
    raw = input(f"{color_name} to move (UCI format, e.g. e2e4, or 'quit'): ")
    return raw.strip()


def main() -> None:
    """Run the interactive play loop until the game ends or the user quits."""
    print("=" * 60)
    print("Interactive Chess Demo (no AI yet — just you and the rules)")
    print("Type moves in UCI format, e.g. e2e4, g1f3, e7e8q (promotion).")
    print("Type 'quit' at any time to exit.")
    print("=" * 60)

    board = create_board()
    print_board(board)

    while True:
        # Check for game-over BEFORE asking for a move, so we stop as soon
        # as the previous move ended the game.
        if is_game_over(board):
            break

        user_input = _prompt_for_move(board)

        if user_input.lower() == "quit":
            print("Exiting. Thanks for playing!")
            return

        move_played = play_move(board, user_input)

        if not move_played:
            # play_move() already printed why it was rejected.
            # We simply loop back and ask again without changing the board.
            continue

        print_board(board)
        whose_turn(board)

    print("Game finished. Final position:")
    print_board(board)


if __name__ == "__main__":
    main()
