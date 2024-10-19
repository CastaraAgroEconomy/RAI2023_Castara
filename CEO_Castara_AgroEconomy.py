import streamlit as st

# Define global variables for tracking user selections
selected_role = None
selected_subrole = None
selected_action = None
selected_activity = None

# Display the cover page and login first
st.image('Assets/Media/Images/Cover_page.jpg')

# Login section
if "authenticated" not in st.session_state:
    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")
    
    if st.button("Login"):
        if username == "admin" and password == "password":  # Simple validation
            st.session_state.authenticated = True
            st.write("Login successful!")
        else:
            st.write("Invalid credentials, please try again.")
else:
    st.write(f"Welcome {username}!")
    
    # Radio button selection system for user journey
    if selected_role is None:
        st.write("Choose a User Role:")
        selected_role = st.radio("Select Role", ["Franchisee", "Investor", "Management"])
    
    if selected_role and selected_subrole is None:
        st.write(f"Selected Role: {selected_role}")
        st.write("Choose a Sub-Role:")
        if selected_role == "Franchisee":
            selected_subrole = st.radio("Select Sub-Role", ["Owner", "Manager", "Staff"])
        elif selected_role == "Investor":
            selected_subrole = st.radio("Select Sub-Role", ["Partner", "Shareholder", "Advisory"])
        elif selected_role == "Management":
            selected_subrole = st.radio("Select Sub-Role", ["Operations", "Finance", "HR"])
    
    if selected_subrole and selected_action is None:
        st.write(f"Selected Sub-Role: {selected_subrole}")
        st.write("Choose an Action:")
        selected_action = st.radio("Select Action", ["Plan", "Monitor", "Report"])
    
    if selected_action and selected_activity is None:
        st.write(f"Final selection: {selected_role} -> {selected_subrole} -> {selected_action}")
        st.write("Choose an Activity under Plan:")
        selected_activity = st.radio("Select Activity", ["Develop Strategy", "Resource Allocation", "No further option"])
        
        if selected_activity:
            st.write(f"Final selection: {selected_role} -> {selected_subrole} -> {selected_action} -> {selected_activity}")
            
            if st.button("Next"):
                st.write(f"You selected: {selected_role} -> {selected_subrole} -> {selected_action} -> {selected_activity}")
                st.write("Proceeding to the next stage...")
                # Placeholder for next step logic based on valid combination

    # Log out button
    if st.button("Log Out"):
        del st.session_state['authenticated']
        st.write("Logged out successfully. Please login again.")
        st.experimental_rerun()

    # Help button
    if st.button("Help"):
        st.write("Help page is under development.")
        # Placeholder for future Help page logic

    # Clear screen and return to the start if invalid combination selected (logic placeholder)
    if selected_role and selected_subrole and selected_action and selected_activity:
        if selected_role != "Franchisee" or selected_subrole != "Owner" or selected_action != "Plan" or selected_activity != "Develop Strategy":
            st.write("Invalid combination of choices selected. Please review and revise accordingly.")
            # Reset all selections
            selected_role = None
            selected_subrole = None
            selected_action = None
            selected_activity = None
            st.experimental_rerun()
