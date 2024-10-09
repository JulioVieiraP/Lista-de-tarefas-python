import customtkinter as ctk


class TaskList(ctk.CTkScrollableFrame):
    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)
        self.pack(fill="both", expand=True, padx=10, pady=10)

    def update_tasks(self, tasks):
        # Limpa o conteúdo anterior
        for widget in self.winfo_children():
            widget.destroy()

        for task in tasks:
            # Criar um frame para cada tarefa
            task_item_frame = ctk.CTkFrame(self, fg_color="lightgrey")
            task_item_frame.pack(fill="x", padx=5, pady=5)

            # Label para exibir a tarefa
            task_label = ctk.CTkLabel(task_item_frame, text=task, text_color="blue")
            task_label.pack(side="left", pady=10, padx=10)
