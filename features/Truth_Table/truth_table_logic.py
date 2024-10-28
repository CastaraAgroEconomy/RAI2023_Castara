# Truth Table generating script created by Claude 3.5 Sonnet
import streamlit as st
import numpy as np

if 'selected_role' not in st.session_state:
    st.session_state.selected_role = None
    
if 'selected_sub_role' not in st.session_state:
    st.session_state.selected_sub_role = None

if 'selected_action' not in st.session_state:
    st.session_state.selected_action = None

if 'selected_activity' not in st.session_state:
    st.session_state.selected_activity = None

if 'self' not in st.session_state:
    st.session_state.self = None

R_go = False

st.write("⚠️ - Truth Table that determines if selected combination is valid, is being tested.")

class TruthTable:
    def __init__(self, n=14, x=30, m=30, y=35, selected_role, selected_sub_role, selected_action, selected_activity):
        self.selected_role = selected_role
        self.selected_sub_role = selected_sub_role
        self.selected_action = selected_action
        self.selected_activity = selected_activity
        
        self.n = n
        self.x = x
        self.m = m
        self.y = y
        self.table = np.zeros((n, x, m, y), dtype=int)
        self.generate_table()

    def generate_table(self, selected_role, selected_sub_role, selected_action, selected_activity):
        # This is where we would implement the AI logic to generate the truth table
        # For now, we'll use a simple rule-based system as a placeholder
        for n in range(self.n):
            for x in range(self.x):
                for m in range(self.m):
                    for y in range(self.y):
    
                        # For the actual rules, 
                        # the external script containing actual rules, 
                        # "Rules.py" is to be called out instead.
                        # said script is called up by thefunction valid_selection
    
                        validate_selection(selected_role, selected_sub_role, selected_action, selected_activity)
    
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
R = TruthTable(
    st.session_state.selected_role,
    st.session_state.selected_sub_role,
    st.session_state.selected_action,
    st.session_state.selected_activity)

def validate_selection(selected_role, selected_sub_role, selected_action, selected_activity):
    # Map selections to indices (this mapping should be consistent with your main script)
    
    # The above previous lines of code, now replaced by these lines of code, calls an external function containing 
    # List  [A] = 14 roles
    # List  [B] = 30 sub-roles
    # List  [C] = 30 actions
    # List  [D] = 35 activities
    # Table [R] = 441000 combinations
    
    n = roles.index(role)
    x = sub_roles[role].index(sub_role)
    m = actions.index(action)
    y = activities.index(activity)

    if R.is_valid_combination(n, x, m, y):
        st.session_state.R_go = True        
        return True, None
    else:
        next_selection = R.get_next_valid_selection(n, x, m, y)
        st.session_state.R_go = False
        return False, next_selection
