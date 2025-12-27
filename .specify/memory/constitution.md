## Project Constitution: Hackathon To-Do App
## 1. Core Principles
Spec-Driven Development (SDD): No code shall be written before a spec.md, plan.md, and tasks.md exist in the feature directory.

Vertical Slicing: Each feature must be implemented in independent, testable user stories (P1, P2, P3).

Authoritative Source: The specs/ directory is the source of truth. If the code deviates from the spec, the code is wrong.

## 2. Technical Strategy
Runtime: Python 3.13+.

Architecture: Modular design only.

src/models.py: Pure data structures (Dataclasses).

src/services.py: Business logic and data persistence. No print or input.

src/cli.py: User interface and interaction loop.

Persistence (Phase 2): Use JSON for storage to maintain simplicity and human-readability.

## 3. The Feedback Flywheel
Record: Every significant prompt and response must be logged in history/prompts/.

Reflect: Each PHR must include a "Reflection" note on failure modes or successful patterns.

Iterate: Use the reflection from previous tasks to improve the prompts for the next task.

## 4. Constraint Gates
Gate 01: Any new dependency must be justified in an ADR (Architecture Decision Record).

Gate 02: All services.py logic must have 100% test coverage in pytest before the CLI is updated.
