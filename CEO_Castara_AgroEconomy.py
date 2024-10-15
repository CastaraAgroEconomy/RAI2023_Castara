import streamlit as st

# Initialize screen counter for unique keys
screen_counter = 0

def login_screen(counter):
    """Display the login screen and return login status."""
    unique_key_suffix = counter  # Use the current screen counter for unique keys
    username = st.text_input("Username", key=f"username_input_{unique_key_suffix}")
    password = st.text_input("Password", type="password", key=f"password_input_{unique_key_suffix}")
    
    if st.button("Login", key=f"login_button_{unique_key_suffix}"):
        if username == "admin" and password == "password":  # Simple placeholder authentication
            st.session_state.logged_in = True
            return True
        else:
            st.error("Invalid credentials!")
    
    return False

def home_screen(counter):
    """Display the home screen."""
    st.title("Welcome to the Castara AgroEconomy App")
    if st.button("Logout", key=f"logout_button_{counter}"):
        st.session_state.logged_in = False  # Reset login status

def main():
    global screen_counter
    # Check if the user is logged in
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # Main application loop
    while True:
        if st.session_state.logged_in:
            home_screen(screen_counter)
        else:
            logged_in = login_screen(screen_counter)
            if logged_in:
                screen_counter += 1  # Increment counter only when logged in
            st.experimental_rerun()  # Refresh to update UI

if __name__ == "__main__":
    main()
