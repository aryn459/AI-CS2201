states = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']
colors = ['Red', 'Green', 'Blue']

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

def valid(state, color, assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment:
            if assignment[neighbor] == color:
                return False
    return True


def solve(assignment):
    if len(assignment) == len(states):
        return assignment

    for state in states:
        if state not in assignment:
            current_state = state
            break

    for color in colors:
        if valid(current_state, color, assignment):
            assignment[current_state] = color

            result = solve(assignment)
            if result is not None:
                return result

            del assignment[current_state]

    return None


result = solve({})

for state in result:
    print(f"{state}: {result[state]}")