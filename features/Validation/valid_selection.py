# This script defines the options in the four lists 
# and provides functions to validate user selections against a Truth Table

# import itertools
# import pandas as pd

from RAI2023_Castara.features.Validation.Rules import is_valid_combination

# Define lists A, B, C, and D
A = ["Agricultural Engineers", "Horticulturists", "System Specialist", "Plant Scientists", "Operations Managers",
     "Maintenance Staff", "Quality Control Personnel", "Harvest Workers", "Climate Control Specialists",
     "Nutrient Management Specialists", "Franchise Operators", "Franchisors", "Management Personnel", "Investors"]

B = ["Head of Agricultural Engineering", "Lead Horticulturist", "Systems Integration Engineer", "Plant Science Director", "Operations Director", 
     "Maintenance Supervisor", "Quality Assurance Manager", "Harvest Team Leader", "Environmental Systems Manager", "Nutrient Systems Manager", 
     "Data Analytics Manager", "Production Supervisor", "Food Safety Compliance Officer", "Automation Engineer", "Plant Health Inspector", 
     "Franchise Owner", "Regional Franchise Manager", "Franchise Operations Director", "Chief Investment Officer", "Investment Manager", 
     "Portfolio Manager", "Executive Director", "Chief Operations Officer", "Chief Financial Officer", "Business Development Manager", 
     "Franchise Development Director", "Investment Analyst", "Financial Controller", "Franchise Compliance Manager", "Investor Relations Manager"] 

C = ["System Design & Optimization", "Environmental Parameter Monitoring", "Nutrient Solution Management", "Plant Health Assessment", "Growth Cycle Planning", 
     "Equipment Maintenance", "Quality Control Inspections", "Harvest Scheduling", "Data Collection & Analysis", "Compliance Monitoring",
     "System Troubleshooting", "Resource Usage Optimization", "Production Planning”, “Safety Protocol Implementation”, “Team Coordination”, 
     "Investment Performance Monitoring", "Franchise Performance Review", "Financial Analysis", "Business Expansion Planning", "Franchise Agreement Management", 
     "Risk Assessment", "Return on Investment Analysis", "Franchise Standards Enforcement", "Capital Allocation", "Market Analysis", "Investor Reporting",
     "Franchise Training Program Management", "Performance Metrics Review", "Strategic Planning", "Compliance Auditing” ]

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

def validate_choice(selected_role, selected_sub_role, selected_action, selected_activity):
    """Validate the selection by checking if the combination matches valid rules."""
    st.write(" ")
    st.write("⚠️ - Preparing to validate selected choices as a combination .... ")
    return is_valid_combination(selected_role, selected_sub_role, selected_action, selected_activity)
