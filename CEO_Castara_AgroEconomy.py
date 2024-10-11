import streamlit as st

from Get_yield_data import yield_tracking
from Get_performance_data  import franchise_performance
from Get_financial_data import financial_data


# Function to clear the display
def clear_display():
    st.session_state.clear_screen = True

# Placeholder for user authentication
def authenticate_user(username, password):
    return True  # Simplified for testing

# Login screen with validation
def login_screen():
    st.title("Castara AgroEconomy C-Suite Pilot")
    st.image("Castara_AgroEconomy_Mobile_App.JPG", caption="Vertical Farming franchise master control center for key management roles", use_column_width=True)
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
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
        st.button = ""
   

# Display role-specific dashboard
def display_dashboard():
    user_role = st.session_state.user_role
    if user_role == "Franchisee":
        st.header("Franchisee Dashboard")
        yield_tracking()
    elif user_role == "Management":
        st.header("Management Dashboard")
        franchise_performance()
    
    else:
        st.header(f"{user_role} Dashboard")
        st.write(f"Welcome to the {user_role} Dashboard.")
    
    if st.button("Proceed to Options"):
        clear_display()

# Main menu with role options
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

# Display content based on selected option
def display_content():
    st.header(f"{st.session_state.user_role} - {st.session_state.option}")
    st.write(f"Displaying content for {st.session_state.user_role}'s {st.session_state.option}.")
    
    if st.button("Return to Dashboard"):
        clear_display()
        display_dashboard()

# Main app function
def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'clear_screen' not in st.session_state:
        st.session_state.clear_screen = False
    if 'user_role' not in st.session_state:
        st.session_state.user_role = None
    if 'option' not in st.session_state:
        st.session_state.option = None

    if st.session_state.clear_screen:
        st.session_state.clear_screen = False
        st.empty()

    if not st.session_state.logged_in:
        login_screen()
    elif not st.session_state.user_role:
        role_selection_screen()
    elif not st.session_state.option:
        display_dashboard()
        main_menu()
    else:
        display_content()

# Run app
if __name__ == "__main__":
    main()
