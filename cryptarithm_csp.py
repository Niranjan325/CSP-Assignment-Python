"""
Constraint Satisfaction Problem: Cryptarithm Solver

A cryptarithm is a puzzle where letters represent digits 0-9.
This program solves the classic puzzle: SEND + MORE = MONEY

Each letter represents a unique digit, and the first letter
of each word cannot be 0.
"""

from itertools import permutations


class CryptarithmCSP:
    def __init__(self, words, result):
        self.words = words
        self.result = result
        # Get all unique letters
        self.letters = set()
        for word in self.words + [self.result]:
            for char in word:
                self.letters.add(char)
        self.letters = list(self.letters)

    def word_to_number(self, word, assignment):
        return int(''.join(str(assignment[c]) for c in word))

    def is_valid(self, assignment):
        # Check leading zeros
        for word in self.words + [self.result]:
            if assignment[word[0]] == 0:
                return False

        # Calculate sum of words
        total = sum(self.word_to_number(word, assignment) for word in self.words)

        # Calculate result value
        result_val = self.word_to_number(self.result, assignment)

        return total == result_val

    def solve(self):
        digits = range(10)
        for perm in permutations(digits, len(self.letters)):
            assignment = dict(zip(self.letters, perm))
            if self.is_valid(assignment):
                return assignment
        return None


def main():
    # Classic cryptarithm: SEND + MORE = MONEY
    words = ["SEND", "MORE"]
    result = "MONEY"

    print("=" * 50)
    print("CRYPTARITHM SOLVER - CSP")
    print("=" * 50)
    print("\nPuzzle: SEND + MORE = MONEY\n")

    solver = CryptarithmCSP(words, result)

    print(f"Letters to assign: {solver.letters}")
    print(f"Number of letters: {len(solver.letters)}")
    print("\nSolving...")

    solution = solver.solve()

    if solution:
        print("\nSOLUTION FOUND!\n")
        print("-" * 50)
        print("Letter to Digit Mapping:")
        print("-" * 50)
        for letter in sorted(solution.keys()):
            print(f"  {letter} = {solution[letter]}")

        print("\n" + "-" * 50)
        print("Verification:")
        print("-" * 50)

        send = solver.word_to_number("SEND", solution)
        more = solver.word_to_number("MORE", solution)
        money = solver.word_to_number("MONEY", solution)

        print(f"  SEND  = {send}")
        print(f"  MORE  = {more}")
        print(f"  ------------")
        print(f"  MONEY = {money}")
        print()

        if send + more == money:
            print(f"  {send} + {more} = {money}")
            print("  Equation verified: CORRECT!")
        else:
            print("  ERROR: Equation does not match!")

    else:
        print("\nNo solution found.")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
