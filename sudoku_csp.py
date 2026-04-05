"""
Constraint Satisfaction Problem: Sudoku Solver

This program solves a Sudoku puzzle using CSP with backtracking
and constraint propagation techniques.
"""

class SudokuCSP:
    def __init__(self, grid):
        self.grid = [row[:] for row in grid]  # Deep copy
        self.size = 9
        self.box_size = 3

    def is_valid(self, row, col, num):
        # Check row
        if num in self.grid[row]:
            return False

        # Check column
        for r in range(self.size):
            if self.grid[r][col] == num:
                return False

        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if self.grid[r][c] == num:
                    return False

        return True

    def find_empty(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == 0:
                    return (r, c)
        return None

    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True  # Solved!

        row, col = empty

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num

                if self.solve():
                    return True

                self.grid[row][col] = 0  # Backtrack

        return False

    def display(self, title=""):
        if title:
            print(f"\n{title}")
            print("=" * 25)

        for i, row in enumerate(self.grid):
            if i % 3 == 0 and i != 0:
                print("-" * 25)
            row_str = ""
            for j, val in enumerate(row):
                if j % 3 == 0 and j != 0:
                    row_str += " | "
                row_str += f" {val}" if val != 0 else " ."
            print(row_str)


def main():
    # Sample Sudoku puzzle (0 represents empty cells)
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("=" * 50)
    print("SUDOKU SOLVER - CSP WITH BACKTRACKING")
    print("=" * 50)

    solver = SudokuCSP(puzzle)

    print("\nINPUT PUZZLE:")
    solver.display()

    print("\n" + "=" * 50)
    print("SOLVING...")
    print("=" * 50)

    if solver.solve():
        print("\nSOLUTION FOUND!\n")
        solver.display("SOLVED SUDOKU:")

        # Verify solution
        print("\n" + "=" * 50)
        print("VERIFICATION")
        print("=" * 50)

        valid = True

        # Check rows
        for i, row in enumerate(solver.grid):
            if sorted(row) != list(range(1, 10)):
                print(f"  ERROR: Row {i+1} invalid")
                valid = False

        # Check columns
        for col in range(9):
            column = [solver.grid[row][col] for row in range(9)]
            if sorted(column) != list(range(1, 10)):
                print(f"  ERROR: Column {col+1} invalid")
                valid = False

        # Check boxes
        for box_row in range(3):
            for box_col in range(3):
                box = []
                for r in range(3):
                    for c in range(3):
                        box.append(solver.grid[box_row*3+r][box_col*3+c])
                if sorted(box) != list(range(1, 10)):
                    print(f"  ERROR: Box ({box_row+1},{box_col+1}) invalid")
                    valid = False

        if valid:
            print("  All rows, columns, and 3x3 boxes valid!")
            print("  Solution verified successfully!")

    else:
        print("\nNo solution exists for this puzzle.")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
