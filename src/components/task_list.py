import customtkinter as ctk


class TaskList:
    def __init__(self, window):
        self.task_frame = ctk.CTkScrollableFrame(window)
        self.task_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def update_tasks(self, tasks):
        # Limpa o conteúdo anterior
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for task in tasks:
            # Criar um frame para cada tarefa
            task_item_frame = ctk.CTkFrame(self.task_frame, fg_color="lightgrey")
            task_item_frame.pack(fill="x", padx=5, pady=5)

            # Label para exibir a tarefa
            task_label = ctk.CTkLabel(task_item_frame, text=task, text_color="blue")
            task_label.pack(side="left", pady=10, padx=10)
