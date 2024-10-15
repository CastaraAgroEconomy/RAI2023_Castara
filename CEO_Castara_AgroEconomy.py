import streamlit as st
from features.weather_yield_estimation.Get_yield_data import yield_tracking
from features.weather_yield_estimation.Get_performance_data import franchise_performance
from features.Utility.Clear_screen import clear_display

# Function to clear the display
def clear_display():
    st.empty()  # Clear the Streamlit display
    return

# Initial App screen when first executed
def home_screen():
    st.title("Castara AgroEconomy C-Suite Pilot")
    st.image("Assets/Media/Images/Castara_AgroEconomy_Mobile_App.JPG",
              caption="Vertical Farming franchise master control center for key user & operations roles & options",
              use_column_width=True)

# Placeholder for user authentication
def authenticate_user(username, password):
    return True  # Simplified for testing

# Login screen with validation
def login_screen():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not username or not password:
            st.error("Please enter both Username and Password.")
        else:
            if authenticate_user(username, password):
                return True  # Indicate successful login
            else:
                st.error("Authentication failed. Please check your credentials.")
    return False  # Indicate failed login

# Role selection screen
def role_selection_screen():
    st.header("Select Your Role")
    user_role = st.selectbox("Select your role", ["Franchisee", "Management", "Investor", "Technical Staff"])
    if st.button("Next"):
        return user_role  # Return selected role
    return None  # No role selected

# Display role-specific dashboard
def display_dashboard(user_role):
    if user_role == "Franchisee":
        st.header("Franchisee Dashboard")
        yield_tracking()
    elif user_role == "Management":
        st.header("Management Dashboard")
        franchise_performance()
    else:
        st.header(f"{user_role} Dashboard")
        st.write(f"Welcome to the {user_role} Dashboard. This feature will be developed in future.")

# Options menu with role options
def options_menu(user_role):
    st.sidebar.title("Navigation")
    options = {
        "Franchisee": ["Yield Management", "Financial Performance"],
        "Management": ["Franchise Performance", "Strategic Planning"],
        "Investor": ["Financial Overview", "Sustainability Impact"],
        "Technical Staff": ["Equipment Monitoring", "Maintenance Logs"],
    }
    selected_option = st.sidebar.selectbox("Choose Action", options.get(user_role, []))

    if st.button("Select"):
        return selected_option  # Return selected option
    return None  # No option selected

# Display content based on selected option
def display_content(user_role, selected_option):
    st.write(f"Displaying content for {user_role} - {selected_option}.")
    # Placeholder for future implementations
    st.write("⚠️ This feature will be implemented here.")

# Main app execution
def main():
    clear_display()  # Clear display at start
    home_screen()  # Show home screen

    logged_in = False
    user_role = None

    # Main loop
    while True:
        if not logged_in:
            logged_in = login_screen()  # Handle login
        else:
            if user_role is None:
                user_role = role_selection_screen()  # Role selection
            else:
                display_dashboard(user_role)  # Show dashboard
                selected_option = options_menu(user_role)  # Get option selection
                if selected_option:
                    display_content(user_role, selected_option)  # Display content for selected option
            if st.button("Logout"):
                logged_in = False  # Reset for next login

# Run app
if __name__ == "__main__":
    main()
