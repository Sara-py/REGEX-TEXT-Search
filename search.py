# 1. Regex to Postfix Converter


def precedence(op):
    if op == '*':
        return 3
    elif op == '.':
        return 2
    elif op == '|':
        return 1
    return 0

def insert_concatenation(regex):
    result = ""
    for i in range(len(regex)):
        c = regex[i]
        result += c
        if i + 1 < len(regex):
            d = regex[i + 1]
            if (c not in '(|' and d not in '|)*'):
                result += '.'
    return result

def regex_to_postfix(regex):
    output = []
    stack = []
    regex = insert_concatenation(regex)

    for c in regex:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        elif c in {'|', '.', '*'}:
            while stack and precedence(stack[-1]) >= precedence(c):
                output.append(stack.pop())
            stack.append(c)
        else:
            output.append(c)

    while stack:
        output.append(stack.pop())

    return ''.join(output)


# 2. NFA Construction


class State:
    def __init__(self):
        self.transitions = {}   # symbol -> set of states
        self.epsilon = set()    # epsilon transitions

class NFA:
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

def build_nfa_from_postfix(postfix):
    stack = []

    for c in postfix:
        if c == '.':
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            nfa1.accept.epsilon.add(nfa2.start)
            stack.append(NFA(nfa1.start, nfa2.accept))

        elif c == '|':
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            start = State()
            accept = State()
            start.epsilon.update([nfa1.start, nfa2.start])
            nfa1.accept.epsilon.add(accept)
            nfa2.accept.epsilon.add(accept)
            stack.append(NFA(start, accept))

        elif c == '*':
            nfa1 = stack.pop()
            start = State()
            accept = State()
            start.epsilon.update([nfa1.start, accept])
            nfa1.accept.epsilon.update([nfa1.start, accept])
            stack.append(NFA(start, accept))

        else:
            start = State()
            accept = State()
            start.transitions[c] = {accept}
            stack.append(NFA(start, accept))

    return stack.pop()


# 3. NFA to DFA Conversion


class DFAState:
    def __init__(self, nfa_states):
        self.nfa_states = frozenset(nfa_states)
        self.transitions = {}
        self.is_accept = False

class DFA:
    def __init__(self, start_state):
        self.start_state = start_state
        self.states = set()

def epsilon_closure(states):
    stack = list(states)
    closure = set(states)
    while stack:
        state = stack.pop()
        for next_state in state.epsilon:
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)
    return closure

def move(states, symbol):
    result = set()
    for state in states:
        if symbol in state.transitions:
            result.update(state.transitions[symbol])
    return result

def nfa_to_dfa(nfa):
    dfa_states_map = {}
    dfa_start_closure = frozenset(epsilon_closure({nfa.start}))
    start_dfa_state = DFAState(dfa_start_closure)
    start_dfa_state.is_accept = nfa.accept in dfa_start_closure
    dfa_states_map[dfa_start_closure] = start_dfa_state

    queue = [start_dfa_state]

    while queue:
        current_dfa = queue.pop(0)
        symbols = set()
        for nfa_state in current_dfa.nfa_states:
            symbols.update(nfa_state.transitions.keys())

        for symbol in symbols:
            move_result = move(current_dfa.nfa_states, symbol)
            closure = frozenset(epsilon_closure(move_result))
            if not closure:
                continue
            if closure not in dfa_states_map:
                new_dfa_state = DFAState(closure)
                new_dfa_state.is_accept = nfa.accept in closure
                dfa_states_map[closure] = new_dfa_state
                queue.append(new_dfa_state)
            current_dfa.transitions[symbol] = dfa_states_map[closure]

    dfa = DFA(start_dfa_state)
    dfa.states = set(dfa_states_map.values())
    return dfa


# 4. Search Matcher


def search_in_text(dfa, text):
    matches = []
    for i in range(len(text)):
        current = dfa.start_state
        j = i
        while j < len(text) and text[j] in current.transitions:
            current = current.transitions[text[j]]
            j += 1
            if current.is_accept:
                matches.append((i, text[i:j]))  # (start_index, match)
                break  # remove this break if you want overlapping matches
    return matches

def search_in_file(dfa, filename):
    results = []
    with open(filename, 'r') as f:
        for line_number, line in enumerate(f, 1):
            line = line.rstrip('\n')
            matches = search_in_text(dfa, line)
            for start_idx, match in matches:
                results.append((line_number, start_idx, match))
    return results


# 5. Main Function


def main():
    import os
    mode = input("Search in (1) file or (2) text? Enter 1 or 2: ").strip()
    regex = input("Enter regular expression: ")
    postfix = regex_to_postfix(regex)
    print(f"Postfix: {postfix}")
    nfa = build_nfa_from_postfix(postfix)
    dfa = nfa_to_dfa(nfa)

    if mode == '1':
        filename = input("Enter file path: ").strip()
        if not os.path.exists(filename):
            print("File not found.")
            return
        results = search_in_file(dfa, filename)
        if results:
            for line, col, match in results:
                print(f"Match at line {line}, column {col}: '{match}'")
        else:
            print("No matches found.")
    else:
        text = input("Enter text: ")
        results = search_in_text(dfa, text)
        if results:
            for index, match in results:
                print(f"Match at index {index}: '{match}'")
        else:
            print("No matches found.")



if __name__ == "__main__":
    main()
