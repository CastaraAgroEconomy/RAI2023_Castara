import streamlit as st

# Placeholder for valid credentials (admin/password for testing)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

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

if 'R_go' not in st.session_state:
    st.session_state.R_go = False
        
# from features.Truth_Table.truth_table_logic import gen_tab
# from features.Validation.valid_selection import check_for_valid_match

# Define the main function that controls the flow
def main():

# Initialize session state variables
    if "stage" not in st.session_state:
        st.session_state.stage = "login"
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
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

    # Login button with on_click function to advance stage
    if st.button("Login", on_click=lambda: login_check(username, password)):
        pass  # Placeholder to hold button logic; action is in login_check

def login_check(username, password):
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        st.session_state.logged_in = True
        st.session_state.stage = "role_selection"  # Move to the next stage
        st.success("Login successful!")
    else:
        st.error("Invalid credentials. Please try again.")

# Role selection screen
def select_role(content_placeholder):
    st.title("Select Your Role")
    roles = ["Agricultural Engineers", "Horticulturists", "System Technicians", "Plant Scientists", "Operations Managers",
             "Maintenance Staff", "Quality Control Personnel", "Harvest Workers", "Climate Control Specialists",
             "Nutrient Management Specialists", "Franchise Operators", "Franchisors", "Management Personnel", "Investors"]
    selected_role = st.radio("Choose a role", roles)

    if st.button("Proceed", on_click=lambda: set_stage("sub_role_selection", "selected_role", selected_role)):
        pass

# Sub-role selection screen
def select_sub_role(content_placeholder):
    st.title(f"Select Sub-role for {st.session_state.selected_role}")
    sub_roles = ["Head of Agricultural Engineering", "Lead Horticulturist", "Systems Integration Engineer", "Plant Science Director",
                 "Operations Director", "Maintenance Supervisor", "Quality Assurance Manager", "Harvest Team Leader",
                 "Environmental Systems Manager", "Nutrient Systems Manager", "Data Analytics Manager", "Production Supervisor",
                 "Food Safety Compliance Officer", "Automation Engineer", "Plant Health Inspector", "Franchise Owner",
                 "Regional Franchise Manager", "Franchise Operations Director", "Chief Investment Officer", "Investment Manager"]
    selected_sub_role = st.radio("Choose a sub-role", sub_roles)

    if st.button("Choose Action", on_click=lambda: set_stage("action_selection", "selected_sub_role", selected_sub_role)):
        pass

# Action selection screen
def select_action(content_placeholder):
    st.title(f"Actions available for {st.session_state.selected_role} - {st.session_state.selected_sub_role}")
    actions = ["System Design & Optimization", "Environmental Parameter Monitoring", "Nutrient Solution Management",
               "Plant Health Assessment", "Growth Cycle Planning", "Equipment Maintenance", "Quality Control Inspections",
               "Harvest Scheduling", "Data Collection & Analysis", "Compliance Monitoring", "System Troubleshooting",
               "Resource Usage Optimization", "Production Planning", "Safety Protocol Implementation", "Team Coordination"]
    selected_action = st.radio("Choose an action", actions)

    if st.button("Choose Activity", on_click=lambda: set_stage("activity_selection", "selected_action", selected_action)):
        pass

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

    if st.button("Finalize", on_click=lambda: finalize_selection(selected_activity)):
        pass

def set_stage(stage, key, value):
    st.session_state[key] = value
    st.session_state.stage = stage

def finalize_selection(activity):
    st.session_state.selected_activity = activity
    # gen_tab(self, R_go, selected_role, selected_sub_role, selected_action, selected_activity)
    # check_for_valid_match(R_go, selected_role, selected_sub_role, selected_action, selected_activity)
    

    if 'R_go' == True:
        st.success(f"Journey completed successfully! Role={st.session_state.selected_role}, "
        f"Sub-role={st.session_state.selected_sub_role}, Action={st.session_state.selected_action}, "
        f"Activity={st.session_state.selected_activity}") 
        st.write("⚠️ - When implemented, appropriate feature will activate at this point")
        st.button("Logout", on_click=logout)
    else:
        st.write("⚠️ - Testing system navigation; returning to first list")
        content_placeholder = st.empty()
        selected_role = " "
        selected_sub_role = " "
        selected_action = " "
        selected_activity = " "
        "Proceed" = False
        select_role(content_placeholder)
        content_placeholder = st.empty()
        "Choose Action" = False
        select_sub_role(content_placeholder)
        "Choose Activity" = False
        content_placeholder = st.empty()
        select_action(content_placeholder)
        "Finalize" = False
        content_placeholder = st.empty()
        select_activity(content_placeholder)
        content_placeholder = st.empty()
        selected_role = " "
        selected_sub_role = " "
        selected_action = " "
        selected_activity = " "
        return

# Logout function
def logout():
    st.session_state.clear()  # Clears all session states for a fresh start
    st.session_state.stage = "login"  # Return to login

if __name__ == "__main__":
    main()
