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
def main_menu(user_role):
    """ Displays the main menu based on user role. """
    st.write(" ")
    st.write(" ")
    display_dashboard(user_role)
    #if user_role ==
        

# Update display_dashboard() function to include yield tracking for Franchisee
def display_dashboard(user_role):
    """ Display the dashboard based on user role. """
    st.header(f"{user_role} Dashboard")
    st.write(" ")
    if user_role == "Franchisee":
        yield_tracking()  # This will call the function from get_yield_data.py
    elif user_role == "Management":
        financial_data()  # This will call the function from get_financial_data.py
    else:
        st.write("Welcome to the Castara AgroEconomy dashboard.")

# Main app function
def main():
    # Placeholder for authentication (to be expanded)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if authenticate_user(username, password):
        # Select user role (for demo purposes)
        user_role = st.selectbox("Select your role", ["Franchisee", "Management", "Investor", "Technical Staff"])
        main_menu(user_role)
        display_dashboard(user_role)
    else:
        st.error("Authentication failed.")

# Run app
if __name__ == "__main__":
    main()
