import pytest
from src.Models import Task


@pytest.fixture(autouse=True)
def setup_db():
    # Limpa o banco de dados antes de cada teste
    Task.delete().execute()

    # executa os testes
    yield

    # Limpa o banco de dados após cada teste
    Task.delete().execute()


def test_add_task():
    # Adiciona uma nova tarefa
    Task.create(title="tarefa 1", complete=False)

    tasks = Task.select()
    assert len(tasks) == 1
    assert tasks[0].title == "tarefa 1"


def test_remove_task():
    # Adiciona uma nova tarefa
    Task.create(title="tarefa 2")

    # Remove a tarefa adicionada
    Task.delete().where(Task.title == "tarefa 2").execute()

    tasks = Task.select()
    assert len(tasks) == 0


def test_get_all_tasks():
    # Adiciona várias tarefas
    Task.create(title="tarefa 3")
    Task.create(title="tarefa 4")

    tasks = Task.select()
    assert len(tasks) == 2
    assert tasks[0].title == "tarefa 3"
    assert tasks[1].title == "tarefa 4"
