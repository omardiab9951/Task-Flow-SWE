TaskFlow – Database Design 

# **TaskFlow** 

## Database Design 

|**Item**|**Detail**|
|---|---|
|Project|TaskFlow – Task Management System (University Software Engineering Course Project)|
|Phase|Phase 3 – Database Design|
|Based on|SRS v1.2 §7 and §4–§8; System Design & Architecture (Phase 2); TaskFlow Idea; Architecture<br>Decisions; Master Progress Report v1.2|
|Date|20 November 2026|
|Status|Proposed design for team review and agreement. No implementation is claimed.|



### **1. Database Overview** 

TaskFlow lets each registered user manage a private list of tasks with deadlines, priorities, statuses and one of three fixed categories (SRS §1.2). The database stores everything the application must keep between sessions (NFR-7): user accounts, the three fixed categories, and each user’s tasks. 

The SRS (§3.2, NFR-9) and the System Design (Data layer) specify **SQLite** , running on the same host as the Flask backend. Only the backend accesses the database (System Design §3), so no separate database server is needed. The design contains **three tables** : users, categories and tasks. These are exactly the three entities listed in SRS §7.1. No other table is required by any documented requirement. 

### **2. Requirements That Shape the Design** 

|**Requirement**|**Effect on the database**|
|---|---|
|FR-1 to FR-5, NFR-1, BR-6|usersstores name, unique email andpassword_hash(never the plain password). Login<br>state is held in the session, not in extra tables (see Section 9).|
|FR-7, BR-5|Every task carriesuser_id, so every query can be limited to the logged-in user’s own tasks.|
|FR-14, FR-16, FR-21, FR-22,<br>BR-1, BR-2|tasksholds title, description, category, priority, status and deadline. Required fields are<br>NOT NULL; priority and status accept only the allowed values.|
|FR-15|created_atis filled automatically when a row is inserted.|
|FR-24, FR-25|categoriesholds exactly Study, Personal and Work.tasks.category_idholds one value, so<br>each task has exactly one category.|
|FR-32|Search is a query on tasks.title combined with the filters. No new table, column, or index is<br>needed.|
|FR-8 to FR-10, FR-26 to FR-30,<br>FR-33 to FR-36, BR-3, BR-4|No extra tables. The dashboard, category counts, filters, sorting and calendar are queries<br>overtasks(deadline, status, priority, category_id).|
|FR-37 to FR-39|Name and email are updated inusers;password_hashis replaced after the current<br>password is verified.|
|NFR-9, NFR-10|SQLite needs no database server. Database constraints add a second layer of validation<br>behind the client and server checks.|



Page 1 of 7 

TaskFlow – Database Design 

### **3. Entities, Relationships and ERD** 

#### **3.1 Entities** 

|**Table**<br>|**Represents**<br>~~ee~~|**Why it needs its own table**<br>~~e~~|
|---|---|---|
|users<br>|A registered person with a private account.<br>|Account data is stored once per person and is<br>separate from the many tasks each person owns.<br>|
|categories|The fixed categories Study, Personal and<br>Work.|SRS §7.1 lists Category as an entity; each name is<br>stored once and tasks refer to it.|
|tasks|One task belonging to one user and one<br>category.|It is the main data of the system: title, description,<br>priority, status, deadline and creation date.|



#### **3.2 Relationships** 

|**Relationship**<br>~~a~~|**Cardinality**<br>|**Implemented by**<br>|**Meaning**<br>~~e~~|
|---|---|---|---|
|users→tasks<br>|1 : M<br>|tasks.user_id→users.id<br>|One user has many tasks (possibly<br>none yet). Each task belongs to exactly<br>one user. (SRS §7.2)<br>|
|categories→tasks|1 : M|tasks.category_id→<br>categories.id|One category has many tasks. Each task<br>belongs to exactly one category. (SRS<br>§7.2)|



There is no direct relationship between users and categories: the categories are shared and fixed, and a user’s tasks in a category are found through tasks. No M:N relationship and no junction table exists in this design. 

#### **3.3 Entity Relationship Diagram** 



<!-- Start of picture text -->
users<br>PK id INTEGER a<br>name TEXT tasks<br>UQ email TEXT PK id INTEGER<br>password_hash TEXT aim) FK user_id INTEGER<br>created_at TEXT Od FK category_id INTEGER<br>J title TEXT<br>classifies } description TEXT<br>(2M) 1 priority TEXT<br>categories status TEXT<br>PK id INTEGER deadline = TEXT<br>UQ name TEXT created_at TEXT<br><!-- End of picture text -->

**Figure 1 – TaskFlow ERD.** PK = primary key, FK = foreign key, UQ = unique. At the users/categories end of a line, the double bar means “exactly one”. At the tasks end, the crow’s foot with a circle means “zero or many”. 

Page 2 of 7 

TaskFlow – Database Design 

### **4. Data Dictionary** 

SQLite has no separate date type, so dates and timestamps are stored as ISO-8601 TEXT, which sorts correctly by date. Table names are plural; the SRS entity names (User, Category, Task) map to them one to one. 

Deadlines are stored as 'YYYY-MM-DD HH:MM' text in Egypt local time (Africa/Cairo). If the user enters only a date, the backend stores 23:59. Always use this one format so sorting stays correct. 

#### **4.1 users** 

|**Column**|**Type**|**Key**|**Constraints / default**|**Purpose**|**Source**|
|---|---|---|---|---|---|
|id|INTEGER|PK|Auto-generated|Unique identifier of the user.|SRS §7.1|
|name|TEXT||NOT NULL|Name entered at registration;<br>editable in Profile.|FR-1, FR-38|
|email|TEXT|UQ|NOT NULL, UNIQUE|Login identifier; no two accounts<br>share an email.|FR-1 to FR-3,<br>BR-6|
|password_hash|TEXT||NOT NULL|Secure hash of the password; the<br>plain password is never stored.|NFR-1, FR-39|
|created_at|TEXT||NOT NULL, default current<br>timestamp|When the account was created.|SRS §7.1|



#### **4.2 categories** 

|**Column**|**Type**|**Key**|**Constraints / default**|**Purpose**|**Source**|
|---|---|---|---|---|---|
|id|INTEGER|PK|Auto-generated|Unique identifier of the category.|SRS §7.1|
|name|TEXT|UQ|NOT NULL, UNIQUE, only<br>‘Study’, ‘Personal’ or ‘Work’|Category name. The three rows<br>are inserted once when the<br>database is created.|FR-24, SRS<br>§7.1|



#### **4.3 tasks** 

|**Column**|**Type**|**Key**|**Constraints / default**|**Purpose**|**Source**|
|---|---|---|---|---|---|
|id|INTEGER|PK|Auto-generated|Unique identifier of the task.|SRS §7.1|
|user_id|INTEGER|FK|NOT NULL, →users.id|The owner of the task.|FR-7, BR-5|
|category_id|INTEGER|FK|NOT NULL, →categories.id|The task’s single category.|FR-16, FR-25|
|title|TEXT||NOT NULL|Short name of the task.|FR-14, FR-16|
|description|TEXT||Optional (may be empty)|Extra details about the task.|FR-14|
|priority|TEXT||NOT NULL, default<br>‘Medium’, only Low /<br>Medium / High|How important the task is.|FR-21, BR-1|
|status|TEXT||NOT NULL, default<br>‘Pending’, only Pending / In<br>Progress / Completed|Progress of the task; ‘Completed’<br>marks it done.|FR-22, BR-2,<br>BR-3|
|deadline|TEXT||NOT NULL|Due date and optional time<br>(default 23:59, Africa/Cairo), used<br>for sorting, the dashboard, and<br>the calendar.|FR-16, FR-30,<br>FR-33|



Page 3 of 7 

TaskFlow – Database Design 

|**Column**|**Type**|**Key**|**Constraints / default**|**Purpose**|**Source**|
|---|---|---|---|---|---|
|created_at|TEXT||NOT NULL, default current<br>i|Creation date, recorded<br>i|FR-15|
||||timestamp|automatically.||



'Overdue' is not stored. A task is overdue when it is not completed and its deadline is earlier than the current Egypt time. The backend calculates it. created_at uses SQLite CURRENT_TIMESTAMP, which is UTC. 

The defaults 'Medium' and 'Pending' are defined in SRS v1.2 (FR-14). 

### **5. Constraints and Business Rules** 

|**Rule**|**How the database supports it**|**Constraint / location**|
|---|---|---|
|BR-1|Priority accepts only Low, Medium or High.|CHECK ontasks.priority|
|BR-2|Status accepts only Pending, In Progress or<br>Completed.|CHECK ontasks.status|
|BR-3|Completing a task is an update of its status to<br>‘Completed’. No separate flag is stored.|Backend UPDATE oftasks.status|
|BR-4|The dashboard leaves out completed tasks.|Query filter: status <> ‘Completed’|
|BR-5, FR-7|Each task has an owner; the backend adds the<br>owner to every query. SQLite has no row-level<br>security, so this check is made by the backend.|tasks.user_id+ backend queries|
|BR-6|Emails cannot repeat.|UNIQUE onusers.email|
|FR-16|A task cannot be saved without title, category<br>and deadline.|NOT NULL on the three columns|
|FR-24, FR-25|Only three categories exist; each task has exactly<br>one.|CHECK + UNIQUE oncategories.name; NOT<br>NULL FKcategory_id|
|FR-15|Creation date is automatic.|DEFAULT current timestamp|
|Valid links|A task cannot point to a missing user or category.|FOREIGN KEY constraints;PRAGMA<br>foreign_keys = ONon every connection|



### **6. Normalization** 

The design is in **Third Normal Form (3NF)** : 

- **1NF:** every column holds one simple value, and every table has a primary key. 

- **2NF:** every primary key is a single column, so no column can depend on only part of a key. 

- **3NF:** no non-key column depends on another non-key column. The category name is stored once in categories and user details once in users; tasks stores only the ids that point to them. 

Values that can be calculated are not stored: the category task counts and the three upcoming tasks on the dashboard come from queries over tasks. 

### **7. Main Data Operations** 

All operations use parameterized queries (NFR-3), and every operation on tasks is limited to the logged-in user’s user_id. 

Page 4 of 7 

TaskFlow – Database Design 

|**Use case**|**Database operation**|**Tables**|
|---|---|---|
|UC-1 Register|INSERT a user (the UNIQUE constraint rejects a duplicate email).|users|
|UC-2 Log in|SELECT the user by email; compare the entered password with<br>password_hash.|users|
|UC-3 Log out|No database operation; the session ends.|–|
|UC-4 Dashboard|SELECT the user's non-completed tasks (overdue ones included)<br>ordered by deadline, first 3; COUNT all tasks per category<br>regardless of status.|tasks,categories|
|UC-5 Create task|INSERT a task with the session user’s id;created_atis automatic.|tasks|
|UC-6 View all tasks|SELECT all tasks of the user.|tasks|
|UC-7 Edit task|UPDATE the task WHERE id and user_id match.|tasks|
|UC-8 Delete task|DELETE the task WHERE id and user_id match (after confirmation).|tasks|
|UC-9 Mark complete|UPDATEstatusto ‘Completed’.|tasks|
|UC-10 Category<br>tasks|SELECT the user’s tasks WHERE category_id matches.|tasks|
|UC-11 Search, filter,<br>and sort|SELECT with an optional title keyword (title LIKE ? using a<br>parameter such as %keyword%) and optional priority / status /<br>category conditions, ORDER BY deadline ascending or descending.|tasks|
|UC-12 Calendar|SELECT the user’s tasks whose deadline falls in the chosen month<br>or date.|tasks|
|UC-13 Profile|SELECT and UPDATE name and email.|users|
|UC-14 Change<br>password|Verify the current password againstpassword_hash, then<br>UPDATEpassword_hash.|users|



### **8. SQL Schema (SQLite)** 

SQLite is the documented DBMS, so the schema is given in SQLite syntax. This script was run successfully and its constraints were tested: invalid priority or status, a duplicate email, a fourth category, a missing deadline and a task pointing to a missing user were all rejected. 

<mark>-- TaskFlow database schema (SQLite) -- Run PRAGMA foreign_keys = ON; on every connection (SQLite does not enforce FKs by default).</mark> 

<mark>CREATE TABLE users ( id             INTEGER PRIMARY KEY AUTOINCREMENT, name           TEXT    NOT NULL, email          TEXT    NOT NULL UNIQUE, password_hash  TEXT    NOT NULL, created_at     TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP ); CREATE TABLE categories ( id             INTEGER PRIMARY KEY AUTOINCREMENT, name           TEXT    NOT NULL UNIQUE CHECK (name IN ('Study', 'Personal', 'Work')) ); CREATE TABLE tasks (</mark> 

Page 5 of 7 

TaskFlow – Database Design 

<mark>id             INTEGER PRIMARY KEY AUTOINCREMENT, user_id        INTEGER NOT NULL, category_id    INTEGER NOT NULL, title          TEXT    NOT NULL, description    TEXT, priority       TEXT    NOT NULL DEFAULT 'Medium' CHECK (priority IN ('Low', 'Medium', 'High')), status         TEXT    NOT NULL DEFAULT 'Pending' CHECK (status IN ('Pending', 'In Progress', 'Completed')), deadline       TEXT    NOT NULL, created_at     TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (user_id)     REFERENCES users (id), FOREIGN KEY (category_id) REFERENCES categories (id) ); -- The three f</mark> i <mark>xed categories (FR-24) INSERT INTO categories (name) VALUES ('Study'), ('Personal'), ('Work');</mark> 

### **9. Design Decisions** 

- **Three tables only.** SRS §7.1 lists three entities and no requirement needs more. 

- **Categories as a table.** The SRS names Category as an entity. Tasks refer to it by category_id, and the three fixed names are stored once. 

- **Priority and status as CHECK constraints.** Each has three fixed values (BR-1, BR-2). The SRS lists no priority or status entity, so lookup tables are not added. 

- **No sessions table.** The architecture describes a session cookie but no session storage in the database. How sessions are managed is a backend decision (Phase 4). 

- **No extra indexes.** Only the indexes that SQLite creates for primary keys and UNIQUE columns are used. The SRS expects light, low-concurrency use (§3.2, §10); indexes can be added later if testing shows a need. 

- **Search needs no schema change. Title search uses a parameterized LIKE query; no extra index is added (FR-32).** 

- **Session expiry (NFR-12) and CSRF protection (NFR-11) are backend work. No database change is needed.** 

### **10. Assumptions and Open Items** 

A1-A6 were resolved by SRS v1.2 and team decisions. A7-A8 remain open and the team should confirm them. 

|**ID**|**Topic**|**What the documents say**|**Design choice and impact**|
|---|---|---|---|
|A1|DBMS approval|SRS §3.2 requires SQLite. The Progress<br>Report says formal approval of the stack is<br>not specified, and Architecture Decisions<br>says the team has not yet confirmed it.|Resolved: SRS v1.2 requires SQLite and<br>the team confirmed the Flask approach.<br>Formal confirmation of AD-2 is still<br>pending in Architecture_Decisions.md.|
|A2|Categories: shared or per<br>user|TaskFlow Idea says each user has private<br>“tasks and categories”. SRS v1.2 says the<br>three categories are fixed and user-<br>created categories are out of scope.|Resolved: Fixed, shared categories<br>(FR-24). No user_id on categories. No<br>schema change.|
|A3|Deadline: date or date<br>and time|The SRS says “deadline” and “deadline<br>dates”, uses one time zone, and does not<br>say whether a time of day is needed.|Resolved: Date required, time<br>optional (default 23:59), Africa/Cairo.<br>Stored as 'YYYY-MM-DD HH:MM' text.<br>No schema change.|



Page 6 of 7 

TaskFlow – Database Design 

|**ID**|**Topic**|**What the documents say**|**Design choice and impact**|
|---|---|---|---|
|A4|Default priority and<br>status|Only title, category and deadline are<br>required (FR-16). Priority and status are<br>optional on the form (Diagram 06), and no<br>defaults are stated.|Resolved: Defaults Medium and Pending<br>are in FR-14. No schema change.|
|A5|Personal information and<br>account settings|FR-38 and FR-40 do not list the fields. SRS<br>§7.1 givesusersonly name, email,<br>password_hash and created_at.|Resolved: Only name, email, and<br>password change (FR-38, FR-40). No extra<br>columns.|
|A6|Dashboard category<br>count|FR-10 does not say whether completed<br>tasks are counted.|Resolved: FR-10 counts all statuses. No<br>schema change.|
|A7|Email letter case|BR-6 requires unique emails; it does not<br>say whether “A@x.com” and “a@x.com”<br>are the same.|No schema impact. The backend can<br>convert emails to lowercase before<br>saving.|
|A8|Account deletion|Not in the requirements. Task deletion is a<br>normal delete (FR-19).|No cascading delete and no “deleted” flag<br>are added.|



Page 7 of 7 

