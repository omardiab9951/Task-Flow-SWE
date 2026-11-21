# **TaskFlow: Phase 4, Backend Development Planning**

**Scope:** Planning only, no implementation | **Prepared by:** Member 4 (name to be added) | **Status:** Proposed design for team review

## **1. Purpose and Scope**

This report plans the TaskFlow backend: how Flask receives requests, checks the user, validates input, talks to SQLite, and sends a response. It follows SRS v1.2, the Phase 2 architecture, the Phase 3 database design, and the Phase 5 frontend plan.

**Scope boundaries:**

- The routes and fields in Section 6 are **proposals**. They become final only when the whole team agrees the API contract **after all five research phases** are finished.
- Phase 4 owns the detailed endpoints. Phase 5 owns how the interface uses them.
- The database tables are used exactly as designed in Phase 3. No table or column is changed here.
- Nothing in this report is implemented yet.

## **2. Backend Approach**

- **Language and framework:** Python 3.9 or newer with Flask (SRS 3.2).
- **Page delivery (confirmed by the team):** Flask renders the main pages with templates and provides a small set of JSON endpoints for dynamic actions (task form or modal, mark complete, delete, calendar data).
- **Database access:** Python's built-in `sqlite3` module with plain SQL, using the schema from Phase 3.
- **Extra libraries (kept to a minimum):** `Flask-WTF` for CSRF protection, `pytest` for tests, and `tzdata` so Africa/Cairo works on Windows.

### **2.1 Backend Decisions (all Proposed)**

| ID | Decision | Why | Rejected alternative |
|---|---|---|---|
| B-1 | Flask's built-in signed session cookie holds the login | Simple, no extra library, no session table (Phase 3) | Flask-Login (more to learn for little gain) |
| B-2 | `sqlite3` with plain SQL | Matches the Phase 3 SQL schema; easy to read and test | SQLAlchemy ORM (extra concepts for a small project) |
| B-3 | `Flask-WTF` `CSRFProtect` | Ready-made protection for every POST, PUT, and DELETE (NFR-11) | Writing our own token code (easy to get wrong) |
| B-4 | Werkzeug password hashing | Already installed with Flask; never stores plain passwords (NFR-1) | Our own hashing (unsafe) |
| B-5 | Blueprints split by feature | Separate routes, data code, and templates (NFR-8) | One large `app.py` (hard to maintain) |

## **3. Project Structure**

```
taskflow/
├── run.py                 # starts the app
├── config.py              # settings (secret key, session time, time zone)
├── schema.sql             # the Phase 3 SQL schema
├── requirements.txt
├── taskflow/
│   ├── __init__.py        # create_app(): sets up Flask, CSRF, blueprints
│   ├── db.py              # opens the SQLite connection, creates the database
│   ├── auth.py            # register, login, logout, login_required
│   ├── tasks.py           # dashboard, task pages, task JSON endpoints
│   ├── calendar.py        # calendar page and calendar JSON endpoint
│   ├── profile.py         # profile and password change
│   ├── models.py          # database functions (users, categories, tasks)
│   ├── validators.py      # input checks
│   ├── templates/         # HTML pages (Phase 5)
│   └── static/            # CSS and JavaScript
└── tests/                 # pytest files
```

Rule: **routes** receive and answer requests, **validators** check input, **models** talk to the database. A route never contains SQL.

## **4. How the Backend Handles a Request**

1. The browser sends an HTTP request with the session cookie (and a CSRF token if it changes data).
2. Flask checks the CSRF token. If it is missing or wrong, the request is rejected.
3. The `login_required` check reads the session. No valid session: pages redirect to Login, JSON endpoints return 401.
4. The route validates the input. Invalid input: nothing is saved, and an error is returned.
5. The route calls a function in `models.py`, which runs a parameterized SQL query limited to the logged-in user.
6. The route returns an HTML page (rendered with a template) or JSON.

## **5. Authentication and Sessions**

| Action | Backend steps |
|---|---|
| **Register** (FR-1, FR-2) | Trim the name; trim and lowercase the email; validate; hash the password; INSERT the user. If the email already exists (UNIQUE error), return a message. On success, go to Login. |
| **Login** (FR-3, FR-4) | Find the user by email; compare the password with `password_hash`; on success, `session.clear()`, store `user_id`, set `session.permanent = True`, go to Dashboard. On failure, show **one generic message** ("Invalid email or password"), and do not say which part was wrong. |
| **Logout** (FR-5) | `POST` request; `session.clear()`; go to Login. The top-bar Logout must be a small form button (not a link), because it changes state and needs a CSRF token. |
| **Protected pages** (FR-6) | A `login_required` decorator on every route except Login and Register. A logged-in user who opens Login or Register is sent to the Dashboard. |
| **Change password** (FR-39) | Verify the current password; validate the new one; replace `password_hash`. |

**Session settings (NFR-2, NFR-12):**

```python
PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)   # inactivity limit
SESSION_COOKIE_HTTPONLY = True                       # JavaScript cannot read the cookie
SESSION_COOKIE_SAMESITE = "Lax"                      # extra CSRF protection
SESSION_COOKIE_SECURE = True                         # only when the site uses HTTPS
```

Flask refreshes a permanent session on every request, so the 30 minutes count from the **last activity**. The `SECRET_KEY` is read from an environment variable and is never written in the code or committed to GitHub.

## **6. Proposed Routes and Endpoints**

### **6.1 Page routes (Flask renders HTML)**

| Method | Route | Purpose | Login needed |
|---|---|---|---|
| GET, POST | `/register` | Register form and submit | No |
| GET, POST | `/login` | Login form and submit | No |
| POST | `/logout` | End the session | Yes |
| GET | `/dashboard` | Up to 3 nearest incomplete tasks and category counts | Yes |
| GET | `/tasks` | All Tasks, with query options (below) | Yes |
| GET | `/category/<name>` | Tasks of one category (`study`, `personal`, `work`); same query options | Yes |
| GET | `/calendar` | Calendar page | Yes |
| GET, POST | `/profile` | View and update name and email | Yes |
| POST | `/profile/password` | Change password | Yes |

**Query options for `/tasks` and `/category/<name>`** (filtering, search, and sorting work together, FR-27 to FR-32):

| Option | Allowed values |
|---|---|
| `category` | `Study`, `Personal`, `Work` (only on `/tasks`) |
| `priority` | `Low`, `Medium`, `High` |
| `status` | `Pending`, `In Progress`, `Completed` |
| `q` | Keyword searched in the task title |
| `sort` | `deadline_asc` (default) or `deadline_desc` |

Any other value is ignored or rejected. It is never put into SQL directly.

### **6.2 JSON endpoints (dynamic actions)**

| Method | Route | Purpose | Success |
|---|---|---|---|
| POST | `/api/tasks` | Create a task (FR-14 to FR-16) | 201 and the task |
| GET | `/api/tasks/<id>` | Get one task (edit form, calendar details) | 200 and the task |
| PUT | `/api/tasks/<id>` | Edit any field of a task (FR-18) | 200 and the task |
| DELETE | `/api/tasks/<id>` | Delete a task (FR-19; the confirmation is in the interface) | 200 and {"deleted": true, "id": <id>} |
| POST | `/api/tasks/<id>/complete` | Set status to Completed (FR-20, BR-3) | 200 and the task |
| GET | `/api/calendar?month=YYYY-MM` | Tasks of one month (FR-33, FR-34) | 200 and {"tasks": [...]} |
| GET | `/api/calendar?date=YYYY-MM-DD` | Tasks of one date (FR-35) | 200 and {"tasks": [...]} |

All JSON endpoints need a login. All POST, PUT, and DELETE requests need the CSRF token in the `X-CSRFToken` header. The page includes the token in a `<meta name="csrf-token">` tag, and the JavaScript reads it from there.

### **6.3 Task data (request and response)**

**Request (create and edit):**

| Field | Required | Notes |
|---|---|---|
| `title` | Yes | Text, 1 to 100 characters |
| `category` | Yes | `Study`, `Personal`, or `Work`; the backend finds the `category_id` |
| `deadline_date` | Yes | `YYYY-MM-DD` |
| `deadline_time` | No | `HH:MM`; if empty, 23:59 is used |
| `description` | No | Text, up to 1000 characters |
| `priority` | No | `Low`, `Medium`, or `High`; default `Medium` |
| `status` | No | `Pending`, `In Progress`, or `Completed`; default `Pending` |

**Response (one task):**

```json
{
  "task": {
    "id": 12,
    "title": "Submit SE report",
    "description": "",
    "category": "Study",
    "priority": "High",
    "status": "Pending",
    "deadline": "2026-12-18 17:00",
    "created_at": "2026-11-21 10:30",
    "is_overdue": false
  }
}
```

`is_overdue` is calculated by the backend and is never stored. `created_at` is stored in UTC and converted to Africa/Cairo before it is sent.

### **6.4 Errors and status codes**

**Error format:** `{ "error": "Short message", "fields": { "title": "Title is required" } }`. The `fields` part is used only for validation errors, so the frontend can show each message next to its field and keep the user's input.

| Code | Meaning | What the frontend does |
|---|---|---|
| 400 | Validation error | Show messages next to the fields |
| 401 | Not logged in or session expired | Redirect to Login |
| 400 (CSRF) | Missing or wrong CSRF token | Show a message and reload the page |
| 404 | Task not found **or not owned by this user** | Show an error; no data shown |
| 500 | Server error | Show a short message and let the user retry |

Not-owned tasks return **404, not 403**, so a user cannot discover which task ids belong to other people (BR-5).

### **6.5 What each page needs (matches the Phase 5 table)**

| Frontend page or action | Backend route |
|---|---|
| Register, Login, Logout | `/register`, `/login`, `/logout` |
| Dashboard | `/dashboard` |
| All Tasks, search, filter, sort | `/tasks?...` |
| Category Tasks | `/category/<name>?...` |
| Create, Edit task | `POST /api/tasks`, `PUT /api/tasks/<id>` (and `GET` to fill the edit form) |
| Delete task | `DELETE /api/tasks/<id>` |
| Mark complete | `POST /api/tasks/<id>/complete` |
| Calendar | `/calendar`, `/api/calendar?...` |
| Profile and password | `/profile`, `/profile/password` |

## **7. Backend and Database Communication**

**Connection:** one SQLite connection per request, opened when needed and closed when the request ends. Every connection runs `PRAGMA foreign_keys = ON;` (SQLite does not enforce foreign keys by default). The database is created from `schema.sql`, which also inserts the three fixed categories.

**Rule 1: parameterized queries only (NFR-3).** Values are never joined into the SQL text.

```python
# Safe: the value travels separately from the SQL
db.execute("SELECT * FROM users WHERE email = ?", (email,))
```

**Rule 2: ownership on every task query (FR-7, BR-5).** The `user_id` always comes from the **session**, never from the request.

```python
db.execute("UPDATE tasks SET status = 'Completed' WHERE id = ? AND user_id = ?",
           (task_id, session["user_id"]))
# If no row changed (rowcount == 0), return 404.
```

**Main queries:**

| Feature | Query idea |
|---|---|
| Dashboard tasks | The user's tasks WHERE `status <> 'Completed'` ORDER BY `deadline` ASC LIMIT 3. Overdue tasks are included. |
| Category counts | `categories LEFT JOIN tasks` on `category_id` and the user's id, `GROUP BY` category. Counts all statuses; a category with no tasks shows 0. |
| All Tasks with options | Start with `WHERE user_id = ?`; add `AND priority = ?`, `AND status = ?`, `AND category_id = ?`, `AND title LIKE ? ESCAPE '\'` only for the options that were sent. `ORDER BY deadline` takes ASC or DESC from a fixed list. |
| Category Tasks | Same as above with the category fixed. |
| Calendar month | `deadline >= 'YYYY-MM-01' AND deadline < 'next month 01'` |
| Calendar date | `deadline >= 'YYYY-MM-DD' AND deadline < 'next day'` |

**Search:** the keyword is wrapped as `%keyword%` and bound as a parameter. The characters `%` and `_` typed by the user are escaped, so they are treated as normal letters.

**Dates and time zone:**

- Deadlines are saved as the text `YYYY-MM-DD HH:MM` in Egypt time (Africa/Cairo), so sorting by text is the same as sorting by time.
- If no time is entered, `23:59` is saved.
- "Now" is `datetime.now(ZoneInfo("Africa/Cairo"))`. A task is overdue when its status is not Completed and its deadline is earlier than now.

## **8. Validation Rules (server side, NFR-10)**

The browser also checks input, but the backend always checks again.

| Field | Rule |
|---|---|
| Name | Required, trimmed, up to 100 characters |
| Email | Required, valid format, lowercase, unique |
| Password | Required, at least 8 characters (proposed rule; see Section 12) |
| Task title | Required, 1 to 100 characters |
| Category | One of Study, Personal, Work |
| Deadline | Valid date (required); valid time if given |
| Priority, status | Only the allowed values (BR-1, BR-2) |
| Description | Optional, up to 1000 characters |

On any failure, nothing is saved and a 400 response with field messages is returned.

## **9. Security Plan**

| Risk | Protection | Requirement |
|---|---|---|
| Stolen passwords | Store only hashes (Werkzeug) | NFR-1 |
| Guessing which part of a login was wrong | One generic login error | FR-4 |
| Session theft or misuse | Signed cookie, HttpOnly, SameSite=Lax, Secure on HTTPS, 30-minute expiry, cleared on login and logout | NFR-2, NFR-12 |
| CSRF (a malicious site acting as the user) | CSRF token on every request that changes data, including login and register | NFR-11 |
| SQL injection | Parameterized queries only; sort order and filters chosen from fixed lists | NFR-3 |
| XSS | Jinja2 auto-escaping stays on; JavaScript inserts text with `textContent`, never `innerHTML` | NFR-3 |
| Reading or changing another user's tasks | `user_id` from the session in every task query; 404 for others' tasks | FR-7, BR-5 |
| Bad input | Server-side validation | NFR-10 |
| Leaked secrets | `SECRET_KEY` from an environment variable; debug mode off in the final version | NFR-2 |

## **10. Testing Plan**

Tools: `pytest` and Flask's test client, with a **temporary SQLite database for each test** so tests never touch real data.

| Level | What is tested |
|---|---|
| **Unit** | Validators; password hash and check; deadline building (default 23:59); overdue calculation; email lowercase |
| **Integration** | Each route with the database: register, login, logout, task create/edit/delete/complete, dashboard, filters, search, sort, calendar, profile, password change |
| **Security** | See the table below |
| **End-to-end (manual)** | The user stories US-1 to US-7 in a real browser, with the frontend |

**Key security tests:**

| Test | Expected result |
|---|---|
| User B reads, edits, or deletes User A's task | 404; nothing changes |
| Open a protected page or endpoint without logging in | Redirect (pages) or 401 (JSON) |
| POST without a CSRF token | Rejected |
| Title `'; DROP TABLE tasks; --` | Saved as plain text; tables still exist |
| Title `<script>alert(1)</script>` | Shown as text, never runs |
| Session older than 30 minutes of inactivity | Rejected; user must log in again |
| Register with a duplicate email (also in capitals) | Rejected with a message |
| Change password with a wrong current password | Rejected; hash unchanged |

**Acceptance checks from the SRS** (examples): the dashboard shows up to three incomplete tasks in deadline order, overdue included (US-2); category count equals all tasks in that category (US-4); a keyword shows only tasks whose title contains it, together with the filters (US-5).

**Definition of Done:** an endpoint is Done only when its tests pass, the results are recorded, and it does not break earlier features.

## **11. Build Order by Sprint**

| Sprint | Backend work |
|---|---|
| 1 (setup, authentication) | Project structure, `schema.sql`, database connection, register, login, logout, sessions, CSRF, `login_required`, authentication tests |
| 2 (tasks) | Task create, read, edit, delete, complete, validation, ownership tests |
| 3 (dashboard, organization) | Dashboard queries, category counts, category pages, search, filters, sorting |
| 4 (calendar, profile, final) | Calendar endpoints, profile update, password change, security review, bug fixes |

## **12. Assumptions and Open Items**

Everything below is **Proposed** and should be confirmed by the team.

| ID | Topic | Proposal |
|---|---|---|
| O-1 | API contract | The routes, fields, and codes in Section 6 are drafts. They are final only after all five research phases, then changed in any phase that needs it. A draft contract is in API_Contract_Agreement.md. |
| O-2 | Password rule | The SRS only says "valid input." Proposed: at least 8 characters. |
| O-3 | Email letter case (Phase 3, A7) | Lowercase every email before saving and before login. |
| O-4 | 404 or 403 for others' tasks | 404. The Phase 5 report names this case "Forbidden"; the frontend can show one general error for both. |
| O-5 | Category in the API | Send the category **name** (`Study`), not the id. The backend maps it to `category_id`. |
| O-6 | Login attempt limits | Not in the SRS, so not planned. Could be added later (brute-force protection). |
| O-7 | Account deletion (Phase 3, A8) | Out of scope for this version. |
| O-8 | CSRF library | `Flask-WTF` `CSRFProtect`. Confirm that adding one extra library is acceptable. |
| O-9 | Windows time zone data | Add `tzdata` to `requirements.txt` so Africa/Cairo works on Windows. |
