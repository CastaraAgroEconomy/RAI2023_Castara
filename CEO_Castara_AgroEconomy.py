import streamlit as st

# Importing feature modules for weather, yield tracking, performance, and utility
from features.weather_yield_estimation.Get_yield_data import yield_tracking
from features.weather_yield_estimation.Get_performance_data import franchise_performance
from features.weather_yield_estimation.Get_financial_data import financial_data
from features.Utility.Clear_screen import clear_display

# -----------------------------------------------------------------------------
# SCREEN CLEAR FUNCTIONALITY & DESIGN
# -----------------------------------------------------------------------------
# The purpose of this function is to clear the current content from the screen 
# before loading the next screen. This is essential for navigation between views.
def clear_display():
    st.session_state.clear_display = True
    st.empty()  # Clears the screen by creating an empty placeholder
    return

# -----------------------------------------------------------------------------
# HOME SCREEN - INITIAL STARTUP SCREEN
# -----------------------------------------------------------------------------
# The app starts here when executed for the first time. It displays a welcome 
# message and an image to provide an overview of the app's functionality.
def home_screen():
    st.title("Castara AgroEconomy C-Suite Pilot")
    st.image("Assets/Media/Images/Castara_AgroEconomy_Mobile_App.JPG", 
             caption="Vertical Farming franchise master control center for key user & operations roles & options", 
             use_column_width=True)
    return False
    
# -----------------------------------------------------------------------------
# AUTHENTICATION FUNCTION
# -----------------------------------------------------------------------------
# Placeholder authentication for simplicity during testing. 
# In the future, this would connect to a user database or API.
def authenticate_user(username, password):
    return True  # Simplified for testing

# -----------------------------------------------------------------------------
# LOGIN SCREEN
# -----------------------------------------------------------------------------
# This function collects the user's credentials and handles login. It clears the 
# screen and proceeds to the role selection screen upon successful login.
def login_screen():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login", key="login_process_button"):
        if not username or not password:
            st.error("Please enter both Username and Password.")
        else:
            if authenticate_user(username, password):
                st.session_state.logged_in = True
                clear_display()  # Clear screen after login
                role_selection_screen()
            else:
                st.error("Authentication failed. Please check your credentials.")

# -----------------------------------------------------------------------------
# ROLE SELECTION SCREEN
# -----------------------------------------------------------------------------
# After login, users are required to select their role, which will determine 
# which dashboard and options are presented to them.
def role_selection_screen():
    st.header("Select Your Role")
    user_role = st.selectbox("Select your role", ["Franchisee", "Management", "Investor", "Technical Staff"], 
                             key="user_role_selection")
    if st.button("Next", key="user_role_select_button"):
        st.session_state.user_role = user_role
        clear_display()  # Clear screen before displaying the dashboard
        display_dashboard_internal(user_role)

# -----------------------------------------------------------------------------
# ROLE-SPECIFIC DASHBOARD
# -----------------------------------------------------------------------------
# This function loads role-specific dashboards with relevant features.
# Each role has different performance and management options.
def display_dashboard_internal(user_role):
    if user_role == "Franchisee":
        st.header("Franchisee Dashboard")
        yield_tracking()  # Load Franchisee-specific yield tracking data
    elif user_role == "Management":
        st.header("Management Dashboard")
        franchise_performance()  # Load performance data for Management
    else:
        st.header(f"{user_role} Dashboard")
        st.write(f"Welcome to the {user_role} Dashboard.")
        st.write("⚠️ The {user_role} Dashboard will be installed at a future date.")
    
    # After loading the dashboard, show options menu based on role
    options_menu(user_role)

# -----------------------------------------------------------------------------
# OPTIONS MENU FOR ROLE-SPECIFIC ACTIONS
# -----------------------------------------------------------------------------
# Users can choose from available actions based on their role.
# The function displays a sidebar with relevant options.
def options_menu(user_role):
    st.sidebar.title("Navigation")
    
    if user_role == "Franchisee":
        option = st.sidebar.selectbox("Choose Action", ["Yield Management", "Financial Performance"], 
                                      key="Franchisee_option_select")
    elif user_role == "Management":
        option = st.sidebar.selectbox("Choose Action", ["Franchise Performance", "Strategic Planning"], 
                                      key="Management_option_select")
    elif user_role == "Investor":
        option = st.sidebar.selectbox("Choose Action", ["Financial Overview", "Sustainability Impact"], 
                                      key="Investor_option_select")
    elif user_role == "Technical Staff":
        option = st.sidebar.selectbox("Choose Action", ["Equipment Monitoring", "Maintenance Logs"], 
                                      key="Technical_Staff_option_select")
    
    if st.button("Select Option", key="option_select_button"):
        st.session_state.option = option
        clear_display()  # Clear screen before displaying content
        display_content(user_role, option)

# -----------------------------------------------------------------------------
# DISPLAY CONTENT BASED ON SELECTED OPTIONS
# -----------------------------------------------------------------------------
# The function loads role and option-specific content based on user selections.
def display_content(user_role, option):
    st.write(f"Displaying content for {user_role} - {option}.")
    
    if user_role == "Franchisee":
        if option == "Yield Management":
            st.write("⚠️ - Yield Management feature to be implemented here")
        elif option == "Financial Performance":
            st.write("⚠️ - Financial Performance feature to be implemented here")
    elif user_role == "Management":
        if option == "Franchise Performance":
            st.write("⚠️ - Franchise Performance feature to be implemented here")
        elif option == "Strategic Planning":
            st.write("⚠️ - Strategic Planning feature to be implemented here")
    elif user_role == "Investor":
        if option == "Financial Overview":
            st.write("⚠️ - Financial Overview feature to be implemented here")
        elif option == "Sustainability Impact":
            st.write("⚠️ - Sustainability Impact feature to be implemented here")
    elif user_role == "Technical Staff":
        if option == "Equipment Monitoring":
            st.write("⚠️ - Equipment Monitoring feature to be implemented here")
        elif option == "Maintenance Logs":
            st.write("⚠️ - Maintenance Logs feature to be implemented here")

# -----------------------------------------------------------------------------
# MAIN FUNCTION - ENTRY POINT FOR APP
# -----------------------------------------------------------------------------
# This function manages the application flow and ensures the state of the app 
# persists across reruns.
def main():
    home_screen()
    
    # Initialize session states if not already set
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'clear_screen' not in st.session_state:
        st.session_state.clear_screen = False
    if 'user_role' not in st.session_state:
        st.session_state.user_role = None
    if 'option' not in st.session_state:
        st.session_state.option = None

    # Clear screen initially
    if not st.session_state.clear_display:
        clear_display()
    
    # Control flow based on session state
    if not st.session_state.logged_in:
        login_screen()  # Show login if not logged in
    elif not st.session_state.user_role:
        role_selection_screen()  # Show role selection if no role is selected
    else:
        user_role = st.session_state.user_role
        display_dashboard_internal(user_role)  # Load dashboard for selected role

# Run the Streamlit app
if __name__ == "__main__":
    main()
