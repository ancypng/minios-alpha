## 3. Documentation Deliverables (`docs/`)

- [x] **`docs/User_Manual.pdf` (§22):**
  - [x] 1. Introduction
  - [x] 2. System Requirements
  - [x] 3. Installation
  - [x] 4. How to Start MiniOS
  - [x] 5. Login Instructions (demo accounts, password masking)
  - [x] 6. Complete Command Reference (Name, Purpose, Syntax, Example for every command)
  - [x] 7. Common Errors & Troubleshooting
  - [x] 8. How to Exit MiniOS
- [ ] **`docs/Technical_Documentation.pdf` (§23):**
  - [ ] 1. Introduction & Project Scope
  - [ ] 2. Project Objectives
  - [ ] 3. System Architecture (Component Diagram: Shell → Files, Processes, Memory, Users, System Info)
  - [ ] 4. Program Structure (`main.py`, `filesystem.py`, `processes.py`, `memory.py`, `users.py`)
  - [ ] 5. File Management Architecture (in-memory tree & JSON persistence)
  - [ ] 6. Process Simulation Design (PID management, states, limits)
  - [ ] 7. Memory Simulation Design (RAM partitioning, allocation/release logic)
  - [ ] 8. User Authentication System (SHA-256 hashing, session state)
  - [ ] 9. Error Handling & Shell Stability
  - [ ] 10. Verification & Test Plan (unit tests, interactive tests)
  - [ ] 11. Problems Encountered & Technical Solutions
  - [ ] 12. Conclusion & Operating Systems Concepts Demonstrated

## 4. Screenshots Deliverables (`screenshots/`) (§24)

> **Important:** Must show actual MiniOS running in CMD (no source code screenshots).

- [ ] `screenshots/startup.png` — MiniOS startup banner and prompt
- [ ] `screenshots/login.png` — Login prompt, authentication, welcome screen
- [ ] `screenshots/help.png` — Full `help` command output
- [ ] `screenshots/filesystem.png` — `mkdir`, `create`, `write`, `read`, `dir`, `delete`
- [ ] `screenshots/processes.png` — `run calculator`, `run editor`, `process` table, `kill`
- [ ] `screenshots/memory.png` — `memory` initial status, `allocate 200`, updated status, `free 200`
- [ ] `screenshots/systeminfo.png` — Full `systeminfo` command output
- [ ] `screenshots/error_handling.png` — Invalid command, invalid file, bad PID, bad memory amount
- [ ] `screenshots/exit.png` — `exit` / `shutdown` command execution

## 5. Individual Contribution Reports (`individual-reports/`) (§25)

Each team member must submit a PDF (`individual-reports/<name_or_student_id>.pdf`) answering:

- [ ] Student Name, Group Name, Assigned Role (§17–18)
- [ ] What did I contribute to the project?
- [ ] What features did I personally develop?
- [ ] What problems did I encounter?
- [ ] How did I solve those problems?
- [ ] What did I learn from this project?
- [ ] Evidence of my contribution (commits, screenshots, code references)

## 6. Demonstration Video (§26–28)

- [ ] **Recording Length:** 5 to 10 minutes
- [ ] **Live Demonstration Sequence:**
  1. Start MiniOS (`python main.py`)
  2. Login demonstration
  3. Help command (`help`)
  4. File Management (`dir`, `mkdir`, `create`, `read`, `delete`)
  5. Process Management (`run`, `process`, `kill`)
  6. Memory Management (`memory`, `allocate`, `free`)
  7. User & System Information (`whoami`, `systeminfo`)
  8. Error Handling (show response to invalid commands/inputs)
  9. Exit (`exit`)
- [ ] **Team Presentation Requirement (§27):** Every member introduces themselves and briefly explains their assigned portion.
- [ ] **Hosting Platform (§28):** Upload to YouTube (Unlisted), Google Drive, or OneDrive with public/instructor viewing access verified.

## 7. Git & Canvas Submission Checklist (§20, §29–30)

- [x] Local Git repository initialized on `main` branch.
- [x] Remote GitHub repository (`minios-alpha`) created and pushed.
- [x] Ensure repository is accessible to the instructor.
- [ ] Canvas LMS Submission prepared:
  - [ ] Group Name: `MiniOS Alpha` (Group 1)
  - [ ] Full list of Group Members & student numbers
  - [ ] Working GitHub Repository link
  - [ ] Working Demo Video link (Google Drive / YouTube)
