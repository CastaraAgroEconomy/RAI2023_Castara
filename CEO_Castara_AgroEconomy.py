import streamlit as st
from features.Truth_Table.truth_table_logic import validate_selection
from features.Utility.Clear_screen import clear_display

# Placeholder for valid credentials (admin/password for testing)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

# Define the main function that will control the flow
def main():
    # Display cover page image
    st.image('Assets/Media/Images/Cover_page.jpg', use_column_width=True)

# Navigation section start App with null parameters
    selected_role = " "
    selected_sub_role = " "
    selected_action = " "
    selected_activity = " "

    
    # Call_login_flag(selected_role)
    # Login function
    st.title("Castara AgroEconomy venture")
    
    # Input fields for username and password
    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")
    
    # Login button
    if st.button("Login"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.logged_in = True
            st.success("Login successful !")  # Display login success
        else:
            st.error("Invalid credentials. Please try again.")

    
    clear_display()

    
    # Call_user_role_flag(selected_role, selected_sub_role)
    # User role selection screen
    st.title("Select Your Role")

    roles = ["Agricultural Engineers", "Horticulturists", "System Technicians", "Plant Scientists", "Operations Managers",
     "Maintenance Staff", "Quality Control Personnel", "Harvest Workers", "Climate Control Specialists",
     "Nutrient Management Specialists", "Franchise Operators", "Franchisors", "Management Personnel", "Investors"]
    
    # Display radio buttons for role selection
    selected_role = st.radio("Choose a role", roles)
    
    # Proceed button
    if st.button("Proceed"):
        st.write(f"You selected {selected_role}")
    #   Call the next step or function after role selection made in the main function
        st.session_state.go_user = True
    #   selected_sub_role = " "
    #   sub_role_selection(selected_role, selected_sub_role)
    else:
        st.write("⚠️ - press button to continue")

    
    clear_display()

    
    # Call_sub_role_flag(selected_role, selected_sub_role, selected_action)
    # Sub-role selection based on the selected user role
    st.title(f"Select Sub-role for {selected_role}")

    # Define sub-roles for each user role (example data)
    sub_roles = ["Head of Agricultural Engineering", "Lead Horticulturist", "Systems Integration Engineer", "Plant Science Director",
     "Operations Director", "Maintenance Supervisor", "Quality Assurance Manager", "Harvest Team Leader",
     "Environmental Systems Manager", "Nutrient Systems Manager", "Data Analytics Manager", "Production Supervisor",
     "Food Safety Compliance Officer", "Automation Engineer", "Plant Health Inspector", "Franchise Owner",
     "Regional Franchise Manager", "Franchise Operations Director", "Chief Investment Officer", "Investment Manager"]
        
    selected_sub_role = st.radio("Choose a sub-role", sub_roles[selected_role])

    # sub_role_selection(selected_role, selected_sub_role)
    if st.button("Choose Action"):
        st.session_state.go_sub_role = True
        st.write(f"You selected the sub-role: {selected_sub_role}")
    #   selected_action = " "
    #   action_selection(selected_role, selected_sub_role, selected_action)
    else:
        st.write("⚠️ - press button to continue")

    
    clear_display()

    
    # Call_action_flag(selected_role, selected_sub_role, selected_action, selected_activity)
    # Action selection screen
    st.title(f"Actions available for {selected_role} - {selected_sub_role}")

    actions = ["System Design & Optimization", "Environmental Parameter Monitoring", "Nutrient Solution Management",
     "Plant Health Assessment", "Growth Cycle Planning", "Equipment Maintenance", "Quality Control Inspections",
     "Harvest Scheduling", "Data Collection & Analysis", "Compliance Monitoring", "System Troubleshooting",
     "Resource Usage Optimization", "Production Planning", "Safety Protocol Implementation", "Team Coordination"]
    selected_action = st.radio("Choose an action", actions)
    
    # action_selection(selected_role, selected_sub_role, selected_action)
    if st.button("choose Activity"):
        st.session_state.go_action = True
        st.write(f"You selected the action: {selected_action}")
        selected_activity = " "
    #   activity_selection(selected_role, selected_sub_role, selected_action, selected_activity)
    else:
        st.write("⚠️ - press button to continue")

    
    clear_display()


  # Activity selection screen

    st.title(f"Activities for {selected_role} - {selected_sub_role} - {selected_action}")
    activity = [pH Level Monitoring", "Electrical Conductivity (EC) Testing", "Temperature Control Adjustment",
     "Humidity Level Management", "Light Intensity Calibration", "Nutrient Mix Preparation", "Water Quality Testing",
     "Growth Rate Documentation", "Equipment Sanitization", "System Flow Rate Checks", "Plant Spacing Optimization",
     "Harvest Weight Recording", "Equipment Calibration", "Safety Inspection Rounds", "Inventory Management",
     "Growth Data Recording", "Team Schedule Creation", "Maintenance Log Updates", "Quality Check Documentation",
     "Compliance Report Generation"]
    selected_activity = st.radio("Choose an activity", activity)
    
    if st.button("Finalize"):
        is_valid, next_selection = validate_selection(selected_role, selected_sub_role, selected_action, selected_activity)
        
        if is_valid:
            st.session_state.go_activity = True
            st.write(f"Final choice: Role={selected_role}, Sub-role={selected_sub_role}, Action={selected_action}, Activity={selected_activity}")
            st.success("Journey completed successfully!")
            st.button("Logout", on_click=logout)
        else:
            st.error("Invalid combination. Please go back and change your selection.")
            if next_selection == "selected_role":
                selected_role = " "
                st.session_state.go_user = False
            #   user_role_selection(selected_role)
            elif next_selection == "selected_sub_role":
                selected_sub_role = " "
                st.session_state.go_sub_role = False
            #   sub_role_selection(selected_role, selected_sub_role)
            elif next_selection == "selected_action":
                selected_action = " "
                st.session_state.go_action = False
            #   action_selection(selected_role, selected_sub_role, selected_action)
            elif next_selection == "selected_activity":
                selected_activity = " "
                st.session_state.go_activity = False
            #   activity_selection(selected_role, selected_sub_role, selected_action, selecity_activity)
            else:
                st.error("Unexpected error. Please start over.")



# Inital Dashboard display section


    
# Call login flag function to set flag and select login and user_role
def Call_login_flag(selected_role):

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        
    #  if not st.session_state.logged_in:
    #  login()  # Go to login page if not logged in
    else:
    #    selected_role = " "
    #    user_role_selection(selected_role)  # Proceed to user role selection if logged in
         st.write("⚠️ - you are already logged in")
    return



# Call user_role flag function to set flag and run to select role and sub_role 
def Call_user_role_flag(selected_role, selected_sub_role):
    if 'go_user' not in st.session_state:
        st.session_state.go_user = False
        
        if not st.session_state.go_user:
    #      selected_role = " "
    #      user_role_selection(selected_role)  # Go to user_role page if list not selected
           st.write("⚠️ - Select a role")
    else:
    #   selected_sub_role = " "
    #   sub_role_selection(selected_role, selected_sub_role)  # Go to sub-user role selection if go_user set
        st.write("⚠️ - default pre-selected, you may change")
    return


    
    
# Call user sub_role flag function to set the flag and run to select sub_role and action
def Call_sub_role_flag(selected_role, selected_sub_role, selected_action):
    if 'go_sub_role' not in st.session_state:
        st.session_state.go_sub_role = False
        
        if not st.session_state.go_sub_role:
    #      selected_sub_role = " "
    #      sub_role_selection(selected_role, selected_sub_role) # Go to sub-user role page if go_sub_role not set
           st.write("⚠️ - Select a sub-role")
    else:
    #    selected_action = " "
    #    action_selection(selected_role, selected_sub_role, selected_action)  # Go to action selection page if go_sub_role set
         st.write("⚠️ - default pre-selected, you may change")
    return




# Call action flag function to set flag and select action and activities
def Call_action_flag(selected_role, selected_sub_role, selected_action,selected_activity):
    if 'go_action' not in st.session_state:
        st.session_state.go_action = False
        
        if not st.session_state.go_action:
    #      selected_action = " "
    #      action_selection(selected_role, selected_sub_role) # Go to activity page if go_activity not set
           st.write("⚠️ - Select an action")
    else:
    #   selected_activity = " "
    #   activity_selection(selected_role, selected_sub_role, selected_action, selected_activity)  # Go to activity selection page if go_activity set
        st.write("⚠️ - default pre-selected, you may change")
    return



# Logout function
def logout():
    st.session_state.logged_in = False
    st.rerun()  # Use st.rerun() here as well

if __name__ == "__main__":
    main()
