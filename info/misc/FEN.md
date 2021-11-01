# FEN format - Forsyth-Edwards Notation

## Purpose
A FEN "record" defines a particular game position, all in one text line and using only the ASCII character set.
A text file with only FEN data records should have the file extension ".fen".

## Definition
A FEN record contains six fields. The separator between fields is a space. The fields are:

1. Piece placement (from White's perspective). Each rank is described, starting with rank 8 and ending with rank 1; within each rank, the contents of each square are described from file "a" through file "h".
   - Following the Standard Algebraic Notation (SAN), each piece is identified by a single letter taken from the standard English names
     * pawn = "P",
     * knight = "N",
     * bishop = "B",
     * rook = "R",
     * queen = "Q",
     * and king = "K"
   - White pieces are designated using upper-case letters ("PNBRQK") while black pieces use lowercase ("pnbrqk").
   - Empty squares are noted using digits 1 through 8 (the number of empty squares).
   - Most importantly, "/" separates ranks.
1. Active color. "w" means White moves next, "b" means Black moves next.
1. Castling availability. If neither side can castle, this is "-". Otherwise, this has one or more letters:
   - "K" (White can castle kingside),
   - "Q" (White can castle queenside),
   - "k" (Black can castle kingside), and/ or "q" (Black can castle queenside).
   - A move that temporarily prevents castling does not negate this notation.
1. _En passant_ target square in algebraic notation. If there's no _en passant_ target square, this is "-".
   - If a pawn has just made a two-square move, this is the position "behind" the pawn. This is recorded regardless of whether there is a pawn in position to make an _en passant_ capture.
   - See also [/3/]
1. Halfmove clock: The number of halfmoves since the last capture or pawn advance, used for the fifty-move rule.
1. Fullmove number: The number of the full move. It starts at 1, and is incremented after Black's move.

## Examples

1. Main board:
   - [lichess link](https://lichess.org/editor/rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR_w_KQkq_-_0_1)
     * FEN: `rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1`
     * (sample: [here](https://lichess.org/@/hclm/tv))

1. Game, end of a game, white check-mates blacks:
   - [lichess link](https://lichess.org/editor?fen=5Rk1%2F2p1P1pp%2F1p6%2F2n1q3%2F8%2F1b6%2FPP4PP%2F7K+b+-+-+0+29)
     * FEN: `5Rk1/2p1P1pp/1p6/2n1q3/8/1b6/PP4PP/7K b - - 0 29`

1. Game, end of a game due to time forfeit (white wins at _fullmove_ 27)
   - ![chess game](https://lichess1.org/game/export/gif/MsWQnkKY.gif "Chess game at Lichess.org")
     * FEN: `3R1b1k/pp4r1/2p4p/4QPn1/4N3/6P1/PPP3PK/4q3 b - - 8 27`
     * Raw PGN game [here](https://lichess.org/game/export/MsWQnkKY?evals=0&clocks=0)
     * Raw PGN game with clocks, [here](https://lichess.org/game/export/MsWQnkKY?evals=0&clocks=1)
     * Annotated PGN game, [here](https://lichess.org/game/export/MsWQnkKY?literate=1)
     * Final position, [here](https://lichess.org/editor?fen=3R1b1k%2Fpp4r1%2F2p4p%2F4QPn1%2F4N3%2F6P1%2FPPP3PK%2F4q3+b+-+-+8+27)

## References

* /1/ [PGN_standard_1994-03-12.txt](https://ia802908.us.archive.org/26/items/pgn-standard-1994-03-12/PGN_standard_1994-03-12.txt)
* [/2/]: https://github.com/serrasqueiro/xadrez/tree/master/info/misc/PGN_standard_1994-03-12.txt    "PGN_standard"
* /2/: Local copy of [PGN_standard] [/2/]
* [/3/]: https://github.com/serrasqueiro/xadrez/tree/master/info/misc/PGN_standard_1994-03-12.txt    "PGN_standard en_passant"
* /3/: PGN standard, _en passant_ -- section 16.2.3.4
* /10/ about Markdown, and how to make links in Markdown: [here](https://daringfireball.net/projects/markdown/syntax#link)
