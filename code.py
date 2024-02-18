import random

class Grammar:
    def __init__(self, VN, VT, P, S):
        self.VN, self.VT, self.P, self.S = VN, VT, P, S

    def generate_valid_strings(self):
        return [self.generate_string() for _ in range(5)]

    def generate_string(self):
        result, changed = [self.S], True

        while changed:
            changed, temp = False, []

            for ch in result:
                temp.extend(self.P.get(ch, [ch]))

            changed = len(temp) != len(result)
            result = temp

        return ''.join(result)

    def to_finite_automaton(self):
        Q = set(self.VN)
        q0 = self.S
        F = {symbol for symbol, productions in self.P.items() if not productions}
        delta = {state: {p[0]: p[1] for p in (production[:2] for production in productions if len(production) > 1)} for state, productions in self.P.items()}
        return FiniteAutomaton(Q, self.VT, delta, q0, F)

class FiniteAutomaton:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q, self.Sigma, self.delta, self.q0, self.F = Q, Sigma, delta, q0, F

    def string_belongs_to_language(self, input_string):
        current_state = self.q0
        for symbol in input_string:
            if current_state not in self.delta or symbol not in self.delta[current_state]:
                return False
            current_state = self.delta[current_state][symbol]
        return current_state in self.F

VN, VT = {'S', 'F', 'L'}, {'a', 'b', 'c', 'd'}
P, S = {'S': ['bS', 'aF', 'd'], 'F': ['cF', 'dF', 'aL', 'b'], 'L': ['aL', 'c']}, 'S'

grammar = Grammar(VN, VT, P, S)
valid_strings = grammar.generate_valid_strings()
print("5 Valid Strings:", *valid_strings, sep='\n')

automaton = grammar.to_finite_automaton()
input_string = "ab"
print(f"Does '{input_string}' belong to the language? {automaton.string_belongs_to_language(input_string)}")
