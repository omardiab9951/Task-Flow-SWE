# TaskFlow - Architecture Decisions

I chose a three-layer client-server design to keep presentation, application logic and data access separate. HTML, CSS, JavaScript, Python Flask and SQLite follow SRS v1.2. SQLite runs on the Flask host, avoiding the need for a separate database server.

I defined the main system components and their communication in Diagrams 01 and 07. I am waiting for the team to confirm the proposed architecture and technologies before implementation.

## Decision Log

| ID | Decision | Status | Why | Rejected alternatives |
| --- | --- | --- | --- | --- |
| AD-1 | Three-layer client-server design (presentation, application, data). | Proposed | Keeps UI, logic, and data separate. | One mixed layer (hard to maintain and test). |
| AD-2 | Flask + SQLite on the Flask host. | Proposed | Matches SRS v1.2 and needs no separate database server. | MySQL or PostgreSQL (extra setup, against NFR-9). |
| AD-3 | Flask renders the main pages with templates, plus a small set of JSON endpoints for dynamic actions. | Confirmed | Simplest for a beginner team. | A full JSON API where JavaScript builds every page; full page reloads for every action. |
| AD-4 | Session-cookie login, expiring after 30 minutes of inactivity. | Proposed | Built into Flask and simple. | Token-based login (more complex). |
| AD-5 | CSRF token on every request that changes data. | Proposed | Needed because login uses a session cookie. | — |
| AD-6 | Parameterized queries, ownership check on every task request, hashed passwords. | Proposed | Protect private data. | — |
| AD-7 | Defaults Medium and Pending; deadline is a date plus an optional time; one fixed time zone. Time zone: Africa/Cairo (Egypt). | Proposed | Follows SRS v1.2. | — |

## Open Questions

- Resolved: Does the team confirm AD-3? Yes. Flask renders the main pages with templates, plus a small set of JSON endpoints for dynamic actions.
- API contract: agreed after all five research phases.
- Resolved: Which fixed time zone? Africa/Cairo (Egypt local time, including daylight saving).
- Diagrams 01, 02, 06, and 07 still need updating.
