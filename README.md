# CSP-Assignment-Python

Constraint Satisfaction Problem (CSP) assignments implemented in Python. This repository contains solutions to classic CSP puzzles including map coloring, Sudoku, and cryptarithm problems.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithms Used](#algorithms-used)
- [Sample Output](#sample-output)

## Overview

This project demonstrates the application of Constraint Satisfaction Problem (CSP) techniques to solve four classic puzzles:

1. **Australia Map Coloring** - Color the 7 regions of Australia with 3 colors such that no adjacent regions share the same color.
2. **Telangana District Map Coloring** - Color all 33 districts of Telangana state with 4 colors such that no adjacent districts share the same color.
3. **Sudoku Solver** - Solve a 9x9 Sudoku puzzle using backtracking and constraint propagation.
4. **Cryptarithm Solver** - Solve the classic SEND + MORE = MONEY puzzle where each letter represents a unique digit.

## Project Structure

```
CSP-Assignment-Python/
|-- .gitignore
|-- README.md
|-- requirements.txt
|-- map_coloring_australia.py
|-- map_coloring_telangana.py
|-- sudoku_csp.py
|-- cryptarithm_csp.py
```

### File Descriptions

| File | Description |
|------|-------------|
| `map_coloring_australia.py` | CSP solution for Australia map coloring with 7 regions |
| `map_coloring_telangana.py` | CSP solution for Telangana's 33 districts |
| `sudoku_csp.py` | Backtracking-based Sudoku solver |
| `cryptarithm_csp.py` | Letter-to-digit mapping solver for SEND+MORE=MONEY |
| `requirements.txt` | Project dependencies (uses Python standard library only) |

## Installation

No external dependencies are required. All programs use Python's standard library.

```bash
# Clone the repository
git clone https://github.com/Niranjan325/CSP-Assignment-Python.git
cd CSP-Assignment-Python

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Usage

Run any of the Python scripts using:

```bash
python map_coloring_australia.py
python map_coloring_telangana.py
python sudoku_csp.py
python cryptarithm_csp.py
```

## Algorithms Used

### 1. Backtracking Search
Used in all four programs. The algorithm explores the search space by assigning values to variables one at a time and backtracking when a constraint is violated.

### 2. Minimum Remaining Values (MRV) Heuristic
Used in the Telangana map coloring problem. Selects the variable with the fewest legal values remaining, reducing the search space more quickly.

### 3. Constraint Propagation
After each assignment, the algorithm checks all constraints to ensure consistency before proceeding.

### 4. Permutation-Based Search
Used in the cryptarithm solver, generating all possible digit assignments and checking validity.

## CSP Components

Each problem is modeled with three CSP components:

- **Variables**: The entities to be assigned values (regions, districts, cells, letters)
- **Domains**: The set of possible values for each variable (colors, digits 0-9, digits 1-9)
- **Constraints**: Rules that must be satisfied (adjacent regions different colors, Sudoku rules, arithmetic equations)

## Sample Output

### Australia Map Coloring
```
Western Australia     : Red
Northern Territory    : Green
South Australia       : Blue
Queensland            : Red
New South Wales       : Green
Victoria              : Red
Tasmania              : Red
```

### Telangana District Coloring
```
Total Districts: 33
Colors Used: Red, Green, Blue, Yellow
```

### Sudoku Solver
```
SOLVED SUDOKU:
 5  3  4 |  6  7  8 |  9  1  2
 6  7  2 |  1  9  5 |  3  4  8
 1  9  8 |  3  4  2 |  5  6  7
---------+---------+---------
 8  5  9 |  7  6  1 |  4  2  3
 4  2  6 |  8  5  3 |  7  9  1
 7  1  3 |  9  2  4 |  8  5  6
---------+---------+---------
 9  6  1 |  5  3  7 |  2  8  4
 2  8  7 |  4  1  9 |  6  3  5
 3  4  5 |  2  8  6 |  1  7  9
```

### Cryptarithm (SEND + MORE = MONEY)
```
Letter to Digit Mapping:
  D = 7
  E = 5
  M = 1
  N = 6
  O = 0
  R = 8
  S = 9
  Y = 2

  SEND  = 9567
  MORE  = 1085
  ------------
  MONEY = 10652

  9567 + 1085 = 10652
  Equation verified: CORRECT!
```

## License

This project is for educational purposes.

## Author

Niranjan325
