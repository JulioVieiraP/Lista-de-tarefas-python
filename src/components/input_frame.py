import customtkinter as ctk
from src.Models import Task


class InputFrame(ctk.CTkFrame):
    def __init__(self, window, **kwargs):
        super().__init__(window, fg_color="transparent", **kwargs)
        self.pack(pady=10)

        # Campo de entrada
        self.input = ctk.CTkEntry(
            self,
            font=("Garamond", 14),
            border_width=2,
            border_color="gray",
            corner_radius=0,
            fg_color="#F0F0F0",
            text_color="gray",
            width=300,
        )
        self.input.pack(side="left", padx=10)

        self.input.bind("<Return>", lambda e: self.add_task())

        # Botão para adicionar tarefa
        self.add_button = ctk.CTkButton(
            self,
            text="Adicionar Tarefa",
            fg_color="#4CAF50",
            text_color="#FFFFFF",
            corner_radius=0,
            width=115,
            font=("Roboto", 11),
            command=self.add_task,
        )
        self.add_button.pack(side="left", padx=10)

        # Janela principal
        self.window = window

    def add_task(self):
        task_title = self.input.get()
        if len(task_title) >= 4:
            # Cria a tarefa diretamente no banco de dados
            Task.create(title=task_title, complete=False)
            self.input.delete(0, "end")
            # Atualiza a lista de tarefas
            self.window.task_list.update_tasks()
