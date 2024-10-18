import streamlit as st

# Function to load media assets
def load_image(image_path):
    from PIL import Image
    return Image.open(image_path)

def load_text(text_path):
    with open(text_path, 'r') as file:
        return file.read()

# Image and text file paths
cover_image_path = 'Assets/Media/Images/Cover_page.jpg'
navigation_text_path = 'Assets/Media/Text/Navigation.txt'

# Initial login routine
st.title("Welcome to the Castara AgroEconomy Venture App")
st.image(load_image(cover_image_path), use_column_width=True)

# Login credentials (just a mockup for now)
username = st.text_input("Enter Username")
password = st.text_input("Enter Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "admin":  # Mockup credentials
        st.success(f"Welcome, {username}!")
        st.write(load_text(navigation_text_path))

        # Navigation with radio buttons
        section = st.radio("Choose a section", ["User Role", "Sub-User Role", "Action", "Activity"])

        if section == "User Role":
            roles = ['Franchisee', 'Manager', 'Investor', 'Supplier', 'Researcher', 'AI Specialist', 'Supply Chain Analyst', 'Market Strategist', 'Finance Officer', 'HR Specialist']
            selected_role = st.selectbox("Select a User Role", roles)
            st.write(f"You selected: {selected_role}")

        elif section == "Sub-User Role":
            sub_roles = {
                'Franchisee': ['Owner', 'Field Operator', 'Site Manager'],
                'Manager': ['Operations', 'Logistics', 'Performance Manager'],
                'Investor': ['Private Equity', 'Venture Capitalist', 'Angel Investor'],
                'Supplier': ['Raw Materials', 'Equipment', 'Logistics Support'],
                'Researcher': ['Crop Scientist', 'Agronomist', 'Economist'],
                'AI Specialist': ['Data Scientist', 'ML Engineer', 'AI Systems Developer'],
                'Supply Chain Analyst': ['Logistics Coordinator', 'Distribution Planner', 'Procurement Officer'],
                'Market Strategist': ['Brand Manager', 'Sales Executive', 'Product Developer'],
                'Finance Officer': ['Accountant', 'Financial Analyst', 'Auditor'],
                'HR Specialist': ['Recruitment Officer', 'Employee Relations', 'Training Coordinator']
            }
            role = st.radio("Choose a Role to filter Sub-User Roles", list(sub_roles.keys()))
            selected_sub_role = st.selectbox(f"Select a Sub-User Role for {role}", sub_roles[role])
            st.write(f"You selected: {selected_sub_role}")

        elif section == "Action":
            actions = ['Initiate Process', 'Monitor Operations', 'Manage Resources', 'Analyze Data', 'Conduct Research', 'Market Products', 'Manage Supply Chain', 'Oversee Finance']
            selected_action = st.selectbox("Select an Action", actions)
            st.write(f"You selected: {selected_action}")

        elif section == "Activity":
            activities = {
                'Initiate Process': ['Request Supplies', 'Approve Budget', 'Allocate Resources'],
                'Monitor Operations': ['Track Crop Health', 'Monitor Weather', 'Assess Yield Performance'],
                'Manage Resources': ['Distribute Equipment', 'Schedule Labor', 'Manage Energy Use'],
                'Analyze Data': ['Run Financial Reports', 'Analyze Crop Data', 'Generate KPIs'],
                'Conduct Research': ['Test New Seeds', 'Conduct Soil Tests', 'Run Trials'],
                'Market Products': ['Develop Campaign', 'Track Sales', 'Analyze Consumer Feedback'],
                'Manage Supply Chain': ['Coordinate Logistics', 'Negotiate Contracts', 'Monitor Deliveries'],
                'Oversee Finance': ['Approve Funding', 'Review Transactions', 'Analyze Investment Performance']
            }
            action = st.radio("Choose an Action to filter Activities", list(activities.keys()))
            selected_activity = st.selectbox(f"Select an Activity for {action}", activities[action])
            st.write(f"You selected: {selected_activity}")
    else:
        st.error("Invalid credentials. Please try again.")
