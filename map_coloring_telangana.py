"""
Constraint Satisfaction Problem: Map Coloring - Telangana Districts

This program colors the map of Telangana state districts using CSP.
Telangana has 33 districts (as per the new reorganization).
Colors: Red, Green, Blue, Yellow

Note: This uses an approximate adjacency model for educational purposes.
For production use, actual district boundary data should be used.
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

        # MRV heuristic: select variable with minimum remaining values
        unassigned = [v for v in self.variables if v not in assignment]
        var = min(unassigned, key=lambda v: len([d for d in self.domains[v]
                                                  if self.is_consistent(assignment, v, d)]))

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
    # 33 Districts of Telangana
    districts = [
        "Adilabad", "Bhadradri", "Hanumakonda", "Hyderabad", "Jagtial",
        "Jangaon", "Jayashankar", "Jogulamba", "Kamareddy", "Karimnagar",
        "Khammam", "Komaram Bheem", "Mahabubabad", "Mahabubnagar",
        "Mancherial", "Medak", "Medchal", "Mulugu", "Nagarkurnool",
        "Nalgonda", "Narayanpet", "Nirmal", "Nizamabad", "Peddapalli",
        "Ranga Reddy", "Rajanna Sircilla", "Sangareddy", "Siddipet",
        "Suryapet", "Vikarabad", "Wanaparthy", "Warangal", "Yadadri"
    ]

    # Available colors
    colors = ["Red", "Green", "Blue", "Yellow"]

    # District names mapping
    district_names = {d: d for d in districts}

    # Approximate adjacency constraints for Telangana districts
    # Based on geographical proximity
    constraints = {
        "Adilabad": ["Komaram Bheem", "Nirmal", "Mancherial"],
        "Bhadradri": ["Khammam", "Suryapet", "Warangal", "Jayashankar"],
        "Hanumakonda": ["Warangal", "Jayashankar", "Mulugu", "Mahabubabad"],
        "Hyderabad": ["Ranga Reddy", "Medchal", "Sangareddy"],
        "Jagtial": ["Karimnagar", "Peddapalli", "Mancherial"],
        "Jangaon": ["Warangal", "Siddipet", "Mulugu", "Suryapet"],
        "Jayashankar": ["Bhadradri", "Khammam", "Mahabubabad", "Mulugu", "Warangal"],
        "Jogulamba": ["Mahabubnagar", "Nagarkurnool", "Wanaparthy"],
        "Kamareddy": ["Nizamabad", "Siddipet", "Medak"],
        "Karimnagar": ["Jagtial", "Peddapalli", "Rajanna Sircilla", "Siddipet"],
        "Khammam": ["Bhadradri", "Mahabubabad", "Suryapet", "Nalgonda"],
        "Komaram Bheem": ["Adilabad", "Nirmal", "Mancherial"],
        "Mahabubabad": ["Khammam", "Jayashankar", "Mulugu", "Warangal"],
        "Mahabubnagar": ["Jogulamba", "Nagarkurnool", "Ranga Reddy", "Wanaparthy"],
        "Mancherial": ["Adilabad", "Komaram Bheem", "Jagtial", "Peddapalli"],
        "Medak": ["Kamareddy", "Siddipet", "Sangareddy", "Medchal"],
        "Medchal": ["Hyderabad", "Ranga Reddy", "Sangareddy", "Medak", "Siddipet"],
        "Mulugu": ["Hanumakonda", "Jayashankar", "Jangaon", "Mahabubabad", "Warangal"],
        "Nagarkurnool": ["Jogulamba", "Mahabubnagar", "Wanaparthy", "Ranga Reddy"],
        "Nalgonda": ["Khammam", "Suryapet", "Yadadri", "Ranga Reddy"],
        "Narayanpet": ["Mahabubnagar", "Wanaparthy"],
        "Nirmal": ["Adilabad", "Komaram Bheem", "Mancherial", "Jagtial"],
        "Nizamabad": ["Kamareddy", "Jagtial", "Rajanna Sircilla"],
        "Peddapalli": ["Jagtial", "Karimnagar", "Mancherial"],
        "Ranga Reddy": ["Hyderabad", "Medchal", "Mahabubnagar", "Nagarkurnool", "Vikarabad", "Nalgonda"],
        "Rajanna Sircilla": ["Karimnagar", "Nizamabad", "Siddipet"],
        "Sangareddy": ["Hyderabad", "Medak", "Medchal", "Siddipet", "Vikarabad"],
        "Siddipet": ["Kamareddy", "Karimnagar", "Medak", "Medchal", "Rajanna Sircilla", "Sangareddy", "Jangaon"],
        "Suryapet": ["Bhadradri", "Khammam", "Jangaon", "Nalgonda", "Yadadri"],
        "Vikarabad": ["Ranga Reddy", "Sangareddy", "Nagarkurnool"],
        "Wanaparthy": ["Jogulamba", "Mahabubnagar", "Nagarkurnool", "Narayanpet"],
        "Warangal": ["Hanumakonda", "Bhadradri", "Jangaon", "Jayashankar", "Mahabubabad", "Mulugu"],
        "Yadadri": ["Nalgonda", "Suryapet", "Ranga Reddy", "Warangal"]
    }

    domains = {d: colors[:] for d in districts}
    csp = CSP(districts, domains, constraints)
    solution = csp.solve()

    print("=" * 60)
    print("TELANGANA DISTRICT MAP COLORING - CSP SOLUTION")
    print("=" * 60)
    print(f"\nTotal Districts: {len(districts)}")
    print(f"Colors Used: {', '.join(colors)}\n")
    print("District-wise Color Assignment:\n")
    print("-" * 60)

    # Group by color for better display
    for color in colors:
        colored = [d for d in districts if solution[d] == color]
        if colored:
            print(f"\n{color}: {len(colored)} districts")
            for d in colored:
                print(f"  - {d}")

    print("\n" + "=" * 60)
    print("CONSTRAINT VERIFICATION")
    print("=" * 60)

    errors = 0
    for district, neighbors in constraints.items():
        for neighbor in neighbors:
            if solution[district] == solution[neighbor]:
                print(f"  ERROR: {district} and {neighbor} same color!")
                errors += 1

    if errors == 0:
        print("  All district adjacency constraints satisfied!")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
