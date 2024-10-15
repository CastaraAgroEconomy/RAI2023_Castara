import streamlit as st
from features.weather_yield_estimation.Get_yield_data import get_yield_data  # Import your data retrieval functions
from features.weather_yield_estimation.Get_performance_data import get_performance_data
from features.weather_yield_estimation.Get_financial_data import get_financial_data
#from features.weather_api_scripts.Get_weather_data import get_weather_data

# Initialize the global counter to track the current screen
screen_counter = 0  # This will control the flow of screens

def main():
    global screen_counter  # Use the global counter for screen management

    # Display the appropriate screen based on the counter value
    if screen_counter == 0:
        screen_counter = login_screen()  # Call the login screen function
    elif screen_counter == 1:
        screen_counter = home_screen()  # Call the home screen function
    elif screen_counter == 2:
        screen_counter = yield_data_screen()  # Call the yield data screen function
    elif screen_counter == 3:
        screen_counter = performance_data_screen()  # Call the performance data screen function
    elif screen_counter == 4:
        screen_counter = financial_data_screen()  # Call the financial data screen function

    # This rerun allows the app to refresh after a screen change
    st.experimental_rerun()  

def login_screen():
    """Displays the login screen."""
    st.title("Login Screen")
    username = st.text_input("Username", key="username_input")  # Unique key for the input
    password = st.text_input("Password", type="password", key="password_input")  # Unique key for password input

    if st.button("Login"):
        if username == "admin" and password == "password":  # Simple authentication
            st.success("Login successful!")
            return 1  # Move to the home screen
        else:
            st.error("Invalid username or password. Please try again.")

    return 0  # Stay on the login screen

def home_screen():
    """Displays the home screen."""
    st.title("Home Screen")
    st.write("Welcome to the Castara AgroEconomy Dashboard!")
    
    # Navigation buttons
    if st.button("View Yield Data"):
        return 2  # Navigate to yield data screen
    if st.button("View Performance Data"):
        return 3  # Navigate to performance data screen
    if st.button("View Financial Data"):
        return 4  # Navigate to financial data screen

    return 1  # Stay on the home screen

def yield_data_screen():
    """Displays the yield data screen."""
    st.title("Yield Data Screen")
    
    yield_data = get_yield_data()  # Call your function to get yield data
    st.write(yield_data)  # Display the yield data

    if st.button("Back to Home"):
        return 1  # Navigate back to the home screen

    return 2  # Stay on the yield data screen

def performance_data_screen():
    """Displays the performance data screen."""
    st.title("Performance Data Screen")
    
    performance_data = get_performance_data()  # Call your function to get performance data
    st.write(performance_data)  # Display the performance data

    if st.button("Back to Home"):
        return 1  # Navigate back to the home screen

    return 3  # Stay on the performance data screen

def financial_data_screen():
    """Displays the financial data screen."""
    st.title("Financial Data Screen")
    
    financial_data = get_financial_data()  # Call your function to get financial data
    st.write(financial_data)  # Display the financial data

    if st.button("Back to Home"):
        return 1  # Navigate back to the home screen

    return 4  # Stay on the financial data screen

if __name__ == "__main__":
    main()  # Run the main function to start the application
