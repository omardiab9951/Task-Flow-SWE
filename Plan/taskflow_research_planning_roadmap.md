**SOFTWARE ENGINEERING COURSE PROJECT** 

# **TaskFlow** 

Task Management System 

## **TaskFlow: Research & Planning Roadmap** 

A shared guide to the five project phases, their research responsibilities, and the team process for discussing and agreeing on decisions. 

**RESEARCH AND PLANNING ONLY** This roadmap describes research responsibilities, phase dependencies, and team decision-making. It does not prescribe implementation or add coding tasks. 

**Prepared for:** The five-member project team 

**Issued:** 17 November 2026 

TaskFlow — Task Management System (17 November 2026) | Page 1 of 7 

|**Contents**|
|---|
|1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3|
|1.1 Suggested technology context . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3|
|1.2 Five-phase overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3|
|1.3 Phase dependencies and workflow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4|
|1.4 Sprint 0 timeline and deadlines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4|
|1.5 Report length . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4|
|2 Phase 1 — Requirements Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5|
|2.1 Coverage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5|
|2.2 Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5|
|3 Phase 2 — System Design & Architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5|
|3.1 Coverage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5|
|3.2 Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5|
|4 Phase 3 — Database Design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6|
|4.1 Coverage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6|
|4.2 Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6|
|5 Phase 4 — Backend Development Planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6|
|5.1 Coverage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6|
|5.2 Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6|
|5.3 Security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6|
|5.4 Testing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6|
|6 Phase 5 — Frontend Development Planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6|
|6.1 Coverage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6|
|6.2 Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6|
|7 Team Workflow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7|
|7.1 Reopening agreed decisions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7|
|7.2 Who owns what . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7|



TaskFlow — Task Management System (17 November 2026) | Page 2 of 7 

### **1 Introduction** 

TaskFlow is a proposed web-based task management application for organizing daily activities. Users are expected to create and manage tasks, set priorities and deadlines, group work into Study, Personal, and Work categories, and track progress. This roadmap divides the project’s early work into five research and planning phases. 

Each phase has one assigned lead. The lead researches the topic, prepares a concise report, and presents it. All five members then discuss the findings and agree on decisions. The assignment identifies who leads the research; it does not make that person the sole decision-maker. 

#### **1.1 Suggested technology context** 

|**Area**|**Suggested technology**|**Scope note**|
|---|---|---|
|Frontend|HTML, CSS, JavaScript|Suggested starting point; not an implementation<br>prescription.|
|Backend|Python Flask|Suggested starting point; detailed planning belongs to<br>Phase 4.|
|Database|SQLite|Suggested starting point; database design belongs to<br>Phase 3.|



#### **1.2 Five-phase overview** 

|**Phase**|**Name**|**Focus**|**Research lead**|
|---|---|---|---|
|01|Requirements Analysis|Define what TaskFlow is intended to solve and do.|Member 1|
|02|System Design & Architecture|Explain the proposed system structure and component|Member 2|
|||communication.||
|03|Database Design|Plan how information can be represented and stored.|Member 3|
|04|Backend Development Planning|Plan server-side responsibilities and data access.|Member 4|
|05|Frontend Development Planning|Plan user-facing pages, interactions, and interface.|Member 5|



The sequence is Phase 1, then Phase 2, followed by Phases 3, 4, and 5 in parallel, and then the API contract is agreed after Phases 3, 4, and 5. 

TaskFlow — Task Management System (17 November 2026) | Page 3 of 7 

#### **1.3 Phase dependencies and workflow** 

A strictly sequential plan would leave four members waiting while one member led a phase. This roadmap therefore proposes two sequential phases, three parallel research phases, a whole-team API-contract step, and updating any research phase if needed: Phase 1 → Phase 2 → Phases 3, 4, and 5 in parallel → API contract agreement (whole team) → update any research phase if needed. 



<!-- Start of picture text -->
Phase 1 → Phase 2 → Phases 3, 4, and 5 in parallel<br>Requirements Analysis System Design & Architecture Database, Backend & Frontend Planning<br>Lead: Member 1 Lead: Member 2 Leads: Members 3, 4, 5<br><!-- End of picture text -->

↓ After all five research phases are finished 



<!-- Start of picture text -->
API contract agreement (whole team) → update any research phase if needed<br><!-- End of picture text -->

Phases 3, 4, and 5 run in parallel after Phase 2, and the API contract is agreed after all five research phases are finished. 

The team agrees the main API endpoints and the data fields each endpoint sends and receives after all five research phases are finished. Until then, endpoint ideas are only proposals. Draft: Research_phases\API_Contract\API_Contract_Agreement.md. If the agreed contract requires changes to any research phase, that phase is updated and the change is recorded (see Section 7.1). The detailed API specification remains owned by Phase 4; see Section 7.2. 

#### **1.4 Sprint 0 timeline and deadlines** 

The research period is a proposed three-day Sprint 0, from Wednesday 18 November to Friday 20 November 2026. It prepares decisions 

for Sprint 1 in the companion **TaskFlow: Agile Iteration-Based Workflow** , which is proposed to start Saturday 21 November. Sprint 0 is a brief planning iteration, not a replacement for the Scrum development Sprints. 

|**Phase / step**|**Report due**|**Presentation and team decision**|
|---|---|---|
|Phase 1: Requirements|Wed 18 Nov 2026|Wed 18 Nov 2026|
|Phase<br>2:<br>System<br>Design<br>&|Thu 19 Nov 2026|Thu 19 Nov 2026|
|Architecture|||
|Phases 3, 4, and 5 (parallel)|Fri 20 Nov 2026|Fri 20 Nov 2026|
|API contract agreement (whole team)|—|After Phases 3, 4, and 5 are presented (date to be set by the team)|



#### **1.5 Report length** 

Each phase report is planned to be about 2–3 pages. This keeps research focused on preparation and avoids letting it delay the development work that follows. 

TaskFlow — Task Management System (17 November 2026) | Page 4 of 7 

### **2 Phase 1 — Requirements Analysis** 

**Lead:** Member 1. **Focus:** define what TaskFlow is intended to solve and do. 

#### **2.1 Coverage** 

|**Topic**|**What the research should establish**|
|---|---|
|Problem statement|Theproblem or need that theproposed application is intended to address.|
|Project objectives|The outcomes theproject aims to support.|
|Functional requirements|Expected behavior, such as creating and managing tasks, priorities, deadlines, categories, and<br>progress.|
|Non-functional requirements|Expectedqualities or constraints on how the application should work.|
|Target users|Thepeople theproposed application is intended to serve.|
|User stories|Short user-centered descriptions of desired capabilities and value.|
|Use cases|Descriptions of how a user may interact with theproposed system to reach agoal.|



#### **2.2 Purpose** 

Phase 1 should establish a shared understanding of users, problems, and expected behavior. The whole team discusses and agrees on the requirements before design work begins. 

### **3 Phase 2 — System Design & Architecture** 

**Lead:** Member 2. **Focus:** explain the proposed system structure and component communication. 

#### **3.1 Coverage** 

- **System architecture:** the high-level structure of the proposed system. 

- **Frontend, backend, and database interaction:** how the main parts relate and exchange information. 

- **Application workflow:** the overall path through the proposed system. 

- **UML diagrams:** a Use Case Diagram and an Activity Diagram. 

- **Component communication:** the planned relationships among system parts. 

**Scope boundary.** Phase 2 owns the high-level architecture and overall workflow only. Detailed API endpoints are specified in Phase 4; Phase 5 plans how the interface uses those endpoints. See Section 7.2. 

#### **3.2 Purpose** 

Phase 2 turns the agreed requirements into a system-level view and a common basis for discussion. Its decisions provide context for the API contract and the parallel work in Phases 3–5. 

TaskFlow — Task Management System (17 November 2026) | Page 5 of 7 

### **4 Phase 3 — Database Design** 

**Lead:** Member 3. **Focus:** plan how information can be represented and stored. 

#### **4.1 Coverage** 

- **Database selection:** consider SQLite as the suggested database. 

- **Database tables:** identify the information the planned system needs to represent. 

- **Entity Relationship Diagram (ERD):** show proposed entities and their relationships. 

- **Relationships between tables:** explain how the planned records connect. 

- **Database operations:** describe the data access the system is expected to need. 

- **Task and category storage:** plan how tasks and Study, Personal, and Work categories may be represented. 

#### **4.2 Purpose** 

Phase 3 should produce a proposed information model and the reasoning behind it for team discussion and agreement. The roadmap assigns the research lead; the team agrees the resulting decisions. 

### **5 Phase 4 — Backend Development Planning** 

**Lead:** Member 4. **Focus:** plan server-side responsibilities and data access. This phase is a research and planning deliverable, not coding. 

#### **5.1 Coverage** 

- Python Flask framework and a proposed backend project structure. 

- User authentication flows: Register, Login, and Logout. 

- CRUD operations for the planned data. 

- Detailed API endpoints, including request and response data fields (working from proposed endpoints that are checked and finalized in the team API contract step). 

- Communication between the backend and the database. 

#### **5.2 Purpose** 

Phase 4 should explain server-side concepts and interfaces as a research and planning deliverable, not coding work. 

#### **5.3 Security** 

The research plan should address password hashing (never plain text), session handling (created, maintained, and closed at logout), and protection of private data (each user can access only their own tasks and categories). 

#### **5.4 Testing** 

The test plan should state what is tested and when. It should distinguish unit, integration, and end-to-end tests, explain what each covers, and give every agreed Phase 1 requirement a clear pass condition. 

### **6 Phase 5 — Frontend Development Planning** 

**Lead:** Member 5. **Focus:** plan user-facing pages, interactions, and interface. 

#### **6.1 Coverage** 

- HTML, CSS, and JavaScript; user-interface and user-experience design. 

- Application pages, dashboard design, and the task-management interface. 

- Calendar and Profile pages. 

- Frontend and backend communication. 

**Scope boundary.** Phase 5 owns how the interface uses the API: which page calls which endpoint and how returned data is shown. Phase 4 owns the detailed endpoints; both work from proposed endpoints that are checked and finalized in the team API contract step described in Section 1.3. 

#### **6.2 Purpose** 

Phase 5 should bring the main user-facing parts into view and check that they support the intended users and agreed requirements. 

TaskFlow — Task Management System (17 November 2026) | Page 6 of 7 

### **7 Team Workflow** 

The same research-first process applies to each phase: 

1. The assigned member researches the phase topic independently. 

2. The lead prepares a detailed but concise report of about 2–3 pages. 

3. The lead presents the report in a team meeting by the deadline in Section 1.4. 

4. All five members discuss the findings, ask questions, and suggest improvements. 

5. The team agrees on the final decisions and records them. 

6. The team follows the flow in Section 1.3: Phases 3, 4, and 5 proceed in parallel after Phase 2; the API contract is agreed after all five phases are finished. 

**Participation principle.** The assigned member researches and presents; all five members take part in discussion and final decisions. 

#### **7.1 Reopening agreed decisions** 

A decision is not beyond review if a later phase identifies a problem. Any member may raise a concern. The team votes, and a simple majority reopens the decision. The team records each reopened decision, its reason, and its final outcome alongside the original decision. 

#### **7.2 Who owns what** 

The boundaries below are agreed by the whole team. They identify the research area responsible for producing the detailed proposal; they do not remove the team’s role in discussing and agreeing decisions. 

|**Topic**|**Owned by**|**What this means**|
|---|---|---|
|High-level architecture and overall<br>workflow|Phase 2 — Member 2|Structure of the whole system, its layers, and how the main<br>user flow moves through them.|
|Detailed API endpoints and data|Phase 4 — Member 4|The concrete endpoint list and request/response data,|
|fields||working from proposed endpoints that are checked and finalized in the team API contract step.|
|How the interface uses the API|Phase 5 — Member 5|Which page calls which endpoint and how the returned data<br>is shown, working from proposed endpoints that are checked and finalized in the team API contract step.|



The roadmap covers the five specified phases and their research responsibilities and team workflow. It does not add phases or extend the assignments beyond research and planning. 

TaskFlow — Task Management System (17 November 2026) | Page 7 of 7 
