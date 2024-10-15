import streamlit as st
from features.weather_yield_estimation.Get_yield_data import yield_tracking
from features.weather_yield_estimation.Get_performance_data import franchise_performance
from features.weather_yield_estimation.Get_financial_data import financial_data

# Function to clear and replace content in screen placeholder
def clear_screen_and_show_content(screen_placeholder, content_func, *args):
    screen_placeholder.empty()  # Clear screen
    with screen_placeholder:    # Refill with new content
        content_func(*args)

# Home screen function
def home_screen():
    st.title("Castara AgroEconomy C-Suite Pilot")
    st.image("Assets/Media/Images/Castara_AgroEconomy_Mobile_App.JPG", 
             caption="Vertical Farming franchise master control center for key user & operations roles & options", 
             use_column_width=True)

# Authentication placeholder function
def authenticate_user(username, password):
    return True  # Placeholder for testing

# Login screen function with validation
def login_screen(screen_placeholder):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if not username or not password:
            st.error("Please enter both Username and Password.")
        else:
            if authenticate_user(username, password):
                st.session_state.logged_in = True
                clear_screen_and_show_content(screen_placeholder, role_selection_screen, screen_placeholder)
            else:
                st.error("Authentication failed. Please check your credentials.")

# Role selection screen function
def role_selection_screen(screen_placeholder):
    st.header("Select Your Role")
    user_role = st.selectbox("Select your role", ["Franchisee", "Management", "Investor", "Technical Staff"])

    if st.button("Next"):
        st.session_state.user_role = user_role
        clear_screen_and_show_content(screen_placeholder, display_dashboard_internal, screen_placeholder, user_role)

# Function to display the dashboard based on user role
def display_dashboard_internal(screen_placeholder, user_role):
    if user_role == "Franchisee":
        st.header("Franchisee Dashboard")
        yield_tracking()
    elif user_role == "Management":
        st.header("Management Dashboard")
        franchise_performance()
    else:
        st.header(f"{user_role} Dashboard")
        st.write(f"⚠️ The {user_role} Dashboard will be installed at a future date.")
    
    # After showing the dashboard, navigate to options
    options_menu(screen_placeholder, user_role)

# Options menu function
def options_menu(screen_placeholder, user_role):
    option = st.sidebar.selectbox("Choose Action", 
                                  get_user_role_options(user_role))
    if st.button("Select Option"):
        clear_screen_and_show_content(screen_placeholder, display_content, user_role, option)

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
def display_content(user_role, option):
    st.write(f"Displaying content for {user_role} - {option}.")
    if option == "Yield Management":
        st.write("⚠️ - Yield Management feature to be implemented.")
    elif option == "Financial Performance":
        st.write("⚠️ - Financial Performance feature to be implemented.")
    # Implement more as needed

# Main app execution
def main():
    # Initialize session state variables
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'user_role' not in st.session_state:
        st.session_state.user_role = None
    
    # Create an empty placeholder for managing content
    screen_placeholder = st.empty()
    
    # Show the appropriate screen based on login state
    if not st.session_state.logged_in:
        home_screen()  # Displays home screen
        login_screen(screen_placeholder)  # Shows login form in placeholder
    elif not st.session_state.user_role:
        role_selection_screen(screen_placeholder)  # Shows role selection in placeholder
    else:
        # Show the dashboard for the user's role
        display_dashboard_internal(screen_placeholder, st.session_state.user_role)

# Run the app
if __name__ == "__main__":
    main()
