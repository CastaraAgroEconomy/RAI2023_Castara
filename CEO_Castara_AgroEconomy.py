import streamlit as st

# Initial configurations and variables
roles = ["Franchisee", "Investor", "Management", "Support Staff", "Owner"]
sub_roles = {
    "Franchisee": ["Owner", "Operator", "Partner", "Assistant"],
    "Investor": ["Silent Partner", "Active Investor", "Consultant"],
    "Management": ["CEO", "CFO", "COO", "Director"],
    "Support Staff": ["Technician", "Customer Service", "Marketer"],
    "Owner": ["Sole Owner", "Majority Owner", "Minority Owner"]
}
plans = ["Plan A", "Plan B", "Plan C"]
activities = {
    "Plan A": ["Develop Strategy", "Resource Allocation", "No further option"],
    "Plan B": ["Budget Planning", "Staffing", "Monitoring"],
    "Plan C": ["Marketing", "Expansion", "Exit Planning"]
}

# Define valid combinations for AI-powered Inference Engine (AI-p IE)
valid_combinations = [
    ("Franchisee", "Owner", "Plan A", "Develop Strategy"),
    ("Management", "CEO", "Plan B", "Staffing"),
    # Add other valid combinations here
]

# Function to check if the selection is valid
def is_valid_combination(role, sub_role, plan, activity):
    return (role, sub_role, plan, activity) in valid_combinations

# Function to handle invalid selections
def invalid_selection():
    st.error("Invalid combination of choices selected. Please review and revise accordingly.")
    st.experimental_rerun()  # Restart the selection process

# Cover Page Image
st.image('Assets/Media/Images/Cover_page.jpg')

# Title and Introduction
st.title("Business Journey Navigation")

# 1. User Role Selection
role = st.radio("Choose your User Role:", roles)

if role:
    sub_role = st.radio(f"Choose your Sub-Role under {role}:", sub_roles[role])

    if sub_role:
        plan = st.radio("Choose your Plan:", plans)

        if plan:
            activity = st.radio(f"Choose an Activity under {plan}:", activities[plan])

            if activity:
                # Display the current path of selections
                st.write(f"Final selection: {role} -> {sub_role} -> {plan} -> {activity}")

                # Navigation buttons
                if st.button("Next"):
                    if not is_valid_combination(role, sub_role, plan, activity):
                        invalid_selection()
                    else:
                        st.success("Valid combination. Proceeding to the next part of the journey...")

                # Log Out button
                if st.button("Log Out"):
                    st.write("You have been logged out.")
                    st.stop()  # Stop the app (user would need to log in again)

                # Help button
                if st.button("Help"):
                    st.video('Assets/Media/Videos/Help.mp4')  # Display the help video
