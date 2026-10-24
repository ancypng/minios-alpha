# MiniOS Alpha — User Manual

**Operating System:** MiniOS Alpha
**Project:** IT 3131 Final Project

---

## 1. Introduction

MiniOS Alpha is a simple command-line operating system simulator written in Python. It runs inside any terminal and simulates fundamental OS components (Command shell, hierarchical file management, process lifecycle tracking, memory allocation, role-based user management, error handling.) It is a simulator designed to demonstrate operating systems concepts, not a real bootable operating system.

---

## 2. System Requirements

- **Operating System:** Windows (Command Prompt / CMD recommended), macOS, or Linux.
- **Python Version:** Python 3.8 or higher.
- **Dependencies:** None (uses standard Python library only: `os`, `sys`, `time`, `datetime`, `json`, `hashlib`, `getpass`, `platform`).

---

## 3. Installation

1. Download or clone the project repository:
   ```cmd
   git clone https://github.com/ancypng/minios-alpha.git
   cd minios-alpha
   ```
2. Verify Python is installed and accessible:
   ```cmd
   python --version
   ```
3. Confirm core project files exist in the directory (`main.py`, `filesystem.py`, `processes.py`, `memory.py`, `users.py`, `requirements.txt`).

---

## 4. How to Start MiniOS

1. Open Windows Command Prompt (CMD) and navigate to the project directory.
2. Launch the simulator:
   ```cmd
   python main.py
   ```
3. MiniOS displays the boot banner and prompts for login:
   ```
   ==================================================
                MINIOS ALPHA v1.0
         Operating Systems Final Project
==================================================

Welcome to MiniOS!

Created by PE, BALICAO, MENDOZA, STP. THOMAS, TUMAYAO

==================================================
                   MiniOS Login
==================================================
Demo accounts: admin / admin123, student / student123

Username: admin
Password:

[OK] Login successful. Welcome, admin!

Type 'help' to see the available commands.
   ```
4. After logging in, the shell prompt appears:
   ```
   MiniOS Alpha>
   ```

---

## 5. Login Instructions

MiniOS Alpha requires authentication before granting shell access.

### Default Accounts

| Username  | Password     | Role          |
| :-------- | :----------- | :------------ |
| `admin`   | `admin123`   | Administrator |
| `student` | `student123` | Standard User |

### Login Steps

1. Enter `admin` or `student` at the `Username:` prompt and press `Enter`.
2. Enter the password at the `Password:` prompt.
   _(Note: Password characters are hidden in CMD for security.)_
3. On successful login, the welcome message is displayed:
   ```
   Login successful.

   Welcome, admin!
   Type 'help' to see the available commands.

   MiniOS>
   ```
4. **Attempt Limit:** The system allows up to 3 consecutive attempts. After 3 failed attempts, MiniOS shuts down automatically.
5. **Switching Users:** Use `logout` or `login` to return to the login screen.

---

## 6. Command List

MiniOS Alpha provides 24 commands and aliases. Each command is documented below using the required reference format.

---

### 6.1 General Commands

#### COMMAND: help

**Purpose:**  
Displays the list of all available commands organized by category.  
**Syntax:**  
`help`  
**Example:**

```cmd
MiniOS> help
Available Commands:

[General]
  help                  Show this list
  clear                 Clear the screen
  date / time           Show the date / the time
  whoami                Show the current user
  systeminfo            Show system information
  history               Show commands typed this session
  echo <text>           Print text
  version               Show the MiniOS version
  exit                  Shut down MiniOS

[Files]
  dir [path]            List files and folders
  mkdir <name>          Create a directory
  create <file>         Create an empty file
  write <file> <text>   Write text into a file
  read <file>           Show a file's contents
  delete <name>         Delete a file or empty directory
  rename <old> <new>    Rename a file or directory
  cd <path>             Change directory (cd .. goes up)
  pwd                   Show the current directory

[Processes]
  run <name>            Start a simulated process
  process               List running processes
  kill <pid>            Terminate a process

[Memory]
  memory                Show memory status
  allocate <MB>         Allocate memory
  free <MB>             Release memory

[Users]
  users                 List user accounts
  logout                Log out and return to login
  login                 Switch user (alias of logout)
```

#### COMMAND: clear

**Purpose:**  
Clears the terminal screen. (`cls` is supported as an alias).  
**Syntax:**  
`clear`  
**Example:**

```cmd
MiniOS> clear
```

#### COMMAND: date

**Purpose:**  
Displays the current system date.  
**Syntax:**  
`date`  
**Example:**

```cmd
MiniOS> date
Current Date: Thursday, October 22, 2026
```

#### COMMAND: time

**Purpose:**  
Displays the current system time in 12-hour AM/PM format.  
**Syntax:**  
`time`  
**Example:**

```cmd
MiniOS> time
Current Time: 09:45:10 PM
```

#### COMMAND: whoami

**Purpose:**  
Displays the username of the current logged-in user.  
**Syntax:**  
`whoami`  
**Example:**

```cmd
MiniOS> whoami
Current User: admin
```

#### COMMAND: systeminfo

**Purpose:**  
Displays simulated hardware, operating system, and session information.  
**Syntax:**  
`systeminfo`  
**Example:**

```cmd
MiniOS> systeminfo
========================================
           SYSTEM INFORMATION
========================================

OS Name:      MiniOS Alpha
Version:      1.0
Architecture: 64-bit
CPU:          Virtual CPU
Memory:       1024 MB (256 MB used)
Host:         Windows (Python 3.11.4)
User:         admin (Administrator)
Processes:    0 running
Files/Dirs:   0 file(s), 2 folder(s)
Uptime:       1m 45s

========================================
```

#### COMMAND: history

**Purpose:**  
Shows the history of commands entered during the current session.  
**Syntax:**  
`history`  
**Example:**

```cmd
MiniOS> history
  1  whoami
  2  dir
  3  systeminfo
  4  history
```

#### COMMAND: echo

**Purpose:**  
Prints the specified text back to the screen.  
**Syntax:**  
`echo <text>`  
**Example:**

```cmd
MiniOS> echo Hello MiniOS
Hello MiniOS
```

#### COMMAND: version

**Purpose:**  
Displays the MiniOS version.  
**Syntax:**  
`version`  
**Example:**

```cmd
MiniOS> version
MiniOS Alpha v1.0
```

#### COMMAND: exit

**Purpose:**  
Shuts down the MiniOS simulator. (`shutdown` is supported as an alias).  
**Syntax:**  
`exit`  
**Example:**

```cmd
MiniOS> exit
Shutting down MiniOS...

Goodbye!
```

---

### 6.2 File Management Commands

#### COMMAND: pwd

**Purpose:**  
Shows the current working directory path.  
**Syntax:**  
`pwd`  
**Example:**

```cmd
MiniOS> pwd
\
```

#### COMMAND: dir

**Purpose:**  
Lists files and directories in the current folder or specified path. (`ls` is supported as an alias).  
**Syntax:**  
`dir [path]`  
**Example:**

```cmd
MiniOS> dir
Directory of \

     <DIR>  Documents
        12  notes.txt
```

#### COMMAND: mkdir

**Purpose:**  
Creates a new directory.  
**Syntax:**  
`mkdir <folder>`  
**Example:**

```cmd
MiniOS> mkdir Documents
Directory created.
```

#### COMMAND: create

**Purpose:**  
Creates a new empty file.  
**Syntax:**  
`create <file>`  
**Example:**

```cmd
MiniOS> create notes.txt
File created.
```

#### COMMAND: write

**Purpose:**  
Writes text into a file. Creates the file if it does not exist.  
**Syntax:**  
`write <file> <text>`  
**Example:**

```cmd
MiniOS> write notes.txt Operating Systems Final Project
File saved.
```

#### COMMAND: read

**Purpose:**  
Displays the contents of a file.  
**Syntax:**  
`read <file>`  
**Example:**

```cmd
MiniOS> read notes.txt
Operating Systems Final Project
```

#### COMMAND: delete

**Purpose:**  
Deletes a file or an empty directory.  
**Syntax:**  
`delete <name>`  
**Example:**

```cmd
MiniOS> delete notes.txt
File deleted.
```

#### COMMAND: rename

**Purpose:**  
Renames an existing file or directory.  
**Syntax:**  
`rename <old> <new>`  
**Example:**

```cmd
MiniOS> rename notes.txt draft.txt
Renamed.
```

#### COMMAND: cd

**Purpose:**  
Changes the current directory. (`cd ..` goes to parent directory; `cd \` returns to root).  
**Syntax:**  
`cd <path>`  
**Example:**

```cmd
MiniOS> cd Documents
Current directory: \Documents

MiniOS> cd ..
Current directory: \
```

---

### 6.3 Process Management Commands

#### COMMAND: run

**Purpose:**  
Starts a new simulated process and assigns it a PID.  
**Syntax:**  
`run <name>`  
**Example:**

```cmd
MiniOS> run calculator
Process started.

PID: 1
Name: calculator
Status: RUNNING
```

#### COMMAND: process

**Purpose:**  
Lists all currently running simulated processes.  
**Syntax:**  
`process`  
**Example:**

```cmd
MiniOS> process
PID    NAME            STATUS    STARTED
1      calculator      RUNNING   21:45:00
```

#### COMMAND: kill

**Purpose:**  
Terminates a simulated process using its PID.  
**Syntax:**  
`kill <pid>`  
**Example:**

```cmd
MiniOS> kill 1
Process 1 terminated.
```

---

### 6.4 Memory Management Commands

#### COMMAND: memory

**Purpose:**  
Displays current memory status including total, used, and free memory.  
**Syntax:**  
`memory`  
**Example:**

```cmd
MiniOS> memory
Memory Status
------------------------
Total Memory: 1024 MB
Used Memory:   256 MB
Free Memory:   768 MB
```

#### COMMAND: allocate

**Purpose:**  
Allocates a specified amount of memory in megabytes (MB).  
**Syntax:**  
`allocate <MB>`  
**Example:**

```cmd
MiniOS> allocate 200
200 MB allocated.
```

#### COMMAND: free

**Purpose:**  
Releases a specified amount of user-allocated memory in megabytes (MB).  
**Syntax:**  
`free <MB>`  
**Example:**

```cmd
MiniOS> free 200
200 MB released.
```

---

### 6.5 User Management Commands

#### COMMAND: users

**Purpose:**  
Lists all registered user accounts, their roles, and identifies the active user.  
**Syntax:**  
`users`  
**Example:**

```cmd
MiniOS> users
USER        ROLE
admin       Administrator  <- you
student     Standard User
```

#### COMMAND: logout

**Purpose:**  
Logs out the current user and returns to the login screen. (`login` is an alias).  
**Syntax:**  
`logout`  
**Example:**

```cmd
MiniOS> logout
Logging out admin...

========================================
              MiniOS Login
========================================
Demo accounts: admin / admin123, student / student123

Username:
```

---

## 7. Common Errors

MiniOS Alpha handles invalid inputs gracefully and does not crash when an error occurs. Below are the most common error messages, their causes, and resolutions:

1. **Unknown Command**
   - _Input:_ `hellooo`
   - _Message:_
     ```
     Unknown command.

     Type 'help' to see the available commands.
     ```
   - _Resolution:_ Verify spelling or type `help` to view valid commands.

2. **File Does Not Exist**
   - _Input:_ `read missing.txt`
   - _Message:_ `Error: File does not exist.`
   - _Resolution:_ Use `dir` to verify the file exists in the current directory.

3. **Entity Already Exists**
   - _Input:_ `mkdir Documents` (when `Documents` already exists)
   - _Message:_ `Error: A file or directory with that name already exists.`
   - _Resolution:_ Choose a different name or delete the existing entity.

4. **Directory Not Empty**
   - _Input:_ `delete Documents` (folder has files inside)
   - _Message:_ `Error: Directory is not empty.`
   - _Resolution:_ Delete the files inside the directory before deleting the directory.

5. **Invalid File/Directory Name**
   - _Input:_ `create report:final`
   - _Message:_ `Error: Invalid name. Avoid / \ : * ? " < > |`
   - _Resolution:_ Remove forbidden special characters from the name.

6. **Process Does Not Exist**
   - _Input:_ `kill 999`
   - _Message:_ `Error: Process does not exist.`
   - _Resolution:_ Use `process` to find valid running PIDs.

7. **Process Limit Reached**
   - _Input:_ `run app` (when 10 processes are already running)
   - _Message:_ `Error: Process limit reached (10). Kill one first.`
   - _Resolution:_ Use `kill <pid>` to terminate an existing process before starting a new one.

8. **Insufficient Free Memory**
   - _Input:_ `allocate 1000` (only 768 MB free)
   - _Message:_ `Error: Not enough free memory. Only 768 MB available.`
   - _Resolution:_ Check `memory` and request an amount less than or equal to free memory.

9. **Cannot Free Unallocated Memory**
   - _Input:_ `free 50` (when 0 MB has been allocated by the user)
   - _Message:_ `Error: Cannot free 50 MB. Only 0 MB is allocated by you.`
   - _Resolution:_ You can only free memory that you previously allocated.

10. **Missing Command Arguments**
    - _Input:_ `write notes.txt`
    - _Message:_ `Error: Missing argument. Usage: write <file> <text>`
    - _Resolution:_ Supply all required parameters indicated by the usage hint.

---

## 8. How to Exit MiniOS

### Method 1: The `exit` Command

Type `exit` or `shutdown` at the prompt:

```cmd
MiniOS> exit
Shutting down MiniOS...

Goodbye!
```

### Method 2: Keyboard Interrupts

Press `Ctrl+C` or `Ctrl+D` (or `Ctrl+Z` on Windows). The system intercepts the interrupt and exits gracefully:

```

Shutting down MiniOS...

Goodbye!
```

### State Persistence

- **Filesystem:** Files and folders persist across reboots via `minios_disk.json`.
- **Processes and Memory:** Simulated processes and dynamic memory allocations are volatile and reset cleanly to default upon restart.
