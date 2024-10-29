# Main Script and function call for the Castara AgroEconomy Mobile App.

import streamlit as st
from features.Truth_Table.truth_table_logic import TruthTable
from features.Validation.valid_selection import validate_selection
from features.Validation.Rules import is_valid_combination

# Set up session state for tracking user selections and login status
if 'is_logged_in' not in st.session_state:
    st.session_state.is_logged_in = False
if 'selected_role' not in st.session_state:
    st.session_state.selected_role = None
if 'selected_sub_role' not in st.session_state:
    st.session_state.selected_sub_role = None
if 'selected_action' not in st.session_state:
    st.session_state.selected_action = None
if 'selected_activity' not in st.session_state:
    st.session_state.selected_activity = None
if 'current_list' not in st.session_state:
    st.session_state.current_list = 'role'
if 'validation_passed' not in st.session_state:
    st.session_state.validation_passed = False

# Login screen setup
def login_screen():
    st.image("Assets/Media/Images/Cover_page.jpg", use_column_width=True)
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":  # Replace with actual authentication
            st.session_state.is_logged_in = True
            st.success("Login successful! Proceed to make your selections.")
        else:
            st.error("Invalid credentials. Please try again.")

# Selection screens for each list
def role_selection_screen():
    st.header("Step 1: Select a Role")
    st.write("Please select a role from the list below:")
    roles = ["Agricultural Engineers", "Horticulturists", "System Specialist", "Plant Scientists",
             "Operations Managers", "Maintenance Staff", "Quality Control Personnel", "Harvest Workers",
             "Climate Control Specialists", "Nutrient Management Specialists", "Franchise Operators",
             "Franchisors", "Management Personnel", "Investors"]
    st.session_state.selected_role = st.selectbox("Select Role", roles)
    if st.button("Confirm Role"):
        st.session_state.current_list = 'sub_role'
        st.rerun()


def sub_role_selection_screen():
    st.header("Select Sub-Role")
    
    # Dropdown to select the sub-role
    st.session_state.selected_sub_role = st.selectbox("Select Sub-Role", sub_roles[st.session_state.selected_role])

    # Button to validate the selection
    if st.button("Validate Selection"):
        # Call validate_selection with required parameters
        valid, next_selection = validate_selection(
            st.session_state.selected_role,
            st.session_state.selected_sub_role,
            st.session_state.selected_action,  # Ensure you pass all necessary parameters
            st.session_state.selected_activity
        )

        if not valid:
            st.error(f"The selected combination is invalid. Please select a valid {next_selection}.")
            # Logic to handle invalid selections (e.g., show previous selection again)
        else:
            st.success("Selection is valid.")
            # Proceed to the next screen or function
            next_function()  # Replace with your function to show the next selection screen

    # Option to go back to the previous screen
    if st.button("Back to Role Selection"):
        role_selection_screen()  # Call the function for the role selection screen

def action_selection_screen():
    st.header(f"Step 3: Select an Action (Sub-Role selected: {st.session_state.selected_sub_role})")
    actions = ["System Design & Optimization", "Environmental Parameter Monitoring", "Nutrient Solution Management",
               "Plant Health Assessment", "Growth Cycle Planning", "Equipment Maintenance", "Quality Control Inspections",
               "Harvest Scheduling", "Data Collection & Analysis", "Compliance Monitoring", "System Troubleshooting",
               "Resource Usage Optimization", "Production Planning", "Safety Protocol Implementation", "Team Coordination"]
    st.session_state.selected_action = st.selectbox("Select Action", actions)
    if st.button("Confirm Action"):
        if validate_selection(st.session_state.selected_role, st.session_state.selected_sub_role, st.session_state.selected_action):
            st.session_state.current_list = 'activity'
        else:
            st.warning("Invalid selection based on Role and Sub-Role. Please select a valid Action.")
        st.rerun()

def activity_selection_screen():
    st.header(f"Step 4: Select an Activity (Action selected: {st.session_state.selected_action})")
    activities = ["pH Level Monitoring", "Electrical Conductivity (EC) Testing", "Temperature Control Adjustment",
                  "Humidity Level Management", "Light Intensity Calibration", "Nutrient Mix Preparation", "Water Quality Testing",
                  "Growth Rate Documentation", "Equipment Sanitization", "System Flow Rate Checks", "Plant Spacing Optimization",
                  "Harvest Weight Recording", "Equipment Calibration", "Safety Inspection Rounds", "Inventory Management",
                  "Growth Data Recording", "Team Schedule Creation", "Maintenance Log Updates", "Quality Check Documentation",
                  "Compliance Report Generation"]
    st.session_state.selected_activity = st.selectbox("Select Activity", activities)
    if st.button("Confirm Activity"):
        if validate_selection(st.session_state.selected_role, st.session_state.selected_sub_role, st.session_state.selected_action, st.session_state.selected_activity):
            st.success("All selections are valid! Proceed to additional features.")
            st.session_state.validation_passed = True
        else:
            st.warning("Invalid selection based on Role, Sub-Role, and Action. Please select a valid Activity.")
        st.rerun()

# Main application logic
if not st.session_state.is_logged_in:
    login_screen()
else:
    if st.button("Logout"):
        st.session_state.is_logged_in = False
        st.rerun()

    # Display the correct selection screen based on the current stage
    if st.session_state.current_list == 'role':
        role_selection_screen()
    elif st.session_state.current_list == 'sub_role':
        sub_role_selection_screen()
    elif st.session_state.current_list == 'action':
        action_selection_screen()
    elif st.session_state.current_list == 'activity':
        activity_selection_screen()

    # Placeholder for additional modules to be added later based on selection validation
    if st.session_state.validation_passed:
        st.write("Placeholder: Additional features will be enabled here based on valid selections.")
