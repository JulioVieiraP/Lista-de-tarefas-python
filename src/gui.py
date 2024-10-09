import customtkinter as ctk
from src.components.header import Header
from src.components.input_frame import InputFrame
from src.components.task_list import TaskList
from src.Models import Task


class TaskManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Inicializando a janela principal
        self.title("Meu app de Tarefas")
        self.geometry("500x600")
        ctk.set_appearance_mode("Dark")

        # Criando os componentes
        self.header = Header(self)

        # Componente de adicionar tarefa
        self.input_frame = InputFrame(self, self.add_task)

        # Componente de Lista das tarefas
        self.task_list = TaskList(self)

    def add_task(self, task_title):
        Task.create(title=task_title, complement=False)
        self.task_list.update_tasks()

    def run(self):
        self.mainloop()
