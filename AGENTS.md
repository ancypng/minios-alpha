## THE FOLLOWING ARE THE PROJECT REQUIREMENTS::

OPERATING SYSTEMS FINAL PROJECT

MiniOS — Simple Command-Line Operating System Simulator

1. Project Overview

For your final project in Operating Systems, you will work in groups to create your own simple MiniOS (Mini Operating System).

Your MiniOS will be a command-line operating system simulator that runs through Windows Command Prompt (CMD).

You are not required to create a real bootable operating system.

Instead, you will create a program that simulates basic operating system functions using a command-line interface.

Your project should demonstrate concepts that you learned in Operating Systems, such as:

Command-line interfaces

File management

Process management

Memory management

User management

System information

Error handling

The main goal is to create a simple but working MiniOS and explain how it works through your documentation.

2. Class Grouping

There are __ students in the class.

You will be divided into groups.

Group Number of Students MiniOS Name
Group 1 ____ MiniOS SC1063
Group 2 MiniOS Beta
Group 3 MiniOS Gamma
Group 4 MiniOS Delta
Group 5 MiniOS Omega
Group 6 MiniOS Nova
Total
Your instructor will provide the final list of members for each group.

Important

Each group will create its own complete MiniOS.

You are NOT combining all six groups into one operating system.

For example:

Group 1 creates MiniOS Alpha.

Group 2 creates MiniOS Beta.

Group 3 creates MiniOS Gamma.

Group 4 creates MiniOS Delta.

Group 5 creates MiniOS Omega.

Group 6 creates MiniOS Nova.

3. What Are You Going to Build?

You will create a program that looks and behaves like a simple command-line operating system.

For example:

========================================
GrouName MINI OS ALPHA v1.0
========================================

Welcome to MiniOS!

MiniOS>
The user can type commands:

MiniOS> help
The system should display the available commands.

The user can then perform operations such as:

MiniOS> dir
MiniOS> mkdir Documents
MiniOS> create notes.txt
MiniOS> read notes.txt
MiniOS> process
MiniOS> memory
MiniOS> systeminfo
MiniOS> exit
Your MiniOS should respond to the commands and perform the appropriate operation.

4. Important: Keep It Simple

This is a simulation of an operating system.

You do NOT need to build a real operating system.

You do NOT need to create:

A bootable operating system

A kernel

Device drivers

A graphical interface

A real CPU scheduler

Real memory management

A real file system

Hardware drivers

Networking

The purpose of this project is to demonstrate your understanding of basic Operating Systems concepts through a simple working program.

5. Programming Language

Your MiniOS must be developed using:

Python

It must be possible to run the program through:

Windows Command Prompt (CMD)

For example:

python main.py
Your project should not require a graphical user interface.

The main interaction should happen through the command line.

6. Required Features

Every group's MiniOS must have the following minimum features.

Feature 1 — Command-Line Interface

Your MiniOS must have its own command prompt.

Example:

MiniOS>
The user should be able to type commands.

Example:

MiniOS> help 7. Feature 2 — Help Command

Your MiniOS must have a:

help
command.

Example:

MiniOS> help

Available Commands:

help
clear
date
time
whoami
dir
mkdir
create
read
delete
process
run
kill
memory
allocate
free
systeminfo
exit
You may add additional commands.

8. Feature 3 — File Management

Your MiniOS must provide basic file management.

At minimum, implement:

dir
mkdir
create
read
delete
Example

Create a directory:

MiniOS> mkdir Documents

Directory created.
Create a file:

MiniOS> create notes.txt

File created.
Read a file:

MiniOS> read notes.txt

Operating Systems Final Project
Delete a file:

MiniOS> delete notes.txt

File deleted.
You may add additional file commands such as:

write
rename
cd
These additional commands are encouraged but not required.

9. Feature 4 — Process Management

Your MiniOS must simulate basic process management.

At minimum, implement:

process
run
kill
Example:

MiniOS> run calculator

Process started.

PID: 1
Name: calculator
Status: RUNNING
The user should be able to view running processes:

MiniOS> process

PID NAME STATUS
1 calculator RUNNING
2 editor RUNNING
The user should also be able to terminate a process:

MiniOS> kill 1

Process 1 terminated.
You are only simulating processes.

You do not need to control actual Windows processes.

10. Feature 5 — Memory Management

Your MiniOS must simulate basic memory management.

At minimum, implement:

memory
allocate
free
Example:

MiniOS> memory

Memory Status
------------------------

Total Memory: 1024 MB
Used Memory: 256 MB
Free Memory: 768 MB
The user should be able to allocate memory:

MiniOS> allocate 200

200 MB allocated.
Then:

MiniOS> memory

Memory Status
------------------------

Total Memory: 1024 MB
Used Memory: 456 MB
Free Memory: 568 MB
The user should also be able to release memory:

MiniOS> free 200

200 MB released.
Again, this is a simulation.

You are not actually controlling the computer's RAM.

11. Feature 6 — User Management

Your MiniOS must have a simple login system.

At minimum, create two user accounts.

For example:

admin
student
When MiniOS starts:

========================================
MiniOS Login
========================================

Username: admin
Password: ****

Login successful.

Welcome, admin!
You must also have:

whoami
Example:

MiniOS> whoami

Current User: admin
You may add:

users
login
logout
if you want to improve your project.

12. Feature 7 — System Information

Your MiniOS must have:

systeminfo
Example:

MiniOS> systeminfo

========================================
SYSTEM INFORMATION
========================================

OS Name: MiniOS Alpha
Version: 1.0
Architecture: 64-bit
CPU: Virtual CPU
Memory: 1024 MB
User: admin

========================================
The information may be simulated.

13. Feature 8 — Error Handling

Your MiniOS must not immediately crash when the user enters an invalid command.

For example:

MiniOS> hellooo
The system should respond:

Unknown command.

Type 'help' to see the available commands.
You should also handle other common errors.

For example:

MiniOS> read missing.txt

Error: File does not exist.
Another example:

MiniOS> kill 999

Error: Process does not exist. 14. Feature 9 — Exit Command

Your MiniOS must have a way to exit.

Use:

exit
Example:

MiniOS> exit

Shutting down MiniOS...

Goodbye!
You may use shutdown instead, but exit must be available if you choose not to use shutdown.

15. Minimum Command List

Your MiniOS must have at least these commands:

General

help
clear
date
time
whoami
systeminfo
exit
File Management

dir
mkdir
create
read
delete
Process Management

process
run
kill
Memory Management

memory
allocate
free
That gives you a minimum of 19 commands/features.

You may add more commands if your group wants to improve the system.

16. Suggested Additional Commands

These are optional:

write
rename
cd
history
users
login
logout
echo
calculator
status
version
Additional useful features may receive consideration during evaluation if they are properly implemented and documented.

Do not add unnecessary features just to make the project complicated.

A simple MiniOS that works correctly is better than a complicated MiniOS that does not work.

17. Group Roles

Each member must have a specific responsibility.

Groups with 6 Students

Student 1 — Project Leader

Responsible for:

Coordinating the group

Managing deadlines

Combining the project

Checking the final version

Student 2 — CLI Developer

Responsible for:

Command prompt

Command processing

help

clear

exit

Student 3 — File Management Developer

Responsible for:

dir

mkdir

create

read

delete

Student 4 — Process and Memory Developer

Responsible for:

process

run

kill

memory

allocate

free

Student 5 — User/System Developer

Responsible for:

Login

whoami

systeminfo

Error handling

Testing

Documentation assistance

18. Groups with 5 Students

For groups with four members, responsibilities can be combined.

Student 1

Project Leader + CLI

Student 2

File Management

Student 3

Process + Memory Management

Student 4

User Management + System Information + Testing

Every student must still contribute to the project.

19. Recommended Project Structure

Your project should be organized.

A recommended structure is:

MiniOS/
│
├── main.py
├── README.md
├── requirements.txt
│
├── users.py
├── filesystem.py
├── processes.py
├── memory.py
│
├── docs/
│ ├── User_Manual.pdf
│ └── Technical_Documentation.pdf
│
├── screenshots/
│ ├── login.png
│ ├── filesystem.png
│ ├── processes.png
│ ├── memory.png
│ └── systeminfo.png
│
└── individual-reports/
├── student1.pdf
├── student2.pdf
├── student3.pdf
└── student4.pdf
You may organize your files differently if your group has a good reason.

20. GitHub Requirement

Each group must create a GitHub repository for its MiniOS.

Example:

minios-alpha
Your GitHub repository will contain your:

Source code

README

Documentation

Screenshots

Individual reports

Your repository must be accessible to your instructor.

21. README.md

Your GitHub repository must contain a README.md.

The README should explain:

Project Name

Example:

MiniOS Alpha
Group Members

List all members.

Project Description

Briefly explain what your MiniOS does.

Features

List the features implemented.

Example:

- Command-line interface
- File management
- Process simulation
- Memory simulation
- User login
- System information
- Error handling
  Requirements

Example:

Python 3.x
Windows CMD
How to Run

Example:

1. Clone the repository.
2. Open CMD.
3. Navigate to the project folder.
4. Run:

python main.py
Available Commands

List all commands supported by your MiniOS.

22. User Manual

Your group must create a User Manual.

The User Manual explains how a normal user can operate your MiniOS.

Include:

1. Introduction

2. System Requirements

3. Installation

4. How to Start MiniOS

5. Login Instructions

6. Command List

For every command, explain:

Command name

Purpose

Syntax

Example

Example:

COMMAND: mkdir

Purpose:
Creates a new directory.

Syntax:
mkdir <folder>

Example:
mkdir Documents 7. Common Errors

8. How to Exit MiniOS

The User Manual should be saved as:

User_Manual.pdf 23. Technical Documentation

Your group must also create Technical Documentation.

This document explains how you developed MiniOS.

Include:

1. Introduction

2. Project Objectives

3. System Architecture

Include a diagram showing the major components.

Example:

                 MiniOS
                    |
             Command Shell
                    |
       +------------+------------+
       |            |            |

File System Processes Memory
|
Users
|
System Info 4. Program Structure

Explain your Python files.

5. File Management

Explain how your file system works.

6. Process Management

Explain how processes are simulated.

7. Memory Management

Explain how memory is simulated.

8. User Management

Explain how login and users work.

9. Error Handling

Explain how your program handles invalid commands and errors.

10. Testing

Explain how you tested your MiniOS.

11. Problems Encountered

Explain problems your group experienced and how you solved them.

12. Conclusion

Explain what your group learned from the project.

Save the document as:

Technical_Documentation.pdf 24. Screenshots

Your GitHub repository must contain screenshots showing that your MiniOS works.

At minimum, include screenshots of:

MiniOS startup

Login

Help command

File management

Process management

Memory management

System information

Error handling

Exit/shutdown

Do not simply take screenshots of your source code.

The screenshots should show the actual MiniOS running in CMD.

25. Individual Contribution Report

Every student must submit an individual contribution report.

The report should contain:

Student Name:

Group:

Assigned Role:

What did I contribute to the project?

What features did I personally develop?

What problems did I encounter?

How did I solve those problems?

What did I learn from this project?

Evidence of my contribution:
This report should be uploaded to the group's GitHub repository.

26. Demo Video

Each group must create a 5–10 minute demonstration video.

The video must show the actual MiniOS running.

Your group should demonstrate:

1. Start MiniOS

python main.py 2. Login

3. Help

help 4. File Management

Demonstrate commands such as:

dir
mkdir
create
read
delete 5. Process Management

Demonstrate:

run
process
kill 6. Memory Management

Demonstrate:

memory
allocate
free 7. User/System Information

Demonstrate:

whoami
systeminfo 8. Error Handling

Enter an invalid command and show how MiniOS responds.

9. Exit

exit 27. What Should Be Shown in the Video?

The video should show:

The CMD window

The MiniOS running

Commands being entered

The results of the commands

The group should briefly explain what each major feature does.

Each member should introduce themselves and briefly explain their contribution.

For example:

"I am Juan, and I developed the file management portion of our MiniOS. I implemented the create, read, and delete commands."

28. Where Can We Upload the Video?

You may upload your demonstration video to:

YouTube as Unlisted

Google Drive

OneDrive

Another video-sharing service approved by your instructor

Make sure the instructor can access the video.

29. Canvas LMS Submission

You will submit your final project through Canvas LMS.

You do NOT need to upload the entire project ZIP file if your GitHub repository contains the complete project.

Your Canvas submission should contain:

Group Information

Group:
MiniOS Name:

Members: 1. 2. 3. 4. 5.
GitHub Repository

GitHub Repository:
PASTE YOUR GITHUB LINK HERE
Demo Video

Demo Video:
PASTE YOUR VIDEO LINK HERE 30. Canvas Submission Checklist

Before submitting, make sure:

All group members are listed.

MiniOS is complete.

GitHub repository is available.

GitHub repository contains the complete source code.

README.md is complete.

User Manual is included.

Technical Documentation is included.

Screenshots are included.

Individual Contribution Reports are included.

Demo Video is uploaded.

Demo Video link is included in Canvas.

Demo Video can be viewed by the instructor.

The GitHub repository can be accessed by the instructor.

The final version of the project is committed to GitHub.

31. Final Project Demonstration

The instructor may review your MiniOS using your:

GitHub repository

Documentation

Screenshots

Demo video

The instructor may also ask individual group members questions about their work.

For example:

"Which part of the project did you develop?"

"How does your process command work?"

"How are files represented in your program?"

"How does your memory allocation work?"

"What happens when an invalid command is entered?"

You must be able to explain your own contribution.

32. Grading Rubric

Your project will be graded using the following:

Category Points
Command-Line Interface 10
File Management 15
Process Management 15
Memory Management 10
User/Login System 10
System Information 5
Error Handling 5
Documentation & User Manual 10
Testing & Screenshots 5
Demo Video & Presentation 10
Individual Contribution 5
TOTAL 100 33. What Makes a Good MiniOS?

A good MiniOS does not need to have hundreds of commands.

A good project should:

Work correctly

Be easy to use

Have clear commands

Handle errors

Have organized code

Be properly documented

Demonstrate Operating Systems concepts

Be reproducible using the GitHub instructions

Clearly show each student's contribution

Remember:

Simple and working is better than complicated and broken.

34. Final Reminder

This is an Operating Systems project, so your project should demonstrate concepts related to operating systems.

Do not focus only on making the program look impressive.

Focus on understanding what you are implementing.

Your MiniOS should demonstrate your understanding of:

Shell → Files → Processes → Memory → Users → System

Your final submission consists of:

1. Working MiniOS

2. GitHub Repository

3. User Manual

4. Technical Documentation

5. Screenshots

6. Individual Contribution Reports

7. Demo Video

8. Canvas Submission

Build it, document it, test it, and be prepared to explain your work.

Good luck, and enjoy building your own MiniOS!
