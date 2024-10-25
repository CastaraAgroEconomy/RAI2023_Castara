# Truth Table generating script created by Claude 3.5 Sonnet
import numpy as np

class TruthTable:
    def __init__(self, n=14, x=30, m=30, y=35):
        self.n = n
        self.x = x
        self.m = m
        self.y = y
        self.table = np.zeros((n, x, m, y), dtype=int)
        self.generate_table()

    def generate_table(self):
        # This is where we would implement the AI logic to generate the truth table
        # For now, we'll use a simple rule-based system as a placeholder
        for n in range(self.n):
            for x in range(self.x):
                for m in range(self.m):
                    for y in range(self.y):
                        # Example rule: combination is valid if all indices are even
                        if n % 2 == 0 and x % 2 == 0 and m % 2 == 0 and y % 2 == 0:
                            self.table[n, x, m, y] = 1

    def is_valid_combination(self, n, x, m, y):
        return self.table[n, x, m, y] == 1

    def get_next_valid_selection(self, n, x, m, y):
        if self.is_valid_combination(n, x, m, y):
            return None  # Current selection is valid
        
        # Check which dimension is invalid and return the appropriate list
        if self.table[n, :, :, :].max() == 0:
            return "role"
        elif self.table[n, x, :, :].max() == 0:
            return "sub_role"
        elif self.table[n, x, m, :].max() == 0:
            return "action"
        else:
            return "activity"

# Initialize the truth table
truth_table = TruthTable()

def validate_selection(role, sub_role, action, activity):
    # Map selections to indices (this mapping should be consistent with your main script)
   
    # This section to be changed so as to call external script function containing expanded 4 lists
    roles = ["Franchisee", "Management", "Investor", "Employee", "Admin"]
    sub_roles = {
        "Franchisee": ["Owner", "Operator"],
        "Management": ["CEO", "COO", "CFO"],
        "Investor": ["Equity Partner", "Angel Investor"],
        "Employee": ["Staff", "Manager"],
        "Admin": ["Super Admin", "Tech Support"]
    }
    actions = ["View Dashboard", "Manage Finances", "Access Reports", "Edit Profile"]
    activities = ["Update Settings", "View Analytics", "Export Data", "Manage Users"]
    # The above 10 lines of code to be replaced by code which call an external function containing 
    # List [A] = 14 roles
    # List [B] = 30 sub-roles
    # List [C] = 30 actions
    # List [D] = 35 activities
    
    n = roles.index(role)
    x = sub_roles[role].index(sub_role)
    m = actions.index(action)
    y = activities.index(activity)

    if truth_table.is_valid_combination(n, x, m, y):
        return True, None
    else:
        next_selection = truth_table.get_next_valid_selection(n, x, m, y)
        return False, next_selection
