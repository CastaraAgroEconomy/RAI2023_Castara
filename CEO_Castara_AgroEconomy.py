import streamlit as st

# Function to handle login logic
def login():
    # Assuming a dummy login for simplicity
    st.image('Assets/Media/Images/Cover_page.jpg', use_column_width=True)
    st.title("Welcome to Castara AgroEconomy")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password123":
            st.session_state['logged_in'] = True
            st.success("Login successful!")
            return True
        else:
            st.error("Invalid username or password.")
    return False

# Main app logic
def app():
    # Ensure user is logged in before displaying content
    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        if not login():
            return  # Stop the function if not logged in
    
    # User role selection
    if 'selected_role' not in st.session_state:
        st.warning("⚠️ - Navigation Instructions")
        st.text("Refer to the top left and right-hand side of the screen for navigation icons when in portrait mode.")
        selected_role = st.selectbox("Please select your Role", ['Franchisee', 'Manager', 'Investor', 'Supplier', 'Researcher', 'AI Specialist', 'Supply Chain Analyst', 'Market Strategist'])
        st.session_state['selected_role'] = selected_role
        st.write(f'You selected: {selected_role}')
        return  # Clear screen and return after role selection
    
    # Sub-role selection
    if 'selected_sub_role' not in st.session_state:
        selected_sub_role = st.selectbox(f"Please select a Sub-Role for {st.session_state['selected_role']}", ['Sub-Role 1', 'Sub-Role 2', 'Sub-Role 3'])
        st.session_state['selected_sub_role'] = selected_sub_role
        st.write(f'You selected: {selected_sub_role}')
        return  # Clear screen and return after sub-role selection
    
    # Action selection
    if 'selected_action' not in st.session_state:
        selected_action = st.selectbox("Please select an Action", ['Initiate Process', 'Monitor Operations', 'Manage Resources', 'Analyze Data', 'Conduct Research'])
        st.session_state['selected_action'] = selected_action
        st.write(f'You selected: {selected_action}')
        return  # Clear screen and return after action selection
    
    # Activity selection
    if 'selected_activity' not in st.session_state:
        selected_activity = st.selectbox("Please select an Activity", ['Request Supplies', 'Submit Report', 'Oversee Project', 'Market Products'])
        st.session_state['selected_activity'] = selected_activity
        st.write(f'You selected: {selected_activity}')
        return  # Clear screen and return after activity selection
    
    # Display final result (representing the final page after all selections)
    st.success(f"Navigation complete! Role: {st.session_state['selected_role']}, Sub-Role: {st.session_state['selected_sub_role']}, Action: {st.session_state['selected_action']}, Activity: {st.session_state['selected_activity']}")
    # Intermediate API calls can be added here, as per the selected paths.

# Start the app
if __name__ == "__main__":
    app()
