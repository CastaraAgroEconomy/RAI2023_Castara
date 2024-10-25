# Validation Rules for conversion to Truth Table "0"s and "1"s
# Example rules for validation

import streamlit as st

def is_valid_combination(role, job_title, action, activity):
    # Rule 1: Only Agricultural Engineers and System Technicians can perform System Design & Optimization
    if action == "System Design & Optimization" and role not in ["Agricultural Engineers", "System Technicians"]:
        return 0
    # Rule 2: Franchise Operators should not perform technical activities like Nutrient Mix Preparation
    if role == "Franchise Operators" and activity in ["Nutrient Mix Preparation", "pH Level Monitoring"]:
        return 0
    # Rule 3: Plant Scientists should focus on Plant Health Assessment and Growth Cycle Planning
    if role == "Plant Scientists" and action not in ["Plant Health Assessment", "Growth Cycle Planning"]:
        return 0
    # Rule 4: Quality Assurance Manager should focus on Quality Control Inspections and Compliance Monitoring
    if job_title == "Quality Assurance Manager" and action not in ["Quality Control Inspections", "Compliance Monitoring"]:
        return 0
    # Rule 5: Franchise Owners should focus on business-related actions like Franchise Performance Review
    if role == "Franchise Operators" and action not in ["Franchise Performance Review", "Business Expansion Planning"]:
        return 0
    # Rule 6: Operations Managers should handle actions like Production Planning and Team Coordination
    if role == "Operations Managers" and action not in ["Production Planning", "Team Coordination"]:
        return 0
      
    # Add more rules as needed based on your business logic
    
    # Default valid if no rule invalidates it
    return 1
