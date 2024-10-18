import streamlit as st

# Set page configuration and display Cover Page Image
st.set_page_config(page_title="Mobile App", layout="centered")
cover_page = st.empty()
cover_page.image('Assets/Media/Images/Cover_page.jpg')

# Function to display navigation instructions
def show_navigation_instructions():
    st.markdown("""
    ### ⚠️ Navigation Instructions
    Refer to the top left and right-hand side of your screen in portrait mode.
    Use the '>' and '<' navigation icons to move forward or backward between the lists.
    You can also jump back using the shortcut buttons provided under each list.
    """)

# Display initial navigation instructions
nav_instructions = st.empty()
nav_instructions.markdown("""
### ⚠️ Navigation Instructions
Refer to the top left and right-hand side of your screen in portrait mode.
Use the '>' and '<' navigation icons to move forward or backward between the lists.
You can also jump back using the shortcut buttons provided under each list.
""")

# Reset session state if not set
if 'step' not in st.session_state:
    st.session_state.step = 'login'

# Function to clear screen before presenting new list
def clear_screen():
    cover_page.empty()
    nav_instructions.empty()

# Function to reset state and logout
def logout():
    st.session_state.step = 'login'
    st.experimental_rerun()

# Function to reset everything and reload login
def reset_session():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.experimental_rerun()

# Login screen logic
if st.session_state.step == 'login':
    login_credentials = st.text_input("Enter your credentials (Username/Password)", type="password")
    if login_credentials:
        st.success("Login successful!")
        st.session_state.step = 'role_selection'
        st.experimental_rerun()

# Role Selection
if st.session_state.step == 'role_selection':
    clear_screen()  # Clear screen before presenting roles
    roles = ['Franchisee', 'Manager', 'Investor', 'Supplier', 'Researcher', 'AI Specialist', 'Supply Chain Analyst', 'Market Strategist', 'No further option']
    
    st.header("Select User Role")
    selected_role = st.radio("Choose a Role:", roles)
    
    if selected_role:
        st.session_state.selected_role = selected_role
        if selected_role != 'No further option':
            st.session_state.step = 'sub_role_selection'
        else:
            st.session_state.step = 'role_selection'
        st.experimental_rerun()

# Sub-Role Selection
if st.session_state.step == 'sub_role_selection':
    clear_screen()  # Clear screen before presenting sub-roles
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
    
    st.header(f"Select Sub-role for {st.session_state.selected_role}")
    selected_sub_role = st.radio(f"Choose a Sub-role under {st.session_state.selected_role}:", sub_roles[st.session_state.selected_role])
    
    if selected_sub_role:
        st.session_state.selected_sub_role = selected_sub_role
        if selected_sub_role != 'No further option':
            st.session_state.step = 'action_selection'
        else:
            st.session_state.step = 'sub_role_selection'
        st.experimental_rerun()

# Action Selection
if st.session_state.step == 'action_selection':
    clear_screen()  # Clear screen before presenting actions
    actions = ['Plan', 'Execute', 'Monitor', 'No further option']
    
    st.header(f"Select Action for {st.session_state.selected_sub_role}")
    selected_action = st.radio("Choose an Action:", actions)
    
    if selected_action:
        st.session_state.selected_action = selected_action
        if selected_action != 'No further option':
            st.session_state.step = 'activity_selection'
        else:
            st.session_state.step = 'action_selection'
        st.experimental_rerun()

# Activity Selection
if st.session_state.step == 'activity_selection':
    clear_screen()  # Clear screen before presenting activities
    activities = {
        'Plan': ['Develop Strategy', 'Resource Allocation', 'No further option'],
        'Execute': ['Implement Solutions', 'On-field Operations', 'No further option'],
        'Monitor': ['Progress Tracking', 'Report Generation', 'No further option']
    }
    
    st.header(f"Select Activity under {st.session_state.selected_action}")
    selected_activity = st.radio(f"Choose an Activity under {st.session_state.selected_action}:", activities[st.session_state.selected_action])
    
    if selected_activity:
        st.session_state.selected_activity = selected_activity
        st.write(f"Final selection: **{st.session_state.selected_role} -> {st.session_state.selected_sub_role} -> {st.session_state.selected_action} -> {st.session_state.selected_activity}**")
        if st.button("Log Out"):
            logout()

# Option to log out
if st.session_state.step != 'login' and st.button("Log Out"):
    reset_session()

# Load Help video
if st.button("Help"):
    st.video('Assets/Media/Video/Help.mp4')
