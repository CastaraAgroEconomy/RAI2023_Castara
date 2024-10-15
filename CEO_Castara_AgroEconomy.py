import streamlit as st

def main():
    # Initialize navigation state
    navigation_flag = st.sidebar.radio("Navigate", ("Home", "Dashboard", "Weather", "Yield"))

    # Define screens based on navigation_flag
    if navigation_flag == "Home":
        show_home()
    elif navigation_flag == "Dashboard":
        show_dashboard()
    elif navigation_flag == "Weather":
        show_weather()
    elif navigation_flag == "Yield":
        show_yield()

# Define each screen function
def show_home():
    st.title("Welcome to the AgroEconomy App")
    st.write("This is the home screen.")

def show_dashboard():
    st.title("Dashboard")
    st.write("Here is the dashboard with key data.")

def show_weather():
    st.title("Weather Data")
    st.write("Display weather data here.")

def show_yield():
    st.title("Yield Estimation")
    st.write("Here is the yield estimation section.")

# Run the app
if __name__ == "__main__":
    main()
