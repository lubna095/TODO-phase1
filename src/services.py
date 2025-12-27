from typing import Dict, List, Optional
from src.models import Task

# In-memory storage for tasks
_tasks: Dict[str, Task] = {}

def create_task(task: Task) -> Task:
    """Creates a new task in memory."""
    if task.name in _tasks:
        raise ValueError(f"Task with name '{task.name}' already exists.")
    _tasks[task.name] = task
    return task

def get_task(name: str) -> Optional[Task]:
    """Retrieves a task by its name from memory."""
    return _tasks.get(name)

def list_tasks() -> List[Task]:
    """Returns a list of all tasks from memory."""
    return list(_tasks.values())

def update_task(name: str, task_update: Task) -> Optional[Task]:
    """Updates an existing task in memory."""
    if name not in _tasks:
        return None
    
    # If the name is being updated, we need to remove the old entry
    if name != task_update.name:
        if task_update.name in _tasks:
            raise ValueError(f"Task with name '{task_update.name}' already exists.")
        del _tasks[name]

    _tasks[task_update.name] = task_update
    return task_update

def delete_task(name: str) -> bool:
    """Deletes a task by its name from memory."""
    if name in _tasks:
        del _tasks[name]
        return True
    return False

def toggle_task_completion(name: str) -> Optional[Task]:
    """Toggles the completion status of a task in memory."""
    task = get_task(name)
    if task:
        task.completed = not task.completed
        _tasks[name] = task # Update the in-memory cache
        return task
    return None


