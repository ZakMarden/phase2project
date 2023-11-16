def task_tracker(text, task):
    words_list = text.split()
    task_positions = []
    if task in words_list:
        for word_index in range(len(words_list)):
            if words_list[word_index] == task:
                task_positions.append(str(word_index + 1))
        return f"{words_list.count(task)} task(s) found in this text at position(s): " + ", ".join(task_positions)
    else:
        return "There are no tasks in this text."
