from src.tasks import TaskManager

task_manager = TaskManager()


def test_add_task():
    task_manager.add_task("tarefa 1")

    assert task_manager.get_tasks() == ["tarefa 1"]


def test_remove_task():
    task_manager.add_task("tarefa 2")
    task_manager.remove_last_task()

    assert task_manager.get_tasks() == ["tarefa 1"]


def test_get_all_tasks():
    task_manager.add_task("tarefa 3")
    task_manager.add_task("tarefa 4")
    print(task_manager.get_tasks())

    assert len(task_manager.get_tasks()) == 3
