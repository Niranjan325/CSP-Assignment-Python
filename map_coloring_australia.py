"""
Constraint Satisfaction Problem: Map Coloring - Australia

This program colors the map of Australia using the minimum number of colors
such that no two adjacent regions have the same color.
Regions: WA, NT, SA, Q, NSW, V, T
Colors: Red, Green, Blue
"""

class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, assignment, var, value):
        for neighbor in self.constraints.get(var, []):
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        var = next(v for v in self.variables if v not in assignment)

        for value in self.domains[var]:
            if self.is_consistent(assignment, var, value):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                del assignment[var]
        return None

    def solve(self):
        return self.backtrack({})


def main():
    # Define the CSP for Australia map coloring
    variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    domains = {var: ["Red", "Green", "Blue"] for var in variables}

    # Adjacency constraints (who borders whom)
    constraints = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["SA", "Q", "V"],
        "V": ["SA", "NSW"],
        "T": []  # Tasmania has no borders
    }

    csp = CSP(variables, domains, constraints)
    solution = csp.solve()

    print("=" * 50)
    print("AUSTRALIA MAP COLORING - CSP SOLUTION")
    print("=" * 50)
    print("\nRegions and their assigned colors:\n")

    region_names = {
        "WA": "Western Australia",
        "NT": "Northern Territory",
        "SA": "South Australia",
        "Q": "Queensland",
        "NSW": "New South Wales",
        "V": "Victoria",
        "T": "Tasmania"
    }

    for var in variables:
        print(f"  {region_names[var]:<22}: {solution[var]}")

    print("\n" + "=" * 50)
    print("Constraint Verification:")
    print("=" * 50)

    for var, neighbors in constraints.items():
        for neighbor in neighbors:
            if solution[var] == solution[neighbor]:
                print(f"  ERROR: {var} and {neighbor} have same color!")
            else:
                print(f"  OK: {var} ({solution[var]}) != {neighbor} ({solution[neighbor]})")

    print("\n" + "=" * 50)
    print("All constraints satisfied!")
    print("=" * 50)


if __name__ == "__main__":
    main()
