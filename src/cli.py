import click
from src.models import Task
from src.services import (
    create_task,
    get_task,
    list_tasks,
    update_task,
    delete_task,
    toggle_task_completion, # Import the new function
)

def cli():
    """A simple CLI to manage tasks."""
    main_loop()

def main_loop():
    while True:
        click.echo("\n--- Task Management CLI ---")
        click.echo("1. Add a new task")
        click.echo("2. View all tasks")
        click.echo("3. Update a task")
        click.echo("4. Delete a task")
        click.echo("5. Toggle task completion")
        click.echo("6. Exit")
        choice = click.prompt("Enter your choice", type=int)

        if choice == 1:
            name = click.prompt("Enter task name")
            description = click.prompt("Enter task description")
            try:
                task = Task(name=name, description=description)
                created_task = create_task(task)
                click.echo(f"Task '{created_task.name}' created successfully.")
            except ValueError as e:
                click.echo(f"Error: {e}", err=True)
        elif choice == 2:
            tasks = list_tasks()
            if not tasks:
                click.echo("No tasks found.")
                continue
            click.echo("\n--- All Tasks ---")
            for task in tasks:
                status = "✓" if task.completed else " "
                click.echo(f"[{status}] {task.name}: {task.description}")
        elif choice == 3:
            name = click.prompt("Enter the name of the task to update")
            current_task = get_task(name)
            if not current_task:
                click.echo(f"Task '{name}' not found.", err=True)
                continue
            
            new_name = click.prompt(f"Enter new name (current: {current_task.name})", default=current_task.name)
            new_description = click.prompt(f"Enter new description (current: {current_task.description})", default=current_task.description)
            
            # For update, we need to preserve the completed status if not explicitly changed
            # The current update_task in services.py doesn't take completed status directly.
            # We'll construct a new Task object with existing completed status.
            task_update = Task(name=new_name, description=new_description, completed=current_task.completed)

            try:
                updated = update_task(name, task_update)
                if updated:
                    click.echo(f"Task '{name}' updated successfully.")
                else:
                    click.echo(f"Failed to update task '{name}'.", err=True)
            except ValueError as e:
                click.echo(f"Error: {e}", err=True)

        elif choice == 4:
            name = click.prompt("Enter the name of the task to delete")
            if delete_task(name):
                click.echo(f"Task '{name}' deleted successfully.")
            else:
                click.echo(f"Task '{name}' not found.", err=True)
        elif choice == 5:
            name = click.prompt("Enter the name of the task to toggle completion")
            task = toggle_task_completion(name)
            if task:
                status = "completed" if task.completed else "not completed"
                click.echo(f"Task '{task.name}' marked as {status}.")
            else:
                click.echo(f"Task '{name}' not found.", err=True)
        elif choice == 6:
            click.echo("Exiting Task Management CLI. Goodbye!")
            break
        else:
            click.echo("Invalid choice. Please try again.")

# Removed individual @cli.command() decorators as functionality is now in main_loop

# The existing @cli.command() functions are removed because the main_loop handles interaction.
# If these functions were intended to be callable directly via command line args in addition to the loop,
# they would need to be re-added and modified to use the service functions directly,
# without prompts, or the main_loop would need to use click's invoke() method, which is more complex.
# For this request, the interactive loop is the primary focus.

