# TaskFlow - Architecture Decisions

I chose a three-layer client-server design to keep presentation, application logic and data access separate. HTML, CSS, JavaScript, Python Flask and SQLite follow SRS v1.1. SQLite runs on the Flask host, avoiding the need for a separate database server.

I defined the main system components and their communication in Diagrams 01 and 07. I am waiting for the team to confirm the proposed architecture and technologies before implementation.
