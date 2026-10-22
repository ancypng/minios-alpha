# MiniOS Alpha

A command-line operating system simulator written in Python for the Operating Systems final project.
It runs in Windows Command Prompt (CMD) and simulates a shell, file system, processes, memory and users.
It is **not** a real bootable operating system.

## Group Members

1. Francyn Pe – Project Leader
2. Matthew Sto. Tomas – CLI Developer
3. Kyle Patrick Mendoza – File Management Developer
4. JC Balicao – Process and Memory Developer
5. Jhetro Jade Tumayao – User/System Developer

## Features

- Command-line interface with its own `MiniOS>` prompt
- File management (simulated file system, saved to `minios_disk.json`)
- Process simulation (run, list, kill)
- Memory simulation (1024 MB total, 256 MB reserved by the "kernel")
- User login with hashed passwords
- System information
- Error handling (unknown commands, missing files, bad PIDs, bad memory amounts)

## Requirements

- Python 3.x (standard library only)
- Windows CMD (also works in other terminals)

## How to Run

1. Clone the repository.
2. Open CMD and go to the project folder.
3. Run:

```
python main.py
```

Demo accounts: `admin` / `admin123` and `student` / `student123`.
Password typing is hidden in CMD (no characters shown).

## Available Commands

| Group     | Commands                                                                                      |
| --------- | --------------------------------------------------------------------------------------------- |
| General   | `help`, `clear`, `date`, `time`, `whoami`, `systeminfo`, `exit`, `history`, `echo`, `version` |
| Files     | `dir`, `mkdir`, `create`, `read`, `delete`, `write`, `rename`, `cd`, `pwd`                    |
| Processes | `process`, `run`, `kill`                                                                      |
| Memory    | `memory`, `allocate`, `free`                                                                  |
| Users     | `users`, `logout`, `login`                                                                    |

## Project Structure

```
main.py          Shell: prompt, command parsing, error handling
filesystem.py    Simulated file system (tree of dictionaries)
processes.py     Simulated process table
memory.py        Simulated memory manager
users.py         Accounts and login
docs/            User_Manual.pdf, Technical_Documentation.pdf
screenshots/     Screenshots of MiniOS running in CMD
individual-reports/
```
