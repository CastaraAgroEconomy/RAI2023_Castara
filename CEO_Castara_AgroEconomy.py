import streamlit as st

# Set page configuration and display Cover Page Image
st.set_page_config(page_title="Mobile App", layout="centered")
st.image('Assets/Media/Images/Cover_page.jpg')

# Function to display navigation instructions
def show_navigation_instructions():
    st.markdown("""
    ### ⚠️ Navigation Instructions
    Refer to the top left and right-hand side of your screen in portrait mode.
    Use the '>' and '<' navigation icons to move forward or backward between the lists.
    You can also jump back using the shortcut buttons provided under each list.
    """)

# Display initial navigation instructions
show_navigation_instructions()

# Login screen
login_credentials = st.text_input("Enter your credentials (Username/Password)", type="password")
if login_credentials:
    st.success("Login successful!")

    # Define the roles, sub-roles, actions, and activities
    roles = ['Franchisee', 'Manager', 'Investor', 'Supplier', 'Researcher', 'AI Specialist', 'Supply Chain Analyst', 'Market Strategist', 'No further option']
    sub_roles = {
        'Franchisee': ['Owner', 'Operator', 'No further option'],
        'Manager': ['HR Manager', 'Project Manager', 'No further option'],
        'Investor': ['Angel Investor', 'Venture Capitalist', 'No further option'],
        'Supplier': ['Local Supplier', 'Global Supplier', 'No further option'],
        'Researcher': ['Data Analyst', 'Field Researcher', 'No further option'],
        'AI Specialist': ['Machine Learning Engineer', 'Data Scientist', 'No further option'],
        'Supply Chain Analyst': ['Logistics Manager', 'Inventory Analyst', 'No further option'],
        'Market Strategist': ['Brand Manager', 'Market Research Analyst', 'No further option']
    }
    actions = ['Plan', 'Execute', 'Monitor', 'No further option']
    activities = {
        'Plan': ['Develop Strategy', 'Resource Allocation', 'No further option'],
        'Execute': ['Implement Solutions', 'On-field Operations', 'No further option'],
        'Monitor': ['Progress Tracking', 'Report Generation', 'No further option']
    }

    # Present role selection via radio buttons
    st.header("Select User Role")
    selected_role = st.radio("Choose a Role:", roles)

    if selected_role != 'No further option':
        # Present sub-role options based on selected role
        st.header(f"Select Sub-role for {selected_role}")
        selected_sub_role = st.radio(f"Choose a Sub-role under {selected_role}:", sub_roles[selected_role])

        if selected_sub_role != 'No further option':
            # Present action options
            st.header(f"Select Action for {selected_sub_role}")
            selected_action = st.radio("Choose an Action:", actions)

            if selected_action != 'No further option':
                # Present activity options based on selected action
                st.header(f"Select Activity under {selected_action}")
                selected_activity = st.radio(f"Choose an Activity under {selected_action}:", activities[selected_action])

                # Display a summary of the selection
                st.write(f"You selected: **{selected_role} -> {selected_sub_role} -> {selected_action} -> {selected_activity}**")

                # Shortcut navigation buttons for jumping back
                if st.button("⬅️ Jump back to Sub-role"):
                    st.session_state.current_step = 'sub_role'
                if st.button("⬅️ Jump back to Role"):
                    st.session_state.current_step = 'role'

                # Option to log out or reset
                if st.button("Log Out"):
                    st.experimental_rerun()

# Ensure to reset flags and parameters if user logs out
if 'current_step' not in st.session_state:
    st.session_state.current_step = 'login'

# Load 'Help.mp4' video for help navigation
if st.button("Help"):
    st.video('Assets/Media/Video/Help.mp4')
