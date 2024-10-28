# Validation Rules for conversion to Truth Table "0"s and "1"s
# Example rules for validation

import streamlit as st

selected_role = session_state.get('selected_role', None)
selected_sub_role = session_state.get('selected_sub_role', None)
selected_action = session_state.get('selected_action', None)
selected_activity = session_state.get('selected_activity', None)

def is_valid_combination(suggested_role, selected_sub_role, selected_action, selected_activity):
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
      
    # Add more rules as needed based on your business logic
    
    # Default valid if no rule invalidates it
    return 1
