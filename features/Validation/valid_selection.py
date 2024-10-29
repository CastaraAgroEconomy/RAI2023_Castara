# This script defines the options in the four lists 
# and provides functions to validate user selections against a Truth Table

import itertools
import pandas as pd
from features.Validation.Rules.py import is_valid_combination()

# Define lists A, B, C, and D
A = ["Agricultural Engineers", "Horticulturists", "System Specialist", "Plant Scientists", "Operations Managers",
     "Maintenance Staff", "Quality Control Personnel", "Harvest Workers", "Climate Control Specialists",
     "Nutrient Management Specialists", "Franchise Operators", "Franchisors", "Management Personnel", "Investors"]

B = ["Head of Agricultural Engineering", "Lead Horticulturist", "Systems Integration Engineer", "System Technician",
     "Plant Science Director", "Operations Director", "Maintenance Supervisor", "Quality Assurance Manager",
     "Harvest Team Leader", "Environmental Systems Manager", "Nutrient Systems Manager", "Data Analytics Manager",
     "Production Supervisor", "Food Safety Compliance Officer", "Automation Engineer", "Plant Health Inspector",
     "Franchise Owner", "Regional Franchise Manager", "Franchise Operations Director", "Chief Investment Officer",
     "Investment Manager"]

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

def get_roles():
    return A

def get_sub_roles():
    return B

def get_actions():
    return C

def get_activities():
    return D

def validate_selection(selected_role, selected_sub_role, selected_action, selected_activity):
    """Validate the selection by checking if the combination matches valid rules."""
    is_valid = is_valid_combination(selected_role, selected_sub_role, selected_action, selected_activity)
    return is_valid, None if is_valid else "selection"
