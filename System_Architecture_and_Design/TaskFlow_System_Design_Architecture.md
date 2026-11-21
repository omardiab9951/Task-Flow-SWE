# **TaskFlow — Phase 2: System Design & Architecture** 

## **1. System Architecture** 

I designed TaskFlow using a Three-Layer Architecture based on the Client-Server model, following SRS v1.2. 

|**Layer**|**Responsibility**|**Technology**|
|---|---|---|
|**Presentation**|User interface and interactions|HTML, CSS, JavaScript|
|**Application**|Business logic and request processing|Python Flask|
|**Data**|Data storage and retrieval|SQLite|



The browser and Flask server are two deployment tiers. SQLite runs on the same server, so a separate database server is not needed. This keeps the project simple and easy to maintain. See Diagram 01. 

## **2. System Components** 

The system consists of the following components: 

- Authentication and Session Management: registration, login, logout and session checks. 

- Task and Category Management: create, view, edit, delete and complete tasks, with filtering and sorting. 

- Dashboard and Calendar: show upcoming incomplete tasks, category counts and tasks by deadline date. 

- Profile Management: view and update account information and change passwords. 

- Database Access: read and save user-specific records. 

The Flask request boundary checks access and directs requests to the appropriate component. See Diagram 07. 

## **3. Component Communication** 

The frontend sends HTTP requests to Flask. Flask checks the session and validates input, passes the request to the appropriate component, accesses SQLite through the data layer, and returns data or an error to the frontend. 

Only the backend accesses SQLite. Each user can access only their own data. For example, a valid task request is saved and the updated list is returned; invalid input produces an error without saving. 

## **Page Delivery Approach (confirmed)** 

Proposal: Flask renders the main pages with templates. JavaScript calls a small set of JSON endpoints for dynamic actions: the task form or modal, mark complete, delete, and calendar data. 

Why: This is simplest for a beginner team because it needs less JavaScript than building every page in the browser, and the calendar and modals still work without full page reloads. 

Rejected: (a) a full JSON API where JavaScript builds every page (more work and more risk); (b) server-rendered pages with a full reload for every action (the calendar and modals would feel clumsy). 

Note: The final list of routes and JSON endpoints is the API contract, agreed after all five research phases. 

## **Security Measures** 

- A session cookie keeps the user logged in. It expires after 30 minutes of inactivity. Logout ends it immediately. 

- CSRF protection: every request that changes data must include a CSRF token. 

- Parameterized queries on every database access (prevents SQL injection). 

- Ownership check: every task request verifies the task belongs to the logged-in user. 

- Passwords are stored as hashes. Displayed output is escaped (prevents XSS). 

TaskFlow · Phase 2  |  1 

## **4. Application Workflow** 

Guests can register or log in. After login, users open the dashboard, which shows up to three nearest incomplete tasks, including overdue ones marked "Overdue", and the Study, Personal and Work category cards, which show the total number of tasks in that category (all statuses). Users can create, view, edit, delete and complete tasks; filter and sort lists; navigate the calendar; and manage their profile. 

Invalid login details show an error. Invalid task details keep the form open; cancellation saves nothing. Task deletion requires confirmation. Logout ends the session. Combined filters and basic account settings are secondary (Should); title search is required (Must). If priority or status is left empty, the defaults are Medium and Pending. A deadline is a date plus an optional time (default 23:59, Africa/Cairo). See Diagrams 02, 04, 05 and 06. 

## **5. System Diagrams** 

I prepared seven diagrams to explain the system structure and behavior: 

1. High-Level Architecture Diagram. 

2. Application Workflow Diagram. 

3. Use Case Diagram. 

4. Main Activity Diagram. 

5. Login Activity Diagram. 

6. Create Task Activity Diagram. 

7. Component Diagram. 

All diagrams are editable using Draw.io. 

## **6. Review and Team Feedback** 

The design follows SRS v1.2 and covers all 14 use cases in Diagram 03. It is a design proposal, not an implementation. 

I have completed the system design and architecture and am waiting for the team's feedback and confirmation of the proposed architecture and technologies. 

## **Open Decisions** 

- [x] Team confirms the page delivery approach 

- [ ] API contract agreed after all five research phases 

  Draft: API_Contract_Agreement.md (waiting for team sign-off)

- [x] Name of the fixed time zone (Africa/Cairo) 

- [ ] Diagrams 01, 02, 06, and 07 updated to match this report 

Decisions and reasons are recorded in Architecture_Decisions.md. 

TaskFlow · Phase 2  |  2 
