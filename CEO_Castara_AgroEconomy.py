import streamlit as st
import pandas as pd
import numpy as np

# Defining maximum configuration values for n, m, x, y
n = 10  # Maximum number of user roles
x = 15  # Maximum number of sub-roles per user role
m = 20  # Maximum number of actions
y = 20  # Maximum number of activities per action

# Initialize the matrices
roles = [f"User Role {i+1}" for i in range(n)]
sub_roles = {role: [f"Sub-Role {j+1}" for j in range(x)] for role in roles}
actions = [f"Action {i+1}" for i in range(m)]
activities = {action: [f"Activity {j+1}" for j in range(y)] for action in actions}

# AI-powered Inference Engine (AI-p IE) - initial placeholder for logic to filter valid combinations
def infer_valid_combinations(selected_role, selected_sub_role, selected_action, selected_activity):
    # Placeholder logic: replace this with actual AI inference rules to determine valid paths
    if selected_role in roles and selected_sub_role in sub_roles[selected_role] and selected_action in actions and selected_activity in activities[selected_action]:
        return True  # Assume valid for now
    return False

# Streamlit UI for selections
st.title("Castara AgroEconomy Venture Navigation")

# Role selection
selected_role = st.selectbox("Select a User Role", roles)

# Sub-role selection based on the selected role
if selected_role:
    selected_sub_role = st.selectbox(f"Select a Sub-Role for {selected_role}", sub_roles[selected_role])

# Action selection
selected_action = st.selectbox("Select an Action", actions)

# Activity selection based on the selected action
if selected_action:
    selected_activity = st.selectbox(f"Select an Activity for {selected_action}", activities[selected_action])

# Display valid combination status using AI-p IE
if selected_role and selected_sub_role and selected_action and selected_activity:
    valid_combination = infer_valid_combinations(selected_role, selected_sub_role, selected_action, selected_activity)
    if valid_combination:
        st.success(f"Valid combination: {selected_role}, {selected_sub_role}, {selected_action}, {selected_activity}")
    else:
        st.error("Invalid combination")

# Option to explore all possible combinations
st.header("Explore All Combinations")

# Generate combinations of all possible selections
all_combinations = [(r, sr, a, act) for r in roles for sr in sub_roles[r] for a in actions for act in activities[a]]

# Display combinations in a dataframe
combinations_df = pd.DataFrame(all_combinations, columns=["User Role", "Sub-Role", "Action", "Activity"])
st.write(combinations_df)

# Option to download the combinations
st.download_button(label="Download All Combinations", data=combinations_df.to_csv(index=False), file_name="combinations.csv")
