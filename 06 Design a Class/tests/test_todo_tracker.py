from lib.todo_tracker import *

#test returns blank list if no tasks given

def test_return_blank_list():
    test = todo_tracker()
    assert test.list_tasks() == "Tasks:\n"

#test returns list of tasks when added

def test_task_list():
    test = todo_tracker()
    test.add_task("test")
    assert test.list_tasks() == "Tasks:\n1. test"

#test returns list with tasks removed if marked complete

def test_task_complete():
    test = todo_tracker()
    test.add_task("test")
    test.add_task("test2")
    test.add_task("test3")
    test.complete_task(1)
    assert test.list_tasks() == "Tasks:\n1. test2\n2. test3"

#test returns error message if try to remove task which doesnt exist

def test_task_complete_error():
    test = todo_tracker()
    test.add_task("test")
    test.add_task("test2")
    test.add_task("test3")
    assert test.complete_task(4) == "Task index out of range. No tasks removed"
    assert test.list_tasks() == "Tasks:\n1. test\n2. test2\n3. test3"