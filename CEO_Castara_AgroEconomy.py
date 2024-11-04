# Main Script and function call for the Castara AgroEconomy Mobile App.
import streamlit as st
import numpy as np

# Placeholder for valid credentials (admin/password for testing)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

#   Initilization of session variables

if 'n' not in st.session_state:
    st.session_state.n = 1

if 'x' not in st.session_state:
    st.session_state.x = 1

if 'm' not in st.session_state:
    st.session_state.m = 1

if 'y' not in st.session_state:
    st.session_state.y = 1

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
    st.session_state.R_go = 0

if 'return_to_main' not in st.session_state:
    st.session_state.return_to_main = False

if 'live' not in st.session_state:
    st.session_state.live = " "


# The two instructions beliw were part if the  Main script of 
# the App session's initilization of the first Module :-
# from RAI2023_Castara.features.Truth_Table.rules_logic import TruthTable
# R = TruthTable()
# They provided for call up of rules_logic.py



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
    elif st.session_state.return_to_main == False:
           if st.session_state.stage == "activity_selection":
              with content_placeholder.container():
                  select_activity(content_placeholder)
             
# =========================
# Returned to main Module :-
# =========================
   
    if st.session_state.R_go == 1:
        with content_placeholder.container():
            st.success(f"Journey completed successfully! Role={st.session_state.selected_role}, "
            f"Sub-role={st.session_state.selected_sub_role}, Action={st.session_state.selected_action}, "
            f"Activity={st.session_state.selected_activity}") 
            
            st.write(" ")
            st.write("⚠️ - When implemented, appropriate feature will activate at this point")
            
            st.session_state.logged_in = True
            st.session_state.stage = "role_selection"
            st.session_state.R_go = 0
    elif st.session_state.stage == "select_activity":
        with content_placeholder.container():        
            st.write(" ")
            st.write("⚠️ - Testing system navigation; feature's function not yet implemented.")
            
            st.write(" ")
            st.write("⚠️ - Currently, you will need to logout and login again, to select different combinations of options.")
            
            st.write(" ")
            st.write("In future, the system will return you to the list which causes the first invalid combination to occur as a result of a selection from that list")
            st.write("Eventually, by the launch release, version 1.xx, only valid options will be presented based on the selected option in the prior presented list")
            
            if st.button("Logout", on_click=lambda: logout()):
                pass
            st.session_state.stage = None
            st.session_state.logged_in = False     

    
# ===================
# End of main Module :-
# ===================



# =========================
# Beginning of first Module :-
# =========================

def Module_1():

# This script does the following: -
#	1.	Builds the Truth Table by iterating through combinations of n, x, m, and y.
#	2.	Validates each combination using the is_valid_combination function from Rules.py.
#	3.	Checks selections in the finalize_selection function, with error handling to guide users back to the selection that needs adjustment.
#	4.	Maintains existing functionalities (no code removed unnecessarily), ensuring that parts like session state handling, error messaging, and st.success()/st.error() remain.

    st.write(" ")
    st.write("⚠️ - Entered Module 1")
    
# Initialize session state variables if not already present
    for key, default in {
        'n': 1, 'x': 1, 'm': 1, 'y': 1,
        'selected_role': None, 'selected_sub_role': None,
        'selected_action': None, 'selected_activity': None,
        'self': None, 'R_go': 0
    }.items():
        if key not in st.session_state:
            st.session_state[key] = default

    st.write(" ")
    st.write("⚠️ - Defining Truth Table Class")
    
    
    class TruthTable:
        def __init__(self, n=14, x=31, m=30, y=35):
            
            st.write("debug 1 - defined __init__ ")
            
            self.n = n
            self.x = x
            self.m = m
            self.y = y
            
            st.write("debug 2 - about to create np table of zeros")
            self.table = np.zeros((n, x, m, y), dtype=int)
            st.write("debug 3 - array created ")
            self.generate_table()
            st.write("debug 4 - general table creation completed ")

            st.write("⚠️ - Generating Truth Table with predefined validation rules")

        def generate_table(self):
            st.write("debug 5 - Repopulating general table")
            try:
                for n in range(self.n):
                    st.write(f"debug 6: Processing n={n}")
                    for x in range(self.x):
                        for m in range(self.m):
                            for y in range(self.y):
                                st.write(f"debug 7: Processing point ({n},{x},{m},{y})")
                                is_valid = self.validate_choice(
                                    st.session_state.selected_role,
                                    st.session_state.selected_sub_role,
                                    st.session_state.selected_action,
                                    st.session_state.selected_activity
                                )
                                st.write("debug 8: validated choice returned")
                                self.table[n, x, m, y] = int(bool(is_valid))
            
            except Exception as e:
                st.error(f"Error in generate_table: {str(e)}")
                raise  # This will show the full error traceback
        
            st.write(" ")
            st.write("⚠️ - Initial Table complete ")
            
            if validate_selection(self, n, x, m, y):
                st.success("Valid combination!")
            else:
                next_step = get_next_valid_selection(self, n, x, m, y)
                st.error(f"Invalid combination. Please re-select your {next_step}.")

            st.session_state.return_to_main = True
            return



        def validate_choice(self, selected_role, selected_sub_role, selected_action, selected_activity):
            """Validate the selection by checking if the combination matches valid rules."""
        
            st.write(" ")
            st.write("⚠️ - Preparing to validate chosen items as a four item combination ")
        
            Module_3()
        
            return is_valid_combination(self, selected_role, selected_sub_role, selected_action, selected_activity)


        
        def get_next_valid_selection(self, n, x, m, y):
            
#       Function to identify the next level within invalid choices and returns it
        
            if self.table[n, :, :, :].max() == 0:
                return "role"
            elif self.table[n, x, :, :].max() == 0:
                return "sub_role"
            elif self.table[n, x, m, :].max() == 0:
                return "action"
            else:
                return "activity"

    
        def validate_selection(self, n, x, m, y):

#       Function to validate selection       
#       Uses the validate_choice function to determine if selection is valid

            st.write(" ")
            st.write("⚠️ - Confirming valid combination; searching")

            Module_2()
            
            is_valid = is_valid_combination(
                st.session_state.selected_role,
                st.session_state.selected_sub_role,
                st.session_state.selected_action,
                st.session_state.selected_activity
            )

            st.write(" ") 
            st.write("⚠️ - Truth Table consulted ")
    
            st.write(" ")
            st.write("⚠️ - Returning execution to central App ")
        
            if is_valid:
                st.session_state.R_go = 1
            else:
                st.session_state.R_go = 0
            return is_valid
            

#   Create instance after class definition
    st.write("debug 0 - About to create TruthTable instance")
    truth_table = TruthTable()  # This line was missing         
    st.write("debug 9: Table generation complete")


        
# =====================
# End of first Module :
# ===================== 



# ==========================
# Beginning of second Module :-
# ==========================

def Module_2():

# This script defines the options in the four lists 
# and provides functions to validate user selections against a Truth Table

# import itertools
# import pandas as pd

# from RAI2023_Castara.features.Validation.Rules import is_valid_combination

# Define lists A, B, C, and D

    st.write(" ")
    st.write("⚠️ - Entered Module 2 ")
    
    A = ["Agricultural Engineers", "Horticulturists", "System Specialist", "Plant Scientists", "Operations Personnel",
         "Maintenance Staff", "Quality Control Personnel", "Harvest Workers", "Climate Control Specialists",
         "Nutrient Management Specialists", "Franchise Operators", "Franchisors", "Management Personnel", "Investors"]

    B = ["Head of Agricultural Engineering", "Lead Horticulturist", "Systems Integration Engineer", "Plant Science Director", "Operations Director", 
         "Operations Managers", "Maintenance Supervisor", "Quality Assurance Manager", "Harvest Team Leader", "Environmental Systems Manager", "Nutrient Systems Manager", 
         "Data Analytics Manager", "Production Supervisor", "Food Safety Compliance Officer", "Automation Engineer", "Plant Health Inspector", 
         "Franchise Owner", "Regional Franchise Manager", "Franchise Operations Director", "Chief Investment Officer", "Investment Manager", 
         "Portfolio Manager", "Executive Director", "Chief Operations Officer", "Chief Financial Officer", "Business Development Manager", 
         "Franchise Development Director", "Investment Analyst", "Financial Controller", "Franchise Compliance Manager", "Investor Relations Manager"] 

    C = ["System Design & Optimization", "Environmental Parameter Monitoring", "Nutrient Solution Management", "Plant Health Assessment", "Growth Cycle Planning", 
         "Equipment Maintenance", "Quality Control Inspections", "Harvest Scheduling", "Data Collection & Analysis", "Compliance Monitoring",
         "System Troubleshooting", "Resource Usage Optimization", "Production Planning", "Safety Protocol Implementation", "Team Coordination", 
         "Investment Performance Monitoring", "Franchise Performance Review", "Financial Analysis", "Business Expansion Planning", "Franchise Agreement Management", 
         "Risk Assessment", "Return on Investment Analysis", "Franchise Standards Enforcement", "Capital Allocation", "Market Analysis", "Investor Reporting",
         "Franchise Training Program Management", "Performance Metrics Review", "Strategic Planning", "Compliance Auditing" ]

    D = ["pH Level Monitoring", "EC - Electrical Conductivity - Testing", "Temperature Control Adjustment", "Humidity Level Management", "Light Intensity Calibration", 
         "Nutrient Mix Preparation", "Water Quality Testing", "Growth Rate Documentation", "Equipment Sanitization", "System Flow Rate Checks", "Plant Spacing Optimization", 
         "Harvest Weight Recording", "Equipment Calibration", "Safety Inspection Rounds", "Inventory Management", "Growth Data Recording", "Team Schedule Creation", 
         "Maintenance Log Updates", "Quality Check Documentation", "Compliance Report Generation", "Investment Portfolio Review", "Franchise Audit Execution", 
         "Financial Statement Analysis", "Market Research Documentation", "Franchise Agreement Review", "Risk Assessment Reports", "ROI Calculations", "Standards Compliance Checks", 
         "Capital Distribution Planning", "Market Trend Analysis", "Investor Report Generation", "Training Program Development", "Performance Metric Tracking", 
         "Strategy Document Creation", "Compliance Report Filing"]

    def get_roles():
        return A

    def get_sub_roles():
        return B

    def get_actions():
        return C

    def get_activities():
        return D

# ======================
# End of second Module :
# ======================



# ==========================
# Begining of Third Module :-
# ==========================

def Module_3():

# Defines the rules for determining if a combination of selected options is a valud one.
# import streamlit as st

    def is_valid_combination(selected_role, selected_sub_role, selected_action, selected_activity):
    
        st.write(" ")
        st.write("⚠️ - Entered Module 3 ")
        
        st.write(" ")
        st.write("⚠️ - One moment please, verifying validity of combination picked from list against Truth Table  ")

    # Rule 1: Only Agricultural Engineers and System Technicians can perform System Design & Optimization
        if selected_action == "System Design & Optimization" and selected_role not in ["Agricultural Engineers", "System Technicians"]:
            return 0
    # Rule 2: Franchise Operators should not perform technical activities like Nutrient Mix Preparation
        if selected_role == "Franchise Operators" and selected_activity in ["Nutrient Mix Preparation", "pH Level Monitoring"]:
            return 0
    # Rule 3: Plant Scientists should focus on Plant Health Assessment and Growth Cycle Planning
        if selected_role == "Plant Scientists" and selected_action not in ["Plant Health Assessment", "Growth Cycle Planning"]:
            return 0
    # Rule 4: Quality Assurance Manager should focus on Quality Control Inspections and Compliance Monitoring
        if selected_sub_role == "Quality Assurance Manager" and selected_action not in ["Quality Control Inspections", "Compliance Monitoring"]:
            return 0
    # Rule 5: Franchise Owners should focus on business-related actions like Franchise Performance Review
        if selected_role == "Franchise Operators" and selected_action not in ["Franchise Performance Review", "Business Expansion Planning"]:
            return 0
    # Rule 6: Operations Managers should handle actions like Production Planning and Team Coordination
        if selected_role == "Operations Managers" and selected_action not in ["Production Planning", "Team Coordination"]:
            return 0
    
    # Default valid if no rule invalidates it
        return 1

# =====================
# End of Third Module :
# =====================



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
    return

def login_check(username, password):
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        st.session_state.logged_in = True
        st.session_state.stage = "role_selection"  # Move to the next stage
        st.success("Login successful!")
    else:
        st.error("Invalid credentials. Please try again.")
    return

# Role selection screen
def select_role(content_placeholder):
    st.title("Select Your Role")
    
    roles = ["Agricultural Engineers", "Horticulturists", "System Specialists", "Plant Scientists", "Operations Personnel",
             "Maintenance Staff", "Quality Control Personnel", "Harvest Workers", "Climate Control Specialists",
             "Nutrient Management Specialists", "Franchise Operators", "Franchisors", "Management Personnel", "Investors"]
    
    selected_role = st.radio("Choose a role", roles)

    if st.button("Proceed", on_click=lambda: set_stage("sub_role_selection", "selected_role", selected_role)):
        pass
    return
    

# Sub-role selection screen
def select_sub_role(content_placeholder):
    st.title(f"Select Sub-role for {st.session_state.selected_role}")
    
    sub_roles = ["Head of Agricultural Engineering", "Lead Horticulturist", "Systems Integration Engineer", "Plant Science Director", 
    "Operations Director", "Operations Manager", "Maintenance Supervisor", "Quality Assurance Manager", "Harvest Team Leader", "Environmental Systems Manager", 
    "Nutrient Systems Manager", "Data Analytics Manager", "Production Supervisor", "Food Safety Compliance Officer", "Automation Engineer", 
    "Plant Health Inspector", "Franchise Owner", "Regional Franchise Manager", "Franchise Operations Director", "Chief Investment Officer", 
    "Investment Manager", "Portfolio Manager", "Executive Director", "Chief Operations Officer", "Chief Financial Officer", "Business Development Manager", 
    "Franchise Development Director", "Investment Analyst", "Financial Controller", "Franchise Compliance Manager", 
    "Investor Relations Manager"]
    
    selected_sub_role = st.radio("Choose a sub-role", sub_roles)

    if st.button("Choose Action", on_click=lambda: set_stage("action_selection", "selected_sub_role", selected_sub_role)):
        pass
    return
    

# Action selection screen
def select_action(content_placeholder):
    st.title(f"Actions available for {st.session_state.selected_role} - {st.session_state.selected_sub_role}")
    
    actions = ["System Design & Optimization", "Environmental Parameter Monitoring", "Nutrient Solution Management", "Plant Health Assessment", 
    "Growth Cycle Planning", "Equipment Maintenance", "Quality Control Inspections", "Harvest Scheduling", "Data Collection & Analysis", 
    "Compliance Monitoring", "System Troubleshooting", "Resource Usage Optimization", "Production Planning", "Safety Protocol Implementation", 
    "Team Coordination", "Investment Performance Monitoring", "Franchise Performance Review", "Financial Analysis", "Business Expansion Planning", 
    "Franchise Agreement Management", "Risk Assessment", "Return on Investment Analysis", "Franchise Standards Enforcement", "Capital Allocation", 
    "Market Analysis", "Investor Reporting", "Franchise Training Program Management", "Performance Metrics Review", "Strategic Planning", "Compliance Auditing" ]
    
    selected_action = st.radio("Choose an action", actions)

    if st.button("Choose Activity", on_click=lambda: set_stage("activity_selection", "selected_action", selected_action)):
        pass
    return
    

# Activity selection screen
def select_activity(content_placeholder):
    st.title(f"Activity for {st.session_state.selected_role} - {st.session_state.selected_sub_role} - {st.session_state.selected_action}")
    
    activities = ["pH Level Monitoring", "EC - Electrical Conductivity - Testing", "Temperature Control Adjustment", "Humidity Level Management", 
    "Light Intensity Calibration", "Nutrient Mix Preparation", "Water Quality Testing", "Growth Rate Documentation", "Equipment Sanitization", 
    "System Flow Rate Checks", "Plant Spacing Optimization", "Harvest Weight Recording", "Equipment Calibration", "Safety Inspection Rounds", 
    "Inventory Management", "Growth Data Recording", "Team Schedule Creation", "Maintenance Log Updates", "Quality Check Documentation", 
    "Compliance Report Generation", "Investment Portfolio Review", "Franchise Audit Execution", "Financial Statement Analysis", "Market Research Documentation", 
    "Franchise Agreement Review", "Risk Assessment Reports", "ROI Calculations", "Standards Compliance Checks", "Capital Distribution Planning", 
    "Market Trend Analysis", "Investor Report Generation", "Training Program Development", "Performance Metric Tracking", "Strategy Document Creation", "Compliance Report Filing"]
    
    selected_activity = st.radio("Choose an activity", activities)

    if st.button("Finalize", on_click=lambda: finalize_selection(selected_activity)):
        pass
    
    return
        

def set_stage(stage, key, value):
    st.session_state[key] = value
    st.session_state.stage = stage
    return


def finalize_selection(selected_activity): 
    st.session_state.selected_activity = selected_activity

#   Begin selection validity check
    st.write(" ")
    st.write("⚠️ - Control passed to validity checker ")
    st.write(" ")
    st.write("⚠️ - Selected combination being validated ")
    
    Module_1()
    return
    


# Logout function
def logout():
    st.session_state.clear()  # Clears all session states for a fresh start
    st.session_state.stage = "login"  # Return to login

if __name__ == "__main__":
    main()
