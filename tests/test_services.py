import pytest
import os
import importlib
from src import services
from src.models import Task

# A sample task for testing
sample_task = Task(name="test_task", description="A task for testing.")

@pytest.fixture(autouse=True)
def run_around_tests():
    # This fixture ensures a clean state by deleting tasks.json and reloading the services module.
    if os.path.exists(services.TASKS_FILE):
        os.remove(services.TASKS_FILE)
    
    # Reload the module to re-initialize the _tasks cache from a clean slate
    importlib.reload(services)

    yield

    if os.path.exists(services.TASKS_FILE):
        os.remove(services.TASKS_FILE)

    # Reload again to ensure a clean state for any subsequent test modules.
    importlib.reload(services)


# The test functions remain the same, but now they are testing the file-persistent logic.

def test_create_task():
    """Test creating a new task."""
    created = services.create_task(sample_task)
    assert created == sample_task
    assert services.get_task(sample_task.name) == sample_task

    # Verify persistence by reloading the service
    importlib.reload(services)
    assert services.get_task(sample_task.name) == sample_task

def test_create_existing_task_fails():
    """Test that creating a task with an existing name raises an error."""
    services.create_task(sample_task)
    with pytest.raises(ValueError):
        services.create_task(sample_task)

def test_get_task():
    """Test retrieving a task."""
    services.create_task(sample_task)
    retrieved = services.get_task(sample_task.name)
    assert retrieved == sample_task

def test_get_nonexistent_task():
    """Test that retrieving a non-existent task returns None."""
    retrieved = services.get_task("nonexistent")
    assert retrieved is None

def test_list_tasks():
    """Test listing all tasks."""
    assert services.list_tasks() == []
    services.create_task(sample_task)
    assert services.list_tasks() == [sample_task]
    
    task2 = Task(name="task2", description="another task")
    services.create_task(task2)
    
    # Verify persistence
    importlib.reload(services)
    
    # The order is not guaranteed, so we check for presence
    assert sample_task in services.list_tasks()
    assert task2 in services.list_tasks()
    assert len(services.list_tasks()) == 2

def test_update_task():
    """Test updating an existing task."""
    services.create_task(sample_task)
    
    updated_task_data = Task(name="test_task", description="An updated description.")
    updated = services.update_task(sample_task.name, updated_task_data)
    
    assert updated == updated_task_data
    assert services.get_task(sample_task.name).description == "An updated description."

    # Verify persistence
    importlib.reload(services)
    assert services.get_task(sample_task.name).description == "An updated description."


def test_update_task_rename():
    """Test updating a task's name."""
    services.create_task(sample_task)
    
    renamed_task = Task(name="new_name_task", description="A task for testing.")
    updated = services.update_task(sample_task.name, renamed_task)
    
    assert updated == renamed_task
    assert services.get_task(sample_task.name) is None
    assert services.get_task("new_name_task") == renamed_task

    # Verify persistence
    importlib.reload(services)
    assert services.get_task(sample_task.name) is None
    assert services.get_task("new_name_task") == renamed_task

def test_update_task_rename_conflict():
    """Test that renaming a task to an existing name fails."""
    task1 = Task(name="task1", description="desc1")
    task2 = Task(name="task2", description="desc2")
    services.create_task(task1)
    services.create_task(task2)
    
    task1_updated = Task(name="task2", description="desc1_updated")
    with pytest.raises(ValueError):
        services.update_task("task1", task1_updated)

def test_update_nonexistent_task():
    """Test that updating a non-existent task returns None."""
    updated = services.update_task("nonexistent", sample_task)
    assert updated is None

def test_delete_task():
    """Test deleting a task."""
    services.create_task(sample_task)
    assert services.get_task(sample_task.name) is not None
    
    deleted = services.delete_task(sample_task.name)
    assert deleted is True
    assert services.get_task(sample_task.name) is None

    # Verify persistence
    importlib.reload(services)
    assert services.get_task(sample_task.name) is None

def test_delete_nonexistent_task():
    """Test that deleting a non-existent task returns False."""
    deleted = services.delete_task("nonexistent")
    assert deleted is False
