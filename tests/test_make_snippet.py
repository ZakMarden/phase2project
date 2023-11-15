from lib.make_snippet import *

#test for less than 5 words

def test_less_than_5():
    assert make_snippet("1 2 3 4 5") == "1 2 3 4 5"

#test for more than 5

def test_more_than_5():
    assert make_snippet("1 2 3 4 5 6") == "1 2 3 4 5..."

