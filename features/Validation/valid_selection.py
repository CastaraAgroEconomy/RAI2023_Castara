# Updated menu List [A], [B], [C], [D], 
# which produce a (14,30,30,35) four dimensional Matrix,
# Truth Table with 441,000 combinations

import streamlit as st
import itertools
import pandas as pd

selected_role = st.session_state.selected_role
selected_sub_role = st.session_state.selected_sub_role
selected_action = st.session_state. selected_action
selected_activity = st.session_state.selected_activity

# Define the matrices
A = ["Agricultural Engineers", "Horticulturists", "System Technicians", "Plant Scientists", "Operations Managers",
     "Maintenance Staff", "Quality Control Personnel", "Harvest Workers", "Climate Control Specialists",
     "Nutrient Management Specialists", "Franchise Operators", "Franchisors", "Management Personnel", "Investors"]

B = ["Head of Agricultural Engineering", "Lead Horticulturist", "Systems Integration Engineer", "Plant Science Director",
     "Operations Director", "Maintenance Supervisor", "Quality Assurance Manager", "Harvest Team Leader",
     "Environmental Systems Manager", "Nutrient Systems Manager", "Data Analytics Manager", "Production Supervisor",
     "Food Safety Compliance Officer", "Automation Engineer", "Plant Health Inspector", "Franchise Owner",
     "Regional Franchise Manager", "Franchise Operations Director", "Chief Investment Officer", "Investment Manager"]

C = ["System Design & Optimization", "Environmental Parameter Monitoring", "Nutrient Solution Management",
     "Plant Health Assessment", "Growth Cycle Planning", "Equipment Maintenance", "Quality Control Inspections",
     "Harvest Scheduling", "Data Collection & Analysis", "Compliance Monitoring", "System Troubleshooting",
     "Resource Usage Optimization", "Production Planning", "Safety Protocol Implementation", "Team Coordination"]

D = ["pH Level Monitoring", "Electrical Conductivity (EC) Testing", "Temperature Control Adjustment",
     "Humidity Level Management", "Light Intensity Calibration", "Nutrient Mix Preparation", "Water Quality Testing",
     "Growth Rate Documentation", "Equipment Sanitization", "System Flow Rate Checks", "Plant Spacing Optimization",
     "Harvest Weight Recording", "Equipment Calibration", "Safety Inspection Rounds", "Inventory Management",
     "Growth Data Recording", "Team Schedule Creation", "Maintenance Log Updates", "Quality Check Documentation",
     "Compliance Report Generation"]

# Example rules for validation
def is_valid_combination(selected_role, selected_sub_role, selected_action, selected_activity):
    # Rule 1: Only Agricultural Engineers and System Technicians can perform System Design & Optimization
    if action == "System Design & Optimization" and role not in ["Agricultural Engineers", "System Technicians"]:
        return 0
    # Rule 2: Franchise Operators should not perform technical activities like Nutrient Mix Preparation
    if selected_role == "Franchise Operators" and activity in ["Nutrient Mix Preparation", "pH Level Monitoring"]:
        return 0
    # Rule 3: Plant Scientists should focus on Plant Health Assessment and Growth Cycle Planning
    if selected_role == "Plant Scientists" and action not in ["Plant Health Assessment", "Growth Cycle Planning"]:
        return 0
    # Rule 4: Quality Assurance Manager should focus on Quality Control Inspections and Compliance Monitoring
    if selected_sub_role == "Quality Assurance Manager" and action not in ["Quality Control Inspections", "Compliance Monitoring"]:
        return 0
    # Rule 5: Franchise Owners should focus on business-related actions like Franchise Performance Review
    if selected_role == "Franchise Operators" and action not in ["Franchise Performance Review", "Business Expansion Planning"]:
        return 0
    # Rule 6: Operations Managers should handle actions like Production Planning and Team Coordination
    if selected_role == "Operations Managers" and action not in ["Production Planning", "Team Coordination"]:
        return 0
    # Add more rules as needed based on your business logic
    
    # Default valid if no rule invalidates it
    return 1

# Generate all combinations
combinations = list(itertools.product(A, B, C, D))

# Initialize the truth table
truth_table = []

# Validate each combination based on the rules
for combination in combinations:
    role, job_title, action, activity = combination
    valid = is_valid_combination(role, job_title, action, activity)
    truth_table.append(combination + (valid,))

# Convert to a pandas DataFrame
df = pd.DataFrame(truth_table, columns=['Role (A)', 'Job Title/Position (B)', 'Action (C)', 'Activity (D)', 'Valid/Invalid (R)'])

# Save the truth table to a CSV file for further analysis or processing
df.to_csv('expanded_truth_table.csv', index=False)

# Display the first few rows
print(df.head())
