#-*- coding: iso-8859-1 -*-
# pgn.py  (c)2021  Henrique Moreira

"""
List PGN functions
"""

# pylint: disable=no-self-use, missing-function-docstring

USUAL_HEADER = (
    "Event",	# "Rated Blitz game"
    "Site",	# "https://lichess.org/${game-name}"
    "Date",	# ISO-like date, e.g. 2021.06.27
    "White",
    "Black",	# ...white and black player names (or nicknames)
    "Result",	# "1-0", "0-1", "0-0" (draw)
    "UTCDate",	# same as 'Date', if on same clock day
    "UTCTime",	# UTC time, HH:MM:SS format
    "WhiteElo",	# current ELO of white player
    "BlackElo",	# current ELO of black player
    "WhiteRatingDiff",
    "BlackRatingDiff",	# ... white and black difference after the game (play)
    "Variant",	# usualy "Standard"
    "TimeControl",	# e.g. "300+3" means 300 seconds, plus 3 secs. per move
    "ECO",	# "B01" (?)
    "Opening",	# string describing the opening
    "Termination",	# Normal|Time forfeit|...
    "Annotator",	# person, or e.g. "lichess.org"
)

DEF_ENCODING_IN = "utf-8"

ASCII_ARROW = 8594	# ASCII 8594d = 0x2192 --> (rightwards arrow)


class Pgn():
    """ PGN abstract class.
    Generally handles PGN textual format(s).
    """
    def __init__(self, fname:str, encoding=DEF_ENCODING_IN):
        self._filename = fname
        self._data = open(fname, "r", encoding=encoding).read().split("\n")
        self.head, self.tail = self._pre_process()

    def filename(self) -> str:
        """ Returns the PGN filename/ path """
        return self._filename

    def _pre_process(self):
        """ Parses header and body (called 'tail')
        """
        head, tail = [], []
        idx = 0
        for item in self._data:
            idx += 1
            if item.startswith("["):
                head.append(item.strip())
            else:
                break
        for item in self._data[idx:]:
            brief = item.strip()
            if not brief:
                continue
            tail.append(brief)
        return head, tail

class PgnAnnotation(Pgn):
    """ PGN with annotation """
    _moves = None

    def moves(self) -> dict:
        """ Returns the moves.
        """
        if self._moves is None:
            self.indexing()
        return self._moves

    def indexing(self, debug=0):
        assert len(self.tail) == 1, f"Expected 1 element, got {len(self.tail)}"
        self._annotated_iter(self.tail[0])
        there = self._moves
        if debug <= 0:
            return True
        that_many = sorted(there)
        for move_nr in that_many:
            what = there[move_nr][0]
            print("." * 20, "MOVE", move_nr, ":", what, "." * 20)
            alist = there[move_nr][1:]
            for kind, line in alist:
                shown = simpler_text(line)
                assert shown.strip() == shown, f"Too many blanks: '{line}'"
                print(kind, shown)
        return True

    def _annotated_iter(self, text:str):
        state, move, astr = "@", 0, ""
        quote = ""
        moves = {}
        moves_alt = {}
        idx = -1
        while idx+1 < len(text):
            last = text[idx] if idx >= 0 else ""
            idx += 1
            achr = text[idx]
            if achr == "." and text[idx+1] == " " and (last == "" or last.isdigit()):
                assert state in ("@", "}")
                try:
                    move = int(astr)
                except ValueError:
                    print(f"# LAST: '{last}.' state={state}, astr='{astr}'")
                    assert False
                move_str = ""
                idx += 1
                while True:
                    idx += 1
                    if text[idx] == " ":
                        break
                    move_str += text[idx]
                assert move not in moves, f"Duplicated move number: {move}"
                moves[move] = [("MOVE", move_str,)]
                moves_alt[move] = []
                astr = ""
                idx += 1
                state = "."
                continue
            elif achr == "{":
                state = "{"
                assert move > 0
                if astr != " ":
                    moves[move].append(("PRE", text_info(astr)))
                quote, astr = "", ""
            elif achr == "}":
                state = "}"
                if quote and quote != astr:
                    moves[move].append(("INF", text_info(quote)))
                quote += achr
                astr += achr
                assert move > 0
                moves[move].append(("POS", text_info(astr)))
                quote = ""
                astr = ""
                continue
            if state in ("{",):
                quote += achr
            elif state in ("}",):
                if achr == "(":
                    paren = ""	# paren = parentheses
                    while True:
                        paren += text[idx]
                        if text[idx] == ")":
                            moves_alt[move].append(text_info(paren))
                            idx += 1
                            break
                        idx += 1
                    continue
            astr += achr
        self._moves = moves

def simpler_text(line:str, pre=" ", post=" ") -> str:
    """ Returns similar string, but stripped out from pre or post chars.
    """
    res = line
    if pre:
        if res.startswith(pre):
            res = res[len(pre):]
    if post:
        if res.endswith(post):
            res = res[:-len(post)]
    return res

def text_info(astr) -> str:
    """ Reworks arrow as '-->'
    """
    new = astr.replace(chr(ASCII_ARROW), "-->")
    return new


if __name__ == "__main__":
    print("Import chessmod.pgn !")
