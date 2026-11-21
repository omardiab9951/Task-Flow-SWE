# **TaskFlow: Phase 5, Frontend Development Planning** 

**Date:** 20 November 2026 | **Scope:** Planning only, no implementation **Prepared by:** Omar Nasr 

## **1. Purpose and Scope** 

This report plans the TaskFlow user interface: how users move through the system, what each page shows, and how each page uses the backend. It follows SRS v1.2 and the Phase 2 architecture. 

**Scope boundaries:** 

- Detailed API endpoints and request/response fields belong to the Phase 4 backend plan. 

- This report only states what each page needs from the API and how it displays the result. 

- Overall architecture belongs to the Phase 2 design. 

## **2. Frontend Approach** 

- **Technologies:** HTML, CSS, and JavaScript. Flask renders the main pages with templates, and JavaScript calls a small set of JSON endpoints for dynamic actions (task form or modal, mark complete, delete, calendar data). 

- **Design goals** (from the SRS): a simple interface, a task created in under a minute, pages loading in under 2 seconds, and a responsive layout for desktop and mobile. 

- **Structure:** one shared layout (top navigation bar) reused by all private pages, so the interface stays consistent and easy to maintain. 

- **Styling:** every page uses the same color system (Section 3) and shared styling (Section 4). Design templates are shown in Section 10. 

## **3. Color System** 

The design uses a "Fresh Indigo" style: a light, slightly tinted background, white cards, and one strong indigo accent. 

### **3.1 Core Palette** 

|Use|Color name|Code|
|---|---|---|
|Page background|Pale lavender white|`#F8F9FF`|
|Cards, forms, top bar|White|`#FFFFFF`|
|Headings and main text|Deep indigo-navy|`#1E1B4B`|
|Secondary text|Slate|`#64748B`|
|Buttons, links, active tab|Indigo|`#4F46E5`|
|Hover and selected fill|Indigo tint (very light indigo)|`#EEF2FF`|
|Borders and dividers|Light gray|`#E5E7EB`|



### **3.2 Category Colors** 

Used only on category icons. 

|Category|Color name|Code|
|---|---|---|
|Study|Teal|`#0D9488`|
|Personal|Sky blue|`#0284C7`|
|Work|Dark slate|`#475569`|



### **3.3 Priority Colors** 

Soft pills, used only on priority badges. 

|Priority|Text|Fill|
|---|---|---|
|High|Rose red `#BE123C`|Light rose `#FFE4E6`|
|Medium|Amber brown `#B45309`|Light amber `#FEF3C7`|
|Low|Emerald green `#047857`|Light mint `#D1FAE5`|



### **3.4 Color Rules** 

- Each color has one meaning: indigo for actions, category colors for icons only, red/amber/green for priority only. 

- All text keeps strong contrast (at least 4.5:1). Secondary text is never lighter than slate <mark>`#64748B` .</mark> 

## **4. Shared Styling** 

These rules apply to every page. 

|Element|Shared style|
|---|---|
|Font|Inter, with a sans-serif fallback|
|Cards|White, 12px rounded corners, soft shadow|
|Buttons|Primary: solid indigo with white text. Secondary: outlined|
|Priority badge|Filled soft pill (colors in Section 3.3)|
|Status badge|Small_outlined_badge (Pending, In Progress, Completed), so it is<br>not confused with the_filled_priority badge|
|Category icon|Colored icon (colors in Section 3.2)|
|Top navigation bar|White bar reused by all private pages; the active tab uses<br>indigo|
|Overdue label|Small text label "Overdue" shown on overdue incomplete tasks. It is a label, not a status. Its color is still to be decided by the team.|



|Element|Shared style|
|---|---|
|Hover and selected states|Indigo tint (very light indigo) `#EEF2FF`|
|Borders and dividers|Light gray `#E5E7EB`|



## **5. Pages and Navigation** 

The system has 7 pages. After login, the top bar shows **Dashboard, All Tasks, Calendar, Profile, and Logout** . Category Tasks opens from the Dashboard category cards. 

Logout is a small form button (POST with a CSRF token), not a link.

|Page|What it shows|What the user can do|
|---|---|---|
|**Login**|Email and password form|Log in, go to Register|
|**Register**|Name, email, password form|Create an account, go to Login|
|**Dashboard**|Up to 3 nearest incomplete tasks (overdue included); 3 category<br>cards with counts|Add a task, show all tasks, open a<br>category, mark a task complete|
|**All Tasks**|List of all the user's tasks with search, filters, and<br>sort|Create, view, edit, delete, complete;<br>search; filter; sort|
|**Category Tasks**|Tasks of one category (Study, Personal,<br>or Work)|Same actions as All Tasks|
|**Calendar**|Month grid with tasks on their deadline<br>dates|Change month, select a date, open<br>task details|
|**Profile**|Personal information and password<br>section|Update information, change password|



Task creation and editing use **one reusable form (modal)** , shared by the Dashboard, All Tasks, Category Tasks, and Calendar. 

## **6. Page Details** 

### **6.1 Dashboard** 

- Heading with the user's name, plus the **+ Add New Task** (solid indigo) and **Show All Tasks** (outlined) buttons. 

- Up to three task cards, nearest deadline first, including overdue tasks marked Overdue. If there are none, show "No upcoming tasks". Each card shows category, title, deadline, status badge, priority badge, and a "mark complete" circle. 

- Three category cards (Study, Personal, Work) with a colored icon tile, the total task count (all statuses), and an arrow. Clicking one opens Category Tasks. 

### **6.2 All Tasks and Category Tasks** 

- A filter bar: category, priority, status. A sort control: deadline earliest or latest. A search box finds tasks by a keyword in the title (required). Search works together with the filters. 

- The filter bar, search box, and sort control send their values as query options to `/tasks` (or `/category/<name>`); the page reloads with the result. The category filter appears only on All Tasks.

- Each task row shows title, category, deadline, priority badge, status badge, and Edit, Delete, and Complete actions. 

- Delete always asks for confirmation. 

- Empty state: a short message ("No tasks yet") with an Add New Task button. 

### **6.3 Add / Edit Task Form (modal)** 

- Required: title, category, deadline. Optional: description, priority, status. 

- When priority or status is left empty, the defaults are Medium and Pending. Priority choices are Low, Medium, and High. Status choices are Pending, In Progress, and Completed.

- Deadline: a date (required) and a time (optional). If no time is entered, 23:59 is used. All times are Egypt time (Africa/Cairo). There is no time zone picker.

- Every form that changes data includes a CSRF token. 

- Edit opens the same form with existing values filled in. 

- On a validation error, the form stays open and keeps what the user typed. 

- The creation date is recorded automatically and is not shown as an input. 

### **6.4 Calendar** 

- Month grid with previous and next buttons. Dates with tasks show a small indigo marker. 

- Selecting a date shows that day's tasks in a side panel. Selecting a task opens its details. 

### **6.5 Profile** 

- View and update name and email (the email must stay unique). Change password requires the current password. No other settings are included in this version. 

### **6.6 Login and Register** 

- Simple centered forms with a link to the other page. Login shows one generic error message for wrong credentials. 

## **7. Frontend–Backend Communication** 

The browser sends HTTP requests with the session cookie, and Flask returns data or an error. The table lists what each page needs from the backend. These needs are proposals until the whole team agrees the API contract after all five research phases. 

Field names and routes are in API_Contract_Agreement.md.

|Page / action|Needs from the backend|Frontend shows|
|---|---|---|
|Register|Create an account|Success: go to Login. Error: field<br>messages (including an already-used email)|
|Login|Check credentials, start a session|Success: Dashboard. Error: generic<br>message|
|Logout|End the session|Return to Login|
|Dashboard|Up to 3 nearest incomplete tasks (overdue included); total task count<br>per category; user's name|Task cards, category cards, and the<br>name in the heading|
|All Tasks|The user's tasks, with filter and sort<br>options|Task list|
|Category Tasks|Tasks of one category|Task list|
|Search tasks|Tasks matching a title keyword, with the active filters and sort|Task list|
|Create / Edit task|Save the task for the logged-in user|Updated list, or errors in the form|



|Page / action|Needs from the backend|Frontend shows|
|---|---|---|
|Delete task|Remove one task|Task disappears from the list|
|Mark complete|Set status to Completed|Badge updates|
|Calendar|Tasks for a month; tasks for one date|Markers, then the day's task list|
|Profile|Read and update user info; change<br>password|Updated info, or error messages|



**How the frontend handles errors** 

- **Validation error:** show the message next to the field and keep the user's input. 

- **Session expired:** redirect to Login (after 30 minutes of inactivity). 

- **Not found or not owned (404):** show an error and do not display the data. 

- **CSRF failure:** show a short message and reload the page.

- **Server or network error:** show a short message and let the user retry. 

The frontend also checks input before sending (empty fields, valid dates), but the backend always validates again. 

## **8. Responsive Design** 

- **Desktop:** top navigation bar, three cards per row. 

- **Mobile:** menu collapses into a single button, cards stack in one column, filters collapse into a "Filters" toggle, and the modal fills the screen. 

- Buttons and badges stay large enough to tap. 

## **9. Testing Plan for the Frontend** 

- Check every page on desktop and mobile widths. 

- Test each form with valid and invalid input.

- Test title search on its own and together with the filters. 

- Check that each error case (validation, expired session, forbidden) shows the correct message. 

- Check that status and priority badges update after edits. 

- Check text contrast and keyboard use on forms. 

## **10. Design Templates** 

The templates below show the color system (Section 3) and shared styling (Section 4) applied to a full page, a modal, and a form page. They are visual references for the look and feel. The other pages follow the same styling.

The templates are visual references only. If they differ from the text or SRS v1.2, the text and SRS v1.2 take priority. Known differences to update in the pictures: the time zone selector (use Egypt time), the status labels (use Pending / In Progress / Completed), the Weekly Momentum statistics (not in the SRS), and the Confirm Password field and Terms checkbox on the Register page (not in the SRS). 



<!-- Start of picture text -->
TaskFlow V AllTasks Calendar Profle Logout &<br>Welcome back, Omar<br>OM@ WeeklyMomentumvouveconpleted=~ Ontrack DUE TODAY COMPLETED PACE<br>tts acs the week 70% gostresched ic as Be<br>——_—<br>Upcoming Tasks NearestFirst View full roster ><br>Buy groceries Teammeeting ‘Submit SEreport<br>Categories structured workload buckets Active<br>© study . Personal . Work<br>Btasks a ‘Btasks: Ss ‘tasks<br><!-- End of picture text -->

**Template 1:** Page layout (Dashboard) 

**Template 2:** Modal (Add / Edit Task) 



<!-- Start of picture text -->
TaskFlow ¥ Logout B<br>2 EatTask | + NewTask | © Task 104 x<br>Edit Task Details<br>CORE INFORMATION + Required fields<br>Task Title * 18/100<br>‘Submit SE report<br>Study 2 Personal Work<br>ite & Well-being =) Projects& Team<br>Deadline * UTC -05:00 Eastern Time<br>6 142026 o © 05:00PM fo}<br>EXTENDED PROPERTIES Optional adjustments<br>Complete requirements analysis, system architecture diagram, and submit via<br>university portal<br>© High © Med © Low © Pending @ Active @ Done<br><!-- End of picture text -->

**Template 3:** Form page (Register) 



<!-- Start of picture text -->
© taskFiow<br>TaskFlow<br>Create your account<br>Star organizing your study, personal, and work<br>Name<br>Fall tasks today<br>Email address<br>2<br>Password<br>@ amon °<br>Contrm Password<br>©) oxen °<br>age tthe Terms<br>ot Seren and vay Poy<br>Aready have an account? Login<br>ORGANIZE SEAMLESSLY ACROSS<br>©sity) Parent Ch wor<br>€¢2028 TeoTacos. lrigisreared. Toms Privacy + Suppor<br><!-- End of picture text -->
