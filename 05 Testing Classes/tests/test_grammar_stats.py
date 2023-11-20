from lib.grammar_stats import *

#test for 9 falses 1 true, should return 10

def test_1_true_9_false():
    test = GrammarStats()
    test.check("Aaaaa.","aaaa","aaaa","aaaa","aaaa","aaaa","aaaa","aaaa","aaaa","aaaa")
    assert test.percentage_good() == 10

def test_9_true_1_false():
    test = GrammarStats()
    test.check("aaaa","Aaaa.","Aaaa.","Aaaa.","Aaaa.","Aaaa.","Aaaa.","Aaaa.","Aaaa.","Aaaa.")
    assert test.percentage_good() == 90

