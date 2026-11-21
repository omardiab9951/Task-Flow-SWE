# TaskFlow API Contract Agreement

Status: Draft for team agreement. Not agreed until all five members sign in Section 12.

## 1. Header

| Item | Value |
|---|---|
| Project | TaskFlow – Task Management System |
| Document | API Contract Agreement |
| Version | 1.0 (draft) |
| Based on | SRS v1.2; Phases 2, 3, 4, and 5 |
| Status | Draft for team agreement. Not agreed until all five members sign in Section 12. |

## 2. Purpose and ownership

This is the shared agreement between the frontend and backend. Phase 4 owns the endpoints. Phase 5 owns how pages use them.

## 3. General rules

1. **R-1:** There are two route types: page routes (Flask returns HTML) and JSON endpoints (under `/api/`).
2. **R-2:** JSON uses UTF-8, snake_case field names, and `Content-Type: application/json`.
3. **R-3:** Login uses a session cookie. A session expires after 30 minutes of inactivity. Page routes redirect to `/login`; JSON endpoints return 401.
4. **R-4:** Every POST, PUT, and DELETE, including login, register, and logout, needs a CSRF token. Forms use a hidden field `csrf_token`. JavaScript sends `X-CSRFToken`, read from `<meta name="csrf-token">`. Logout is a small form button (POST), not a link.
5. **R-5:** The client sends `deadline_date` (`YYYY-MM-DD`) and optional `deadline_time` (`HH:MM`). The backend stores and returns `YYYY-MM-DD HH:MM` in Egypt time (`Africa/Cairo`). No time means 23:59. `created_at` is returned in the same format, converted to `Africa/Cairo`.
6. **R-6:** The backend uses the logged-in user's id from the session, never from the request. A task that does not exist or belongs to another user returns 404.
7. **R-7:** The API uses the category **name** (`Study`, `Personal`, `Work`), not the id.
8. **R-8:** “Overdue” is the boolean `is_overdue`, calculated by the backend. It is not a status.
9. **R-9:** After a successful create, edit, delete, or complete, the frontend refreshes the current page so server-rendered lists and counts stay correct.
10. **R-10:** There is no pagination and no API version number in this version.
11. **R-11:** The frontend checks input first; the backend always validates again.
12. **R-12:** Any member can ask to change this contract. The team decides by simple majority vote. The change is recorded in the change log (Section 12) and the affected reports are updated.

## 4. Data formats

### 4.1 Allowed values

| Field | Allowed values |
|---|---|
| `priority` | `Low`, `Medium`, `High` |
| `status` | `Pending`, `In Progress`, `Completed` |
| `category` | `Study`, `Personal`, `Work` |

### 4.2 Page form fields

| Form | Fields |
|---|---|
| Register | `name`, `email`, `password` |
| Login | `email`, `password` |
| Profile | `name`, `email` |
| Change password | `current_password`, `new_password` |

There is no Confirm Password field because it is not in the SRS. This changes if the team adds it.

### 4.3 Task request fields

| Field | Required | Limit or format | Default |
|---|---|---|---|
| `title` | Yes | Text, 1–100 characters | — |
| `category` | Yes | `Study`, `Personal`, or `Work` | — |
| `deadline_date` | Yes | `YYYY-MM-DD` | — |
| `deadline_time` | No | `HH:MM` | 23:59 |
| `description` | No | Text, up to 1000 characters | Empty |
| `priority` | No | `Low`, `Medium`, or `High` | `Medium` |
| `status` | No | `Pending`, `In Progress`, or `Completed` | `Pending` |

### 4.4 Returned task object

| Field | Meaning |
|---|---|
| `id` | Task id |
| `title` | Task title |
| `description` | Task description |
| `category` | Category name |
| `priority` | Priority value |
| `status` | Status value |
| `deadline` | `YYYY-MM-DD HH:MM` in `Africa/Cairo` |
| `created_at` | `YYYY-MM-DD HH:MM` in `Africa/Cairo` |
| `is_overdue` | Backend-calculated boolean |

### 4.5 Error object

```json
{"error": "...", "fields": {}}
```

`fields` is used for validation messages.

## 5. Page routes (Flask returns HTML)

| Method | Route | Form fields or query options | On success | On error |
|---|---|---|---|---|
| GET, POST | `/register` | `name`, `email`, `password`, `csrf_token` | Account created; go to Login | Show field messages |
| GET, POST | `/login` | `email`, `password`, `csrf_token` | Start session; go to Dashboard | Show generic login message |
| POST | `/logout` | `csrf_token` | End session; go to Login | Show CSRF message and reload |
| GET | `/dashboard` | — | Render dashboard | Redirect to Login if needed |
| GET | `/tasks` | `category`, `priority`, `status`, `q`, `sort=deadline_asc` or `deadline_desc` | Render matching tasks | Redirect to Login if needed |
| GET | `/category/<name>` | `priority`, `status`, `q`, `sort=deadline_asc` or `deadline_desc` | Render matching category tasks | Redirect to Login if needed |
| GET | `/calendar` | — | Render calendar page | Redirect to Login if needed |
| GET, POST | `/profile` | `name`, `email`, `csrf_token` | Render or update profile | Show field messages |
| POST | `/profile/password` | `current_password`, `new_password`, `csrf_token` | Change password | Show field messages |

`category` is available only on `/tasks`. The category name in `/category/<name>` is `study`, `personal`, or `work`.

## 6. JSON endpoints

| Method | Route | Request | Success response | Errors | Requirement ID |
|---|---|---|---|---|---|
| POST | `/api/tasks` | Task request fields; `X-CSRFToken` | 201, `{"task": {...}}` | 400, 401, 500 | FR-14–FR-16 |
| GET | `/api/tasks/<id>` | — | 200, `{"task": {...}}` | 401, 404, 500 | FR-18, FR-36 |
| PUT | `/api/tasks/<id>` | Task request fields; `X-CSRFToken` | 200, `{"task": {...}}` | 400, 401, 404, 500 | FR-18 |
| DELETE | `/api/tasks/<id>` | `X-CSRFToken` | 200, `{"deleted": true, "id": <id>}` | 400, 401, 404, 500 | FR-19 |
| POST | `/api/tasks/<id>/complete` | `X-CSRFToken` | 200, `{"task": {...}}` | 400, 401, 404, 500 | FR-20, BR-3 |
| GET | `/api/calendar?month=YYYY-MM` | `month` | 200, `{"tasks": [...]}` | 400, 401, 500 | FR-33, FR-34 |
| GET | `/api/calendar?date=YYYY-MM-DD` | `date` | 200, `{"tasks": [...]}` | 400, 401, 500 | FR-35 |

## 7. Status codes

| Code | Meaning | Frontend action |
|---|---|---|
| 200 | Successful read or change | Use the returned data; refresh after a task change |
| 201 | Task created | Refresh the current page |
| 400 | Validation or CSRF error | Show field messages for validation; show a short CSRF message and reload |
| 401 | Not logged in or session expired | Redirect to Login |
| 404 | Task not found or not owned | Show an error and do not display the data |
| 500 | Server error | Show a short message and let the user retry |

## 8. Responsibility matrix

| Page / action | Route | Frontend sends | Backend returns | Frontend handles |
|---|---|---|---|---|
| Login | `/login` | Form fields and CSRF token | Redirect to Dashboard or generic error | Invalid credentials, CSRF |
| Register | `/register` | Form fields and CSRF token | Redirect to Login or field messages | Validation, duplicate email, CSRF |
| Dashboard: view | `/dashboard` | — | Rendered tasks, counts, name | Redirect to Login |
| Dashboard: add / complete | `/api/tasks`; `/api/tasks/<id>/complete` | Task fields or CSRF header | Task object | 400, 401, 404, 500; refresh on success |
| All Tasks: view, filter, search, sort | `/tasks` | Query options | Rendered task list | Redirect to Login |
| All Tasks: create, edit, delete, complete | Task API routes | Task fields or CSRF header | Task or delete object | 400, 401, 404, 500; refresh on success |
| Category Tasks: view, filter, search, sort | `/category/<name>` | `priority`, `status`, `q`, `sort` | Rendered category task list | Redirect to Login |
| Category Tasks: create, edit, delete, complete | Task API routes | Task fields or CSRF header | Task or delete object | 400, 401, 404, 500; refresh on success |
| Calendar: page | `/calendar` | — | Rendered calendar page | Redirect to Login |
| Calendar: month / date / details | `/api/calendar`; `/api/tasks/<id>` | `month` or `date` | `{"tasks": [...]}` or task object | 400, 401, 404, 500 |
| Profile: view / update | `/profile` | Form fields and CSRF token | Rendered profile or field messages | Validation, duplicate email, CSRF |
| Profile: password | `/profile/password` | Password fields and CSRF token | Success or field messages | Validation, wrong current password, CSRF |
| Logout | `/logout` | CSRF token in a POST form | Redirect to Login | CSRF |

## 9. Traceability

| Requirement | Route that serves it |
|---|---|
| FR-1 | `/register` |
| FR-2 | `/register` |
| FR-3 | `/login` |
| FR-4 | `/login` |
| FR-5 | `/logout` |
| FR-6 | All protected page routes and JSON endpoints |
| FR-7 | All task routes and endpoints |
| FR-8 | `/dashboard` |
| FR-9 | `/dashboard` |
| FR-10 | `/dashboard` |
| FR-11 | `/category/<name>` |
| FR-12 | `POST /api/tasks` |
| FR-13 | `/tasks` |
| FR-14 | `POST /api/tasks` |
| FR-15 | `POST /api/tasks` (backend records it) |
| FR-16 | `POST /api/tasks` |
| FR-17 | `/tasks` |
| FR-18 | `GET` and `PUT /api/tasks/<id>` |
| FR-19 | `DELETE /api/tasks/<id>` |
| FR-20 | `POST /api/tasks/<id>/complete` |
| FR-21 | `POST` and `PUT /api/tasks` |
| FR-22 | `POST` and `PUT /api/tasks` |
| FR-23 | interface only |
| FR-24 | database only |
| FR-25 | database only |
| FR-26 | `/category/<name>` |
| FR-27 | `/tasks` and `/category/<name>` |
| FR-28 | `/tasks` and `/category/<name>` |
| FR-29 | `/tasks` |
| FR-30 | `/tasks` and `/category/<name>` |
| FR-31 | `/tasks` and `/category/<name>` |
| FR-32 | `/tasks` and `/category/<name>` |
| FR-33 | `/calendar`; `/api/calendar?month=YYYY-MM` |
| FR-34 | `/api/calendar?month=YYYY-MM` |
| FR-35 | `/api/calendar?date=YYYY-MM-DD` |
| FR-36 | `GET /api/tasks/<id>` |
| FR-37 | `/profile` |
| FR-38 | `/profile` |
| FR-39 | `/profile/password` |
| FR-40 | `/profile`, `/profile/password` |

## 10. Examples

Create task request:

```json
{
  "title": "Submit SE report",
  "category": "Study",
  "deadline_date": "2026-12-18",
  "deadline_time": "17:00",
  "description": "Submit through the university portal.",
  "priority": "High",
  "status": "Pending"
}
```

Create task response (201):

```json
{
  "task": {
    "id": 12,
    "title": "Submit SE report",
    "description": "Submit through the university portal.",
    "category": "Study",
    "priority": "High",
    "status": "Pending",
    "deadline": "2026-12-18 17:00",
    "created_at": "2026-11-21 10:30",
    "is_overdue": false
  }
}
```

Validation-error response (400):

```json
{
  "error": "Please correct the highlighted fields.",
  "fields": {
    "title": "Title is required",
    "deadline_date": "Deadline date is required"
  }
}
```

## 11. Open points

All items below are **Proposed**.

| ID | Topic | Proposal |
|---|---|---|
| O-2 | Password rule | At least 8 characters. |
| O-3 | Email letter case | Lowercase every email before saving and before login. |
| O-4 | Other user's task | Return 404, not 403. |
| O-5 | Category in the API | Send the category name, not the id. |
| O-6 | Login attempt limits | Not planned in this version; may be added later. |
| O-7 | Account deletion | Out of scope for this version. |
| O-8 | CSRF library | Use `Flask-WTF` `CSRFProtect`; confirm that one extra library is acceptable. |
| O-9 | Windows time zone data | Add `tzdata` to `requirements.txt` so `Africa/Cairo` works on Windows. |
| C-1 | Frontend ownership error wording | The Phase 5 report called this “Forbidden.” The contract follows the Phase 4 and SRS privacy rule: return 404 for not found or not owned. |
| C-2 | Category option on a category route | Phase 4 says `/category/<name>` has the same query options, while its detailed options table says `category` is only for `/tasks`. The contract uses the detailed rule: `category` is only for `/tasks`. |

## 12. Sign-off and change log

| Member | Role | Agreed | Date |
|---|---|---|---|
| Member 1 | Requirements | [ ] | |
| Member 2 | Architecture | [ ] | |
| Member 3 | Database | [ ] | |
| Member 4 | Backend | [ ] | |
| Member 5 | Frontend | [ ] | |

| Version | Date | Change |
|---|---|---|
| 1.0 | | Draft created from Phases 1-5 |
