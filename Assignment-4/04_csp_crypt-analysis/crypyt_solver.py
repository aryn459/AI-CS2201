letters = ['T', 'W', 'O', 'F', 'U', 'R']
digits = list(range(10))


def is_consistent(assignment):
    if len(set(assignment.values())) != len(assignment):
        return False

    if 'T' in assignment and assignment['T'] == 0:
        return False
    if 'F' in assignment and assignment['F'] == 0:
        return False

    return True


def is_solution(a):
    if len(a) != len(letters):
        return False

    T, W, O = a['T'], a['W'], a['O']
    F, U, R = a['F'], a['U'], a['R']

    TWO = 100*T + 10*W + O
    FOUR = 1000*F + 100*O + 10*U + R

    return TWO + TWO == FOUR


def select_unassigned_variable(assignment):
    for v in letters:
        if v not in assignment:
            return v
    return None


def backtrack(assignment):
    if len(assignment) == len(letters):
        if is_solution(assignment):
            return assignment
        return None

    var = select_unassigned_variable(assignment)

    for value in digits:
        assignment[var] = value

        if is_consistent(assignment):
            result = backtrack(assignment)
            if result is not None:
                return result

        del assignment[var]

    return None

solution = backtrack({})

if solution:
    print("Solution:")
    for k in sorted(solution):
        print(k, "=", solution[k])

    T, W, O = solution['T'], solution['W'], solution['O']
    F, U, R = solution['F'], solution['U'], solution['R']

    TWO = 100*T + 10*W + O
    FOUR = 1000*F + 100*O + 10*U + R

    print("\nVerification:")
    print(f"{TWO} + {TWO} = {FOUR}")
else:
    print("No solution found")