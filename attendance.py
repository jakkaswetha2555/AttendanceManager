```python
import json
import os
import math
from datetime import datetime


DATA_FILE = "data.json"


# ---------------------------------------------------------
# DATA HANDLING
# ---------------------------------------------------------

def load_data():
    """Load attendance data from JSON file."""
    if not os.path.exists(DATA_FILE):
        return {
            "target_percentage": 75,
            "subjects": []
        }

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {
            "target_percentage": 75,
            "subjects": []
        }


def save_data(data):
    """Save attendance data to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ---------------------------------------------------------
# ATTENDANCE CALCULATIONS
# ---------------------------------------------------------

def current_percentage(attended, total):
    """Calculate current attendance percentage."""
    if total == 0:
        return 0.0

    return (attended / total) * 100


def classes_needed_for_target(attended, total, target):
    """
    Calculate how many consecutive classes must be attended
    to reach the target percentage.
    """

    if total == 0:
        return 0

    if current_percentage(attended, total) >= target:
        return 0

    needed = 0

    while current_percentage(
        attended + needed,
        total + needed
    ) < target:

        needed += 1

    return needed


def classes_skippable_at_target(attended, total, target):
    """
    Calculate how many future classes can be missed while
    still maintaining the target percentage.
    """

    if total == 0:
        return 0

    if current_percentage(attended, total) < target:
        return 0

    skippable = 0

    while current_percentage(
        attended,
        total + skippable + 1
    ) >= target:

        skippable += 1

    return skippable


# ---------------------------------------------------------
# SUBJECT OPERATIONS
# ---------------------------------------------------------

def find_subject(data, subject_id):
    """Find a subject using its ID."""

    for subject in data["subjects"]:
        if subject["id"] == subject_id:
            return subject

    return None


def add_subject(data, subject_name):
    """Add a new subject."""

    subject_id = len(data["subjects"]) + 1

    subject = {
        "id": subject_id,
        "subject": subject_name,
        "total_classes": 0,
        "attended_classes": 0,
        "is_important": False,
        "missed_notes": []
    }

    data["subjects"].append(subject)
    save_data(data)

    print(f"\n✓ Subject '{subject_name}' added successfully.")


def delete_subject(data, subject_id):
    """Delete a subject."""

    subject = find_subject(data, subject_id)

    if subject is None:
        print("\n✗ Subject not found.")
        return

    data["subjects"].remove(subject)
    save_data(data)

    print(f"\n✓ '{subject['subject']}' deleted successfully.")


def mark_attended(data, subject_id):
    """Mark one class as attended."""

    subject = find_subject(data, subject_id)

    if subject is None:
        print("\n✗ Subject not found.")
        return

    subject["total_classes"] += 1
    subject["attended_classes"] += 1

    save_data(data)

    print(
        f"\n✓ Attended marked for {subject['subject']}."
    )


def mark_missed(data, subject_id):
    """Mark one class as missed and optionally save a note."""

    subject = find_subject(data, subject_id)

    if subject is None:
        print("\n✗ Subject not found.")
        return

    subject["total_classes"] += 1

    print(
        f"\n✗ Missed class recorded for "
        f"{subject['subject']}."
    )

    topics = input(
        "Enter topics covered (optional): "
    ).strip()

    note = {
        "date": datetime.now().strftime("%d %b"),
        "topics": topics,
        "recovered": False
    }

    subject["missed_notes"].append(note)

    save_data(data)

    print("✓ Missed class saved.")


# ---------------------------------------------------------
# MANUAL ATTENDANCE
# ---------------------------------------------------------

def manual_update(data, subject_id):
    """Manually update attended and total classes."""

    subject = find_subject(data, subject_id)

    if subject is None:
        print("\n✗ Subject not found.")
        return

    try:
        attended = int(
            input("Enter attended classes: ")
        )

        total = int(
            input("Enter total classes: ")
        )

        if attended < 0 or total < 0:
            print("\n✗ Values cannot be negative.")
            return

        if attended > total:
            print(
                "\n✗ Attended classes cannot exceed "
                "total classes."
            )
            return

        subject["attended_classes"] = attended
        subject["total_classes"] = total

        save_data(data)

        print("\n✓ Attendance updated successfully.")

    except ValueError:
        print("\n✗ Please enter valid numbers.")


# ---------------------------------------------------------
# IMPORTANT SUBJECT
# ---------------------------------------------------------

def toggle_important(data, subject_id):
    """Mark or unmark a subject as important."""

    subject = find_subject(data, subject_id)

    if subject is None:
        print("\n✗ Subject not found.")
        return

    subject["is_important"] = not subject["is_important"]

    save_data(data)

    if subject["is_important"]:
        print(
            f"\n⭐ {subject['subject']} marked as important."
        )
    else:
        print(
            f"\n✓ {subject['subject']} is no longer important."
        )


# ---------------------------------------------------------
# MISSED CONCEPTS
# ---------------------------------------------------------

def view_notes(data, subject_id):
    """Display missed concepts for a subject."""

    subject = find_subject(data, subject_id)

    if subject is None:
        print("\n✗ Subject not found.")
        return

    notes = subject["missed_notes"]

    if not notes:
        print("\nNo missed concepts found.")
        return

    print(
        f"\n--- Missed Concepts: "
        f"{subject['subject']} ---"
    )

    for index, note in enumerate(notes, start=1):

        status = (
            "Recovered"
            if note["recovered"]
            else "Pending"
        )

        topics = note["topics"] or "Topics not noted"

        print(
            f"\n{index}. {note['date']}"
        )
        print(f"   Topics: {topics}")
        print(f"   Status: {status}")


def edit_note(data, subject_id):
    """Edit a missed concept note."""

    subject = find_subject(data, subject_id)

    if subject is None:
        print("\n✗ Subject not found.")
        return

    notes = subject["missed_notes"]

    if not notes:
        print("\nNo notes available.")
        return

    view_notes(data, subject_id)

    try:
        number = int(
            input("\nEnter note number to edit: ")
        )

        if number < 1 or number > len(notes):
            print("\n✗ Invalid note number.")
            return

        new_topics = input(
            "Enter updated topics: "
        ).strip()

        notes[number - 1]["topics"] = new_topics

        save_data(data)

        print("\n✓ Note updated.")

    except ValueError:
        print("\n✗ Invalid input.")


def delete_note(data, subject_id):
    """Delete a missed concept note."""

    subject = find_subject(data, subject_id)

    if subject is None:
        print("\n✗ Subject not found.")
        return

    notes = subject["missed_notes"]

    if not notes:
        print("\nNo notes available.")
        return

    view_notes(data, subject_id)

    try:
        number = int(
            input("\nEnter note number to delete: ")
        )

        if number < 1 or number > len(notes):
            print("\n✗ Invalid note number.")
            return

        notes.pop(number - 1)

        save_data(data)

        print("\n✓ Note deleted.")

    except ValueError:
        print("\n✗ Invalid input.")


def recover_note(data, subject_id):
    """Mark a missed concept as recovered."""

    subject = find_subject(data, subject_id)

    if subject is None:
        print("\n✗ Subject not found.")
        return

    notes = subject["missed_notes"]

    if not notes:
        print("\nNo notes available.")
        return

    view_notes(data, subject_id)

    try:
        number = int(
            input("\nEnter note number recovered: ")
        )

        if number < 1 or number > len(notes):
            print("\n✗ Invalid note number.")
            return

        notes[number - 1]["recovered"] = True

        save_data(data)

        print("\n✓ Concept marked as recovered.")

    except ValueError:
        print("\n✗ Invalid input.")


# ---------------------------------------------------------
# TARGET PERCENTAGE
# ---------------------------------------------------------

def change_target(data):
    """Change the required attendance percentage."""

    try:
        target = float(
            input(
                "\nEnter target attendance percentage "
                "(0-100): "
            )
        )

        if target < 0 or target > 100:
            print("\n✗ Target must be between 0 and 100.")
            return

        data["target_percentage"] = target
        save_data(data)

        print(
            f"\n✓ Target attendance changed to "
            f"{target:.2f}%."
        )

    except ValueError:
        print("\n✗ Please enter a valid percentage.")


# ---------------------------------------------------------
# SUBJECT DISPLAY
# ---------------------------------------------------------

def display_subject(data, subject):
    """Display complete information about one subject."""

    attended = subject["attended_classes"]
    total = subject["total_classes"]

    target = data["target_percentage"]

    percentage = current_percentage(
        attended,
        total
    )

    needed = classes_needed_for_target(
        attended,
        total,
        target
    )

    skippable = classes_skippable_at_target(
        attended,
        total,
        target
    )

    print("\n" + "-" * 55)

    print(
        f"{'⭐ ' if subject['is_important'] else ''}"
        f"{subject['subject']}"
    )

    print(
        f"Attendance: "
        f"{attended}/{total} "
        f"({percentage:.2f}%)"
    )

    print(
        f"Target: {target:.2f}%"
    )

    if percentage < target:
        print(
            f"⚠ Attend {needed} more class(es) "
            f"to reach {target:.2f}%."
        )
    else:
        print(
            f"✓ You can skip {skippable} "
            f"class(es) safely."
        )

    pending = sum(
        1
        for note in subject["missed_notes"]
        if not note["recovered"]
    )

    if pending:
        print(
            f"📚 {pending} missed concept(s) "
            f"to recover."
        )

    print("-" * 55)


def display_all_subjects(data):
    """Display all subjects."""

    if not data["subjects"]:
        print("\nNo subjects added yet.")
        return

    print("\n========== ALL SUBJECTS ==========")

    for subject in data["subjects"]:
        display_subject(data, subject)


# ---------------------------------------------------------
# OVERALL ATTENDANCE
# ---------------------------------------------------------

def overall_attendance(data):
    """Calculate overall attendance."""

    total = sum(
        subject["total_classes"]
        for subject in data["subjects"]
    )

    attended = sum(
        subject["attended_classes"]
        for subject in data["subjects"]
    )

    percentage = current_percentage(
        attended,
        total
    )

    target = data["target_percentage"]

    below = sum(
        1
        for subject in data["subjects"]
        if (
            subject["total_classes"] > 0
            and current_percentage(
                subject["attended_classes"],
                subject["total_classes"]
            ) < target
        )
    )

    print("\n========== OVERALL ATTENDANCE ==========")

    print(
        f"Overall: {attended}/{total} "
        f"({percentage:.2f}%)"
    )

    print(
        f"Target: {target:.2f}%"
    )

    print(
        f"Subjects: {len(data['subjects'])}"
    )

    print(
        f"Subjects below target: {below}"
    )

    if percentage >= target:
        print("✓ Overall attendance is on track.")
    else:
        print("⚠ Overall attendance is below target.")
```
