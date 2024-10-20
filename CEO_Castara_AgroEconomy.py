import streamlit as st

# Placeholder for valid credentials (admin/password for testing)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

# Define the main function that will control the flow
def main():
    # Display cover page image
    st.image('Assets/Media/Images/Cover_page.jpg', use_column_width=True)
    
    # Initialize session state for login
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        
    if not st.session_state.logged_in:
        login()  # Go to login page if not logged in
    else:
        user_role_selection()  # Proceed to user role selection if logged in

# Login function
def login():
    st.title("Login")
    
    # Input fields for username and password
    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")
    
    # Login button
    if st.button("Login"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.logged_in = True
            st.success("Login successful!")  # Display login success
            st.rerun()  # Use st.rerun() instead of st.experimental_rerun()
        else:
            st.error("Invalid credentials. Please try again.")

# ... (rest of the functions remain the same)

# Logout function
def logout():
    st.session_state.logged_in = False
    st.rerun()  # Use st.rerun() here as well

if __name__ == "__main__":
    main()
