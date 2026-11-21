# **TaskFlow: Project Structure and File Ownership**

**Status:** Proposed for team confirmation | **Based on:** Backend plan (Section 3), Frontend plan (Sections 5 and 6), Database design, API Contract draft, and `Development_Task_Division.md`

## **1. Purpose**

This document shows every folder and file planned for the TaskFlow code project, and **which position owns each one**. Rule: **each file has one owner.** Only the owner edits a file directly. Everyone else asks the owner or opens a pull request that the owner reviews.

## **2. Legend**

| Tag | Position | Member |
|---|---|---|
| `[SM]` | Scrum Master and Product Owner | Member 2 |
| `[FS]` | Full-Stack Developer | Member 1 |
| `[DB]` | Database Developer | Member 3 |
| `[BE]` | Backend Developer | Member 4 |
| `[FE]` | Frontend Developer | Member 5 |

The member numbers match the research phases. If your team uses a different mapping, swap the names. The ownership stays the same.

## **3. Project Tree**

```
taskflow/                         (repository root)
├── README.md                     [SM]  how to install, set SECRET_KEY, run, test
├── .gitignore                    [SM]  ignores the database file, caches, secrets
├── requirements.txt              [SM]  Flask, Flask-WTF, pytest, tzdata
├── config.py                     [SM]  settings (session time, time zone, cookie options)
├── run.py                        [SM]  starts the app
├── schema.sql                    [DB]  the Phase 3 tables + the 3 fixed categories
│
├── instance/                           created when the app runs; NOT committed
│   └── taskflow.db               [DB]  the SQLite database file (generated)
│
├── taskflow/                           the application package
│   ├── __init__.py               [BE]  create_app, CSRF, session settings, JSON error handlers
│   ├── db.py                     [DB]  opens the connection, foreign keys ON, creates the database
│   ├── models.py                 [DB]  every database function and query
│   ├── validators.py             [BE]  input checks (auth and tasks)
│   ├── query_options.py          [BE]  safe reading of filter, search, and sort options
│   ├── auth.py                   [BE]  register, login, logout, login_required
│   ├── tasks.py                  [BE]  /dashboard, /tasks, and the task JSON endpoints
│   ├── categories.py             [FS]  /category/<name> route
│   ├── calendar.py               [FS]  /calendar page and /api/calendar endpoints
│   ├── profile.py                [FS]  /profile and /profile/password routes
│   │
│   ├── templates/                      HTML pages (Jinja2)
│   │   ├── base.html             [FE]  layout, navigation bar, CSRF meta tag
│   │   ├── login.html            [FE]
│   │   ├── register.html         [FE]
│   │   ├── dashboard.html        [FE]
│   │   ├── tasks.html            [FE]  All Tasks page
│   │   ├── error.html            [FE]  404 and 500 pages
│   │   ├── category.html         [FS]  Category Tasks page
│   │   ├── calendar.html         [FS]
│   │   ├── profile.html          [FS]
│   │   └── partials/                   reusable pieces
│   │       ├── _task_modal.html      [FE]  add and edit form
│   │       ├── _filter_bar.html      [FE]  search, filters, sort
│   │       ├── _task_card.html       [FE]  dashboard task card
│   │       ├── _task_row.html        [FE]  task list row
│   │       └── _category_card.html   [FE]  dashboard category card
│   │
│   └── static/
│       ├── css/
│       │   └── style.css         [FE]  colors, shared styling, responsive rules
│       └── js/
│           ├── api.js            [FE]  shared fetch helper (CSRF header, 401 redirect, errors)
│           ├── tasks.js          [FE]  modal, create, edit, delete, complete
│           └── calendar.js       [FS]  month navigation, date panel, task details
│
├── tests/
│   ├── conftest.py               [FS]  shared pytest setup (temporary test database)
│   ├── test_models.py            [DB]
│   ├── test_validators.py        [BE]
│   ├── test_query_options.py     [BE]
│   ├── test_auth.py              [BE]
│   ├── test_tasks_api.py         [BE]  includes ownership tests
│   ├── test_categories.py        [FS]
│   ├── test_calendar.py          [FS]
│   ├── test_profile.py           [FS]
│   ├── integration/
│   │   ├── test_auth_flow.py     [FS]  register → login → logout
│   │   ├── test_task_flow.py     [FS]  create → edit → complete → delete
│   │   └── test_security.py      [FS]  CSRF, SQL injection, XSS, session expiry
│   └── manual/
│       ├── frontend_checks.md    [FE]  pages on desktop and mobile, forms, errors
│       └── user_stories_checklist.md  [SM]  US-1 to US-7 before the demo
│
└── docs/                               project documents
    ├── research/                 [SM]  the five research reports and the SRS (author of each phase edits their own)
    ├── API_Contract_Agreement.md [SM]  keeper; changes follow the team vote and change log
    ├── Development_Task_Division.md   [SM]
    ├── Project_Structure_and_Ownership.md  [SM]
    └── final/                    [SM]  final report and demo slides
```

## **4. File Details**

### **4.1 Root files**

| File | Purpose | Owner | Sprint |
|---|---|---|---|
| `README.md` | Setup and run instructions | `[SM]` | 1, updated at the end |
| `.gitignore` | Keeps the database, `__pycache__`, and secrets out of GitHub | `[SM]` | 1 |
| `requirements.txt` | Library list. Anyone who needs a new library asks through a pull request. | `[SM]` | 1 |
| `config.py` | Session time (30 minutes), cookie options, time zone (`Africa/Cairo`) | `[SM]` | 1 |
| `run.py` | Starts the app | `[SM]` | 1 |
| `schema.sql` | Phase 3 tables and the three category rows | `[DB]` | 1 |

### **4.2 Backend package (`taskflow/`)**

| File | Purpose | Owner | Sprint |
|---|---|---|---|
| `__init__.py` | `create_app`, CSRF, session settings, JSON error handlers (401, CSRF, 404, 500) | `[BE]` | 1 |
| `db.py` | Connection per request, `PRAGMA foreign_keys = ON`, database creation | `[DB]` | 1 |
| `models.py` | Users, tasks, categories, dashboard, filter, calendar, and profile queries (parameterized, `user_id` from the session) | `[DB]` | 1 to 4 |
| `validators.py` | Name, email, password, title, category, deadline, priority, status | `[BE]` | 1 to 2 |
| `query_options.py` | Reads `priority`, `status`, `category`, `q`, `sort` from fixed lists | `[BE]` | 3 |
| `auth.py` | Register, login, logout, `login_required` | `[BE]` | 1 |
| `tasks.py` | `/dashboard`, `/tasks`, `/api/tasks`, complete, delete | `[BE]` | 2 to 3 |
| `categories.py` | `/category/<name>` | `[FS]` | 3 |
| `calendar.py` | `/calendar`, `/api/calendar?month=` and `?date=` | `[FS]` | 4 |
| `profile.py` | `/profile`, `/profile/password` | `[FS]` | 4 |

### **4.3 Frontend (`templates/` and `static/`)**

| File | Purpose | Owner | Sprint |
|---|---|---|---|
| `base.html` | Layout, navigation bar, Logout form button, CSRF meta tag | `[FE]` | 1 |
| `login.html`, `register.html` | Login and Register pages with the CSRF field | `[FE]` | 1 |
| `tasks.html` | All Tasks page | `[FE]` | 2 |
| `error.html` | Friendly 404 and 500 pages | `[FE]` | 2 |
| `partials/_task_modal.html` | Add and edit form | `[FE]` | 2 |
| `partials/_task_row.html` | One row in a task list | `[FE]` | 2 |
| `dashboard.html` | Dashboard page | `[FE]` | 3 |
| `partials/_task_card.html`, `_category_card.html` | Dashboard cards | `[FE]` | 3 |
| `partials/_filter_bar.html` | Search box, filters, sort control | `[FE]` | 3 |
| `category.html` | Category Tasks page | `[FS]` | 3 |
| `calendar.html` | Calendar page | `[FS]` | 4 |
| `profile.html` | Profile page | `[FS]` | 4 |
| `css/style.css` | Colors, shared styling, responsive layout | `[FE]` | 1 to 4 |
| `js/api.js` | Shared fetch helper | `[FE]` | 2 |
| `js/tasks.js` | Modal and task actions | `[FE]` | 2 |
| `js/calendar.js` | Calendar behavior | `[FS]` | 4 |

### **4.4 Tests**

| File | Tests | Owner | Sprint |
|---|---|---|---|
| `conftest.py` | Shared setup and temporary database | `[FS]` | 1 |
| `test_models.py` | Database functions | `[DB]` | 1 to 4 |
| `test_validators.py`, `test_query_options.py`, `test_auth.py`, `test_tasks_api.py` | Backend code | `[BE]` | 1 to 3 |
| `test_categories.py`, `test_calendar.py`, `test_profile.py` | Full-Stack features | `[FS]` | 3 to 4 |
| `integration/` | Full flows and security tests | `[FS]` | 1 to 4 |
| `manual/frontend_checks.md` | Page and form checks | `[FE]` | 2 to 4 |
| `manual/user_stories_checklist.md` | US-1 to US-7 | `[SM]` | 4 |

## **5. Files That Need Hand-Offs**

| File | Owner | Who else depends on it | Agreement |
|---|---|---|---|
| `base.html` | `[FE]` | `[BE]` provides `csrf_token()`; `[FS]` extends it for the three FS pages | `[FE]` adds the CSRF meta tag and the Logout form |
| `partials/_filter_bar.html` | `[FE]` | `[FS]` reuses it on `category.html` | `[FE]` keeps it reusable; `[FS]` does not edit it |
| `js/api.js` | `[FE]` | `[FS]` uses it in `calendar.js` | `[FE]` documents the functions at the top of the file |
| `models.py` | `[DB]` | `[BE]` and `[FS]` call its functions | Names agreed at the start of each Sprint (for example `get_tasks(user_id, filters)`) |
| `__init__.py` | `[BE]` | `[FS]` registers the three FS blueprints | `[BE]` adds the lines through a reviewed pull request |
| `requirements.txt` | `[SM]` | Everyone | New libraries go through a pull request |

## **6. Files per Position**

| Position | Source files | Tests | Other |
|---|---|---|---|
| `[SM]` Member 2 | `config.py`, `run.py` | `manual/user_stories_checklist.md` | `README.md`, `.gitignore`, `requirements.txt`, the whole `docs/` folder, GitHub board |
| `[FS]` Member 1 | `categories.py`, `calendar.py`, `profile.py`, 3 pages, `calendar.js` | `conftest.py`, 3 feature tests, `integration/` | |
| `[DB]` Member 3 | `schema.sql`, `db.py`, `models.py` | `test_models.py` | |
| `[BE]` Member 4 | `__init__.py`, `auth.py`, `tasks.py`, `validators.py`, `query_options.py` | 4 test files | |
| `[FE]` Member 5 | `base.html`, 6 pages, 5 partials, `style.css`, `api.js`, `tasks.js` | `manual/frontend_checks.md` | |

## **7. Assumptions and Open Items**

All items are **Proposed** and need the team's confirmation.

| ID | Topic | Proposal |
|---|---|---|
| S-1 | Database file location | `instance/taskflow.db` (Flask's instance folder), generated and never committed. |
| S-2 | New files | `categories.py` and `query_options.py` are small additions to the Backend report structure. Also new: `error.html`, the partials, and the `docs/`, `instance/`, and `tests/manual/` folders. |
| S-3 | Module names | `calendar.py` and `profile.py` share a name with Python's built-in `calendar` and `profile` modules. This is safe when the app is run from the project root. If strange import errors ever appear, rename them to `calendar_routes.py` and `profile_routes.py`. |
| S-4 | Blueprint registration | Each blueprint is registered in `__init__.py`. `[BE]` owns that file, so `[FS]` asks for the three lines through a pull request. |
| S-5 | Document folders | The `docs/` layout is a suggestion. Your current `Docs` and `Team_Work` folders can stay as they are. |
| S-6 | Combined role | `[SM]` holds both Scrum Master and Product Owner duties (see `Development_Task_Division.md`). |
