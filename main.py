```python
from attendance import (
    load_data,
    add_subject,
    delete_subject,
    mark_attended,
    mark_missed,
    manual_update,
    toggle_important,
    view_notes,
    edit_note,
    delete_note,
    recover_note,
    change_target,
    display_all_subjects,
    overall_attendance,
    find_subject
)


# ---------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------

def show_subject_list(data):
    """Display subjects with their IDs."""

    if not data["subjects"]:
        print("\nNo subjects available.")
        return False

    print("\n---------- SUBJECTS ----------")

    for subject in data["subjects"]:
        print(
            f"{subject['id']}. "
            f"{subject['subject']}"
        )

    return True


def get_subject_id(data):
    """Ask the user for a subject ID."""

    if not show_subject_list(data):
        return None

    try:
        subject_id = int(
            input("\nEnter subject ID: ")
        )

        if find_subject(data, subject_id) is None:
            print("\n✗ Subject not found.")
            return None

        return subject_id

    except ValueError:
        print("\n✗ Enter a valid number.")
        return None


# ---------------------------------------------------------
# MENU
# ---------------------------------------------------------

def show_menu(data):

    target = data["target_percentage"]

    print("\n")
    print("=" * 55)
    print("             ATTENDANCE MANAGER")
    print("=" * 55)

    print(
        f"Current Target Attendance: "
        f"{target:.2f}%"
    )

    print("-" * 55)

    print("1.  Add Subject")
    print("2.  View All Subjects")
    print("3.  Mark Class Attended")
    print("4.  Mark Class Missed")
    print("5.  Manually Update Attendance")
    print("6.  Change Target Percentage")
    print("7.  Mark / Unmark Important Subject")
    print("8.  View Missed Concepts")
    print("9.  Edit Missed Concept")
    print("10. Delete Missed Concept")
    print("11. Mark Concept as Recovered")
    print("12. Overall Attendance")
    print("13. Delete Subject")
    print("0.  Exit")

    print("=" * 55)


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

def main():

    data = load_data()

    while True:

        show_menu(data)

        choice = input(
            "\nEnter your choice: "
        ).strip()

        # ---------------------------------------------
        # ADD SUBJECT
        # ---------------------------------------------

        if choice == "1":

            subject_name = input(
                "\nEnter subject name: "
            ).strip()

            if not subject_name:
                print("\n✗ Subject name cannot be empty.")
            else:
                add_subject(
                    data,
                    subject_name
                )

        # ---------------------------------------------
        # VIEW SUBJECTS
        # ---------------------------------------------

        elif choice == "2":

            display_all_subjects(data)

        # ---------------------------------------------
        # MARK ATTENDED
        # ---------------------------------------------

        elif choice == "3":

            subject_id = get_subject_id(data)

            if subject_id is not None:
                mark_attended(
                    data,
                    subject_id
                )

        # ---------------------------------------------
        # MARK MISSED
        # ---------------------------------------------

        elif choice == "4":

            subject_id = get_subject_id(data)

            if subject_id is not None:
                mark_missed(
                    data,
                    subject_id
                )

        # ---------------------------------------------
        # MANUAL UPDATE
        # ---------------------------------------------

        elif choice == "5":

            subject_id = get_subject_id(data)

            if subject_id is not None:
                manual_update(
                    data,
                    subject_id
                )

        # ---------------------------------------------
        # CHANGE TARGET
        # ---------------------------------------------

        elif choice == "6":

            change_target(data)

        # ---------------------------------------------
        # IMPORTANT SUBJECT
        # ---------------------------------------------

        elif choice == "7":

            subject_id = get_subject_id(data)

            if subject_id is not None:
                toggle_important(
                    data,
                    subject_id
                )

        # ---------------------------------------------
        # VIEW NOTES
        # ---------------------------------------------

        elif choice == "8":

            subject_id = get_subject_id(data)

            if subject_id is not None:
                view_notes(
                    data,
                    subject_id
                )

        # ---------------------------------------------
        # EDIT NOTE
        # ---------------------------------------------

        elif choice == "9":

            subject_id = get_subject_id(data)

            if subject_id is not None:
                edit_note(
                    data,
                    subject_id
                )

        # ---------------------------------------------
        # DELETE NOTE
        # ---------------------------------------------

        elif choice == "10":

            subject_id = get_subject_id(data)

            if subject_id is not None:
                delete_note(
                    data,
                    subject_id
                )

        # ---------------------------------------------
        # RECOVER NOTE
        # ---------------------------------------------

        elif choice == "11":

            subject_id = get_subject_id(data)

            if subject_id is not None:
                recover_note(
                    data,
                    subject_id
                )

        # ---------------------------------------------
        # OVERALL ATTENDANCE
        # ---------------------------------------------

        elif choice == "12":

            overall_attendance(data)

        # ---------------------------------------------
        # DELETE SUBJECT
        # ---------------------------------------------

        elif choice == "13":

            subject_id = get_subject_id(data)

            if subject_id is not None:
                delete_subject(
                    data,
                    subject_id
                )

        # ---------------------------------------------
        # EXIT
        # ---------------------------------------------

        elif choice == "0":

            print(
                "\nSaving data..."
            )

            print(
                "✓ Attendance Manager closed."
            )

            break

        else:

            print(
                "\n✗ Invalid choice. "
                "Please select a valid option."
            )


if __name__ == "__main__":
    main()
```
