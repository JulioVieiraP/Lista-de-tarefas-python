import customtkinter as ctk
from src.Models import Task


class TaskList(ctk.CTkScrollableFrame):
    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)
        self.pack(fill="both", expand=True, padx=10, pady=10)
        self.update_tasks()

    def update_tasks(self):
        # Limpa o conteúdo anterior
        for widget in self.winfo_children():
            widget.destroy()

        for task in Task.select():
            # Criar um frame para cada tarefa
            task_item_frame = ctk.CTkFrame(self, fg_color="lightgrey")
            task_item_frame.pack(fill="x", padx=5, pady=5)

            # Label para exibir a tarefa
            task_label = ctk.CTkLabel(
                task_item_frame, text=task.title, text_color="blue"
            )
            task_label.pack(side="left", pady=10, padx=10)

            delete_button = ctk.CTkButton(
                task_item_frame,
                text="Excluir",
                fg_color="red",
                command=lambda task_id=task.id: self.delete_task(task_id),
            )
            delete_button.pack(side="right", padx=10)

    def delete_task(self, task_id):
        # Deletando a tarefa do banco de dados
        Task.delete_by_id(task_id)
        self.update_tasks()
