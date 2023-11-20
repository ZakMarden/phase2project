class todo_tracker():
    def __init__(self):
        self.tasklist = []
        pass

    def add_task(self, task):
        self.tasklist.append(task)
        pass

    def complete_task(self, task_index):
        if 0<task_index<=len(self.tasklist):
            print(f"Removing task {task_index}") 
            self.tasklist.pop(task_index - 1)
        else:
            print("Task index out of range. No tasks removed")
            return "Task index out of range. No tasks removed"
        pass

    def list_tasks(self):
        tasks = [f"{i+1}. {self.tasklist[i]}" for i in range(len(self.tasklist))]
        tasks_full = "\n" + "\n".join(tasks)
        print(f"Tasks:{tasks_full}")
        return f"Tasks:{tasks_full}"


test = todo_tracker()
test.add_task("test1")
test.add_task("test 2")
test.add_task("test three")
test.list_tasks()
test.complete_task(2)
test.list_tasks()
