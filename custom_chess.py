# https://quera.org/problemset/60138
# ----------------------------------

from typing import Annotated, Final, Literal

# Custom Types
PositionType = tuple[int, int]
ColorType = Annotated[str, Literal["black", "white"]]
SortType = Annotated[str, Literal["k", "p"]]

# Sorts
KING_SORT: Final = "k"
PAWN_SORT: Final = "p"

# Colors
BLACK_COLOR: Final = "black"
WHITE_COLOR: Final = "white"

# Positions
BLACK_KING_INIT_POSITION: Final = (10, 10)
WHITE_KING_INIT_POSITION: Final = (-10, -10)

# Messages
INVALID_QUERY_MESSAGE: Final = "invalid query"


class Piece:
    def __init__(
        self,
        sort: SortType,
        color: ColorType,
        position: PositionType,
    ):
        self.sort = sort
        self.color = color
        self.position = position


class Board:
    def __init__(self) -> None:
        self.position: dict[PositionType, Piece] = {
            BLACK_KING_INIT_POSITION: Piece(
                sort=KING_SORT,
                color=BLACK_COLOR,
                position=BLACK_KING_INIT_POSITION,
            ),
            WHITE_KING_INIT_POSITION: Piece(
                sort=KING_SORT,
                color=WHITE_COLOR,
                position=WHITE_KING_INIT_POSITION,
            ),
        }

    def add(self, piece: Piece) -> None:
        if piece.sort == KING_SORT or piece.position in self.position:
            print(INVALID_QUERY_MESSAGE)
        else:
            self.position[piece.position] = piece

    def remove(self, position: PositionType) -> None:
        piece = self.position.get(position, None)
        if not piece or piece.sort == KING_SORT:
            print(INVALID_QUERY_MESSAGE)
        else:
            self.position.pop(position)

    def move(self, piece: Piece, position2: PositionType):
        current_piece = self.position.get(piece.position, None)
        target_piece = self.position.get(position2, None)
        if (
            # matching current piece with input piece
            not current_piece
            or current_piece.sort != piece.sort
            or current_piece.color != piece.color
            or current_piece.position == position2
        ) or (
            # prevent targeting king piece or own pieces
            target_piece is not None
            and (
                target_piece.sort == KING_SORT
                or target_piece.color == current_piece.color
            )
        ):
            print(INVALID_QUERY_MESSAGE)
        else:
            if target_piece is not None:
                self.position.pop(position2)

            self.position.pop(current_piece.position)
            current_piece.position = position2
            self.position[position2] = current_piece

    def is_mate(self, color: ColorType) -> bool:
        opponent_color = WHITE_COLOR if color == BLACK_COLOR else BLACK_COLOR
        for position, piece in self.position.items():
            if piece.sort.casefold() == KING_SORT and piece.color == color:
                king_x, king_y = position
                break

        for x in range(king_x - 1, king_x + 2):
            for y in range(king_y - 1, king_y + 2):
                # skipping king's position
                if x == king_x and y == king_y:
                    continue

                adjacent_piece = self.position.get((x, y), None)
                if (
                    adjacent_piece
                    and adjacent_piece.sort.casefold() == PAWN_SORT
                    and adjacent_piece.color == opponent_color
                ):
                    return True
        return False
