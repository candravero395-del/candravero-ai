class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks
