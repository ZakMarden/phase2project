from lib.task_tracker import *


"""
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

"""

"""
Function Signature
Name: task_tracker()
Arguments: two strings, text and string to check for
Returns: String telling user how many tasks there are, and their positions in the text
"""

#Test 1: return number of tasks if above 0

def test_return_true_if_found():
    assert task_tracker("1 2 3 #TODO 5", "#TODO") == "1 task(s) found in this text at position(s): 4"

#Test 2: return "There are no tasks in this text" if string is not in the text

def test_return_false_if_not_found():
    assert task_tracker("1 2 3", "#TODO") == "There are no tasks in this text."

#Test 3: check for multiple tasks in text

def test_for_mult_tasks():
    assert task_tracker("1 #TODO 3 #TODO 5", "#TODO") == "2 task(s) found in this text at position(s): 2, 4"