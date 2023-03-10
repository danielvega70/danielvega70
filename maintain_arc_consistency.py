from collections import deque

VARIABLES = ["A", "B", "C", "D", "E", "F", "G"]
DOMAINS = {
    "A": ["Monday", "Tuesday", "Wednesday"],
    "B": ["Monday", "Tuesday", "Wednesday"],
    "C": ["Monday", "Tuesday", "Wednesday"],
    "D": ["Monday", "Tuesday", "Wednesday"],
    "E": ["Monday", "Tuesday", "Wednesday"],
    "F": ["Monday", "Tuesday", "Wednesday"],
    "G": ["Monday", "Tuesday", "Wednesday"]
}
CONSTRAINTS = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("D", "E"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]

def maintain_arc_consistency(variables, domains, constraints):
    # Initialize queue with all arcs in the constraints
    queue = deque(constraints)

    # Repeat until the queue is empty
    while queue:
        x, y = queue.popleft()

        # Remove inconsistent values from domain of x
        if remove_inconsistent_values(x, y, variables, domains):
            # If domain of x is empty, then no solution
            if not domains[x]:
                return None

            # Add all arcs (x, z) to queue where z is a neighbor of x
            for z in get_neighbors(x, variables, constraints):
                if z != y:
                    queue.append((z, x))

    return domains


def remove_inconsistent_values(x, y, variables, domains):
    removed = False
    for x_val in domains[x]:
        if all(not constraints_satisfied(x_val, y_val, x, y) for y_val in domains[y]):
            domains[x].remove(x_val)
            removed = True
    return removed


def constraints_satisfied(x_val, y_val, x, y):
    return (x_val != y_val) and ((x, y) in CONSTRAINTS or (y, x) in CONSTRAINTS)


def get_neighbors(x, variables, constraints):
    neighbors = set()
    for (a, b) in constraints:
        if x == a:
            neighbors.add(b)
        elif x == b:
            neighbors.add(a)
    return neighbors


solution = maintain_arc_consistency(VARIABLES, DOMAINS, CONSTRAINTS)
print(solution)
