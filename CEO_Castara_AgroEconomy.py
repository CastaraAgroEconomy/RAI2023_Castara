import streamlit as st

# Placeholder for valid credentials (admin/password for testing)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

# Define the main function that will control the flow
def main():

    placeholder = st.empty()
    
    # Display cover page image
    st.image('Assets/Media/Images/Cover_page.jpg', use_column_width=True)

# Navigation section start App with null parameters
    selected_role = " "
    selected_sub_role = " "
    selected_action = " "
    selected_activity = " "

    
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

    
    placeholder.empty()

    
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
        st.session_state.selected_role = selected_role
    else:
        st.write("⚠️ - press button to continue")

    
    placeholder.empty()

    
    # Sub-role selection based on the selected user role
    st.title(f"Select Sub-role for {selected_role}")

    # Define sub-roles for each user role (example data)
    sub_roles = ["Head of Agricultural Engineering", "Lead Horticulturist", "Systems Integration Engineer", "Plant Science Director", 
    "Operations Director", "Maintenance Supervisor", "Quality Assurance Manager", "Harvest Team Leader", 
    "Environmental Systems Manager", "Nutrient Systems Manager", "Data Analytics Manager", "Production Supervisor", 
    "Food Safety Compliance Officer", "Automation Engineer", "Plant Health Inspector", "Franchise Owner", 
    "Regional Franchise Manager", "Franchise Operations Director", "Chief Investment Officer", "Investment Manager"]
        
    selected_sub_role = st.radio("Choose a sub-role", sub_roles)

    # sub_role_selection(selected_role, selected_sub_role)
    if st.button("Choose Action"):
        st.write(f"You selected the sub-role: {selected_sub_role}")
        st.session_state.selected_sub_role = selected_sub_role
    else:
        st.write("⚠️ - press button to continue")

    
    placeholder.empty()

    
    # Action selection screen
    st.title(f"Actions available for {selected_role} - {selected_sub_role}")

    actions = ["System Design & Optimization", "Environmental Parameter Monitoring", "Nutrient Solution Management", 
    "Plant Health Assessment", "Growth Cycle Planning", "Equipment Maintenance", "Quality Control Inspections", 
    "Harvest Scheduling", "Data Collection & Analysis", "Compliance Monitoring", "System Troubleshooting", 
    "Resource Usage Optimization", "Production Planning", "Safety Protocol Implementation", "Team Coordination"]
    selected_action = st.radio("Choose an action", actions)
    
    # action_selection(selected_role, selected_sub_role, selected_action)
    if st.button("choose Activity"):
       st.write(f"You selected the action: {selected_action}")
       st.session_state.selected_action = selected_action
       selected_activity = " "
    else:
        st.write("⚠️ - press button to continue")

    
    placeholder.empty()


  # Activity selection screen

    st.title(f"Activity for {selected_role} - {selected_sub_role} - {selected_action}")
    activity = ["pH Level Monitoring", "Electrical Conductivity (EC) Testing", "Temperature Control Adjustment", 
    "Humidity Level Management", "Light Intensity Calibration", "Nutrient Mix Preparation", "Water Quality Testing", 
    "Growth Rate Documentation", "Equipment Sanitization", "System Flow Rate Checks", "Plant Spacing Optimization", 
    "Harvest Weight Recording", "Equipment Calibration", "Safety Inspection Rounds", "Inventory Management", 
    "Growth Data Recording", "Team Schedule Creation", "Maintenance Log Updates", "Quality Check Documentation", 
    "Compliance Report Generation"]
    selected_activity = st.radio("Choose an activity", activity)
    
    if st.button("Finalize"):
        st.session_state.selected_activity = selected_activity  
        
    # Change required to next line. Set and use session_state values in lieu of calling valid_selection function
        is_valid == st.session_state.R_go_nogo
        
        if is_valid:
            st.write(f"Final choice: Role={selected_role}, Sub-role={selected_sub_role}, Action={selected_action}, Activity={selected_activity}")
            st.success("Journey completed successfully!")
            st.button("Logout", on_click=logout)
        else:
            st.error("Invalid combination. Please go back and change your selection.")
            if next_selection == "selected_role":
                selected_role = " "
            elif next_selection == "selected_sub_role":
                selected_sub_role = " "
            elif next_selection == "selected_action":
                selected_action = " "
            elif next_selection == "selected_activity":
                selected_activity = " "
            else:
                st.error("Unexpected error. Please start over.")


    placeholder.empty()


# Call appropriate feature function for User's journey


# Logout function
def logout():
    st.session_state.logged_in = False
    st.rerun()  # Use st.rerun() here as well

if __name__ == "__main__":
    main()
