"""
environment.py

Purpose
-------
Day 1 is about learning the `python-chess` library deeply, BEFORE we ever
attach a neural network or an RL agent to it. Every function here is
deliberately small and isolated so you can call them one at a time from a
Python REPL or a notebook and see exactly what each piece of the library
does.

We are NOT building an AI here. `python-chess` already knows every rule of
chess (legal moves, check, checkmate, castling, en passant, promotion,
draws, etc.). Our job today is only to understand its API, because in
later days we will:

  - Day 3: turn a `chess.Board` into a tensor a neural network can read.
  - Day 6+: use `board.legal_moves` to generate the action space for MCTS
    and self-play.

So think of this file as "getting fluent in the language the chess engine
speaks" before we teach it to think.
"""

import chess


def create_board() -> chess.Board:
    """Create a new chess board in the standard starting position.

    Why: `chess.Board()` is the single object that represents the entire
    state of a chess game — piece positions, whose turn it is, castling
    rights, en passant target square, and move history. Every other
    function in this file operates on this object.

    Returns:
        chess.Board: A board initialized to the standard starting position.
    """
    board = chess.Board()
    print("Created a new board in the standard starting position.")
    return board


def print_board(board: chess.Board) -> None:
    """Print a human-readable ASCII representation of the board.

    Why: While the engine internally represents the board as bitboards
    (very fast for computation, but unreadable to humans), we need a
    visual way to sanity-check what's happening as we experiment.

    Args:
        board: The board to print.
    """
    print(board)
    print()  # blank line for readability


def print_fen(board: chess.Board) -> None:
    """Print the FEN (Forsyth-Edwards Notation) string for the board.

    Why: FEN is a compact, standardized text format that fully describes a
    chess position in a single line. It is the "save file" format for
    chess positions. Later, when we read human games or save training
    positions, FEN will be how we store and reload exact board states.

    Args:
        board: The board whose FEN string we want to print.
    """
    fen = board.fen()
    print(f"FEN: {fen}")


def list_legal_moves(board: chess.Board) -> list[chess.Move]:
    """List every legal move available in the current position.

    Why: `board.legal_moves` is the library automatically calculating
    every rules-legal move for the side to move — including tricky cases
    like pins, checks, castling rights, and en passant. This is the exact
    set of "actions" an RL agent will choose from later. Today we just
    print them to see how the library represents moves.

    Args:
        board: The board to compute legal moves for.

    Returns:
        list[chess.Move]: All legal moves in the current position.
    """
    moves = list(board.legal_moves)
    print(f"There are {len(moves)} legal moves in this position:")
    print(", ".join(move.uci() for move in moves))
    return moves


def play_move(board: chess.Board, uci_move: str) -> bool:
    """Attempt to play a move given in UCI notation (e.g. 'e2e4').

    Why: UCI (Universal Chess Interface) notation is a simple, unambiguous
    way to describe a move: "from square" + "to square" (+ optional
    promotion piece). It is the format chess engines use to communicate
    moves to each other, and it's the format we will later use to encode
    an RL agent's chosen action.

    This function validates the move against the CURRENT legal moves
    before playing it — it will never let an illegal move happen.

    Args:
        board: The board to play the move on. Modified in place.
        uci_move: The move in UCI format, e.g. "e2e4" or "e7e8q" for
            promotion to a queen.

    Returns:
        bool: True if the move was legal and played, False if it was
            rejected as illegal or malformed.
    """
    try:
        move = chess.Move.from_uci(uci_move)
    except chess.InvalidMoveError:
        print(f"'{uci_move}' is not a validly formatted UCI move.")
        return False

    if move not in board.legal_moves:
        print(f"'{uci_move}' is not a legal move in this position.")
        return False

    board.push(move)
    print(f"Played move: {uci_move}")
    return True


def undo_move(board: chess.Board) -> None:
    """Undo the most recently played move.

    Why: `board.pop()` reverses the last `push()`, restoring the board to
    its previous state (including castling rights and en passant state,
    not just piece positions). This is essential later for tree search
    algorithms like MCTS, which need to explore a move, evaluate it, and
    then "back up" to try a different move from the same position.

    Args:
        board: The board to undo the last move on. Modified in place.
    """
    if not board.move_stack:
        print("No moves to undo — the board is at its initial state.")
        return

    last_move = board.pop()
    print(f"Undid move: {last_move.uci()}")


def reset_board(board: chess.Board) -> None:
    """Reset the board back to the standard starting position.

    Why: Rather than creating a brand-new `chess.Board()` object, this
    reuses the same object and resets its internal state. This pattern
    will matter later for efficiency when we run many self-play games in a
    loop and don't want to keep allocating new objects.

    Args:
        board: The board to reset. Modified in place.
    """
    board.reset()
    print("Board reset to the standard starting position.")


def is_game_over(board: chess.Board) -> bool:
    """Check whether the game has ended, and print the reason if so.

    Why: A game can end in many ways: checkmate, stalemate, insufficient
    material, the fifty-move rule, threefold repetition, etc.
    `board.is_game_over()` checks all of these for us. Later, this exact
    check will tell our self-play loop and RL training loop when to stop a
    game and assign a final reward (win/loss/draw).

    Args:
        board: The board to check.

    Returns:
        bool: True if the game has ended, False otherwise.
    """
    over = board.is_game_over()
    if over:
        print(f"Game over. Result: {board.result()} (outcome: {board.outcome()})")
    else:
        print("Game is still in progress.")
    return over


def whose_turn(board: chess.Board) -> chess.Color:
    """Print and return whose turn it is to move.

    Why: `board.turn` is a simple boolean-like value (`chess.WHITE` or
    `chess.BLACK`) that tells us the side to move. This becomes important
    later when we encode the board for a neural network — the network
    needs to know whose perspective it's evaluating from.

    Args:
        board: The board to check.

    Returns:
        chess.Color: chess.WHITE or chess.BLACK.
    """
    turn = board.turn
    color_name = "White" if turn == chess.WHITE else "Black"
    print(f"It is {color_name}'s turn to move.")
    return turn


def _demo() -> None:
    """A small manual walkthrough of every function above.

    Why: Run `python src/environment.py` to see each function in action,
    in a sensible order, without needing to open a separate REPL session.
    This is just a convenience demo — the real interactive tool is
    play.py.
    """
    board = create_board()
    print_board(board)
    print_fen(board)
    whose_turn(board)
    list_legal_moves(board)

    play_move(board, "e2e4")
    print_board(board)
    whose_turn(board)

    play_move(board, "e7e5")
    print_board(board)

    play_move(board, "e2e4")  # illegal now — pawn already moved and square occupied differently
    undo_move(board)
    print_board(board)

    is_game_over(board)
    reset_board(board)
    print_board(board)


if __name__ == "__main__":
    _demo()
