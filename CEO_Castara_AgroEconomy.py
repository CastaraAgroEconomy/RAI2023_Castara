import streamlit as st
import pandas as pd

# Defining maximum configuration values for n, m, x, y
n = 10  # Maximum number of user roles
x = 15  # Maximum number of sub-roles per user role
m = 20  # Maximum number of actions
y = 20  # Maximum number of activities per action

# User roles (A)
roles = [
    "Franchise Owner",
    "Franchisee",
    "Management",
    "Investor",
    "Consultant",
    "Agronomist",
    "Supply Chain Manager",
    "Financial Analyst",
    "Customer Relations",
    "Technical Support"
]

# Sub-user roles (B) associated with each user role (Bn)
sub_roles = {
    "Franchise Owner": [
        "Strategic Planner", "Operational Leader", "Growth Advisor", "Investment Planner", "Risk Manager",
        "Compliance Officer", "Brand Strategist", "Revenue Optimizer", "Expense Controller", "Human Resource Lead"
    ],
    "Franchisee": [
        "Retail Manager", "Local Operations Manager", "Sales Supervisor", "Stock Controller", "Regional Liaison",
        "Logistics Coordinator", "Franchise Development Officer", "Training Facilitator", "Customer Service Leader", "Marketing Director"
    ],
    "Management": [
        "Marketing & Sales Manager", "Customer Relations Manager", "Distribution Manager", "Product & Services Manager", 
        "Facilities & Resources Manager", "Project Manager", "Supply Chain and Partner Manager", "Cost & Expense Accounting Manager", 
        "Revenue Streams Manager", "Franchisee Manager", "Quality Assurance Manager", "Financial Reporting Manager", "Risk & Compliance Manager", 
        "Technology Manager", "Sustainability Officer"
    ],
    # Add sub-roles for other roles...
}

# Actions (C)
actions = [
    "Monitor Crop Growth", "Optimize Supply Chain", "Generate Financial Reports", "Manage Staff", "Develop New Products", 
    "Review Marketing Strategy", "Adjust Franchisee Agreements", "Oversee Risk Management", "Allocate Resources", "Evaluate Franchisee Performance", 
    "Handle Customer Complaints", "Update Inventory", "Manage External Partnerships", "Analyze Market Trends", "Conduct Training", 
    "Review Financial Projections", "Implement Technology Solutions", "Plan Expansion", "Monitor Legal Compliance", "Execute Marketing Campaigns"
]

# Activities (D) associated with each action (Dn)
activities = {
    "Monitor Crop Growth": [
        "Check Soil Quality", "Analyze Crop Yield", "Review Water Usage", "Evaluate Pest Control Measures", "Monitor Weather Impact",
        "Inspect Plant Health", "Record Growth Metrics", "Generate Crop Reports", "Update Irrigation Settings", "Plan Fertilizer Use", 
        "Check for Disease Outbreak", "Adjust Planting Schedules", "Evaluate Seed Varieties", "Monitor Harvest Timelines", "Optimize Growth Environments",
        "Ensure Regulatory Compliance", "Compare to Historical Data", "Coordinate with Agronomists", "Manage Field Equipment", "Track Crop Maturity"
    ],
    "Optimize Supply Chain": [
        "Review Supplier Contracts", "Analyze Shipping Efficiency", "Track Delivery Times", "Manage Inventory Levels", "Assess Packaging Options",
        "Negotiate New Contracts", "Evaluate Supplier Performance"
    ],
    # Add entries for other actions...
}

# Error handling: Ensure all actions are represented in activities dictionary
for action in actions:
    if action not in activities:
        activities[action] = ["No specific activities available"]

# Create all combinations of roles, sub-roles, actions, and activities
all_combinations = [(r, sr, a, act) for r in roles for sr in sub_roles.get(r, []) for a in actions for act in activities.get(a, [])]

# Display the first 10 combinations for preview
st.write("Sample Combinations:")
st.write(all_combinations[:10])

# Display total combinations count
st.write(f"Total number of combinations: {len(all_combinations)}")
