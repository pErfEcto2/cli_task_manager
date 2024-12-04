import pytest
from task_manager import TaskManager
from lib import sanitized_input, print_tasks


task = {"id": 1, "title": "Test Task", "desc": "Test Desc", 
        "category": "Work", "deadline": "11-11-1111", "priority": "high", 
        "is_done": False}

@pytest.fixture
def sample_task_manager(tmp_path):
    return TaskManager(path=str(tmp_path / "tasks.json"))

def test_add_task(sample_task_manager, monkeypatch):
    tm = sample_task_manager
    input_iter = iter(["Test Task", "Test Desc", "Work", "11-11-1111", "high"])
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))
    tm.add()
    assert len(tm.tasks) == 1
    assert tm.tasks[0]["title"] == "Test Task"
    assert tm.tasks[0]["priority"] == "high"

def test_delete_task_by_id(sample_task_manager):
    tm = sample_task_manager
    tm.tasks.append(task)
    tm.delete("1")
    assert len(tm.tasks) == 0

def test_delete_task_by_name(sample_task_manager):
    tm = sample_task_manager
    tm.tasks.append(task)
    tm.delete("Test Task")
    assert len(tm.tasks) == 0

def test_mark_done(sample_task_manager):
    tm = sample_task_manager
    tm.tasks.append(task)
    tm.done("1")
    assert tm.tasks[0]["is_done"] is True

def test_find_task(sample_task_manager):
    tm = sample_task_manager
    tm.tasks.append(task)
    result = tm.find(["Test"])
    assert len(result) == 1
    assert result[0]["title"] == "Test Task"

def test_show_tasks(sample_task_manager):
    tm = sample_task_manager
    tm.tasks.append(task)
    tm.tasks.append({"id": 2, "title": "Test Task 2", "desc": "Test Desc 2", 
                     "category": "gaming", "deadline": "22-22-2222", "priority": "high", "is_done": False})
    result = tm.show("Work")
    assert len(result) == 1
    assert result[0]["title"] == "Test Task"

def test_sanitized_input(monkeypatch):
    inputs = iter(["invalid", "Test"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = sanitized_input(r"^(Test)$", "Prompt: ")
    assert result == ["Test"]

def test_print_tasks(capsys):
    print_tasks([task])
    captured = capsys.readouterr()
    assert "Test Desc" in captured.out
    assert "high" in captured.out
