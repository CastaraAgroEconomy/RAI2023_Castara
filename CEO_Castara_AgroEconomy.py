import streamlit as st

# Mock Login System
def login():
    """Simulate a login system"""
    st.title("Castara AgroEconomy Venture Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state["authenticated"] = True
            st.success("Login successful!")
        else:
            st.error("Invalid credentials. Please try again.")

# Media asset display
def display_media_asset():
    """Display media asset on a cleared screen"""
    st.image("features/Assets/Media/Images/Cover_page.jpg", caption="Castara AgroEconomy Venture")

# Role selection
def role_selection():
    """Display user role selection on a cleared screen"""
    roles = [
        "Franchisee", "Management", "Investor", 
        "Agronomist", "Operations Coordinator", 
        "Supply Chain Coordinator", "IT Specialist", "Finance Manager", 
        "Research and Development", "Sales and Marketing"
    ]
    return st.selectbox("Select User Role", roles)

# Sub-role selection
def sub_role_selection(role):
    """Display sub-role selection based on user role"""
    sub_roles = {
        "Franchisee": ["Owner", "Operator", "Worker", "Consultant", "Partner"],
        "Management": ["Marketing Manager", "Customer Relations Manager", "Operations Manager", "Product Manager", "Finance Manager"],
        "Investor": ["Equity Investor", "Angel Investor", "Venture Capitalist", "Private Investor", "Crowdfunder"],
        "Agronomist": ["Field Agronomist", "Soil Scientist", "Plant Breeder", "Crop Advisor", "Agro Researcher"],
        "Operations Coordinator": ["Logistics", "Field Supervisor", "Harvest Supervisor", "Distribution Coordinator", "Operations Assistant"],
        # Fill out the other roles with appropriate sub-roles
    }
    return st.selectbox("Select Sub-Role", sub_roles.get(role, []))

# Action selection
def action_selection():
    """Display action selection on a cleared screen"""
    actions = [
        "Initiate Process", "Monitor Operations", "Manage Resources", 
        "Analyze Data", "Conduct Research", 
        "Market Products", "Manage Supply Chain", "Oversee Finance", 
        "Research Innovation", "Negotiate Contracts"
    ]
    return st.selectbox("Select Action", actions)

# Activity selection
def activity_selection(action):
    """Display activity selection based on action"""
    activities = {
        "Initiate Process": ["Start Farm Cycle", "Plan Schedule", "Request Supplies", "Assign Workers", "Allocate Resources"],
        "Monitor Operations": ["Check Soil", "Monitor Crops", "Check Weather", "Monitor Equipment", "Review Tasks"],
        "Manage Resources": ["Review Budgets", "Approve Requests", "Allocate Materials", "Order Inventory", "Authorize Expenses"],
        # Add more activities corresponding to actions
    }
    return st.selectbox("Select Activity", activities.get(action, []))

# Main logic to control the flow
def main():
    # Login system
    if "authenticated" not in st.session_state:
        login()
    else:
        # Show media asset after login
        display_media_asset()

        # Clear the screen for role selection
        st.write("### Please select your User Role")
        selected_role = role_selection()
        st.write(f"You selected: {selected_role}")

        # Clear the screen for sub-role selection based on role
        if selected_role:
            st.write("### Please select your Sub-Role")
            selected_sub_role = sub_role_selection(selected_role)
            st.write(f"You selected: {selected_sub_role}")

        # Clear the screen for action selection
        if selected_sub_role:
            st.write("### Please select an Action")
            selected_action = action_selection()
            st.write(f"You selected: {selected_action}")

        # Clear the screen for activity selection based on action
        if selected_action:
            st.write("### Please select an Activity")
            selected_activity = activity_selection(selected_action)
            st.write(f"You selected: {selected_activity}")

# Running the app
if __name__ == "__main__":
    main()
