# xadrez
Aggregated repositories for chess!

## Quick how-to

* Initialize sub-modules:
  + `git submodule update --init --recursive`
  + and update all sub-modules (if you plan to change them):
  + `git submodule foreach "(git checkout master; git pull)"`

## References

### Programmer links

* /1/ [PGN Standard](https://archive.org/details/pgn-standard-1994-03-12)
  + _opensource_ , _english_ , see also [Digital Chess Problems](http://www.anders.thulin.name/posts/pgn/) from Anders Thulin.
* /2/ [Standard](https://tim-mann.org/Standard): Portable Game Notation Specification and Implementation Guide
  + by Steven J. Edwards
* /3/ [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) - Forsyth-Edwards Notation ([Wikipedia](http://en.wikipedia.org/))
  + very short notation that briefs a chess board position. The purpose of FEN is to provide all the necessary information to restart a game from a particular position.
    - see example of a board at [Lichess](https://lichess.org/): [here](https://lichess.org/editor?fen=5Rk1/2p1P1pp/1p6/2n1q3/8/1b6/PP4PP/7K+b+-+-+0+29), [game 'TVlRl9db'](https://lichess.org/TVlRl9db/white#57)
