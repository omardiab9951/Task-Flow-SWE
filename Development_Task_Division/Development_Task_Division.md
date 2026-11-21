# **TaskFlow: Development Task Division**

**Status:** Proposed for team confirmation | **Applies to:** Sprints 1 to 4 | **Based on:** SRS v1.2, the Backend plan (Phase 4), the Frontend plan (Phase 5), the Database design (Phase 3), the API Contract draft, and the Agile workflow

## **1. Purpose**

This document divides the TaskFlow development work among the five members. The goal is simple: **each file has one owner**, so two people do not edit the same file at the same time. Each member also writes the tests for their own code, so no separate QA position is needed.

## **2. Positions**

| Member | Position | Main responsibility |
|---|---|---|
| **Member 1** | Full-Stack Developer | Builds complete features that touch both the backend and the frontend (about 30% of the tasks of each side). Sets up the shared tests. |
| **Member 2** | Scrum Master and Product Owner | Runs the team and the Sprint events, orders the backlog, writes the acceptance checks, tests the final product, and prepares the demo and documentation. |
| **Member 3** | Database Developer | Owns the database and every query. |
| **Member 4** | Backend Developer | Owns the Flask application, authentication, validation, and most routes and JSON endpoints. |
| **Member 5** | Frontend Developer | Owns the pages, the styling, and the JavaScript for most of the interface. |

The member numbers match the research phases (Member 3 did Phase 3, and so on). If your team prefers a different mapping, swap the names. Nothing else in this document changes.

## **3. File Ownership**

| Owner | Files and areas |
|---|---|
| **Member 2** | `config.py`, `run.py`, `requirements.txt`, GitHub repository, branches, project board, acceptance checks, manual test checklist, final documentation |
| **Member 3** | `schema.sql`, `db.py`, `models.py` (all database functions and queries) |
| **Member 4** | `taskflow/__init__.py` (create_app, CSRF, session settings, JSON error handlers), `auth.py`, `tasks.py` (dashboard, All Tasks, task JSON endpoints), `validators.py`, `query_options.py` |
| **Member 5** | `templates/` (base layout, Login, Register, Dashboard, All Tasks, task modal), `static/css/`, `static/js/` (modal, task actions, shared fetch helper) |
| **Member 1** | `categories.py`, `calendar.py`, `profile.py`, `templates/` (Category Tasks, Calendar, Profile), `static/js/calendar.js`, `tests/conftest.py` and the integration tests |

`categories.py` and `query_options.py` are two small files added to the structure in the Backend report (Section 3). They keep one owner per file.

## **4. The Full-Stack 30% Rule**

Member 1 builds three complete features, each with its backend part and its frontend part. This gives Member 1 about 30% of the work on each side, and the rest stays with the Backend and Frontend developers.

| Feature | Backend part | Frontend part |
|---|---|---|
| Category Tasks | `/category/<name>` route | Category Tasks page |
| Calendar | `/calendar` and `/api/calendar` endpoints | Calendar page (month navigation, date panel, task details) |
| Profile | `/profile` and `/profile/password` routes | Profile page (name, email, password change) |

| Side | Total tasks | Member 4 or 5 | Member 1 |
|---|---|---|---|
| Backend | 9 | 6 (67%) | 3 (33%) |
| Frontend | 10 | 7 (70%) | 3 (30%) |

**Backend tasks:** app setup and error handlers, authentication, validators, task endpoints, query options, dashboard and All Tasks routes (Member 4); category route, calendar endpoints, profile routes (Member 1).
**Frontend tasks:** base layout and CSS, Login and Register, Dashboard, All Tasks with filter bar, task modal, shared JavaScript and mobile polish (Member 5); Category Tasks page, Calendar page, Profile page (Member 1).

## **5. Work per Sprint**

| Sprint | Member 1 (Full-Stack) | Member 2 (Scrum Master and Product Owner) | Member 3 (Database) | Member 4 (Backend) | Member 5 (Frontend) |
|---|---|---|---|---|---|
| **1: Setup and login** | Set up pytest (`conftest.py`, temporary test database); write the integration tests for register, login, logout | Repo, branches, project board; `config.py`, `run.py`, `requirements.txt`; Sprint Planning; acceptance checks for authentication | `schema.sql`, database connection, `PRAGMA foreign_keys`, seed the 3 categories, user functions (create, find by email) | `create_app`, CSRF, session settings (30 minutes), JSON error handlers; register, login, logout; `login_required`; authentication validators; own tests | Base layout, navigation bar, CSS colors and shared styling; Login and Register pages with the CSRF field |
| **2: Core tasks** | Integration tests for task create, edit, delete, complete; review the task code of both sides | Acceptance checks for tasks; order the backlog; review pull requests | Task functions: create, get by id (with owner), edit, delete, complete, list | Task JSON endpoints; task validators; deadline building (default 23:59); `is_overdue`; ownership tests | All Tasks page (list, badges, empty state); task modal (create and edit); delete confirmation; shared fetch helper (CSRF header, 401 redirect, error messages) |
| **3: Dashboard and organization** | `/category/<name>` route and Category Tasks page (reusing Member 5's filter bar); tests; **may start Profile early** | Acceptance checks for US-2, US-4, US-5; security check of the auth code; pull request reviews | Dashboard queries (3 nearest, category counts with LEFT JOIN); filter, search, and sort query (fixed lists, parameters only) | `query_options.py`; `/dashboard` and `/tasks` routes; tests | Dashboard page (task cards, category cards, buttons); filter bar, search box, sort control; empty states |
| **4: Calendar, profile, finish** | Calendar endpoints and page; Profile routes and page; tests | Full manual test of US-1 to US-7; security review; Sprint Review; final demo; final report | Calendar queries (month and date); profile update and password functions; bug fixes | Bug fixes; final check of validation and error handling; performance check (pages under 2 seconds) | Mobile and responsive polish; contrast and keyboard check; error message polish |

Member 2 runs Sprint Planning, the Daily Scrum, Sprint Review, and Sprint Retrospective in every Sprint (see the Agile plan).

## **6. Testing**

- Every member writes the `pytest` tests for their own code, using the shared setup from Member 1.
- Member 1 writes the integration tests that cover a full feature from request to database.
- Member 2 runs the manual test of the user stories and the security checklist before the demo.
- A task is Done only when it meets the Definition of Done in the Agile plan.

## **7. Working Rules**

1. One branch per feature (for example `feature/login`), and small commits.
2. Another member reviews every pull request. **Nobody merges their own work.**
3. The `main` branch must always run.
4. If you need a change in a file you do not own, ask the owner or open a pull request they review.
5. Any change to the API contract follows the team vote and the change log (Section 12 of the contract).
6. Members 3 and 4 agree the database function names at the start of each Sprint (for example `get_tasks(user_id, filters)`). Members 4 and 5 follow the API contract.

## **8. Order That Matters**

1. **First:** Member 2 pushes the repository and Member 3 pushes `schema.sql`, because the others depend on them.
2. **Member 5 does not need to wait for the backend.** Build the pages with fake data from the contract examples, then connect them.
3. **Member 4 creates `create_app` early in Sprint 1.** Members 1, 3, and 5 need it to run their code.

## **9. Assumptions and Open Items**

All items are **Proposed** and need the team's confirmation.

| ID | Topic | Proposal |
|---|---|---|
| D-1 | Member-to-position mapping | As in Section 2. Swap names if the team prefers. |
| D-2 | Combined role | Member 2 holds both Scrum Master and Product Owner. If the load is too heavy, Member 1 can take over ordering the backlog. |
| D-3 | Member 1 in Sprints 1 and 2 | The three features depend on the login and task base, so Member 1 has a lighter feature load early. Member 1 uses the time for the shared tests and for code reviews. |
| D-4 | Sprint 4 load | Calendar and Profile both land in Sprint 4 for Member 1. If time is short, Member 1 starts Profile in Sprint 3. The Product Owner decides. |
| D-5 | New files | `categories.py` and `query_options.py` are small additions to the Backend report structure. Update Backend Section 3 or keep them as a team decision. |
| D-6 | API contract | Development depends on the contract. It must be signed by all five members before Sprint 1 starts. |
