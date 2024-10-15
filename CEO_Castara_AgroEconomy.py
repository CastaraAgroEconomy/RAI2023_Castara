import streamlit as st
from features.weather_yield_estimation.Get_yield_data import yield_tracking
from features.weather_yield_estimation.Get_performance_data import franchise_performance
from features.weather_yield_estimation.Get_financial_data import financial_data

# Function to handle clearing of the display
def clear_screen(placeholder):
    placeholder.empty()  # Clears all content in the placeholder

# Home screen function
def home_screen(placeholder):
    placeholder.title("Castara AgroEconomy C-Suite Pilot")
    placeholder.image("Assets/Media/Images/Castara_AgroEconomy_Mobile_App.JPG",
                      caption="Vertical Farming franchise master control center for key user & operations roles & options",
                      use_column_width=True)

# Login screen function with validation
def login_screen(placeholder):
    username = placeholder.text_input("Username")
    password = placeholder.text_input("Password", type="password")
    
    if placeholder.button("Login"):
        if not username or not password:
            placeholder.error("Please enter both Username and Password.")
        else:
            if authenticate_user(username, password):
                st.session_state.logged_in = True
                placeholder.empty()  # Clear the screen after successful login
                role_selection_screen(placeholder)
            else:
                placeholder.error("Authentication failed. Please check your credentials.")

# Simple authentication placeholder function
def authenticate_user(username, password):
    return True  # Simplified for demonstration

# Role selection screen function
def role_selection_screen(placeholder):
    placeholder.header("Select Your Role")
    user_role = placeholder.selectbox("Select your role", 
                                      ["Franchisee", "Management", "Investor", "Technical Staff"])

    if placeholder.button("Next"):
        st.session_state.user_role = user_role
        placeholder.empty()  # Clear the screen before showing the dashboard
        display_dashboard_internal(placeholder, user_role)

# Function to display the dashboard based on user role
def display_dashboard_internal(placeholder, user_role):
    if user_role == "Franchisee":
        placeholder.header("Franchisee Dashboard")
        yield_tracking()
    elif user_role == "Management":
        placeholder.header("Management Dashboard")
        franchise_performance()
    else:
        placeholder.header(f"{user_role} Dashboard")
        placeholder.write(f"⚠️ The {user_role} Dashboard will be installed at a future date.")
    
    # After showing dashboard, move to options
    options_menu(placeholder, user_role)

# Options menu function
def options_menu(placeholder, user_role):
    option = placeholder.sidebar.selectbox("Choose Action", 
                                           get_user_role_options(user_role))
    if placeholder.button("Select Option"):
        placeholder.empty()  # Clear the screen before showing selected option content
        display_content(placeholder, user_role, option)

# Fetches role-specific options
def get_user_role_options(user_role):
    role_options = {
        "Franchisee": ["Yield Management", "Financial Performance"],
        "Management": ["Franchise Performance", "Strategic Planning"],
        "Investor": ["Financial Overview", "Sustainability Impact"],
        "Technical Staff": ["Equipment Monitoring", "Maintenance Logs"]
    }
    return role_options.get(user_role, [])

# Function to display content based on selected option
def display_content(placeholder, user_role, option):
    placeholder.write(f"Displaying content for {user_role} - {option}.")
    # Placeholder for real implementation of options
    if option == "Yield Management":
        placeholder.write("⚠️ - Yield Management feature to be implemented.")
    elif option == "Financial Performance":
        placeholder.write("⚠️ - Financial Performance feature to be implemented.")

# Main app execution
def main():
    # Initialize session state variables
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'user_role' not in st.session_state:
        st.session_state.user_role = None
    
    # Create an empty placeholder to manage screen transitions
    placeholder = st.empty()
    
    # Logic for managing different app screens
    if not st.session_state.logged_in:
        home_screen(placeholder)  # Displays home screen
        login_screen(placeholder)  # User can log in
    elif not st.session_state.user_role:
        role_selection_screen(placeholder)  # User can select their role
    else:
        # Display dashboard based on the user role
        user_role = st.session_state.user_role
        display_dashboard_internal(placeholder, user_role)

# Run the app
if __name__ == "__main__":
    main()
