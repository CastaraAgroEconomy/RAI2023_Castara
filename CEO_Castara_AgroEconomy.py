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
        display_dashboard()
    else:
        st.write("press button to advance")
   

# Display role-specific dashboard
def display_dashboard():
    user_role = st.session_state.user_role
    if user_role == "Franchisee":
        clear_display()
        st.header("Franchisee Dashboard")
        yield_tracking()
    elif user_role == "Management":
        clear_display()
        st.header("Management Dashboard")
        franchise_performance()
    else:
        st.header(f"{user_role} Dashboard")
        clear_display()
        st.write(f"Welcome to the {user_role} Dashboard.")
    
    if st.button("Proceed to Options"):
        clear_display()
        main_menu()
    else:
        st.write("press button to advance")

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
        display_content()
    else:
        st.write("press button to advance")

# Display content based on selected option
def display_content():
    #st.header(f"{st.session_state.user_role} - {st.session_state.option}")
    st.write(f"Displaying content for {st.session_state.user_role}'s {st.session_state.option}.")
    
    if st.session_state.user_role == "Franchisee":
        if st.session_state.option == "Yield Management":
            clear_display()
            st.write("⚠️ - Feature not yet implemented")
        elif st.session_state.option == "Financial Performance":
            clear_display()
            financial_data()   
    if st.session_state.user_role == "Management":
        if st.session_state.option == "Financial Performance":
            clear_display()
            financial_data()
        elif st.session_state.option == "Strategic Planning":
            clear_display()
            st.write("⚠️ - Feature not yet implemented")
    elif st.session_state.user_role == "Investor":
        if st.session_state.option == "Financial Overview":
            clear_display()
            st.write("⚠️ - Feature not yet implemented")
        elif st.session_state.option == "Sustainability Impact":
            clear_display()
            st.write("⚠️ - Feature not yet implemented")
    elif st.session_state.user_role == "Technical Staff":
        if st.session_state.option == "Equipment Monitoring":
            clear_display()
            st.write("⚠️ - Feature not yet implemented")
        elif st.session_state.option == "Monitoring Logs":
            clear_display()
            st.write("⚠️ - Feature not yet implemented")
    
    if st.button("Return to Dashboard"):
        clear_display()
        display_dashboard()
    else:
        st.write("press button to advance")

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
