#-*- coding: iso-8859-1 -*-
# pgns.py  (c)2020  Henrique Moreira

"""
List PGN functions
"""

# pylint: disable=no-self-use, missing-function-docstring

import sys
import re
import os.path
import datetime
import filing.dirs as dirs

VALID_WHERE = (
    "lichess",
)

def main_test():
    """ Only for tests! """
    is_ok = run_test(sys.argv[1:])
    assert is_ok

def run_test(args):
    """ Basic tests """
    for param in args:
        test_dir(param, ".pgn")
    return True

def test_dir(apath:str, suffix:str):
    """ Test one dir """
    pgn_list = pgn_from_dir(apath, suffix)
    for item in pgn_list:
        simpler = item[1:]
        print(simpler, end="\n\n")

def pgn_from_dir(apath:str, suffix:str=".pgn") -> list:
    """ Returns list of PGN files for dir 'apath'
    """
    adir = dirs.ADir(apath, filter_out="*~")
    names = adir.by_name()
    #there = adir.get_by("latin"); lichess_list = there["l"]
    tups = [path_tup(name)  for name in names if name.endswith(suffix) or not suffix]
    return tups

def path_tup(path:str) -> tuple:
    """ Returns pair dirname and basename from 'path' string.
    """
    name = os.path.basename(path)
    # https://regex101.com/r/yQD44m/1
    #	lichess_2021.07.05_annotated.CMA0cChA.pgn
    pat = r"^([^_]*_)?((\d{4})\.(\d{2})\.(\d{2})_)(annotated|raw).([^.]+).pgn$"
    where = "lichess"
    infos = {
        "date": None,
        "date-string": None,
        "where": where,
        "game-id": "",
        "annotated": "?",
    }
    res = re.match(pat, name)
    if res:
        msg = pgn_infos(res, infos)
        assert msg == "", f"pgn_infos(): {msg}"
    return (os.path.dirname(path), name, infos)

def pgn_infos(rexp, infos:dict):
    if rexp is None:
        return ""	# No error, but nothing parsed
    where = rexp.group(1)
    year, month, day = int(rexp.group(3)), int(rexp.group(4)), int(rexp.group(5))
    annotated = rexp.group(6)
    lichess_game = rexp.group(7)
    assert where
    assert len(lichess_game) >= 8, f"Short 'lichess_game': '{lichess_game}'"
    where = where.rstrip("_")
    if where not in VALID_WHERE:
        return f"'where' invalid: '{where}'"
    adate = datetime.date(year, month, day)
    infos["date"] = adate
    infos["date-string"] = adate.strftime("%a %Y.%d.%m")
    infos["game-id"] = lichess_game
    infos["annotated"] = annotated
    return ""

# Main script
if __name__ == "__main__":
    print("Import chessmod.pgns !")
    main_test()
