import customtkinter as ctk
from src.tasks import TaskManager
from tkinter import PhotoImage


class TaskManagerApp:
    def __init__(self):
        # Inicializando a janela principal
        self.root = ctk.CTk()
        self.root.title("Meu app de Tarefas")
        self.root.geometry("500x600")
        ctk.set_appearance_mode("Dark")

        # Inicializando o gerenciador de tarefas
        self.task_manager = TaskManager()

        # Componentes da interface
        self.create_widgets()

    def create_widgets(self):
        # Cabeçalho
        self.fonte_cabecalho = ("Garamond", 24, "bold")
        self.cabecalho = ctk.CTkLabel(
            self.root,
            font=self.fonte_cabecalho,
            text="Meu App de Tarefas",
        )
        self.cabecalho.pack(pady=20)

        # Frame para segurar os inputs
        self.frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.frame.pack(pady=10)

        # Campo de entrada
        self.input = ctk.CTkEntry(
            self.frame,
            font=("Garamond", 14),
            border_width=2,
            border_color="gray",
            corner_radius=0,
            fg_color="#F0F0F0",
            text_color="gray",
            width=300,
        )
        self.input.pack(side="left", padx=10)

        # Botão para adicionar tarefa
        self.add_button = ctk.CTkButton(
            self.frame,
            text="Adicionar Tarefa",
            fg_color="#4CAF50",
            text_color="#FFFFFF",
            corner_radius=0,
            width=115,
            font=("Roboto", 11),
            command=self.add_task,
        )
        self.add_button.pack(side="left", padx=10)

        # Frame para a lista de tarefas
        self.task_frame = ctk.CTkScrollableFrame(self.root)
        self.task_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def add_task(self):
        task = self.input.get()
        if len(task) >= 4:
            self.task_manager.add_task(task)
            self.update_task_listbox()
            self.input.delete(0, "end")

    def update_task_listbox(self):
        # Limpa o conteúdo anterior
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for task in self.task_manager.get_tasks():
            # Criar um frame para cada tarefa
            task_item_frame = ctk.CTkFrame(self.task_frame, fg_color="lightgrey")
            task_item_frame.pack(fill="x", padx=5, pady=5)

            # Label para exibir a tarefa
            task_label = ctk.CTkLabel(task_item_frame, text=task, text_color="blue")
            task_label.pack(side="left", pady=10, padx=10)

    def run(self):
        self.root.mainloop()
