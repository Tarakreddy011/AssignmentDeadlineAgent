assignments = []


def add_assignment(name, due_date):
    assignment = {
        "name": name,
        "due_date": due_date
    }

    assignments.append(assignment)

    return {
        "success": True,
        "message": f"Added '{name}' due on {due_date}.",
        "assignment": assignment
    }


def get_upcoming():
    sorted_assignments = sorted(
        assignments,
        key=lambda x: x["due_date"]
    )

    return {
        "success": True,
        "assignments": sorted_assignments
    }


if __name__ == "__main__":
    print(add_assignment("AI Project", "2026-09-08"))
    print(add_assignment("DBMS Assignment", "2026-09-12"))

    print("\nUpcoming assignments:")
    print(get_upcoming())