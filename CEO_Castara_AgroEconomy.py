import streamlit as st

# Placeholder for valid credentials (admin/password for testing)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

# Initialize session state variables
if "stage" not in st.session_state:
    st.session_state.stage = "login"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Define the main function that controls the flow
def main():
    content_placeholder = st.empty()  # Create a single placeholder for all content
    
    # Stage-based rendering using the placeholder
    if st.session_state.stage == "login":
        with content_placeholder.container():
            login(content_placeholder)
    elif st.session_state.stage == "role_selection":
        with content_placeholder.container():
            select_role(content_placeholder)
    elif st.session_state.stage == "sub_role_selection":
        with content_placeholder.container():
            select_sub_role(content_placeholder)
    elif st.session_state.stage == "action_selection":
        with content_placeholder.container():
            select_action(content_placeholder)
    elif st.session_state.stage == "activity_selection":
        with content_placeholder.container():
            select_activity(content_placeholder)

# Login function
def login(content_placeholder):
    st.image('Assets/Media/Images/Cover_page.jpg', use_column_width=True)
    st.title("Castara AgroEconomy Venture")

    # Input fields for username and password
    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")

    # Login button
    if st.button("Login"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.session_state.stage = "role_selection"  # Move to the next stage
        else:
            st.error("Invalid credentials. Please try again.")

# Role selection screen
def select_role(content_placeholder):
    st.title("Select Your Role")
    roles = ["Agricultural Engineers", "Horticulturists", "System Technicians", "Plant Scientists", "Operations Managers",
             "Maintenance Staff", "Quality Control Personnel", "Harvest Workers", "Climate Control Specialists",
             "Nutrient Management Specialists", "Franchise Operators", "Franchisors", "Management Personnel", "Investors"]
    selected_role = st.radio("Choose a role", roles)

    if st.button("Proceed"):
        st.session_state.selected_role = selected_role
        st.session_state.stage = "sub_role_selection"  # Move to the next stage

# Sub-role selection screen
def select_sub_role(content_placeholder):
    st.title(f"Select Sub-role for {st.session_state.selected_role}")
    sub_roles = ["Head of Agricultural Engineering", "Lead Horticulturist", "Systems Integration Engineer", "Plant Science Director",
                 "Operations Director", "Maintenance Supervisor", "Quality Assurance Manager", "Harvest Team Leader",
                 "Environmental Systems Manager", "Nutrient Systems Manager", "Data Analytics Manager", "Production Supervisor",
                 "Food Safety Compliance Officer", "Automation Engineer", "Plant Health Inspector", "Franchise Owner",
                 "Regional Franchise Manager", "Franchise Operations Director", "Chief Investment Officer", "Investment Manager"]
    selected_sub_role = st.radio("Choose a sub-role", sub_roles)

    if st.button("Choose Action"):
        st.session_state.selected_sub_role = selected_sub_role
        st.session_state.stage = "action_selection"  # Move to the next stage

# Action selection screen
def select_action(content_placeholder):
    st.title(f"Actions available for {st.session_state.selected_role} - {st.session_state.selected_sub_role}")
    actions = ["System Design & Optimization", "Environmental Parameter Monitoring", "Nutrient Solution Management",
               "Plant Health Assessment", "Growth Cycle Planning", "Equipment Maintenance", "Quality Control Inspections",
               "Harvest Scheduling", "Data Collection & Analysis", "Compliance Monitoring", "System Troubleshooting",
               "Resource Usage Optimization", "Production Planning", "Safety Protocol Implementation", "Team Coordination"]
    selected_action = st.radio("Choose an action", actions)

    if st.button("Choose Activity"):
        st.session_state.selected_action = selected_action
        st.session_state.stage = "activity_selection"  # Move to the next stage

# Activity selection screen
def select_activity(content_placeholder):
    st.title(f"Activity for {st.session_state.selected_role} - {st.session_state.selected_sub_role} - {st.session_state.selected_action}")
    activities = ["pH Level Monitoring", "Electrical Conductivity (EC) Testing", "Temperature Control Adjustment",
                  "Humidity Level Management", "Light Intensity Calibration", "Nutrient Mix Preparation", "Water Quality Testing",
                  "Growth Rate Documentation", "Equipment Sanitization", "System Flow Rate Checks", "Plant Spacing Optimization",
                  "Harvest Weight Recording", "Equipment Calibration", "Safety Inspection Rounds", "Inventory Management",
                  "Growth Data Recording", "Team Schedule Creation", "Maintenance Log Updates", "Quality Check Documentation",
                  "Compliance Report Generation"]
    selected_activity = st.radio("Choose an activity", activities)

    if st.button("Finalize"):
        st.session_state.selected_activity = selected_activity
        # Here you would add any validation for your selections, if necessary
        st.success(f"Journey completed successfully! Role={st.session_state.selected_role}, "
                   f"Sub-role={st.session_state.selected_sub_role}, Action={st.session_state.selected_action}, "
                   f"Activity={st.session_state.selected_activity}")
        st.button("Logout", on_click=logout)

# Logout function
def logout():
    st.session_state.clear()  # Clears all session states for a fresh start
    st.session_state.stage = "login"  # Return to login

if __name__ == "__main__":
    main()
