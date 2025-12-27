---
phr_id: 018
phr_title: Fix AttributeError in main.py Entry Point
phr_stage: green
phr_date_iso: 2025-12-27
phr_surface: agent
phr_model: 
phr_feature: phase1-console
phr_branch: 
phr_user: 
phr_command: fix the error "AttributeError: 'function' object has no attribute 'main_loop'"
phr_labels: ["bug-fix", "entry-point", "import-error"]
phr_links:
  spec: null
  ticket: null
  adr: null
  pr: null
phr_files_yaml:
  - main.py
phr_tests_yaml: []
---

### Prompt

fix the error "AttributeError: 'function' object has no attribute 'main_loop'"

### Response

An `AttributeError` was occurring because `main.py` was importing the `cli` function from `src/cli.py` instead of the `cli` module itself. The call to `cli.main_loop()` was therefore attempting to find a `main_loop` attribute on a function object, which does not exist.

The fix replaces the incorrect import statement `from src.cli import cli` with `from src import cli`. This ensures that `cli` refers to the module, allowing the `main_loop` function within it to be correctly resolved and called.

### Outcome

The `AttributeError` is resolved. The `main.py` entry point now correctly imports the `cli` module and invokes the `main_loop()` function, allowing the CLI application to start as intended.

```python
# main.py content after modification
from src import cli

if __name__ == '__main__':
    cli.main_loop()
```
