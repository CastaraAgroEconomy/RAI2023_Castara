import streamlit as st

from Get_yield_data import yield_tracking
from Get_performance_data  import franchise_performance
from Get_financial_data import financial_data
from Clear_screen import clear_display


# Function to clear the display
def clear_display():
    st.session_state.clear_display = True

# Placeholder for user authentication
def authenticate_user(username, password):
    return True  # Simplified for testing

# Login screen with validation
def login_screen():
    st.title("Castara AgroEconomy C-Suite Pilot")
    st.image("Castara_AgroEconomy_Mobile_App.JPG", caption="Vertical Farming franchise master control center for key management roles", use_column_width=True)
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login", key="login_process_button"):
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
    user_role = st.selectbox("Select your role", ["Franchisee", "Management", "Investor", "Technical Staff"], key="user_role_selection")
    if st.button("Next", key="user_role_select_button"):
        st.session_state.user_role = user_role
        clear_display()
        display_dashboard_internal(user_role)
        st.write("press button to advance")
   

# Display role-specific dashboard
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
    
    if st.button("Proceed to Options", key="proceed_option_select_button"):
        st.write("⚠️ Select option")
        st.write(" ")
        main_menu()


# Main menu with role options
def main_menu():
    st.sidebar.title("Navigation")
    user_role = st.session_state.user_role
    
    if user_role == "Franchisee":
        option = st.sidebar.selectbox("Choose Action", ["Yield Management", "Financial Performance"], key="Franchisee_option_select")
    elif user_role == "Management":
        option = st.sidebar.selectbox("Choose Action", ["Franchise Performance", "Strategic Planning"], key="Management_option_select")
    elif user_role == "Investor":
        option = st.sidebar.selectbox("Choose Action", ["Financial Overview", "Sustainability Impact"], key="Investor_option_select")
    elif user_role == "Technical Staff":
        option = st.sidebar.selectbox("Choose Action", ["Equipment Monitoring", "Maintenance Logs"], key="Technical_Staff_option_select")
    
    if st.button("Select Option", key="option_select_button"):
        st.session_state.option = option
        clear_display()
        display_content(user_role, option)
    else:
        st.write("press button to advance")

# Display content based on selected option
def display_content(user_role, option):
    #st.header(f"{st.session_state.user_role} - {st.session_state.option}")
    st.write(f"Displaying content for {st.session_state.user_role} & {st.session_state.option}.")
    
    if user_role == "Franchisee":
        if option == "Yield Management":
            st.write("⚠️ - Yield Management feature to be implemented here")
        elif option == "Financial Performance":
            st.write("⚠️ - Financial Performance feature to be implemented here")
    if user_role == "Management":
        if option == "Financial Performance":
            st.write("⚠️ - Financial Performance feature to be implemented here")
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
        elif option == "Monitoring Logs":
            st.write("⚠️ - Monitoring Logs feature to be implemented here")
    
    if st.button("Return to Dashboard", key="RTD_select_button"):
        clear_display()
        display_dashboard_internal(user_role)
    else:
        st.write("press to advance")

# Main app function
def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False # sets off
    if 'clear_screen' not in st.session_state:
        st.session_state.clear_screen = False # sets off
    if 'user_role' not in st.session_state:
        st.session_state.user_role = None # sets null
    if 'option' not in st.session_state:
        st.session_state.option = None # sets null

    if st.session_state.clear_screen:
        st.session_state.clear_screen = False # sets off
        st.empty()

    if not st.session_state.logged_in: 
        clear_display() # clears display if not logged in
        login_screen() # presents the login screen
    elif not st.session_state.user_role:
        clear_display() # clears the display if user_role is null
        role_selection_screen() # request a user_role
    elif not st.session_state.option:
        clear_display() # clears the display if option is null
        display_dashboard() # displays the default user_role dashboard
        clear_display() # clears the display if option is null
        main_menu() # selects from a choice of options for a given user_role
    else:
        display_content() # displays the appropriate content for a given user_role and option combination

# Run app
if __name__ == "__main__":
    main()
