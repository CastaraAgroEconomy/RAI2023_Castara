import streamlit as st

# Media asset display
def display_media_asset():
    """Display media asset on a cleared screen"""
    st.image("Assets/Media/Images/Cover_page.jpg", caption="Castara AgroEconomy Venture")

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
            st.session_state["step"] = 1  # Start at the role selection step
        else:
            st.error("Invalid credentials. Please try again.")


# Role selection
def role_selection():
    """Display user role selection on a cleared screen"""
    roles = [
        "Franchisee", "Management", "Investor", 
        "Agronomist", "Operations Coordinator", 
        "Supply Chain Coordinator", "IT Specialist", "Finance Manager", 
        "Research and Development", "Sales and Marketing"
    ]
    selected_role = st.selectbox("Select User Role", roles)
    if st.button("Next"):
        st.session_state["role"] = selected_role
        st.session_state["step"] = 2  # Move to the sub-role selection step

# Sub-role selection
def sub_role_selection():
    """Display sub-role selection based on user role"""
    sub_roles = {
        "Franchisee": ["Owner", "Operator", "Worker", "Consultant", "Partner"],
        "Management": ["Marketing Manager", "Customer Relations Manager", "Operations Manager", "Product Manager", "Finance Manager"],
        "Investor": ["Equity Investor", "Angel Investor", "Venture Capitalist", "Private Investor", "Crowdfunder"],
        "Agronomist": ["Field Agronomist", "Soil Scientist", "Plant Breeder", "Crop Advisor", "Agro Researcher"],
        "Operations Coordinator": ["Logistics", "Field Supervisor", "Harvest Supervisor", "Distribution Coordinator", "Operations Assistant"],
    }
    selected_sub_role = st.selectbox("Select Sub-Role", sub_roles.get(st.session_state["role"], []))
    if st.button("Next"):
        st.session_state["sub_role"] = selected_sub_role
        st.session_state["step"] = 3  # Move to the action selection step

# Action selection
def action_selection():
    """Display action selection on a cleared screen"""
    actions = [
        "Initiate Process", "Monitor Operations", "Manage Resources", 
        "Analyze Data", "Conduct Research", 
        "Market Products", "Manage Supply Chain", "Oversee Finance", 
        "Research Innovation", "Negotiate Contracts"
    ]
    selected_action = st.selectbox("Select Action", actions)
    if st.button("Next"):
        st.session_state["action"] = selected_action
        st.session_state["step"] = 4  # Move to the activity selection step

# Activity selection
def activity_selection():
    """Display activity selection based on action"""
    activities = {
        "Initiate Process": ["Start Farm Cycle", "Plan Schedule", "Request Supplies", "Assign Workers", "Allocate Resources"],
        "Monitor Operations": ["Check Soil", "Monitor Crops", "Check Weather", "Monitor Equipment", "Review Tasks"],
        "Manage Resources": ["Review Budgets", "Approve Requests", "Allocate Materials", "Order Inventory", "Authorize Expenses"],
    }
    selected_activity = st.selectbox("Select Activity", activities.get(st.session_state["action"], []))
    if st.button("Finish"):
        st.session_state["activity"] = selected_activity
        st.success(f"Process complete! You selected: {st.session_state['role']}, {st.session_state['sub_role']}, {st.session_state['action']}, {st.session_state['activity']}")

# Main logic to control the flow
def main():

    display_media_asset()
    
    # Login system
    if "authenticated" not in st.session_state:
        login()
    else:
        # Show media asset after login
        display_media_asset()

        # Step-based navigation for each selection screen
        step = st.session_state.get("step", 1)

        if step == 1:
            st.write("### Please select your User Role")
            role_selection()

        elif step == 2:
            st.write("### Please select your Sub-Role")
            sub_role_selection()

        elif step == 3:
            st.write("### Please select an Action")
            action_selection()

        elif step == 4:
            st.write("### Please select an Activity")
            activity_selection()

# Running the app
if __name__ == "__main__":
    main()
