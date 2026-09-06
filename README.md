# 📚 Attendance Manager

A Python-based Attendance Management System that helps students track attendance, calculate required classes, and manage missed concepts.

## Features

* Add subjects
* Delete subjects
* Mark classes as attended
* Mark classes as missed
* Calculate attendance percentage
* Calculate classes required to reach a target
* Calculate classes that can be safely skipped
* Set any attendance target from 0% to 100%
* Mark important subjects
* Manually update attendance
* Track missed concepts
* Edit missed concepts
* Delete missed concepts
* Mark concepts as recovered
* Calculate overall attendance
* Automatically save data

## Project Structure

```text
AttendanceManager/
│
├── main.py
├── attendance.py
├── data.json
└── README.md
```

## Requirements

Python 3.x

No external libraries are required.

## How to Run

Open the project folder in VS Code.

Open the terminal and run:

```bash
python main.py
```

## How Attendance Is Calculated

### Current Attendance

```text
Attendance % = (Attended Classes / Total Classes) × 100
```

Example:

```text
Attended = 18
Total = 20

Attendance = (18 / 20) × 100
           = 90%
```

### Classes Needed

If the current attendance is below the selected target, the program calculates how many consecutive classes must be attended to reach that target.

Example:

```text
Current = 18 / 25
Target = 75%

Required classes = 1
```

### Classes That Can Be Skipped

If attendance is already above the target, the program calculates how many future classes can be missed while remaining at or above the selected target.

## Configurable Target

The default target is:

```text
75%
```

But the user can change it to:

```text
70%
75%
80%
85%
90%
95%
```

or any other value between 0 and 100.

## Data Storage

The application stores data in:

```text
data.json
```

This means attendance information remains available even after closing the program.

## Example

```text
Subject: Data Structures

Attended: 18
Total: 22

Attendance: 81.82%
Target: 75%

You can skip 2 classes safely.
```

## Technologies

* Python
* JSON
* File Handling
* Functions
* Lists
* Dictionaries
* Loops
* Conditional Statements

## Future Improvements

The project can later be upgraded with:

* Graphical User Interface
* Login system
* SQLite database
* Attendance charts
* Monthly reports
* Export to PDF
* Email notifications
* Web version
* Mobile application

```
```
