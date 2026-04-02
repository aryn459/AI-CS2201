letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
digits = list(range(10))


def is_consistent(assignment):
    if len(set(assignment.values())) != len(assignment):
        return False
    if 'S' in assignment and assignment['S'] == 0:
        return False
    if 'M' in assignment and assignment['M'] == 0:
        return False

    return True


def is_solution(assignment):
    if len(assignment) != len(letters):
        return False

    S, E, N, D = assignment['S'], assignment['E'], assignment['N'], assignment['D']
    M, O, R, Y = assignment['M'], assignment['O'], assignment['R'], assignment['Y']

    SEND = 1000*S + 100*E + 10*N + D
    MORE = 1000*M + 100*O + 10*R + E
    MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

    return SEND + MORE == MONEY


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
else:
    print("No solution found")