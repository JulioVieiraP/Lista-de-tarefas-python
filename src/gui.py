import customtkinter as ctk
from src.components.header import Header
from src.components.input_frame import InputFrame
from src.components.task_list import TaskList
from src.tasks import TaskManager


class TaskManagerApp:
    def __init__(self):
        # Inicializando a janela principal
        self.root = ctk.CTk()
        self.root.title("Meu app de Tarefas")
        self.root.geometry("500x600")
        ctk.set_appearance_mode("Dark")

        # Inicializando o gerenciador de tarefas
        self.task_manager = TaskManager()

        # Criando os componentes
        self.header = Header(self.root)
        self.input_frame = InputFrame(self.root, self.add_task)
        self.task_list = TaskList(self.root)

    def add_task(self):
        task = self.input_frame.get_task()
        if len(task) >= 4:
            self.task_manager.add_task(task)
            self.update_task_listbox()
            self.input_frame.clear_input()

    def update_task_listbox(self):
        tasks = self.task_manager.get_tasks()
        self.task_list.update_tasks(tasks)

    def run(self):
        self.root.mainloop()
