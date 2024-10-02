class TaskManager:
    def __init__(self):
        # Lista de tarefas
        self.tasks = []

    def add_task(self, task):
        # Adiciona uma nova tarefa à lista
        self.tasks.append(task)

    def remove_last_task(self):
        # Remove a última tarefa da lista
        if self.tasks:
            self.tasks.pop()

    def get_tasks(self):
        # Retorna a lista de tarefas
        return self.tasks
