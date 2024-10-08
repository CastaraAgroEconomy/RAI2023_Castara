import streamlit as st
import pandas as pd
from Get_yield_data import yield_tracking
from Get_financial_data import financial_data
from Get_performance_data import franchise_performance

# App title
st.title("Castara AgroEconomy C-Suite Pilot")
st.image("Castara_AgroEconomy_Mobile_App.JPG", caption="Vertical Farming franchise master control center for key management roles", use_column_width=True)

# Placeholder for user authentication (to be integrated later)
def authenticate_user(username, password):
    """ Placeholder function for user authentication. """
    # Authentication logic to be added
    return True

# Use session state to control clearing and pausing
def clear_display():
    if st.button("Next"):
        st.session_state['next'] = True

# Main menu with role and action selection
def main_menu(user_role):
    st.sidebar.title("Navigation")
    
    if user_role == "Franchisee":
        option = st.sidebar.selectbox("Choose Action", ["Yield Management", "Financial Performance"])
        return option
    
    elif user_role == "Management":
        option = st.sidebar.selectbox("Choose Action", ["Franchise Performance", "Strategic Planning"])
        return option
    
    elif user_role == "Investor":
        option = st.sidebar.selectbox("Choose Action", ["Financial Overview", "Sustainability Impact"])
        return option
    
    elif user_role == "Technical Staff":
        option = st.sidebar.selectbox("Choose Action", ["Equipment Monitoring", "Maintenance Logs"])
        return option
    return None

# Display the dashboard based on role and action
def display_dashboard(user_role, option):
    st.header(f"{user_role} Dashboard")

    # Check if we should pause before clearing
    if 'next' not in st.session_state or not st.session_state['next']:
        clear_display()
        st.stop()

    # After clearing, display the new content
    st.session_state['next'] = False  # Reset for next round

    if user_role == "Franchisee":
        if option == "Yield Management":
            yield_tracking()
        elif option == "Financial Performance":
            st.write("Financial Performance: Coming soon.")

    elif user_role == "Management":
        if option == "Franchise Performance":
            franchise_performance()
        elif option == "Strategic Planning":
            st.write("Strategic Planning: Coming soon.")

    elif user_role == "Investor":
        if option == "Financial Overview":
            st.write("Financial Overview: Coming soon.")
        elif option == "Sustainability Impact":
            st.write("Sustainability Impact: Coming soon.")

    elif user_role == "Technical Staff":
        if option == "Equipment Monitoring":
            st.write("Equipment Monitoring: Coming soon.")
        elif option == "Maintenance Logs":
            st.write("Maintenance Logs: Coming soon.")

# Main app function
def main():
    if 'next' not in st.session_state:
        st.session_state['next'] = False
    
    # Authentication placeholder
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if authenticate_user(username, password):
        user_role = st.selectbox("Select your role", ["Franchisee", "Management", "Investor", "Technical Staff"])
        option = main_menu(user_role)
        display_dashboard(user_role, option)
    else:
        st.error("Authentication failed.")

# Run app
if __name__ == "__main__":
    main()
