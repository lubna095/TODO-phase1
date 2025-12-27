---
description: "Task list for console CLI feature implementation"
---

# Tasks: phase1-console (CLI)

**Input**: Implementation Plan from `/specs/phase1-console/plan.md`
**Prerequisites**: A running TaskController and TaskWorker environment.

## Phase 1: Setup (CLI Project)

**Purpose**: Project initialization for the command-line interface.

- [ ] T001 Create `console_cli` directory for the application source code.
- [ ] T002 Initialize Python project with `pyproject.toml` to manage dependencies (e.g., `requests`, `click`, `pydantic`).

---

## Phase 2: Foundational (Client-side Models & Services)

**Purpose**: Core client-side components for interacting with the task controller API.

- [ ] T003 [P] Implement data models in `console_cli/models.py` for API requests and responses (e.g., `StartSampleRequest`, `InteractRequest`, `CancelRequest`).
- [ ] T004 Implement the `TaskClient` service in `console_cli/client.py` to handle communication with the TaskController endpoints.
- [ ] T005 [P] Implement a configuration module in `console_cli/config.py` to manage the controller's address and other settings.

---

## Phase 3: User Story 1 - CLI Commands (Priority: P1) 🎯 MVP

**Goal**: Provide a command-line interface to interact with the task execution framework.

**Independent Test**: The CLI can be tested by running its commands against a live TaskController and verifying the output.

### Implementation for User Story 1

- [ ] T006 [US1] Create the main CLI entry point in `console_cli/main.py` using the `click` library.
- [ ] T007 [US1] Implement the `list-workers` command to fetch and display the status of all registered workers.
- [ ] T008 [US1] Implement the `list-sessions` command to display currently active task sessions.
- [ ] T009 [US1] Implement the `get-indices <task_name>` command to retrieve the available sample indices for a task.
- [ ] T010 [US1] Implement the `start-sample <task_name> <index>` command to initiate a new task run.
- [ ] T011 [US1] Implement the `interact <session_id> <message>` command to send input to a running task session.
- [ ] T012 [US1] Implement the `cancel <session_id>` command to terminate a running task session.
- [ ] T013 [US1] Implement the `calculate-overall <task_name>` command by collecting local results and sending them to the controller.

**Checkpoint**: At this point, the CLI should be functional for basic task management and interaction.

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect the entire CLI application.

- [ ] T014 [P] Add comprehensive `README.md` documentation for CLI setup and usage.
- [ ] T015 Implement robust error handling and user-friendly feedback for all commands.
- [ ] T016 Add unit tests for the `TaskClient` and data models.
- [ ] T017 [P] Code cleanup and refactoring across the `console_cli` module.

---

## Dependencies & Execution Order

- **Setup (Phase 1)**: Can start immediately.
- **Foundational (Phase 2)**: Depends on Setup. Models and Config can be done in parallel. `TaskClient` depends on models.
- **User Story 1 (Phase 3)**: Depends on Foundational phase. All CLI commands can be developed in parallel after `main.py` is set up.
- **Polish (Phase 4)**: Can be done after User Story 1 is complete.