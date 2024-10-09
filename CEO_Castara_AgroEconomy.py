import streamlit as st

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

# Placeholder for user authentication
def authenticate_user(username, password):
    """ Placeholder function for user authentication. """
    # Authentication logic to be added
    return True

# Function to clear the display
def clear_display():
    st.session_state.clear_screen = True
