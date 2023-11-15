from lib.count_words import *

#test for an empty string

def test_for_an_empty_string():
    wordcount = count_words(" ")
    assert wordcount == 0

#test for one word in string

def test_one_word():
    wordcount = count_words("one")
    assert wordcount == 1

#test for more words

def test_8_words():
    wordcount = count_words("one 2 3 4 5 6 7 8")
    assert wordcount == 8

#test if it counts punctuation

def test_punctuation():
    wordcount = count_words("one 2 3 4 5 ! 6 7 8")
    assert wordcount == 8