# **TaskFlow** 

## **Simplified Software Requirements Specification** 

University Software Engineering Course Project 

Document version: 1.2 (updated from Version 1.1) Project team: Five students Prepared: 19 November 2026 

### **Contents** 

|1 Introduction and Project Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1|
|---|
|1.1 Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1|
|1.2 Project overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1|
|2 Project Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1|
|2.1 In scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1|
|2.2 Out of scope for this version . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1|
|3 Users and System Environment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1|
|3.1 Users . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1|
|3.2 Environment and constraints . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2|
|4 Functional Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2|
|4.1 Authentication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2|
|4.2 Dashboard . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2|
|4.3 Task management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2|
|4.4 Categories, filtering, and sorting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3|
|4.5 Calendar and profile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3|
|5 Non-Functional Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3|
|6 Main Use Cases and User Stories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4|
|6.1 Main use cases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4|
|6.2 Key flows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4|
|6.3 User stories and acceptance criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5|
|7 Database Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5|
|7.1 Main entities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5|
|7.2 Relationships . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5|
|8 Business Rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5|
|9 Main UI Pages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6|
|10 Risks and Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6|
|11 Next Steps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6<br>i|
|11.1 Simplification summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6|



TaskFlow – Simplified Software Requirements Specification 

TaskFlow Development Team 

### **1 Introduction and Project Overview** 

#### **1.1 Purpose** 

This Software Requirements Specification (SRS) describes what TaskFlow should do and the quality it should provide. It is a practical reference for the five-student team, project supervisor, and testers during design, development, and testing. 

#### **1.2 Project overview** 

TaskFlow is a web application for individuals who want to organize personal tasks, deadlines, and progress. A user creates a private account, manages tasks, and views them through a dashboard, lists, filters, and a calendar. 

The planned client-server stack is HTML, CSS, and JavaScript in the browser, a Python Flask backend, and an SQLite database. This document states requirements; it does not claim that any feature has been implemented. 

### **2 Project Scope** 

#### **2.1 In scope** 

- User registration, login, logout, and private account data. 

- Task creation, viewing, editing, deletion, priorities, statuses, deadlines, and completion. 

- The fixed categories Study, Personal, and Work. 

- Dashboard, task lists, category views, filtering and sorting, and calendar view. 

- Profile viewing and updating, password change, and basic account settings. 

#### **2.2 Out of scope for this version** 

Team collaboration or task sharing, user-created categories, file attachments, email or push notifications, recurring tasks, and a native mobile application are not included. 

### **3 Users and System Environment** 

#### **3.1 Users** 

|**User**|**Description**|**Access**|
|---|---|---|
|Registered|A student, employee, or other person managing their own tasks.|Private ac-|
|user||count|
|Guest|A visitor who has not logged in.|Login and|
|||Register<br>pages only|



There is no administrator role in this version. A user must not be able to view or change another user’s information or tasks. 

1 

TaskFlow – Simplified Software Requirements Specification 

TaskFlow Development Team 

#### **3.2 Environment and constraints** 

- The application targets current major browsers (Chrome, Firefox, Edge, and Safari) on desktop and mobile screen sizes. 

- The required stack is HTML, CSS, JavaScript, Python 3 with Flask, and SQLite. 

- Flask renders the main pages with templates and provides a small set of JSON endpoints for dynamic actions (confirmed in the Phase 2 architecture decision).

- Users are expected to have a modern browser and a connection to the application server. Each account has a unique email address. 

- A deadline is a date plus an optional time. If no time is entered, the deadline is the end of that day (23:59). All deadlines use one fixed time zone, Egypt local time (Africa/Cairo), with no per-user time zones. A calendar library such as FullCalendar may be used, but no library is required by this SRS. 

- The three categories are fixed. SQLite is intended for the light, low-concurrency use of this academic project. 

### **4 Functional Requirements** 

Priority meanings: **Must** is required for this version; **Should** is useful but secondary; **Could** is optional if time allows. The priorities below are retained from the original SRS, except FR-32 (search), which was raised from Could to Must in Version 1.2. 

#### **4.1 Authentication** 

|**ID**|**Requirement**|**Priority**|
|---|---|---|
|FR-1|A new user can register with a name, email, andpassword.|Must|
|FR-2|Registration is rejected when the email is alreadyused or the input is invalid.|Must|
|FR-3|A registered user can login with email andpassword.|Must|
|FR-4|The system shows an error for invalid login credentials.|Must|
|FR-5|A logged-in user can logout and end the session.|Must|
|FR-6|Every page except Login and Register requires authentication.|Must|
|FR-7|Each user can access onlytheir own tasks and data.|Must|



#### **4.2 Dashboard** 

|**ID**|**Requirement**|**Priority**|
|---|---|---|
|FR-8|Show up to three incomplete tasks with the earliest deadlines, ordered by earliest deadline. Overdue incomplete tasks are included and marked Overdue. If there are none, show a short 'No upcoming tasks' message.|Must|
|FR-9|Show one categorycard for each of Study, Personal, and Work.|Must|
|FR-10|Show the total number of tasks (all statuses) in each category card.|Must|
|FR-11|Selectinga categorycard opens that category’s task list.|Must|
|FR-12|Provide an Add New Task button that opens the task form.|Must|
|FR-13|Provide a Show All Tasks button that opens the All Taskspage.|Must|



#### **4.3 Task management** 

|**ID**|**Requirement**|**Priority**|
|---|---|---|
|FR-14|Create a task with title, description, category,priority, status, and deadline. If priority or status is not chosen, use Medium and Pending.|Must|
|FR-15|Record each task’s creation date automatically.|Must|
|FR-16|Require a title, category, and deadline when creatinga task. The date is required; the time is optional.|Must|
|FR-17|Allow a user to view all of their own tasks.|Must|



2 

TaskFlow – Simplified Software Requirements Specification 

TaskFlow Development Team 

|**ID**|**Requirement**|**Priority**|
|---|---|---|
|FR-18|Allow a user to edit anyfield of their existingtask.|Must|
|FR-19|Allow a user to delete a task after a confirmationprompt.|Must|
|FR-20|Allow a user to mark a task as completed.|Must|
|FR-21|Support Low, Medium, and Highprioritylevels.|Must|
|FR-22|Support Pending, In Progress, and Completed statuses.|Must|
|FR-23|Use a reusable form or modal for creatingand editingtasks.|Should|



#### **4.4 Categories, filtering, and sorting** 

|**ID**|**Requirement**|**Priority**|
|---|---|---|
|FR-24|Provide exactlythree fixed categories: Study, Personal, and Work.|Must|
|FR-25|Assign each task to exactlyone category.|Must|
|FR-26|Show onlythe selected category’s tasks on its CategoryTaskspage.|Must|
|FR-27|Filter tasks by priority.|Must|
|FR-28|Filter tasks bystatus.|Must|
|FR-29|Filter tasks bycategory.|Must|
|FR-30|Sort tasks bydeadline, earliest first or latest first.|Must|
|FR-31|Allow multiple filters to be combined.|Should|
|FR-32|Allow searching tasks by a keyword in the title. Search works together with the filters.|Must|



#### **4.5 Calendar and profile** 

|**ID**|**Requirement**|**Priority**|
|---|---|---|
|FR-33|Displaytasks on their deadline dates in the calendar.|Must|
|FR-34|Allow navigation between calendar months.|Must|
|FR-35|Allow a user to select a date and view its scheduled tasks.|Must|
|FR-36|Allow a user to open task details from the calendar.|Must|
|FR-37|Allow a user to view theirpersonal information.|Must|
|FR-38|Allow a user to update their name and email. The email must stay unique (BR-6).|Must|
|FR-39|Allow a user to change their password after providing the current password and|Must|
||a new one.||
|FR-40|In this version, account settings means only: name, email, and password change. No other settings are included.|Should|



### **5 Non-Functional Requirements** 

Non-functional requirements describe how well and how safely the system should work. 

|**ID**|**Quality**|**Requirement**|
|---|---|---|
|NFR-1|Security|Storepasswords as secure hashes, never asplain text.|
|NFR-2|Security|Manage sessions securelyand require login forprotectedpages.|
|NFR-3|Security|Use parameterized database queries to help prevent SQL injection, and|
|||escape displayed output to help prevent cross-site scripting(XSS).|



3 

TaskFlow – Simplified Software Requirements Specification 

TaskFlow Development Team 

|**ID**|**Quality**|**Requirement**|
|---|---|---|
|NFR-4|Performance|Pages should load in under 2 seconds under normal use.|
|NFR-5|Usability|Keep the interface simple and consistent; a new user should be able to<br>create a task within one minute without training.|
|NFR-6|Compatibility|Use a responsive interface that works on desktop and mobile screens and<br>current major browsers.|
|NFR-7|Reliability|Keep user data between sessions and handle invalid input without crash-<br>ing.|
|NFR-8|Maintainability|Separate routes, models, and presentation files; document the code.|
|NFR-9|Portability|Run with minimal setup using Python and SQLite, without a separate<br>database server.|
|NFR-10|Data integrity|Validate input on both the client and server.|
|NFR-11|Security|Protect every request that changes data (create, edit, delete, profile, password, login) with a CSRF token or an equivalent protection.|
|NFR-12|Security|A session expires after 30 minutes of inactivity. The user must then log in again. Logout ends the session immediately.|



### **6 Main Use Cases and User Stories** 

#### **6.1 Main use cases** 

|**ID**|**Use case**|**Actor and briefpurpose**|
|---|---|---|
|UC-1|Register|Guest creates an account.|
|UC-2|Login|Guest enters valid credentials to start a session.|
|UC-3|Logout|User ends the session.|
|UC-4|View dashboard|User sees upcomingtasks and categorycards.|
|UC-5|Create task|User enters task details; the system validates and saves the task under<br>that user.|
|UC-6|View all tasks|User views their task list.|
|UC-7|Edit task|User updates an existingtask theyown.|
|UC-8|Delete task|User confirms deletion of a task theyown.|
|UC-9|Mark task complete|User changes a task’s status to Completed.|
|UC-10|View categorytasks|User opens one categoryand sees onlyits tasks.|
|UC-11|Search, filter, and sort|User narrows or orders their task list.|
|UC-12|View calendar|User navigates months, selects a date, and opens a task.|
|UC-13|View/updateprofile|User views or updatespersonal information.|
|UC-14|Changepassword|User supplies the currentpassword and a newpassword.|



#### **6.2 Key flows** 

**Create a task (UC-5):** The logged-in user selects Add New Task, enters the task details, and submits the form. The system validates the input, saves the task with its creation date and user association, and updates the list. If validation fails, the form stays open with errors; if the user cancels, nothing is saved. **Log in (UC-2):** A guest enters an email and password. If they are valid, the system starts a session and opens the dashboard. If they are invalid, the system shows an error and stays on the Login page. 

4 

TaskFlow – Simplified Software Requirements Specification 

TaskFlow Development Team 

#### **6.3 User stories and acceptance criteria** 

|**ID**|**User story**|**Acceptance check**|
|---|---|---|
|US-1|As a new user, I want to register so that I have<br>aprivate account.|Valid details create an account; a duplicate<br>email is rejected with a message.|
|US-2|As a user, I want to see my nearest deadlines<br>so I know what to do first.|The dashboard shows up to three nearest<br>incomplete tasks in deadline order, including overdue ones.|
|US-3|As a user, I want to add tasks quickly so I do<br>not forget them.|A task with required fields is saved and ap-<br>pears in the user’s lists.|
|US-4|As a user, I want to group tasks by category so<br>I can focus on one area.|The selected category shows only its tasks and<br>the dashboard count matches (count = all tasks in that category).|
|US-5|As a user, I want to filter tasks by priority and<br>status.|The list contains only tasks matching the se-<br>lected filters. Searching a keyword shows only tasks whose title contains it.|
|US-6|As a user, I want to see tasks on a calendar to<br>understand mymonthlyworkload.|Tasks appear on deadline dates; selecting a<br>date shows its tasks.|
|US-7|As a user, I want to change my password to<br>keepmyaccount secure.|The password changes only when the current<br>password is correct.|



### **7 Database Requirements** 

#### **7.1 Main entities** 

|**Entity**|**Main data**|
|---|---|
|User|id, name, unique email,password_hash, created_at|
|Category|id, name (Study, Personal, or Work)|
|Task|id, user_id, category_id, title, description,priority, status, deadline, created_at|



#### **7.2 Relationships** 

- One User can have many Tasks (one-to-many). 

- One Category can have many Tasks (one-to-many). 

- Each Task belongs to exactly one User and one Category. `user_id` and `category_id` link the task to those records. 

### **8 Business Rules** 

- **BR-1:** Priority must be Low, Medium, or High. 

- **BR-2:** Status must be Pending, In Progress, or Completed. 

- **BR-3:** Marking a task complete sets its status to Completed. 

- **BR-4:** Completed tasks do not appear among the dashboard’s upcoming tasks. 

- **BR-5:** A user can never view or modify another user’s tasks. 

- **BR-6:** Email addresses must be unique. 

5 

TaskFlow – Simplified Software Requirements Specification 

TaskFlow Development Team 

### **9 Main UI Pages** 

The application has seven pages: Login, Register, Dashboard, All Tasks, Category Tasks, Calendar, and Profile. A common navigation bar links to Dashboard, All Tasks, Calendar, and Profile, and provides Logout. Task creation and editing use a reusable form or modal. Wireframes should be prepared during design. 

### **10 Risks and Limitations** 

|**Risk or limit**|**Possible effect**|**Response**|
|---|---|---|
|Changing or un-|Rework and delays.|Review this SRS with the supervisor be-|
|clear<br>require-||fore design and agree on the scope.|
|ments|||
|Short<br>project|Some features may not be completed.|Build Must requirements first, then|
|schedule||Should, then Could.|
|Security<br>mis-|Private account data may be exposed.|Use password hashing, validation, para-|
|takes||meterizedqueries, and securitytesting.|
|Limited<br>Flask|Slower development.|Learn early and use pair programming|
|experience||where useful.|
|SQLite<br>concur-<br>rencylimits|Performance may suffer with heavy si-<br>multaneous use.|Acceptable for the expected project scale;<br>document the limitation.|



### **11 Next Steps** 

1. Review and approve this SRS with the project supervisor. 

2. Draw a use case diagram from the listed actors and use cases. 

3. Design the entity-relationship diagram (ERD) from the database requirements. 

4. Create wireframes for the seven pages. 

5. Write a test plan using the acceptance criteria and functional requirements. 

6. Plan implementation by priority: Must first, then Should, then Could, subject to team time. 

#### **11.1 Simplification summary** 

Compared with Version 1.0, this version removes repeated explanations, shortens requirement wording, groups requirements into readable tables, and condenses use-case and risk descriptions. It retains the original TaskFlow idea, the fixed categories, the technology stack, and the scope exclusions. Priorities are unchanged except FR-32 (search), now Must. Version 1.2 adds NFR-11 (CSRF) and NFR-12 (session expiry) and clarifies existing requirements. No new user-facing features are introduced, and no implementation is claimed. 

Version 1.2: clarified deadline, dashboard, category count, search (now Must), account settings, CSRF, session expiry, and defaults. Page-delivery approach and time zone confirmed in the Phase 2 architecture decision.

6 
