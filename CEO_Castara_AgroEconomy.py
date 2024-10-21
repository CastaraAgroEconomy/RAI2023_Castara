import streamlit as st
from features.Truth_Table.truth_table_logic import validate_selection
from features.Utility.Clear_screen import clear_display

# Placeholder for valid credentials (admin/password for testing)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

# Define the main function that will control the flow
def main():
    # clear_display()
    # Display cover page image
    st.image('Assets/Media/Images/Cover_page.jpg', use_column_width=True)
    
    # Call login function
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        
    if not st.session_state.logged_in:
        login()  # Go to login page if not logged in
    else:
        selected_role = " "
        user_role_selection(selected_role)  # Proceed to user role selection if logged in
        selected_sub_role = " "
        sub_role_selection(selected_role, selected_sub_role)
        selected_action = " "
        action_selection(selected_role, selected_sub_role, selected_action)
        sekected_activity = " "
        activity_selection(selected_role, selected_sub_role, selected_activity)

# Login function
def login():
    # clear_display()
    st.title("Castara AgroEconomy venture")
    
    # Input fields for username and password
    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")
    
    # Login button
    if st.button("Login"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.logged_in = True
            st.success("Login successful !")  # Display login success
            st.rerun()  # Use st.rerun() instead of st.experimental_rerun()
        else:
            st.error("Invalid credentials. Please try again.")
    
# User role selection screen
def user_role_selection(selected_role):
    # clear_display()
    st.title("Select Your Role")

    roles = ["Franchisee", "Management", "Investor", "Employee", "Admin"]
    
    # Display radio buttons for role selection
    selected_role = st.radio("Choose a role", roles)
    
    if st.button("Proceed"):
        st.write(f"You selected {selected_role}")
        # Call the next step or function after role selection made in the main function
    else:
        st.write(" ⚠️ - press button to continue")

# Sub-role selection based on the selected user role
def sub_role_selection(selected_role, selected_sub_role):
    # clear_display()
    st.title(f"Select Sub-role for {selected_role}")
    
    # Define sub-roles for each user role (example data)
    sub_roles = {
        "Franchisee": ["Owner", "Operator"],
        "Management": ["CEO", "COO", "CFO", "CMO"],
        "Investor": ["General Partner", "Limited Partner", "Angel Investor"],
        "Employee": ["Facility Ops Staff","Technician", "Researcher", "Manager"],
        "Admin": ["General Admin", "Super Admin", "IT Support"]
    }

    if selected_role in sub_roles:
        selected_sub_role = st.radio("Choose a sub-role", sub_roles[selected_role])
        if st.button("Choose Action"):
           st.write(f"You selected the sub-role: {selected_sub_role}")
        else:
           st.write(" ⚠️ - press button to continue")

# Action selection screen
def action_selection(selected_role, selected_sub_role, selected_action):
    # clear_display()
    st.title(f"Actions available for {selected_role} - {selected_sub_role}")

    actions = ["View Dashboard", "Manage Finances", "Access Reports", "Edit Profile", "API calls"]
    
    selected_action = st.radio("Choose an action", actions)
    
    if st.button("choose Activity"):
        st.write(f"You selected the action: {selected_action}")
    else:
        st.write(" ⚠️ - press button to continue")

# Activity selection screen
def activity_selection(selected_role, selected_sub_role, selected_action, selected_activity):
    # clear_display()
    st.title(f"Activities for {selected_role} - {selectes_sub_role} - {selected_action}")
    
    activities = ["Update Settings", "View Analytics", "Export Data", "Manage Users", "Pull sensor data", "Analyze Sensor data", "Adjust component", "Calibrate"]
    
    selected_activity = st.radio("Choose an activity", activities)
    
    if st.button("Finalize"):
        is_valid, next_selection = validate_selection(selected_role, selected_sub_role, selected_action, selected_activity)
        
        if is_valid:
            st.write(f"Final choice: Role={selected_role}, Sub-role={selected_sub_role}, Action={selected_action}, Activity={selected_activity}")
            st.success("Journey completed successfully!")
            st.button("Logout", on_click=logout)
        else:
            st.error("Invalid combination. Please go back and change your selection.")
            if next_selection == "selected_role":
                selected_role = " "
                user_role_selection(selected_role)
            elif next_selection == "selected_sub_role":
                sub_role_selection(selected_role)
            elif next_selection == "selected_action":
                action_selection(selected_role, selected_sub_role)
            elif next_selection == "selected_activity":
                activity_selection(selected_role, selected_sub_role, selected_action)
            else:
                st.error("Unexpected error. Please start over.")
                return
                


# Logout function
def logout():
    st.session_state.logged_in = False
    st.rerun()  # Use st.rerun() here as well

if __name__ == "__main__":
    main()
