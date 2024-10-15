import streamlit as st

# Importing features and utility modules
from features.weather_yield_estimation.Get_yield_data import yield_tracking
from features.weather_yield_estimation.Get_performance_data import franchise_performance
from features.weather_yield_estimation.Get_financial_data import financial_data
from features.Utility.Clear_screen import clear_display

# Function to clear the display
def clear_display():
    st.session_state.clear_display = True  # Sets a flag to indicate screen clearing
    st.empty()  # Clears the screen elements
    return

# Initial App screen displayed when the app is first executed
def home_screen():
    st.title("Castara AgroEconomy C-Suite Pilot")
    st.image("Assets/Media/Images/Castara_AgroEconomy_Mobile_App.JPG", 
             caption="Vertical Farming franchise master control center for key user & operations roles & options", 
             use_column_width=True)
    return False

# Placeholder function for user authentication
def authenticate_user(username, password):
    return True  # Simplified for testing purposes

# Login screen with validation
def login_screen():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login", key="login_process_button"):
        if not username or not password:
            st.error("Please enter both Username and Password.")
        else:
            if authenticate_user(username, password):
                st.session_state.logged_in = True
                clear_display()  # Clears the screen on successful login
                role_selection_screen()  # Navigate to role selection screen
            else:
                st.error("Authentication failed. Please check your credentials.")

# Role selection screen
def role_selection_screen():
    st.header("Select Your Role")
    user_role = st.selectbox("Select your role", ["Franchisee", "Management", "Investor", "Technical Staff"], 
                             key="user_role_selection")
    if st.button("Next", key="user_role_select_button"):
        st.session_state.user_role = user_role
        clear_display()  # Clears the screen before navigating to the dashboard
        display_dashboard_internal(user_role)

# Displays the role-specific dashboard based on the user role
def display_dashboard_internal(user_role):
    if user_role == "Franchisee":
        st.header("Franchisee Dashboard")
        yield_tracking()
    elif user_role == "Management":
        st.header("Management Dashboard")
        franchise_performance()
    else:
        st.header(f"{user_role} Dashboard")
        st.write(f"Welcome to the {user_role} Dashboard.")
        st.write(f"⚠️ The {user_role} Dashboard will be installed at a future date.")
    
    # Display options menu after role-specific dashboard
    options_menu(user_role)

# Options menu for different user roles
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
    
    if st.button("Info Display", key="info_display_select_button"):
        st.session_state.option = option
        clear_display()  # Clear the screen before showing the selected option
        display_content(user_role, option)

# Displays content based on the selected option
def display_content(user_role, option):
    st.write(f"Displaying content for {user_role} & {option}.")
    
    if user_role == "Franchisee":
        if option == "Yield Management":
            st.write("⚠️ - Yield Management feature to be implemented here.")
        elif option == "Financial Performance":
            st.write("⚠️ - Financial Performance feature to be implemented here.")
    elif user_role == "Management":
        if option == "Franchise Performance":
            st.write("⚠️ - Franchise Performance feature to be implemented here.")
        elif option == "Strategic Planning":
            st.write("⚠️ - Strategic Planning feature to be implemented here.")
    elif user_role == "Investor":
        if option == "Financial Overview":
            st.write("⚠️ - Financial Overview feature to be implemented here.")
        elif option == "Sustainability Impact":
            st.write("⚠️ - Sustainability Impact feature to be implemented here.")
    elif user_role == "Technical Staff":
        if option == "Equipment Monitoring":
            st.write("⚠️ - Equipment Monitoring feature to be implemented here.")
        elif option == "Monitoring Logs":
            st.write("⚠️ - Monitoring Logs feature to be implemented here.")

# Main app execution
def main():
    # Check if session state variables are initialized, if not, initialize them
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'clear_display' not in st.session_state:
        st.session_state.clear_display = False
    if 'user_role' not in st.session_state:
        st.session_state.user_role = None
    if 'option' not in st.session_state:
        st.session_state.option = None
    
    # Initial home screen
    if not st.session_state.logged_in:
        home_screen()  # Displays the initial home screen
        login_screen()  # User can log in
    elif not st.session_state.user_role:
        role_selection_screen()  # User can select their role
    else:
        user_role = st.session_state.user_role
        display_dashboard_internal(user_role)  # Displays the role-specific dashboard

# Run the Streamlit app
if __name__ == "__main__":
    main()
