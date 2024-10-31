# This script does the following: -
#	1.	Builds the Truth Table by iterating through combinations of n, x, m, and y.
#	2.	Validates each combination using the is_valid_combination function from Rules.py.
#	3.	Checks selections in the finalize_selection function, with error handling to guide users back to the selection that needs adjustment.
#	4.	Maintains existing functionalities (no code removed unnecessarily), ensuring that parts like session state handling, error messaging, and st.success()/st.error() remain.

import streamlit as st
import numpy as np

from RAI2023_Castara.features.Validation.Rules import validate_choice

# Initialize session state variables if not already present
for key, default in {
    'n': 1, 'x': 1, 'm': 1, 'y': 1,
    'selected_role': None, 'selected_sub_role': None,
    'selected_action': None, 'selected_activity': None,
    'self': None, 'R_go': 0
}.items():
    if key not in st.session_state:
        st.session_state[key] = default


class TruthTable:
    def __init__(self, n=14, x=30, m=30, y=35):
        self.n = n
        self.x = x
        self.m = m
        self.y = y
        self.table = np.zeros((n, x, m, y), dtype=int)
        self.generate_table()

    def generate_table(self):
        st.write(" - Generating Truth Table with predefined validation rules.")
        for n in range(self.n):
            for x in range(self.x):
                for m in range(self.m):
                    for y in range(self.y):
                        is_valid = valid_choice(
                            st.session_state.selected_role,
                            st.session_state.selected_sub_role,
                            st.session_state.selected_action,
                            st.session_state.selected_activity
                        )
                        self.table[n, x, m, y] = int(bool(is_valid))
        st.write(" ")
        st.write(" - Initial Table complete ... ")



        if validate_selection(n, x, m, y):
            st.success("Valid combination!")
        else:
            next_step = R.get_next_valid_selection(n, x, m, y)
            st.error(f"Invalid combination. Please re-select your {next_step}.")
    

    
    def get_next_valid_selection(self, n, x, m, y):
        # Determines the next level with invalid choices and returns it

        
        if self.table[n, :, :, :].max() == 0:
            return "role"
        elif self.table[n, x, :, :].max() == 0:
            return "sub_role"
        elif self.table[n, x, m, :].max() == 0:
            return "action"
        else:
            return "activity"


# Function to validate selection
def validate_selection(n, x, m, y):
    # Uses the validate_choice function to determine if selection is valid

        st.write(" ")
        st.write("⚠️ - Confirming valid combination; searching .... "
    
    is_valid = is_valid_combination(
        st.session_state.selected_role,
        st.session_state.selected_sub_role,
        st.session_state.selected_action,
        st.session_state.selected_activity
    )
    
    if is_valid:
        st.session_state.R_go = 1
    else:
        st.session_state.R_go = 0
    return is_valid
    


st.write(" ")
st.write("⚠️ - Truth Table populated .... ")

st.write(" ")
st.write("⚠️ - Returning to central App execution ..... ")
