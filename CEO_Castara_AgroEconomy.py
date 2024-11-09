# Main Script and function call for the Castara AgroEconomy Mobile App.
import streamlit as st
import numpy as np

# Placeholder for valid credentials (admin/password for testing)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

#   Initilization of session variables

# ==========================
# Beginning of second Module :-
# ==========================

# This script defines the options in the four lists 
# and provides functions to validate user selections against a Truth Table

    
# Initialize matrices A, B, C & D in session_state if not already there

if 'A' not in st.session_state:
    st.session_state.A = ["Agricultural Engineers", "Horticulturists", "System Specialist", "Plant Scientists", "Operations Personnel",
                          "Maintenance Staff", "Quality Control Personnel", "Harvest Workers", "Climate Control Specialists",
                          "Nutrient Management Specialists", "Franchisors", "Franchisees", "Management Personnel", "Investors"]

# Initialize matrices in session_state if not already there
if 'B' not in st.session_state:
    st.session_state.B = ["Head of Agricultural Engineering", "Lead Horticulturist", "Systems Integration Engineer", "Plant Science Director", "Operations Director", 
                          "Operations Manager", "Maintenance Supervisor", "Quality Assurance Manager", "Harvest Team Leader", "Environmental Systems Manager", "Nutrient Systems Manager", 
                          "Data Analytics Manager", "Production Supervisor", "Food Safety Compliance Officer", "Automation Engineer", "Plant Health Inspector", 
                          "Franchise Owner", "Franchise Operator", "Regional Franchise Manager", "Franchise Operations Director", "Chief Investment Officer", "Investment Manager", 
                          "Portfolio Manager", "Chief Executive Officer",  "Chief Operations Officer", "Chief Financial Officer", "Business Development Manager", 
                          "Franchise Development Director", "Investment Analyst", "Financial Controller", "Franchise Compliance Manager", "Investor Relations Manager", "Limited Partner"] 

# Initialize matrices in session_state if not already there
if 'C' not in st.session_state:
    st.session_state.C = ["System Design & Optimization", "Environmental Parameter Monitoring", "Nutrient Solution Management", "Plant Health Assessment", "Growth Cycle Planning", 
                          "Equipment Maintenance", "Quality Control Inspections", "Harvest Scheduling", "Data Collection & Analysis", "Compliance Monitoring",
                          "System Troubleshooting", "Resource Usage Optimization", "Production Planning", "Safety Protocol Implementation", "Team Coordination", 
                          "Investment Performance Monitoring", "Franchise Performance Review", "Financial Analysis", "Business Expansion Planning", "Franchise Agreement Management", 
                          "Risk Assessment", "Return on Investment Analysis", "Franchise Standards Enforcement", "Capital Allocation", "Market Analysis", "Investor Reporting",
                          "Franchise Training Program Management", "Performance Metrics Review", "Strategic Planning", "Compliance Auditing" ]

# Initialize matrices in session_state if not already there
if 'D' not in st.session_state:
    st.session_state.D = ["pH Level Monitoring", "EC - Electrical Conductivity - Testing", "Temperature Control Adjustment", "Humidity Level Management", "Light Intensity Calibration", 
                          "Nutrient Mix Preparation", "Water Quality Testing", "Growth Rate Documentation", "Equipment Sanitization", "System Flow Rate Checks", "Plant Spacing Optimization", 
                          "Harvest Weight Recording", "Equipment Calibration", "Safety Inspection Rounds", "Inventory Management", "Growth Data Recording", "Team Schedule Creation", 
                          "Maintenance Log Updates", "Quality Check Documentation", "Compliance Report Generation", "Investment Portfolio Review", "Franchise Audit Execution", 
                          "Financial Statement Analysis", "Market Research Documentation", "Franchise Agreement Review", "Risk Assessment Reports", "ROI Calculations", "Standards Compliance Checks", 
                          "Capital Distribution Planning", "Market Trend Analysis", "Investor Report Generation", "Training Program Development", "Performance Metric Tracking", 
                          "Strategy Document Creation", "Compliance Report Filing"]


# Initialize defaults for selected items only if matrices are loaded
if 'selected_role' not in st.session_state and 'A' in st.session_state and st.session_state.A:
    st.session_state.selected_role = st.session_state.A[0]

if 'selected_sub_role' not in st.session_state and 'B' in st.session_state and st.session_state.B:
    st.session_state.selected_sub_role = st.session_state.B[0]

if 'selected_action' not in st.session_state and 'C' in st.session_state and st.session_state.C:
    st.session_state.selected_action = st.session_state.C[0]

if 'selected_activity' not in st.session_state and 'D' in st.session_state and st.session_state.D:
    st.session_state.selected_activity = st.session_state.D[0]

# ======================
# End of second Module :
# ======================


# Initalization of other variables in session_stats :-

if 'n' not in st.session_state:
    st.session_state.n = 1

if 'x' not in st.session_state:
    st.session_state.x = 1

if 'm' not in st.session_state:
    st.session_state.m = 1

if 'y' not in st.session_state:
    st.session_state.y = 1

if 'selected_role' not in st.session_state:
    st.session_state.selected_role = st.session_state.A[0]
    
if 'selected_sub_role' not in st.session_state:
    st.session_state.selected_sub_role = st.session_state.B[0]

if 'selected_action' not in st.session_state:
    st.session_state.selected_action = st.session_state.C[0]

if 'selected_activity' not in st.session_state:
    st.session_state.selected_activity = st.session_state.D[0]

if 'self' not in st.session_state:
    st.session_state.self = None

if 'R_go' not in st.session_state:
    st.session_state.R_go = 0

if 'return_to_main' not in st.session_state:
    st.session_state.return_to_main = False

if 'live' not in st.session_state:
    st.session_state.live = " "



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
    elif st.session_state.return_to_main == False:
                    with content_placeholder.container():
                        finalize_selection (content_placeholder)

    


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
    elif st.session_state.stage == "finalize_selection":
        with content_placeholder.container():        
            st.write(" ")
            st.write("⚠️ - Testing system navigation; feature's function not yet implemented.")
            
            st.write(" ")
            st.write("⚠️ - Currently, you will need to logout and login again, to select different User Role")
            
            st.write(" ")
            st.write("However, the system will return you to the list which causes the first invalid combination to occur, other than the User's Role, as a result of an invalid item being selected.")
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
        'self': None, 'R_go': 0, 'return_to_main' : False, 'live' : " "
    }.items():
        if key not in st.session_state:
            st.session_state[key] = default

    st.write(" ")
    st.write("⚠️ - Defining Truth Table Class")
    
    
    class TruthTable:
        def __init__(self, n=2, x=2, m=2, y=2):
            
            st.write("debug 1 - defined 'init' ")
            
            self.n = n
            self.x = x
            self.m = m
            self.y = y
            
            st.write("debug 2 - about to create empty table")
            self.table = np.zeros((n, x, m, y), dtype=int)
            st.write("debug 3 - Empty array created ")
            
            st.write("⚠️ - Generating Truth Table in accordance")
            st.write("..... with predefined validation rules")
            self.generate_table()
            st.write("debug 4 - Truth Table & validity check complete ")


        def generate_table(self):
            st.write("debug 5 - Repopulating array to create Truth table")
            try:
                for n in range(1, self.n): 
                    st.write(f"debug 6: Processing n={n}")
                    for x in range(1, self.x):
                        for m in range(1, self.m):
                            for y in range(1, self.y):
                                st.write(f"debug 7: Validating selection against ({n},{x},{m},{y})")
                                is_valid = self.validate_choice(
                                    st.session_state.n,
                                    st.session_state.x,
                                    st.session_state.m,
                                    st.session_state.y,
                                    st.session_state.selected_role,
                                    st.session_state.selected_sub_role,
                                    st.session_state.selected_action,
                                    st.session_state.selected_activity
                                )
                                st.write("⚠️ - Validation of chosen combination completed")
                                self.table[n, x, m, y] = int(bool(is_valid)) # converts the result, is_valid, into an integer
            
            except Exception as e:
                st.error(f"Error in generate_table: {str(e)}")
                raise  # This will show the full error traceback
        

            if st.session_state.R_go == 1:
                if st.session_state.n == 2 and st.session_state.y == 2:
                    st.write(" ..... Access to feature granted 👍")
                    st.session_state.return_to_main = True
                    return
            elif st.session_state.R_go == 0:
                   if st.session_state.n == 2 and st.session_state.y < 2:
                       st.write(" .....  Continuing to process")
                       st.session_state.return_to_main = False
                       return
                   else:
                       st.write(" ..... Access to feature denied 👎")
                       st.session_state.return_to_main = True
                       return
                


        def validate_choice(self, n, x, m, y, selected_role, selected_sub_role, selected_action, selected_activity):
            """Validate the selection by checking if the combination matches valid rules."""
        
            st.write(" ")
            st.write("⚠️ - Validating chosen items from lists")
            st.write("..... as a four item combination")

            if self.validate_selection(n, x, m, y, selected_role, selected_sub_role, selected_action, selected_activity):
                return self.is_valid_combination(selected_role, selected_sub_role, selected_action, selected_activity)
            else:
                next_step = self.get_next_valid_selection(n, x, m, y)
                st.write("⚠️ - Invalid combination")
                st.write(f"..... please re-select your {next_step}.")
            return 


        
        def validate_selection(self, n, x, m, y, selected_role, selected_sub_role, selected_action, selected_activity):

#           Function to validate selection       
#           Uses the validate_choice function to determine if selection is valid

            st.write(" ")
            st.write("⚠️ - Confirming combination is valid")
            st.write(" ..... searching")
            
            is_valid = self.is_valid_combination(
                st.session_state.selected_role,
                st.session_state.selected_sub_role,
                st.session_state.selected_action,
                st.session_state.selected_activity
            )

            st.write(" ") 
            st.write("⚠️ - Truth Table consulted ")
        
            if is_valid:
                st.session_state.R_go = 1
                st.write("👌 combination is a valid selection")
            else:
                st.session_state.R_go = 0
                st.write(f" the selected combination {n},{x},{m},{y} is invalid")
            return is_valid


    
        def get_next_valid_selection(self, n, x, m, y):

#           Function to identify the next level within invalid choices and returns it

            if self.table[n, :, :, :].max() == 0:
                st.session_state.stage = "sub_role_selection"
                return "Job Function"
            elif self.table[n, x, :, :].max() == 0:
                st.session_state.stage = "action_selection"
                return "Action"
            elif self.table[n, x, m, :].max() == 0:
                st.session_state.stage = "activity_selection"
                return "Activity"
            else: 
                st.session_state.stage = "finalize_selection"
                return "Validate"



        def is_valid_combination(self, selected_role, selected_sub_role, selected_action, selected_activity): 

#           Function to compare selections versus Truth Table data
            st.write(" ")
            st.write("⚠️ - One moment please ")
            st.write(" ")
            st.write("..... verifying validity of combination,")
            st.write("..... picked from list against Truth Table")
            st.write(" ")
            
#           Rule 1: Only Agricultural Engineers and System Technicians can perform System Design & Optimization
            if selected_action == "System Design & Optimization" and selected_role not in ["Agricultural Engineers", "System Technicians"]:
                return 0
#           Rule 2: Franchise Operators should not perform technical activities like Nutrient Mix Preparation
            if selected_role == "Franchise Operators" and selected_activity in ["Nutrient Mix Preparation", "pH Level Monitoring"]:
                return 0
#           Rule 3: Plant Scientists should focus on Plant Health Assessment and Growth Cycle Planning
            if selected_role == "Plant Scientists" and selected_action not in ["Plant Health Assessment", "Growth Cycle Planning"]:
                return 0
#           Rule 4: Quality Assurance Manager should focus on Quality Control Inspections and Compliance Monitoring
            if selected_sub_role == "Quality Assurance Manager" and selected_action not in ["Quality Control Inspections", "Compliance Monitoring"]:
                return 0
#           Rule 5: Franchise Owners should focus on business-related actions like Franchise Performance Review
            if selected_role == "Franchise Operators" and selected_action not in ["Franchise Performance Review", "Business Expansion Planning"]:
                return 0
#           Rule 6: Operations Managers should handle actions like Production Planning and Team Coordination
            if selected_role == "Operations Managers" and selected_action not in ["Production Planning", "Team Coordination"]:
                return 0

        
#           Rule 19: Nutrient Management Specialists should 
            if selected_role == "Nutrient Management Specialists" and selected_sub_role not in [""]:
                return 0       
#           Rule 20: Nutrient Management Specialists should 
            if selected_role == "Nutrient Management Specialists" and selected_action not in [""]:
                return 0       
#           Rule 21: Nutrient Management Specialists should 
            if selected_role == "Nutrient Management Specialists" and selected_activity not in [""]:
                return 0
    

#           Rule 22: Nutrient Management Specialists should 
            if selected_role == "Nutrient Management Specialists" and selected_sub_role not in [""]:
                return 0       
#           Rule 23: Nutrient Management Specialists should 
            if selected_role == "Nutrient Management Specialists" and selected_action not in [""]:
                return 0       
#           Rule 24: Nutrient Management Specialists should 
            if selected_role == "Nutrient Management Specialists" and selected_activity not in [""]:
                return 0
            

#           Rule 25: Nutrient Management Specialists should 
            if selected_role == "Nutrient Management Specialists" and selected_sub_role not in [""]:
                return 0       
#           Rule 26: Nutrient Management Specialists should 
            if selected_role == "Nutrient Management Specialists" and selected_action not in [""]:
                return 0       
#           Rule 27: Nutrient Management Specialists should 
            if selected_role == "Nutrient Management Specialists" and selected_activity not in [""]:
                return 0


#           Rule 28: Nutrient Management Specialists should 
            if selected_role == "Nutrient Management Specialists" and selected_sub_role not in [""]:
                return 0       
#           Rule 29: Nutrient Management Specialists should 
            if selected_role == "Nutrient Management Specialists" and selected_action not in [""]:
                return 0       
#           Rule 30: Nutrient Management Specialists should 
            if selected_role == "Nutrient Management Specialists" and selected_activity not in [""]:
                return 0


#           Rule 31: Franchisees should 
            if selected_role == "Franchisees" and selected_sub_role not in [""]:
                return 0       
#           Rule 32: Franchisees should 
            if selected_role == "Franchisees" and selected_action not in [""]:
                return 0       
#           Rule 33: Franchisees should 
            if selected_role == "Franchisees" and selected_activity not in [""]:
                return 0    


#           Rule 34: Franchisors should have job functions like Franchise Owner,
            if selected_role == "Franchisors" and selected_sub_role not in ["Franchise Owner",]:
                return 0       
#           Rule 35: Franchisors should have actions like 
            if selected_role == "Franchisors" and selected_action not in [""]:
                return 0       
#           Rule 36: Franchisors should have activities like
            if selected_role == "Franchisors" and selected_activity not in [""]:
                return 0       
            
              
#           Rule 37: Management Personnel should have job functions like Head of Agricultural Engineering, Plant Science Director, Operations Director, Operations Manager, Quality Assurance Manager, 
#                    Environmental Systems Manager, Nutrient Systems Manager, Data Analytics Manager, Regional Franchise Manager, Franchise Operations Director, Investment Manager, Portfolio Manager,
#                    Business Development Director, Business Development Manager, Chief Executive Officer, Chief Marketing Officer, Chief Operations Officer, Chief Financial Officer, Franchise Development Director,
#                    Franchise Compliance Manager, Investor Relations Manager,             
            if selected_role == "Management Personnel" and selected_sub_role not in [""]:
                return 0       
#           Rule 38: Management Personnel should 
            if selected_role == "Management Personnel" and selected_action not in [""]:
                return 0       
#           Rule 39: Management Personnel should 
            if selected_role == "Management Personnel" and selected_activity not in [""]:
                return 0       

            
#           Rule 40: Investors should have Job Functions like Investment Analyst, Investor Relations Manager and Limited Partner
            if selected_role == "Investors" and selected_sub_role not in ["Investment Analyst", "Investor Relations Manager", "Limited Partner"]:
                return 0       
#           Rule 41: Investors should handle actions like Investment Performance Monitoring, Franchise Performance Review, Financial Analysis, Risk Assessment, 
#                   Return on Investment Analysis, Capital Allocation, Market Analysis, Investor Reporting, Performance Metrics Review, Compliance Auditing
            if selected_role == "Investors" and selected_action not in ["Investment Performance Monitoring", "Franchise Performance Review", "Financial Analysis", "Risk Assessment", 
                                                                        "Return on Investment Analysis", "Capital Allocation", "Market Analysis", "Investor Reporting", "Performance Metrics Review", "Compliance Auditing"]:
                return 0                                                      
#           Rule 42: Investors should access financial activities like Investment Portfolio Review, Franchise Audit Execution, Financial Statement Analysis, 
#                   Risk Assessment Reports, ROI Calculations, Market Trend Analysis, Investor Report Generation, Performance Metric Tracking
            if selected_role == "Investors" and selected_activity not in ["Investment Portfolio Review", "Franchise Audit Execution", "Financial Statement Analysis", 
                                                                          "Risk Assessment Reports", "ROI Calculations", "Market Trend Analysis", "Investor Report Generation", 
                                                                          "Performance Metric Tracking"]:
                return 0

            
#           Default valid if no rule invalidates it
            st.success("Selected combination not invalid ! ")
            return 1
                
            

#   Create instance after class definition
    st.write("debug 0 - Creating TruthTable instance")
    truth_table = TruthTable()  # This line was missing         
    st.write("debug 9: Table generation completed")


        
# =====================
# End of first Module :
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
    st.header("Select Your Role")
    
    roles = st.session_state.A # refers to list defined in Module 2 for accomodated User roles
    
    selected_role = st.radio("Choose a Role", roles)

    if st.button("Choose a Job Function next", on_click=lambda: set_stage("sub_role_selection", "selected_role", selected_role)):
        pass
    return
     

# Sub-role selection screen
def select_sub_role(content_placeholder):
    st.header(f" Select Job Function for {st.session_state.selected_role}")
    
    sub_roles = st.session_state.B # refers to list defined in Module 2 for accomodated User roles respective job functions (sub roles)
    
    selected_sub_role = st.radio("Choose a Job Function", sub_roles)

    if st.button("Choose an Action next", on_click=lambda: set_stage("action_selection", "selected_sub_role", selected_sub_role)):
        pass
    return
    

# Action selection screen
def select_action(content_placeholder):
    st.header(f"Actions available for {st.session_state.selected_role} - {st.session_state.selected_sub_role}")
    
    actions = st.session_state.C # refers to list defined in Module 2 for allowable actions for the given Users, their roles and associated functions
    
    selected_action = st.radio("Choose an Action", actions)

    if st.button("Choose an Activity next", on_click=lambda: set_stage("activity_selection", "selected_action", selected_action)):
        pass
    return
    

# Activity selection screen
def select_activity(content_placeholder):
    st.header(f"Activity for {st.session_state.selected_role} - {st.session_state.selected_sub_role} - {st.session_state.selected_action}")
    
    activities = st.session_state.D # refers to list defined in Module 2 for accomodated activities allowable for actions
    
    selected_activity = st.radio("Choose an activity", activities)

    if st.button("Validate", on_click=lambda: finalize_selection(selected_activity)):
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
