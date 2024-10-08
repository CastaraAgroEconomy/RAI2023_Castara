import streamlit as st  # Streamlit for app interface
import pandas as pd     # Pandas for data handling
import requests         # Requests for API calls
import datetime         # Date and time functions
# Import the yield tracking function from the get_yield_data script
from Get_yield_data import yield_tracking
# Import the financial data function from the Get_financial_data script
from Get_financial_data import financial_data
# Import the performance data function from the Get_performance_data script
from Get_performance_data import franchise_performance
# Import the clear_display instruction from the Clear_screen instruction script
from Clear_screen import clear_display

# App title
st.title("Castara AgroEconomy C-Suite pilot")

st.image("Castara_AgroEconomy_Mobile_App.JPG", caption="Vertical Farming franchise master control center for key management roles", use_column_width=True)
st.write(" ")

# Placeholder for user authentication (to be integrated later)
def authenticate_user(username, password):
    """ Placeholder function for user authentication. """
    # Authentication logic to be added
    return True

# User role selection and main menu
# Sidebar menu function
def main_menu(user_role, option):
    st.sidebar.title("Navigation")
    st.write(" ")
    st.write(" ")
    if user_role == "Franchisee":
        option = st.sidebar.selectbox("Choose Action", ["Yield Management", "Financial Performance"])
        if option == "Yield Management":
            st.write("⚠️ - Refer to KPIs, coming soon") # Function to show yield KPIs to be added
        elif option == "Financial Performance":
            st.write("⚠️ - Specific individual Financial performance reports coming soon.") # component module to be added later
    elif user_role == "Management":
        option = st.sidebar.selectbox("Choose Action", ["Franchise Performance", "Strategic Planning"])
        if option == "Franchise Performance":
            st.write("⚠️ - Refer to KPIs, coming soon") # Show franchise performance tracking KPIs
        elif option == "Strategic Planning":
            st.write("⚠️ - Strategic planning coming soon.") # component module to be added later
    elif user_role == "Investor":
        option = st.sidebar.selectbox("Choose Action", ["Financial Overview", "Sustainability Impact"])
        st.write(f"⚠️ - {option} coming soon.") 
    elif user_role == "Technical Staff":
        option = st.sidebar.selectbox("Choose Action", ["Equipment Monitoring", "Maintenance Logs"])
        st.write(f"⚠️ - {option} coming soon.") # component module to be added later
    
    # Reset menu selection
    user_role = " "
    option = " " 

    
# Update display_dashboard() function to include yield tracking for Franchisee
def display_dashboard(user_role):
    """ Display the dashboard based on user role. """
    st.header(f"{user_role} Dashboard")
    st.write("⚠️ - Remember to look for the dropdown menu icons '>' and '<' at the top left and right of your screen to access additional features and return to the previous view respectively.")
    st.write(" ")
    st.write(" ")
    if user_role == "Franchisee":
        # This will call the function from get_yield_data.py
        yield_tracking() 
    elif user_role == "Management":
        # This will call the function from get_financial_data.py
        financial_data() 
    else:
        st.write("Welcome to the Castara AgroEconomy dashboard.")

# Main app function
def main():
    # Placeholder for authentication (to be expanded)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    user_role = " "
    option = " "
    if authenticate_user(username, password):
        # Select user role (for demo purposes)
        user_role = st.selectbox("Select your role", ["Franchisee", "Management", "Investor", "Technical Staff"])
        reset_screen = clear_display()
        display_dashboard(user_role) with reset_screen
        st.write(" ")
        reset_screen = clear_display()
        main_menu(user_role, option) with reset_screen
    else:
        st.error("Authentication failed.")

# Run app
if __name__ == "__main__":
    main()
