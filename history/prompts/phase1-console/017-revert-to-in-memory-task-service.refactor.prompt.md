---
phr_id: 017
phr_title: Revert to In-Memory Task Service
phr_stage: refactor
phr_date_iso: 2025-12-27
phr_surface: agent
phr_model: 
phr_feature: phase1-console
phr_branch: 
phr_user: 
phr_command: Ensure src/services.py: Keep the global _tasks dictionary and create_task logic so the data stays in RAM while the menu loop is running
phr_labels: ["refactor", "in-memory", "state-management"]
phr_links:
  spec: null
  ticket: null
  adr: null
  pr: null
phr_files_yaml:
  - src/services.py
phr_tests_yaml: []
---

### Prompt

Ensure src/services.py: Keep the global _tasks dictionary and create_task logic so the data stays in RAM while the menu loop is running

### Response

The `src/services.py` file was refactored to maintain a purely in-memory task storage system. All file I/O logic, including loading from and saving to `tasks.json`, has been removed. The `_tasks` dictionary is now initialized as an empty dictionary, ensuring that data persists only in RAM for the duration of the application's runtime.

### Outcome

The `TaskService` now operates exclusively in-memory, aligning with the user's requirement to keep data transient while the menu loop is active. This change reverts the previous file persistence implementation and simplifies the state management for the `phase1-console` feature.

```python
# src/services.py content after modification
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
```
