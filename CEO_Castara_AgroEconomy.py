import streamlit as st

# Function to clear the display
def clear_display():
    st.session_state.clear_screen = True

# Placeholder for user authentication
def authenticate_user(username, password):
    """ Placeholder function for user authentication. """
    # Authentication logic to be added
    return True

# Login screen with validation
def login_screen():
    st.title("Castara AgroEconomy C-Suite Pilot")
    st.image("Castara_AgroEconomy_Mobile_App.JPG", caption="Vertical Farming franchise master control center for key management roles", use_column_width=True)
    
    # User input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Validation: Ensure both fields are filled before proceeding
    if st.button("Login"):
        if not username or not password:
            st.error("Please enter both Username and Password.")
        else:
            if authenticate_user(username, password):
                st.session_state.logged_in = True
                clear_display()
            else:
                st.error("Authentication failed. Please check your credentials.")

# Role selection screen
def role_selection_screen():
    st.header("Select Your Role")
    user_role = st.selectbox("Select your role", ["Franchisee", "Management", "Investor", "Technical Staff"])
    if st.button("Next"):
        st.session_state.user_role = user_role
        clear_display()

# Display role-specific dashboard
def display_dashboard():
    st.header(f"{st.session_state.user_role} Dashboard")
    st.write("Dashboard content here...")
    if st.button("Proceed to Options"):
        clear_display()

# Display the main menu for role and options
def main_menu():
    st.sidebar.title("Navigation")
    user_role = st.session_state.user_role
    
    if user_role == "Franchisee":
        option = st.sidebar.selectbox("Choose Action", ["Yield Management", "Financial Performance"])
    elif user_role == "Management":
        option = st.sidebar.selectbox("Choose Action", ["Franchise Performance", "Strategic Planning"])
    elif user_role == "Investor":
        option = st.sidebar.selectbox("Choose Action", ["Financial Overview", "Sustainability Impact"])
    elif user_role == "Technical Staff":
        option = st.sidebar.selectbox("Choose Action", ["Equipment Monitoring", "Maintenance Logs"])
    
    if st.button("Select Option"):
        st.session_state.option = option
        clear_display()

# Display content based on selected role and option
def display_content():
    st.header(f"{st.session_state.user_role} - {st.session_state.option}")
    
    if st.session_state.user_role == "Franchisee":
        if st.session_state.option == "Yield Management":
            st.write("Yield Management content goes here.")
        elif st.session_state.option == "Financial Performance":
            st.write("Financial Performance: Coming soon.")
    elif st.session_state.user_role == "Management":
        if st.session_state.option == "Franchise Performance":
            st.write("Franchise Performance: Coming soon.")
        elif st.session_state.option == "Strategic Planning":
            st.write("Strategic Planning: Coming soon.")
    
    if st.button("Return to Dashboard"):
        clear_display()

# Main app function
def main():
    # Initialize session state variables if not already set
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'clear_screen' not in st.session_state:
        st.session_state.clear_screen = False
    if 'user_role' not in st.session_state:
        st.session_state.user_role = None
    if 'option' not in st.session_state:
        st.session_state.option = None

    # Clear the screen if necessary
    if st.session_state.clear_screen:
        st.session_state.clear_screen = False
        st.empty()

    # Control the flow of the app based on session state
    if not st.session_state.logged_in:
        login_screen()
    elif not st.session_state.user_role:
        role_selection_screen()
    elif not st.session_state.option:
        display_dashboard()
        main_menu()
    else:
        display_content()

# Run the app
if __name__ == "__main__":
    main()
