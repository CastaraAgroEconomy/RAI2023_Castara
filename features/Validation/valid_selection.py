# Updated menu List [A], [B], [C], [D], 
# which produce a (14,30,30,35) four dimensional Matrix,
# Truth Table with 441,000 combinations

import streamlit as st
import itertools
import pandas as pd

if 'selected_role' not in st.session_state:
    st.session_state.selected_role = None
    
if 'selected_sub_role' not in st.session_state:
    st.session_state.selected_sub_role = None

if 'selected_action' not in st.session_state:
    st.session_state.selected_action = None

if 'selected_activity' not in st.session_state:
    st.session_state.selected_activity = None

if 'self' not in session_state:
    st.session_state.self = None

if 'R_go' not in st.session_state:
    st.session_state.R_go = 0

from features.Validation.Rules import check_select



def valid_selection(self, R_go, selected_role, selected_sub_role, selected_action, selected_activity)

# Define the matrices
   A = ["Agricultural Engineers", "Horticulturists", "System Specialist", "Plant Scientists", "Operations Managers",
        "Maintenance Staff", "Quality Control Personnel", "Harvest Workers", "Climate Control Specialists",
        "Nutrient Management Specialists", "Franchise Operators", "Franchisors", "Management Personnel", "Investors"]

   B = ["Head of Agricultural Engineering", "Lead Horticulturist", "Systems Integration Engineer", "System Technician", "Plant Science Director",
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


# Generate all combinations
  combinations = list(itertools.product(A, B, C, D))

# Initialize the truth table
  R = []

# Apply rules for validation
  check_select(selected_role, selected_sub_role, selected_action, selected_activity)

# Validate each combination based on the rules
  for combination in combinations:
     selected_role, selected_sub_role, selected_action, selected_activity = combination
     valid = is_valid_combination(selected_role, selected_sub_role, selected_action, selected_activity)
     R.append(combination + (valid,))

# Convert to a pandas DataFrame
  df = pd.DataFrame(R, columns=['Role (A)', 'Job Title/function (B)', 'Action (C)', 'Activity (D)', 'Valid/Invalid (1/0)'])

# Save the truth table to a CSV file for further analysis or processing
  df.to_csv('expanded_truth_table.csv', index=False)

# Display the first few rows
  print(df.head())
