# Main Script and function call for the Castara AgroEconomy Mobile App.
import streamlit as st
import numpy as np
import importlib
import sys
import os

# Definition of sub-folder where feature module scripts are to be found
sub_folder = os.path.join("features", "scripts")

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
    st.session_state.A = ["Agricultural Engineer", "Horticulturist", "System Specialist", "Plant Scientist", "Operations Personnel",
                          "Maintenance Staff", "Quality Control Personnel", "Harvest Worker", "Climate Control Specialist",
                          "Nutrient Management Specialist", "Franchise Operator", "Franchisor", "Management Personnel", "Investor", "Do not select (EOL)"]

# Initialize matrices in session_state if not already there
if 'B' not in st.session_state:
    st.session_state.B = ["Head of Agricultural Engineering", "Lead Horticulturist", "Systems Integration Engineer", "Plant Science Director", "Operations Director", 
                          "Operations Manager", "Maintenance Supervisor", "Quality Assurance Manager", "Harvest Team Leader", "Environmental Systems Manager", "Nutrient Systems Manager", 
                          "Data Analytics Manager", "Production Supervisor", "Food Safety Compliance Officer", "Automation Engineer", "Plant Health Inspector", 
                          "Franchise Owner", "Franchise Operator", "Regional Franchise Manager", "Franchise Operations Director", "Chief Investment Officer", "Investment Manager", 
                          "Portfolio Manager", "Chief Executive Officer",  "Chief Operations Officer", "Chief Financial Officer", "Business Development Manager", 
                          "Franchise Development Director", "Investment Analyst", "Financial Controller", "Franchise Compliance Manager", "Investor Relations Manager", "Limited Partner", "Do not select (EOL)"] 

# Initialize matrices in session_state if not already there
if 'C' not in st.session_state:
    st.session_state.C = ["System Design & Optimization", "Environmental Parameter Monitoring", "Nutrient Solution Management", "Plant Health Assessment", "Growth Cycle Planning", 
                          "Equipment Maintenance", "Quality Control Inspections", "Harvest Scheduling", "Data Collection & Analysis", "Compliance Monitoring",
                          "System Troubleshooting", "Resource Usage Optimization", "Production Planning", "Safety Protocol Implementation", "Team Coordination", 
                          "Investment Performance Monitoring", "Franchise Performance Review", "Financial Analysis", "Business Expansion Planning", "Franchise Agreement Management", 
                          "Risk Assessment", "Return on Investment Analysis", "Franchise Standards Enforcement", "Capital Allocation", "Market Analysis", "Investor Reporting",
                          "Franchise Training Program Management", "Performance Metrics Review", "Strategic Planning", "Compliance Auditing", "Do not select (EOL)"]

# Initialize matrices in session_state if not already there
if 'D' not in st.session_state:
    st.session_state.D = ["pH Level Monitoring", "EC - Electrical Conductivity - Testing", "Temperature Control Adjustment", "Humidity Level Management", "Light Intensity Calibration", 
                          "Nutrient Mix Preparation", "Water Quality Testing", "Growth Rate Documentation", "Equipment Sanitization", "System Flow Rate Checks", "Plant Spacing Optimization", 
                          "Harvest Weight Recording", "Equipment Calibration", "Safety Inspection Rounds", "Inventory Management", "Growth Data Recording", "Team Schedule Creation", 
                          "Maintenance Log Updates", "Quality Check Documentation", "Compliance Report Generation", "Investment Portfolio Review", "Franchise Audit Execution", 
                          "Financial Statement Analysis", "Market Research Documentation", "Franchise Agreement Review", "Risk Assessment Reports", "ROI Calculations", "Standards Compliance Checks", 
                          "Capital Distribution Planning", "Market Trend Analysis", "Investor Report Generation", "Training Program Development", "Performance Metric Tracking", 
                          "Strategy Document Creation", "Compliance Report Filing", "Do not select (EOL)"]


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

if 'skip_final' not in st.session_state:
    st.session_state.skip_final = 0

if 'R_go' not in st.session_state:
    st.session_state.R_go = 0

if 'return_to_main' not in st.session_state:
    st.session_state.return_to_main = False

if 'live' not in st.session_state:
    st.session_state.live = 0

if 'is_valid' not in st.session_state:
    st.session_state.is_valid = 0

if 'validity_check' not in st.session_state:
    st.session_state.validity_check = 0

if 'validity_confirmation' not in st.session_state:
    st.session_state.validity_confirmation = 0

if 'feature_call' not in st.session_state:
    st.session_state.feature_call = "default module name"



# Define the main function that controls the flow

def main():

# Initialize session state variable
    if "stage" not in st.session_state:
        st.session_state.stage = "login"
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        
    content_placeholder = st.empty()  # Create a single placeholder for all content
        
# Stage-based rendering using the placeholder
    if st.session_state.stage == "login":
        with content_placeholder.container():
            login(content_placeholder)
    elif (st.session_state.skip_final == 0) and st.session_state.stage == "role_selection":
        with content_placeholder.container():
            select_role(content_placeholder)
    elif (st.session_state.skip_final == 0) and st.session_state.stage == "sub_role_selection":
        with content_placeholder.container():
            select_sub_role(content_placeholder)
    elif (st.session_state.skip_final == 0) and st.session_state.stage == "action_selection":
        with content_placeholder.container():
            select_action(content_placeholder)
    elif (st.session_state.skip_final == 0) and st.session_state.stage == "activity_selection":
        with content_placeholder.container():
            select_activity(content_placeholder)
    elif st.session_state.skip_final == 0:
        with content_placeholder.container():
            finalize_selection (content_placeholder)


# =========================
# Returned to main Module :-
# =========================
    
    if (st.session_state.R_go == 1) and (st.session_state.live == 1):
        with content_placeholder.container():
            st.write(" ")
            
        st.write(f"⚠️ - Journey completed successfully, Role {st.session_state.selected_role}")
        st.write(f"..... with Sub-role {st.session_state.selected_sub_role} can access {st.session_state.selected_action}")
        st.write(f"..... in order to execute the mission, {st.session_state.selected_activity}")
        
        st.write(" ")
        st.write("⚠️ - When implemented, appropriate feature will activate at this point")
        st.write(" ")

# Replace spaces in Activity with "_" and add ".py" at the end to generate feature name

        feature_module = st.session_state.activity.replace(" ", "_") + ".py"

        with content_placeholder.container():
            st.write(" ")
            st.write(f"⚠️ - launching {feature_module}")
            launch_pad(feature_module)
        
        st.session_state.logged_in = True
        st.session_state.stage = "finalize_selection"

        if st.button("Logout", on_click=lambda: logout()):
            pass
            st.session_state.stage = None
            st.session_state.logged_in = False
            st.session_state.skip_final = 0
        
# Add an "End Execution" button
        if st.button("End Execution"):
            pass
            st.session_state.live = 0  # Update the flag to stop the loop
            st.session_state.skip_final = 0

# Display a message after the loop ends
            st.write(" ")
            st.write("Execution ended.")
            st.write(" ")
    
    elif st.session_state.stage == "finalize_selection":
        with content_placeholder.container():
            st.write(" ")
            
        st.write(" ")
        st.write("⚠️ - Testing system navigation; feature's function not yet implemented.")
        st.write(" ")

                    
    if (st.session_state.R_go == 0) and (st.session_state.live == 1):
        with content_placeholder.container():
            st.write(" ")
            
        st.write(f"⚠️ - Journey unsuccessfull, the Role {st.session_state.selected_role}")
        st.write(f"..... with Sub-role {st.session_state.selected_sub_role}, is not authorized to perform the action {st.session_state.selected_action}")
        st.write(f"..... in order to execute and achieve the mission {st.session_state.selected_activity}")
        
        st.write(" ")
        st.write("⚠️ - You will unfortunately be required to make new selections.")
            
        if st.session_state.logged_in == True:
            with content_placeholder.container():
                st.write(" ")
                
            st.session_state.stage = "role_selection"
     
            st.write(" ")
            st.write("⚠️ - Currently, you will need to logout and login again, to select a different User Role")
            st.write(" ")
            
#.          st.write(" ")
#           st.write("However, the system will return you to the list which causes the first invalid combination to occur, other than the User's Role, as a result of an invalid item being selected.")
#           st.write("Eventually, by the launch release, version 1.xx, only valid options will be presented based on the selected option in the prior presented list")
            
            if st.button("Logout", on_click=lambda: logout()):
                pass
                st.session_state.stage = None
                st.session_state.logged_in = False
                st.session_state.skip_final = 0
        
# Add an "End Execution" button
            if st.button("End Execution"):
                pass
                st.session_state.live = 0  # Update the flag to stop the loop
                st.session_state.skip_final = 0

# Display a message after the loop ends
                st.write(" ")
                st.write("Execution ended.")
                st.write(" ")


    
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
    st.write("⚠️ - Entered verification processing Module ")
    
# Initialize session state variables if not already present
    
    for key, default in {
        'n': 15, 'x': 35, 'm': 31, 'y': 36, 'selected_role' : st.session_state.selected_role, 'selected_sub_role' : st.session_state.selected_sub_role, 'selected_action' : st.session_state.selected_action, 'selected_activity' : st.session_state.selected_activity, 'R_go': 0, 'return_to_main' : False, 'live' : " ",
        }.items():
        
        if key not in st.session_state:
            st.session_state[key] = default

    st.write(" ")
    st.write("⚠️ - Defining Truth Table Class")
 
    class TruthTable:
        def __init__(self, n=14, x=34, m=30, y=35, selected_role = st.session_state.selected_role, selected_sub_role = st.session_state.selected_sub_role, selected_action = st.session_state.selected_action, selected_activity = st.session_state.selected_activity):

            st.write("debug 1 - defined 'init' ")
            
            self.n = int(n)
            self.x = int(x)
            self.m = int(m)
            self.y = int(y)
            self.selected_role = st.session_state.A[0]
            self.selected_sub_role = st.session_state.B[0]
            self.selected_action = st.session_state.C[0]
            self.selected_activity = st.session_state.D[0]
            
            st.write("debug 2 - about to create empty array")
            self.table = np.zeros((n, x, m, y), dtype=int)
            st.write("debug 3 - Empty array created ")
            
            st.write(" ")
            st.write("⚠️ - First generating default Truth Table")
            st.write("..... without predefined rules")
            st.write(" ")
         
            st.write("debug 4 - About to prepare Truth Table")
            st.write("..... updated in accordance with")
            st.write("..... specified valid selection rules")
            st.write(" ")
            
            self.generate_table()          
               
        def generate_table(self):
            
            st.write("debug 5 - Repopulating array ")
            st.write("..... to create a valid Truth table ")
            
            try:
                for n in range(1, self.n): 
                    st.write(f"debug 6: Processing n={n}")
                    for x in range(1, self.x):
                        for m in range(1, self.m):
                            for y in range(1, self.y):
                                
                                st.write(f"debug 7: Beginning validation of selected")
                                st.write(f"..... combination of elements, ({n},{x},{m},{y})")

                                validity_confirmation = 0 # Initialized to 'False'
                                validity_confirmation = self.validate_choice(
                                 n,
                                 x,
                                 m,
                                 y,
                                 self.selected_role,
                                 self.selected_sub_role,
                                 self.selected_action,
                                 self.selected_activity
                                )
                                                          
                                st.write(" ")
                                st.write("⚠️ - Validation of selections completing .... ")
                                
                                if validity_confirmation == 0:
                                    st.session_state.R_go = 0
                                
                                if validity_confirmation == 1:
                                    st.session_state.R_go = 1
                                
                                return
                                                             
            except Exception as e:
                st.error(f"Error in generate_table: {str(e)}")
                raise  # This will show the full error traceback
                
         
            if st.session_state.R_go == 1:
                st.write(" ..... Access to feature granted 👍")
                st.session_state.return_to_main = True
                return
            if st.session_state.R_go == 0:
                if (n := 15) and (y := 36):
                    st.write(" .....  Continuing to process")
                    st.session_state.return_to_main = False
                    return
                if (n == 14) and (y == 36):
                    st.write(" ..... Access to feature denied 👎")
                    st.session_state.return_to_main = True
                    return
          
#       INFERENCE ENGINE - cascading functions

        def validate_choice(self, n, x, m, y, selected_role, selected_sub_role, selected_action, selected_activity):
            """Validate the selection by checking if the combination matches valid rules."""

            st.session_state.live = 1
            selected_role = st.session_state.selected_role
            selected_sub_role = st.session_state.selected_sub_role
            selected_action = st.session_state.selected_action
            selected_activity = st.session_state.selected_activity
            
         
            st.write(" ")      
            st.write(f" Confirming that {selected_role}")
            st.write(f" who selects the Job title {selected_sub_role}")
            st.write(f" is authorized to perform {selected_action}")
            st.write(f" in order to carryout {selected_activity}")
                       
            st.write(" ")
            st.write("⚠️ - Validating combination of selected items ")
            st.write("     from lists; Matrix B, C, D ")
            st.write("     as a four element matrix combination")

            validity_check = 0 # Initialized to 'False'
            validity_check = self.validate_selection(n, x, m, y, selected_role, selected_sub_role, selected_action, selected_activity)

            if validity_check == 0:   # selection not validated, check next Truth Table result
                next_step = self.get_next_valid_selection(n, x, m, y, selected_role, selected_sub_role, selected_action, selected_activity)
            return # valid_confirmation as 0 or 1

        
        def validate_selection(self, n, x, m, y, selected_role, selected_sub_role, selected_action, selected_activity):

#           Function to validate selection       
#           Used by the validate_choice function to determine if selection is valid

            st.write(" ")
            st.write("⚠️ - Confirming combination is valid")
            st.write("     by searching Truth Table array")


            is_valid = 0 # Initialized to 'False'
            is_valid = self.is_valid_combination(n, x, m, y, selected_role, selected_sub_role, selected_action, selected_activity)
                
            st.write(" ") 
            st.write("⚠️ - Truth Table being consulted ")
            st.write(" ")
            st.write(f" For {selected_role} selecting job title {selected_sub_role} ")
            st.write(f" who needs to perform {selected_action} to execute {selected_activity} ")
            st.write(" ")
            st.write(f" this is the returned value from the rules check :-  '{is_valid}' ")
            st.write(" ")

            if  is_valid == 1: # determines that the selected combination is a valid one
                st.write("👌 combination is a valid selection")
            else:
                st.write(f" the selected combination {n},{x},{m},{y} is invalid")
            return # validity_check as 0 or 1

    
        def get_next_valid_selection(self, n, x, m, y, selected_role, selected_sub_role, selected_action, selected_activity):

#           Function to identify the list that resulted in an invalid choice and returns to it

            if self.table[n, :, :, :].max() == 0:
                st.session_state.stage = "sub_role_selection"
                return "Job Title"
            elif self.table[n, x, :, :].max() == 0:
                st.session_state.stage = "action_selection"
                return "Action"
            elif self.table[n, x, m, :].max() == 0:
                st.session_state.stage = "activity_selection"
                return "Activity"
            else: 
                st.session_state.stage = "finalize_selection"
                return "Validate"


        def is_valid_combination(self, n, x, m, y, selected_role, selected_sub_role, selected_action, selected_activity): 

#           Function to prepare for comparison of selections versus Truth Table data
            st.write(" ")
            st.write("⚠️ - One moment please ")
            st.write("..... verifying validity of combination ")
            st.write("..... picked from list, against Truth Table")
            st.write(" ")
 
            
#           NOMINAL RULES : for validity checking
            
#           Rule 1: Agricultural Engineers should have the job title Head of Agricultural Engineering, Systems Integration Engineer, Automation Engineer, Environmental Systems Manager, Maintenance Supervisor, Nutrient Systems Manager, Quality Assurance Manager.
            if selected_role == "Agricultural Engineer" and selected_sub_role not in ["Head of Agricultural Engineering", "Systems Integration Engineer", "Automation Engineer", "Environmental Systems Manager", "Maintenance Supervisor", "Nutrient Systems Manager", "Quality Assurance Manager"]:
                return 0       
#           Rule 2: Agricultural Engineers should handle actions like System Design & Optimization, Environmental Parameter Monitoring, System Troubleshooting, Resource Usage Optimization, Production Planning, Compliance Monitoring.
            if selected_role == "Agricultural Engineer" and selected_action not in ["System Design & Optimization", "Environmental Parameter Monitoring", "System Troubleshooting", "Resource Usage Optimization", "Production Planning", "Compliance Monitoring"]:
                return 0
#           Rule 3: Agricultural Engineers should be able to access activities like pH Level Monitoring, EC (Electrical Conductivity) Testing, Temperature Control Adjustment, System Flow Rate Checks, Equipment Calibration, Maintenance Log Updates, Compliance Report Generation, Team Coordination.
            if selected_role == "Agricultural Engineer" and selected_activity not in ["pH Level Monitoring", "EC (Electrical Conductivity Testing", "Temperature Control Adjustment", "System Flow Rate Checks", "Equipment Calibration", "Maintenance Log Updates", "Compliance Report Generation", "Team Coordination"]:
                return 0

    
#           Rule 4: Horticultralists should have the job title Lead Horticulturist, Plant Science Director, Plant Health Inspector, Quality Assurance Manager, Data Analytics Manager, Nutrient Systems Manager, Harvest Team Leader.
            if selected_role == "Horticulturist" and selected_sub_role not in ["Lead Horticulturist", "Plant Science Director", "Plant Health Inspector", "Quality Assurance Manager", "Data Analytics Manager", "Nutrient Systems Manager", "Harvest Team Leader"]:
                return 0       
#           Rule 5: Horticulturilists should handle actions like Plant Health Assessment, Growth Cycle Planning, Nutrient Solution Management, Environmental Parameter Monitoring, Data Collection & Analysis, Quality Control Inspections, Resource Usage Optimization.
            if selected_role == "Horticulturist" and selected_action not in ["Plant Health Assessment", "Growth Cycle Planning", "Nutrient Solution Management", "Environmental Parameter Monitoring", "Data Collection & Analysis", "Quality Control Inspections", "Resource Usage Optimization"]:
                return 0
#           Rule 6: Horticultralists should be able to handle activities like Growth Rate Documentation, pH Level Monitoring, Nutrient Mix Preparation, Light Intensity Calibration, Humidity Level Management, Temperature Control Adjustment, Plant Spacing Optimization, Water Quality Testing.
            if selected_role == "Horticulturist" and selected_activity not in ["Growth Rate Documentation", "pH Level Monitoring", "Nutrient Mix Preparation", "Light Intensity Calibration", "Humidity Level Management", "Temperature Control Adjustment", "Plant Spacing Optimization", "Water Quality Testing"]:
                return 0

            

#           Rule 7: System Technicians should have the job title Systems Integration Engineer, Automation Engineer, Maintenance Supervisor, Environmental Systems Manager, Data Analytics Manager, Nutrient Systems Manager.
            if selected_role == "System Technician" and selected_sub_role not in ["Systems Integration Engineer", "Automation Engineer", "Maintenance Supervisor", "Environmental Systems Manager", "Data Analytics Manager", "Nutrient Systems Manager"]:
                return 0       
#           Rule 8: System Technicians should handle actions like System Design & Optimization, Environmental Parameter Monitoring, System Troubleshooting, Equipment Maintenance, Compliance Monitoring, Resource Usage Optimization.
            if selected_role == "System Technician" and selected_action not in ["System Design & Optimization", "Environmental Parameter Monitoring", "System Troubleshooting", "Equipment Maintenance", "Compliance Monitoring", "Resource Usage Optimization"]:
                return 0
#           Rule 9: System Technicians should be able to access activities like Equipment Calibration, System Flow Rate Checks, Temperature Control Adjustment, Humidity Level Management, Light Intensity Calibration, Maintenance Log Updates, Safety Inspection Rounds, Equipment Sanitization 
            if selected_role == "System Technician" and selected_activity not in ["Equipment Calibration", "System Flow Rate Checks", "Temperature Control Adjustment", "Humidity Level Management", "Light Intensity Calibration", "Maintenance Log Updates", "Safety Inspection Rounds", "Equipment Sanitization"]:
                return 0



#           Rule 10: Plant Scientists should have the job title Plant Science Director, Lead Horticulturist, Plant Health Inspector, Nutrient, Systems Manager, Data Analytics Manager, Food Safety Compliance Officer, Quality Assurance Manager.
            if selected_role == "Plant Scientist" and selected_sub_role not in ["Plant Science Director", "Lead Horticulturist", "Plant Health Inspector", "Nutrient Systems Manager", "Data Analytics Manager", "Food Safety Compliance Officer", "Quality Assurance Manager"]:
                return 0       
#           Rule 11: Plant Scientists should be able to handle actions like Plant Health Assessment, Growth Cycle Planning, Nutrient Solution Management, Data Collection & Analysis, Quality Control Inspections, Resource Usage Optimization, Environmental Parameter Monitoring.
            if selected_role == "Plant Scientist" and selected_action not in ["Plant Health Assessment", "Growth Cycle Planning", "Nutrient Solution Management", "Data Collection & Analysis", "Quality Control Inspections", "Resource Usage Optimization", "Environmental Parameter Monitoring"]:
                return 0
#           Rule 12: Plant Scientists should be able to access activities like Growth Rate Documentation, Nutrient Mix Preparation, Water Quality Testing, pH Level Monitoring, Equipment Calibration, Plant Spacing Optimization, Compliance Report Generation, Light Intensity Calibration.
            if selected_role == "Plant Scientist" and selected_activity not in ["Growth Rate Documentation", "Nutrient Mix Preparation", "Water Quality Testing", "pH Level Monitoring", "Equipment Calibration", "Plant Spacing Optimization", "Compliance Report Generation", "Light Intensity Calibration"]:
                return 0

            
#           Rule 13: Operations Personnel should have the job title Operations Director, Operations Manager, Production Supervisor, Quality Assurance Manager, Maintenance Supervisor, Data Analytics Manager.
            if selected_role == "Operations Personnel" and selected_sub_role not in ["Operations Director", "Operations Manager", "Production Supervisor", "Quality Assurance Manager", "Maintenance Supervisor", "Data Analytics Manager"]:
                return 0       
#           Rule 14: Operations Personnel should be able to handle actions like Production Planning, Team Coordination, Resource Usage Optimization, Safety Protocol Implementation, Data Collection & Analysis, Quality Control Inspections.
            if selected_role == "Operations Personnel" and selected_action not in ["Production Planning", "Team Coordination", "Resource Usage Optimization", "Safety Protocol Implementation", "Data Collection & Analysis", "Quality Control Inspections"]:
                return 0
#           Rule 15: Operations Personnel should be able to access activities like Team Schedule Creation, Inventory Management, Maintenance Log Updates, Harvest Weight Recording, Compliance Report Generation, Growth Data Recording, Safety Inspection Rounds, Equipment Sanitization.
            if selected_role == "Operations Personnel" and selected_activity not in ["Team Schedule Creation", "Inventory Management", "Maintenance Log Updates", "Harvest Weight Recording", "Compliance Report Generation", "Growth Data Recording", "Safety Inspection Rounds", "Equipment Sanitization"]:
                return 0
            
            
#           Rule 16: Maintenance Staff should have the job title Maintenance Supervisor, Automation Engineer, Environmental Systems Manager, Quality Assurance Manager, Systems Integration Engineer.
            if selected_role == "Maintenance Staff" and selected_sub_role not in ["Maintenance Supervisor", "Automation Engineer", "Environmental Systems Manager", "Quality Assurance Manager", "Systems Integration Engineer"]:
                return            
 #          Rule 17: Maintenance Staff should be able to handle actions like Equipment Maintenance, System Troubleshooting, Environmental Parameter Monitoring, Safety Protocol Implementation, Compliance Monitoring, Resource Usage Optimization.
            if selected_role == "Maintenance Staff" and selected_action not in ["Equipment Maintenance", "System Troubleshooting", "Environmental Parameter Monitoring", "Safety Protocol Implementation", "Compliance Monitoring", "Resource Usage Optimization"]:
                return 0       
#           Rule 18: Maintenance Staff should be able to access activities like Equipment Calibration, System Flow Rate Checks, Equipment Sanitization, Maintenance Log Updates, Safety Inspection Rounds, Light Intensity Calibration, Humidity Level Management, Temperature Control Adjustment.
            if selected_role == "Maintenance Staff" and selected_activity not in ["Equipment Calibration", "System Flow Rate Checks", "Equipment Sanitization", "Maintenance Log Updates", "Safety Inspection Rounds", "Light Intensity Calibration", "Humidity Level Management", "Temperature Control Adjustment"]:
                return 0
            
        
#           Rule 19: Quality Control Personnel should have the job title Quality Assurance Manager, Food Safety Compliance Officer, Plant Health Inspector, Production Supervisor, Data Analytics Manager.
            if selected_role == "Quality Control Personnel" and selected_sub_role not in ["Quality Assurance Manager", "Food Safety Compliance Officer", "Plant Health Inspector", "Production Supervisor", "Data Analytics Manager"]:
                return 0       
#           Rule 20: Quality Control Personnel should be able to handle actions like Quality Control Inspections, Compliance Monitoring, Data Collection & Analysis, Safety Protocol Implementation, Resource Usage Optimization.
            if selected_role == "Quality Control Personnel" and selected_action not in ["Quality Control Inspections", "Compliance Monitoring", "Data Collection & Analysis", "Safety Protocol Implementation", "Resource Usage Optimization"]:
                return 0       
#           Rule 21: Quality Control Personnel should be able to access activities like Quality Check Documentation, Compliance Report Generation, Safety Inspection Rounds, Growth Rate Documentation, pH Level Monitoring, Equipment Calibration, Harvest Weight Recording, System Flow Rate Checks.
            if selected_role == "Quality Control Personnel" and selected_activity not in ["Quality Check Documentation", "Compliance Report Generation", "Safety Inspection Rounds", "Growth Rate Documentation", "pH Level Monitoring", "Equipment Calibration", "Harvest Weight Recording", "System Flow Rate Checks"]:
                return 0
    

#           Rule 22: Harvest Workers should have the job title like Harvest Team Leader, Production Supervisor, Quality Assurance Manager, Plant Health Inspector.
            if selected_role == "Harvest Worker" and selected_sub_role not in ["Harvest Team Leader", "Production Supervisor", "Quality Assurance Manager", "Plant Health Inspector"]:
                return 0       
#           Rule 23: Harvest Workers should be able to handle actions like Harvest Scheduling, Quality Control Inspections, Data Collection & Analysis, Safety Protocol Implementation, Resource Usage Optimization.
            if selected_role == "Harvest Worker" and selected_action not in ["Harvest Scheduling", "Quality Control Inspections", "Data Collection & Analysis", "Safety Protocol Implementation", "Resource Usage Optimization"]:
                return 0       
#           Rule 24: Harvest Workers should be able to access activities like Harvest Weight Recording, Equipment Sanitization, Plant Spacing Optimization, Safety Inspection Rounds, Growth Rate Documentation, Team Schedule Creation, Inventory Management.
            if selected_role == "Harvest Worker" and selected_activity not in ["Harvest Weight Recording", "Equipment Sanitization", "Plant Spacing Optimization", "Safety Inspection Rounds", "Growth Rate Documentation", "Team Schedule Creation", "Inventory Management"]:
                return 0
            

#           Rule 25: Climate Control Specialists should have the job title Environmental Systems Manager, Systems Integration Engineer, Automation Engineer, Maintenance Supervisor, Data Analytics Manager.
            if selected_role == "Climate Control Specialist" and selected_sub_role not in ["Environmental Systems Manager", "Systems Integration Engineer", "Automation Engineer", "Maintenance Supervisor", "Data Analytics Manager"]:
                return 0       
#           Rule 26: Climate Control Specialists should be able to handle actions like Environmental Parameter Monitoring, System Design & Optimization, System Troubleshooting, Resource Usage Optimization, Compliance Monitoring.
            if selected_role == "Climate Control Specialist" and selected_action not in ["Environmental Parameter Monitoring", "System Design & Optimization", "System Troubleshooting", "Resource Usage Optimization", "Compliance Monitoring"]:
                return 0       
#           Rule 27: Climate Control Specialists should be able to access activities like Temperature Control Adjustment, Humidity Level Management, Light Intensity Calibration, System Flow Rate Checks, Equipment Calibration, Maintenance Log Updates, Safety Inspection Rounds, Compliance Report Generation.
            if selected_role == "Climate Control Specialist" and selected_activity not in ["Temperature Control Adjustment", "Humidity Level Management", "Light Intensity Calibration", "System Flow Rate Checks", "Equipment Calibration", "Maintenance Log Updates", "Safety Inspection Rounds", "Compliance Report Generation"]:
                return 0


#           Rule 28: Nutrient Management Specialists should have the job title Nutrient Systems Manager, Data Analytics Manager, Plant Science Director, Systems Integration Engineer, Quality Assurance Manager.
            if selected_role == "Nutrient Management Specialist" and selected_sub_role not in ["Nutrient Systems Manager", "Data Analytics Manager", "Plant Science Director", "Systems Integration Engineer", "Quality Assurance Manager"]:
                return 0       
#           Rule 29: Nutrient Management Specialists should be able to handle actions like Nutrient Solution Management, Environmental Parameter Monitoring, System Troubleshooting, Resource Usage Optimization, Compliance Monitoring.
            if selected_role == "Nutrient Management Specialist" and selected_action not in ["Nutrient Solution Management", "Environmental Parameter Monitoring", "System Troubleshooting", "Resource Usage Optimization", "Compliance Monitoring"]:
                return 0       
#           Rule 30: Nutrient Management Specialists should be able to access activities like Nutrient Mix Preparation, EC (Electrical Conductivity) Testing, pH Level Monitoring, Water Quality Testing, System Flow Rate Checks, Equipment Calibration, Maintenance Log Updates, Compliance Report Generation.
            if selected_role == "Nutrient Management Specialist" and selected_activity not in ["Nutrient Mix Preparation", "EC (Electrical Conductivity) Testing", "pH Level Monitoring", "Water Quality Testing", "System Flow Rate Checks", "Equipment Calibration", "Maintenance Log Updates", "Compliance Report Generation"]:
                return 0


#           Rule 31: Franchise Operator should have the job title Franchise Owner, Regional Franchise Manager, Franchise Compliance Manager, Business Development Manager, Data Analytics Manager.
            if selected_role == "Franchise Operator" and selected_sub_role not in ["Franchise Owner", "Regional Franchise Manager", "Franchise Compliance Manager", "Business Development Manager", "Data Analytics Manager"]:
                return 0       
#           Rule 32: Franchise Operator should be able to handle actions like Franchise Performance Review, Business Expansion Planning, Compliance Monitoring, Financial Analysis, Team Coordination.
            if selected_role == "Franchise Operator" and selected_action not in ["Franchise Performance Review", "Business Expansion Planning", "Compliance Monitoring", "Financial Analysis", "Team Coordination"]:
                return 0       
#           Rule 33: Franchise Operator should be able to access activities like ROI Calculations, Compliance Report Generation, Team Schedule Creation, Market Research Documentation, Financial Statement Analysis, Performance Metric Tracking, Risk Assessment Reports.
            if selected_role == "Franchise Operator" and selected_activity not in ["ROI Calculations", "Compliance Report Generation", "Team Schedule Creation", "Market Research Documentation", "Financial Statement Analysis", "Performance Metric Tracking", "Risk Assessment Reports"]:
                return 0    


#           Rule 34: Franchisors should have the job title Franchise Owner, Franchise Compliance Manager, Financial Controller, Franchise Development Director, Business Development Manager,
#                    Chief Financial Officer, Chief Operations Officer, Chief Marketing Officer, Business Development Director, Franchise Operations Director, Regional Franchise Manager, Franchise Operator,
#                    Operations Manager, Operations Director
            if selected_role == "Franchisor" and selected_sub_role not in ["Franchise Owner", "Franchise Compliance Manager", "Financial Controller", "Franchise Development Director", "Business Development Manager",
                     "Chief Financial Officer", "Chief Operations Officer", "Chief Marketing Officer", "Business Development Director", "Franchise Operations Director", "Regional Franchise Manager", "Franchise Operator",
                     "Operations Manager", "Operations Director"]:
                return 0       
#           Rule 35: Franchisors should handle actions like Compliance Auditing, Strategic Planning, Performance Metrics Review, Franchise Training Program Management, Investor Reporting, Market Analysis, 
#                    Franchise Standards Enforcement, Franchise Agreement Management, Business Expansion Planning, Financial Analysis, Franchise Performance Review
            if selected_role == "Franchisor" and selected_action not in ["Compliance Auditing", "Strategic Planning", "Performance Metrics Review", "Franchise Training Program Management", "Investor Reporting", "Market Analysis", 
                                "Franchise Standards Enforcement", "Franchise Agreement Management", "Business Expansion Planning", "Financial Analysis", "Franchise Performance Review"]:
                return 0       
#           Rule 36: Franchisors should be able to access activities like Franchise Agreement Review, Market Research Documentation, Compliance Report Generation, ROI Calculations, Training Program Development, Performance Metric Tracking, 
#                    Risk Assessment Reports.
            if selected_role == "Franchisor" and selected_activity not in ["Franchise Agreement Review", "Market Research Documentation", "Compliance Report Generation", "ROI Calculations", "Training Program Development", 
                                "Performance Metric Tracking", "Risk Assessment Reports"]:
                return 0       
            
              
#           Rule 37: Management Personnel should have the job title Head of Agricultural Engineering, Plant Science Director, Operations Director, Operations Manager, Quality Assurance Manager, 
#                    Environmental Systems Manager, Nutrient Systems Manager, Data Analytics Manager, Regional Franchise Manager, Franchise Operations Director, Investment Manager, Portfolio Manager,
#                    Business Development Director, Business Development Manager, Chief Executive Officer, Chief Marketing Officer, Chief Operations Officer, Chief Financial Officer, Franchise Development Director,
#                    Franchise Compliance Manager, Investor Relations Manager            
            if selected_role == "Management Personnel" and selected_sub_role not in ["Head of Agricultural Engineering", "Plant Science Director", "Operations Director", "Operations Manager", "Quality Assurance Manager", 
                                "Environmental Systems Manager", "Nutrient Systems Manager", "Data Analytics Manager", "Regional Franchise Manager", "Franchise Operations Director", "Investment Manager", "Portfolio Manager",
                                "Business Development Director", "Business Development Manager", "Chief Executive Officer", "Chief Marketing Officer", "Chief Operations Officer", "Chief Financial Officer", "Franchise Development Director",
                                "Franchise Compliance Manager", "Investor Relations Manager"]:
                return 0       
#           Rule 38: Management Personnel should handle actions like Franchise Training Program Management, Performance Metrics Review, Strategic Planning, Capital Allocation,  Investment Performance Monitoring, Franchise Performance Review, 
#                    Financial Analysis, Business Expansion Planning, Franchise Agreement Management, Risk Assessment, Return on Investment Analysis, Production Planning
            if selected_role == "Management Personnel" and selected_action not in ["Franchise Training Program Management", "Performance Metrics Review", "Strategic Planning", "Capital Allocation", "Investment Performance Monitoring", "Franchise Performance Review", 
                                "Financial Analysis", "Business Expansion Planning", "Franchise Agreement Management", "Risk Assessment", "Return on Investment Analysis", "Production Planning"]:
                return 0       
#           Rule 39: Management Personnel should be able to access activities like Strategy Document Creation, Training Program Development, Investor Report Generation, Market Trend Analysis, Capital Distribution Planning, ROI Calculations, Risk Assessment Reports, 
#                    Franchise Agreement Review, Financial Statement Analysis, Franchise Audit Execution, Investment Portfolio Review, Inventory Management
            if selected_role == "Management Personnel" and selected_activity not in ["Strategy Document Creation", "Training Program Development", "Investor Report Generation", "Market Trend Analysis", "Capital Distribution Planning", "ROI Calculations", "Risk Assessment Reports", 
                                "Franchise Agreement Review", "Financial Statement Analysis", "Franchise Audit Execution", "Investment Portfolio Review", "Inventory Management"]:
                return 0       

            
#           Rule 40: Investors should have Job title Investment Analyst, Investor Relations Manager and Limited Partner
            if selected_role == "Investor" and selected_sub_role not in ["Investment Analyst", "Investor Relations Manager", "Limited Partner"]:
                return 0       
#           Rule 41: Investors should handle actions like Investment Performance Monitoring, Franchise Performance Review, Financial Analysis, Risk Assessment, 
#                    Return on Investment Analysis, Capital Allocation, Market Analysis, Investor Reporting, Performance Metrics Review, Compliance Auditing
            if selected_role == "Investor" and selected_action not in ["Investment Performance Monitoring", "Franchise Performance Review", "Financial Analysis", "Risk Assessment", 
                                                                        "Return on Investment Analysis", "Capital Allocation", "Market Analysis", "Investor Reporting", "Performance Metrics Review", "Compliance Auditing"]:
                return 0                                                      
#           Rule 42: Investors should be able to access activities like Investment Portfolio Review, Franchise Audit Execution, Financial Statement Analysis, 
#                    Risk Assessment Reports, ROI Calculations, Market Trend Analysis, Investor Report Generation, Performance Metric Tracking
            if selected_role == "Investor" and selected_activity not in ["Investment Portfolio Review", "Franchise Audit Execution", "Financial Statement Analysis", 
                                                                          "Risk Assessment Reports", "ROI Calculations", "Market Trend Analysis", "Investor Report Generation", 
                                                                          "Performance Metric Tracking"]:
                return 0
            else:
                return 1

#           End of Nominal Rules return is_valid as 0 or 1
                        
#   Create instance after class definition
    truth_table = TruthTable()  # This line was missing       

    st.write(" ")
    st.write("debug 9 - Validity of selection completed")
    st.write(" ")
    st.session_state.skip_final = 1


        
# =====================
# End of first Module :
# ===================== 




# Login function
def login(content_placeholder):
    st.image('Assets/Media/Images/Cover_page.jpg')
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

    if st.button("Choose a Job Title next", on_click=lambda: set_stage("sub_role_selection", "selected_role", selected_role)):
        st.session_state.selected_role = selected_role
        pass
    return
     

# Sub-role selection screen
def select_sub_role(content_placeholder):
    st.header(f" Select Job Function for {st.session_state.selected_role}")
    
    sub_roles = st.session_state.B # refers to list defined in Module 2 for accomodated User roles respective job functions (sub roles)
    
    selected_sub_role = st.radio("Choose a Job Function", sub_roles)

    if st.button("Choose an Action next", on_click=lambda: set_stage("action_selection", "selected_sub_role", selected_sub_role)):
        st.session_state.selected_sub_role = selected_sub_role
        pass
    return
    

# Action selection screen
def select_action(content_placeholder):
    st.header(f"Actions available for {st.session_state.selected_role} - {st.session_state.selected_sub_role}")
    
    actions = st.session_state.C # refers to list defined in Module 2 for allowable actions for the given Users, their roles and associated functions
    
    selected_action = st.radio("Choose an Action", actions)

    if st.button("Choose an Activity next", on_click=lambda: set_stage("activity_selection", "selected_action", selected_action)):
        st.session_state.selected_action = selected_action
        pass
    return
    

# Activity selection screen
def select_activity(content_placeholder):
    st.header(f"Activity for {st.session_state.selected_role} - {st.session_state.selected_sub_role} - {st.session_state.selected_action}")
    
    activities = st.session_state.D # refers to list defined in Module 2 for accomodated activities allowable for actions
    
    selected_activity = st.radio("Choose an activity", activities)

    if st.button("Validate", on_click=lambda: finalize_selection(selected_activity)):
        st.session_state.selected_activity = selected_activity
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


#   feature access via API
def launch_pad(feature_module):
    st.header(f" Launching Function for {st.session_state.selected_activity}")
    st.write(" ")
    call(feature_module)
    
    return
    

# Logout function
def logout():
    st.session_state.clear()  # Clears all session states for a fresh start
    st.session_state.stage = "login"  # Return to login

if __name__ == "__main__":
    main()
