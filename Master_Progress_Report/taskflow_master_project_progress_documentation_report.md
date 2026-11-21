**SOFTWARE ENGINEERING COURSE PROJECT** 

# **TaskFlow** 

Task Management System 

# **Master Project Progress & Documentation Report** 

**Version 1.2 — Five-Iteration Workflow and Research Record Updated** 

**Current status:** the five original research assignments are In Progress (reports drafted, team decisions pending). Sprint 0 (18–20 November 2026; 3 days) is In Progress — not finished, and is a planning period, not a software Increment. Sprints 1–4 are proposed for 21 November–18 December 2026 (28 days); the whole workflow runs 18 November–18 December 2026 (31 days). Phase 4 security and testing additions remain planned. Development remains Not Started. Current stage: Sprint 0 - in progress, not finished.

### Prepared for the five-member project team 

Issue date: 18 November 2026 — not a stage completion date 

## **Contents** 

|**1 Project Overview**|1|
|---|---|
|1.1 Suggested technology context|1|
|**2 Purpose and Recordkeeping Principles**|1|
|2.1 Updating rules|1|
|**3 Current Project Progress**|2|
|3.1 Research and planning baseline (In Progress)|2|
|3.2 Current stage boundary|2|
|**4 Development Roadmap and Progress Tracker**|3|
|**5 Research Record (In Progress)**|4|
|5.1 Research Phase 1 — Requirements Analysis|4|
|5.2 Research Phase 2 — System Design & Architecture|4|
|5.3 Research Phase 3 — Database Design|4|
|5.4 Research Phase 4 — Backend Development Planning|4|
|5.5 Research Phase 5 — Frontend Development Planning|4|
|**6 Team Responsibilities and Workflow**|5|
|6.1 Initial research responsibility distribution|5|
|6.2 Research-first team workflow|5|
|6.3 Reopening agreed decisions|5|
|6.4 Who owns what|5|
|**7 Proposed Five-Iteration Workflow — Planning Only**|6|
|**8 Decisions, Deliverables, and Open Record Items**|7|
|**9 Version History**|7|
|**10 Future Update Procedure**|8|



Status and dates in this report reflect the supplied project baseline and the companion planning documents. Scheduled deadlines are not treated as evidence of delivery. 

Software Engineering Project Team 

**TaskFlow — Master Project Progress & Documentation Report** 

## **1 Project Overview** 

Project name: TaskFlow — Task Management System. 

Project description. TaskFlow is a web-based task management application designed to help users organize daily activities, manage deadlines, prioritize responsibilities, and track progress in one place. Users will be able to create, edit, delete, and manage tasks; organize them into Study, Personal, and Work categories; set priorities and deadlines; and monitor productivity. 

Team size: five members. 

#### **1.1 Suggested technology context** 

These are the technologies supplied as the project’s suggested stack. Their presence here records the initial project information; it does not claim that the team formally selected or implemented them. 

|**Area**|**Suggested technology**|**Decision status in this baseline**|
|---|---|---|
|Frontend|HTML, CSS, and JavaScript|Suggested; final adoption not specified|
|Backend|Python Flask|Suggested; final adoption not specified|
|Database|SQLite|Suggested; final adoption not specified|



## **2 Purpose and Recordkeeping Principles** 

This report is the central record of TaskFlow’s progress, completed work, decisions, and future project stages. It is versioned and should be updated when the team completes a major activity or supplies new verified project information. The editable Word file is the working master; this PDF is the shareable snapshot of the same report version. 

#### **2.1 Updating rules** 

- Preserve previously completed work and important historical decisions. 

- Add newly completed work, and update the project progress and current stage. 

- Replace or revise outdated information when necessary without erasing important history. 

- Do not mark unfinished work as complete. 

- Record only actual work, decisions, implementation details, or test results supplied by the team. 

- Keep the report consistent, organized, and aligned with the latest verified project status. 

TaskFlow | Master Project Report 

Page 1 

Software Engineering Project Team 

**TaskFlow — Master Project Progress & Documentation Report** 

## **3 Current Project Progress** 

|**Progress area**|**Status as of 18 November 2026**|
|---|---|
|Research & planning|In Progress (reports drafted, team decisions pending)|
|Sprint 0|In Progress|
|Development work|Not Started — no implementation work is reported; the five-iteration workflow is proposed only|
|Current stage|Sprint 0 - in progress, not finished.|



#### **Open Decisions (to finish before Sprint 0 ends)**

- [ ] System architecture choice (Flask builds full pages vs. Flask sends JSON and JavaScript builds the pages)
- [ ] API contract (main endpoints and the data each one sends and receives)
- [ ] Deadline format (date only, or date and time) and time zone
- [ ] Dashboard rule when the user has fewer than three tasks, and whether overdue tasks count
- [ ] Default priority and status when left empty
- [ ] Session expiry time and CSRF protection
- [ ] Search confirmed as a required feature (Must)

#### **3.1 Research and planning baseline (In Progress)** 

The team is in progress on the research and planning process for five assigned research areas (reports drafted, team decisions pending). Security and testing were added to the Phase 4 plan on 18 November 2026; those additions remain planned and are not included in the drafted scope: 

1. Requirements Analysis — Member 1. Report drafted; team review and final decisions pending.

2. System Design & Architecture — Member 2. Report drafted; team review and final decisions pending.

3. Database Design — Member 3. Report drafted; team review and final decisions pending.

4. Backend Development Planning — Member 4. Report drafted; team review and final decisions pending.

5. Frontend Development Planning — Member 5. Report drafted; team review and final decisions pending.

For each area, the assigned member researched the topic and drafted a report for team review. Team discussion, review, and final decisions are still pending before proceeding. The exact phase findings, individual decision outcomes, and meeting dates were not included in the initial information and are not invented here. 

#### **3.2 Current stage boundary** 

The research and planning work is currently in progress during Sprint 0. The project is not yet ready to begin development work, and is not in development. Backend and frontend research planning do not count as implementation. No confirmed implementation assignments, code, integration results, test results, bugs, or final-delivery evidence are recorded in this baseline. 

The dates listed for Sprint 0 and the development period are proposed planning dates. A scheduled date alone does not change the Not Started status of development. 

TaskFlow | Master Project Report 

Page 2 

Software Engineering Project Team 

**TaskFlow — Master Project Progress & Documentation Report** 

## **4 Development Roadmap and Progress Tracker** 

The roadmap separates research in progress from future implementation. The proposed whole workflow runs 18 November–18 December 2026 (31 days): Sprint 0 is 18–20 November (3 days, planning only, currently In Progress), followed by Sprints 1–4 from 21 November–18 December (28 days). All dates are proposals, not evidence of a start or completion; Sprint 0 is not a software Increment. 

|**Stage / iteration**|**Status**|**Main deliverables / record**|**Completion date**|
|---|---|---|---|
|Research Phase 1 —<br>Requirements Analysis|In Progress (reports drafted, team decisions pending)|Problem statement, objectives, functional and non-functional<br>requirements, target users, user stories, and use cases<br>(Report drafted; team review and final decisions pending.)|Not provided|
|Research Phase 2 — System<br>Design & Architecture|In Progress (reports drafted, team decisions pending)|High-level architecture, layer interactions, workflow, UML diagrams,<br>and component communication (Report drafted; team review and final decisions pending.)|Not provided|
|Research Phase 3 — Database<br>Design|In Progress (reports drafted, team decisions pending)|SQLite research, proposed tables, ERD, relationships, operations,<br>and task/category storage (Report drafted; team review and final decisions pending.)|Not provided|
|Research Phase 4 — Backend<br>Development Planning|In Progress (reports drafted, team decisions pending)|Flask planning, authentication, CRUD, API, and database<br>communication (Report drafted; team review and final decisions pending.); security and testing additions<br>remain planned.|Not provided|
|Research Phase 5 — Frontend<br>Development Planning|In Progress (reports drafted, team decisions pending)|HTML/CSS/JavaScript, UI/UX, pages, dashboard, task interface,<br>calendar/profile, and API use (Report drafted; team review and final decisions pending.)|Not provided|
|Sprint 0 — Planning proposal|In Progress|Research planning and team API contract coordination; planning<br>only, not a software Increment.|18–20 Nov 2026<br>(proposed)|
|Sprints 1–4 — Development<br>proposal|Not Started|Proposed development iterations; implementation has not been<br>reported as begun.|21 Nov–18 Dec 2026<br>(proposed; 28 days)|
|Integration, Testing & Final<br>Delivery|Not Started|Future work: integration, test execution/results, bug fixes,<br>improvements, final documentation, presentation, and demonstration.|—|



**Status key:** Completed means the work described is recorded as complete in the supplied baseline. Planned (proposal) records a future or scheduled plan only. In Progress means verified work has begun but is unfinished. Not Started means no work is reported as begun. No implementation stage is reported In Progress. 

The companion research schedule places Sprint 0 activities across 18–20 November. Sprints 1–4 are scheduled for 21 November–18 December 2026; the full five-iteration workflow spans 18 November–18 December 2026. 

TaskFlow | Master Project Report 

Page 3 

Software Engineering Project Team 

**TaskFlow — Master Project Progress & Documentation Report** 

## **5 Research Record (In Progress)** 

This section preserves the scope of the five research assignments currently in progress. It records the subjects covered, not unprovided findings, diagrams, architecture choices, schemas, or implementation artifacts. Each phase report is intended to be concise, about 2–3 pages, as stated in the companion Five Research Phases document. 

#### **5.1 Research Phase 1 — Requirements Analysis** 

**Responsible:** Member 1. Report drafted; team review and final decisions pending. The drafted research/report scope covered: 

- Problem statement and project objectives. 

- Functional and non-functional requirements. 

- Target users, user stories, and use cases. 

#### **5.2 Research Phase 2 — System Design & Architecture** 

**Responsible:** Member 2. Report drafted; team review and final decisions pending. The drafted research/report scope covered: 

- High-level system architecture and frontend, backend, and database interaction. 

- Application workflow, relevant UML diagrams (including Use Case and Activity diagrams), and component communication. 

**Boundary:** Phase 2 owns high-level architecture and overall workflow; detailed API endpoints belong to Phase 4, and how the interface uses the API belongs to Phase 5. 

#### **5.3 Research Phase 3 — Database Design** 

**Responsible:** Member 3. Report drafted; team review and final decisions pending. The drafted research/report scope covered: 

- Database selection research, with SQLite listed as the suggested database. 

- Database tables, an Entity Relationship Diagram (ERD), and relationships between tables. 

- Database operations and how user tasks and categories are to be stored. 

#### **5.4 Research Phase 4 — Backend Development Planning** 

**Responsible:** Member 4. Report drafted; team review and final decisions pending. The drafted planning/report scope covered: 

- Python Flask framework, backend project structure, Register/Login/Logout, CRUD operations, API endpoints, and backend/database communication. 

**Planning update (18 November 2026):** security and testing were added to Phase 4 planning. These additions remain Planned and are not represented as completed research. 

**Boundary:** this records backend planning only; actual backend development remains Not Started. 

#### **5.5 Research Phase 5 — Frontend Development Planning** 

**Responsible:** Member 5. Report drafted; team review and final decisions pending. The drafted planning/report scope covered: 

- HTML, CSS, and JavaScript; UI/UX design; and application pages. 

- Dashboard design and the task management interface for priorities, deadlines, and categories. 

- Calendar and Profile pages; frontend/backend communication, including page-to-endpoint use and presentation of returned data. 

**Boundary:** this records frontend planning only; actual frontend development remains Not Started. 

TaskFlow | Master Project Report 

Page 4 

Software Engineering Project Team 

**TaskFlow — Master Project Progress & Documentation Report** 

## **6 Team Responsibilities and Workflow** 

#### **6.1 Initial research responsibility distribution** 

|**Member**|**Research responsibility**|**Status**|
|---|---|---|
|Member 1|Requirements Analysis|In Progress (reports drafted, team decisions pending) — Report drafted; team review and final decisions pending.|
|Member 2|System Design & Architecture|In Progress (reports drafted, team decisions pending) — Report drafted; team review and final decisions pending.|
|Member 3|Database Design|In Progress (reports drafted, team decisions pending) — Report drafted; team review and final decisions pending.|
|Member 4|Backend Development Planning|In Progress (reports drafted, team decisions pending) — Report drafted; team review and final decisions pending; implementation not started.|
|Member 5|Frontend Development Planning|In Progress (reports drafted, team decisions pending) — Report drafted; team review and final decisions pending; implementation not started.|



Future implementation responsibilities are not formally assigned in the supplied information. Any suggested accountability mapping or illustrative backlog assignments remain proposals until the team confirms them. 

#### **6.2 Research-first team workflow** 

The five-phase workflow proceeds in this order: Phase 1 — Requirements Analysis; Phase 2 — System Design & Architecture; then Phases 3, 4, and 5 run in parallel; then whole-team API contract agreement; then update any research phase if needed. The assigned member leads research and presentation; the whole team participates in discussion and the final decision. Research-phase material is reviewed during Sprint 0 to finalize the team’s decisions and agree the API contract after all five phases. 

The shared API contract identifies the main endpoints and the data fields each sends and receives after all five research phases are finished. Until then, endpoint ideas are proposals. The detailed endpoint specification remains owned by Phase 4, and Phase 5 owns how the interface uses it. 

Each report should be concise (about 2–3 pages), cover the phase responsibilities, and be presented for team discussion. The research schedule in Five Research Phases lists report and decision-meeting deadlines; scheduled deadlines are not themselves evidence of completion. 

#### **6.3 Reopening agreed decisions** 

An agreed decision may be reopened if a later phase uncovers a problem. Any member may raise the concern; the team votes, and a simple majority reopens the decision. Record each reopened decision, the reason for reopening it, and its final outcome alongside the original decision. 

#### **6.4 Who owns what** 

|**Topic**|**Owned by**|**Boundary**|
|---|---|---|
|High-level architecture and overall|Phase 2 (Member 2)|Structure of the whole system, its layers, and how the main user flow moves|
|workflow||through them.|
|Detailed API endpoints and data fields|Phase 4 (Member 4)|Concrete endpoint list and the request/response data each sends and receives.|
|How the interface uses the API|Phase 5 (Member 5)|Which page calls which endpoint and how returned data is presented to the user.|



TaskFlow | Master Project Report 

Page 5 

Software Engineering Project Team 

**TaskFlow — Master Project Progress & Documentation Report** 

## **7 Proposed Five-Iteration Workflow — Planning Only** 

This report records a proposed five-iteration workflow aligned with the companion documents “Agile Scrum Model” and “Five Research Phases”. The whole workflow spans 18 November–18 December 2026 (31 days): Sprint 0 runs 18–20 November (3 days, planning only), then Sprints 1–4 run 21 November–18 December (28 days). The dates are proposals, not confirmed starts or evidence of completed work. 

**Sprint 0 (In Progress):** a short planning and decision-finalization period, not a software Increment and not an official Scrum event. The research assignments are currently drafted and are being reviewed during Sprint 0. After all five phases are finished, the team still needs to agree on the main API endpoints and data fields; until then, endpoint ideas are proposals. Security and testing were added to Phase 4 planning on 18 November and remain Planned. 

**Sprints 1–4:** proposed development iterations. The dates and goals below are planning targets only; no implementation results or delivered Increments are asserted. 

Proposed Sprints 1–4 schedule (goals from Agile Scrum Model): 

|**Sprint**|**Proposed dates**|**Proposed goal**|
|---|---|---|
|Sprint 1|21–27 Nov 2026|Project setup and authentication.|
|Sprint 2|28 Nov–4 Dec 2026|Core task management.|
|Sprint 3|5–11 Dec 2026|Dashboard, categories, search, filtering, and sorting.|
|Sprint 4|12–18 Dec 2026|Calendar, profile, integration, testing, bug fixes, documentation, presentation, and demonstration.|



The companion Five Research Phases schedule lists these Sprint 0 deadlines: 

|**Work item**|**Report due**|**Presentation / team decision**|
|---|---|---|
|Phase 1 — Requirements Analysis|Wednesday 18 November 2026|Wednesday 18 November 2026|
|Phase 2 — System Design & Architecture|Thursday 19 November 2026|Thursday 19 November 2026|
|Phases 3, 4 and 5 — parallel|Friday 20 November 2026|Friday 20 November 2026|
|API contract agreement (whole team)|—|After all five phases are presented (date to be set by the team)|



These are schedule deadlines, not newly verified completion dates. The master report does not supply individual report delivery dates, final decision outcomes, or API contract contents. Development remains Not Started; integration, testing execution, bug fixing, documentation, presentation, and demonstration remain future work unless evidence is later supplied. 

TaskFlow | Master Project Report 

Page 6 

Software Engineering Project Team 

**TaskFlow — Master Project Progress & Documentation Report** 

## **8 Decisions, Deliverables, and Open Record Items** 

The initial information notes that final team decisions are still pending in Sprint 0, and it does not enumerate final decision outcomes. The report therefore does not claim a final architecture, database schema, endpoint design, UI design, or formal adoption of the suggested technology stack. 

|**Record item**|**Current record / open information**|
|---|---|
|Research reports and presentations|All five research assignments are In Progress (reports drafted, team decisions pending). Individual report files and actual delivery/meeting dates were<br>not supplied.|
|Sprint 0 phase deadlines|Phase 1: 18 Nov 2026; Phase 2: 19 Nov 2026; Phases 3–5: 20 Nov 2026; API contract after all five phases (date to be set by the team). These are deadlines from<br>Five Research Phases; actual delivery evidence/dates are not supplied here.|
|Phase 4 security and testing<br>additions|Added to planning on 18 Nov 2026; remain Planned and are not included in the drafted Phase 4 research scope.|
|API contract agreement|Pending after all five research phases; date to be set by the team. Endpoint/data-field contents are not<br>supplied in this report.|
|Agreed research decisions|Team review and final decisions are pending. Reopening<br>concerns and final outcomes should be recorded if any arise.|
|Suggested technology stack|HTML/CSS/JavaScript, Python Flask, and SQLite are suggested; formal approval is not specified.|
|Implementation assignments|Not formally assigned in this report; any companion Scrum-plan allocation remains proposal-only unless confirmed.|
|Implementation and test evidence|No implementation details, executed tests, results, bugs, or delivery artifacts are reported. Development remains Not<br>Started.|



## **9 Version History** 

|**Version**|**Issue date**|**Summary**|
|---|---|---|
|1.0|17 November 2026|Initial baseline: records the supplied project overview, five completed research assignments, team workflow,<br>current stage, and six-stage progress tracker. Stage completion dates were not provided.|
|1.1|17 November 2026|Added the proposed Scrum development schedule as a proposal only; recorded proposed Sprint dates and<br>goals without claiming implementation had started. Preserved Version 1.0; development stages remained Not<br>Started and current stage remained Ready to Begin Development Work.|
|1.2|18 November 2026|Revised the proposed schedule to Sprint 0 plus Sprints 1–4; updated the progress tracker and roadmap; added<br>research deadlines, phase workflow, Phase 4 security/testing planning additions, report length, ownership<br>boundaries, decision-reopening rule, and open record items. Preserved Versions 1.0 and 1.1; research<br>updated to In Progress (reports drafted, team decisions pending) and development remains Not Started.|



TaskFlow | Master Project Report 

Page 7 

Software Engineering Project Team 

**TaskFlow — Master Project Progress & Documentation Report** 

## **10 Future Update Procedure** 

When new project information is provided, update this report in a controlled sequence: 

1. Read the existing report and preserve completed work, previous decisions, and historical records. 

2. Identify the stage or activity the new information relates to; distinguish planning from actual implementation. 

3. Add a factual description of the work performed and any available diagrams, decisions, implementation details, or test evidence. 

4. Update the progress tracker status, completion date if supplied, and the current project stage. 

5. Keep unfinished work marked In Progress or Not Started; never infer completion. 

6. Update the version history and keep the editable master and PDF snapshot aligned. 

7. Replace the previous PDF with the latest verified report version while retaining the prior history inside the report where relevant. 

For an agreed decision that later appears problematic, record the concern, the team vote, the reason for reopening, and the final outcome alongside the original decision. A simple majority is the stated threshold for reopening. 

End of Version 1.2 — Issue date 18 November 2026 

TaskFlow | Master Project Report 

Page 8
