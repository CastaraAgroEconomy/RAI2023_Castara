import streamlit as st

# Initialize a counter to keep track of the current screen
screen_counter = 0

# Function to authenticate user credentials (placeholder)
def authenticate_user(username, password):
    # In a real application, replace this with proper authentication logic
    return username == "admin" and password == "password"  # Example validation

# Login screen function
def login_screen(counter):
    # Generate a unique key suffix using the counter
    unique_key_suffix = f"_{counter}"
    
    # Text input for username with a unique key
    username = st.text_input("Username", key=f"username_input{unique_key_suffix}")
    
    # Text input for password with a unique key
    password = st.text_input("Password", type="password", key=f"password_input{unique_key_suffix}")

    # Login button with a unique key
    if st.button("Login", key=f"login_button{unique_key_suffix}"):
        # Check for empty inputs
        if not username or not password:
            st.error("Please enter both Username and Password.")
        else:
            # Authenticate user
            if authenticate_user(username, password):
                return True  # Indicate successful login
            else:
                st.error("Authentication failed. Please check your credentials.")
    
    return False  # Indicate failed login

# Function to display the home screen after login
def home_screen(counter):
    unique_key_suffix = f"_{counter}"
    
    st.title("Home Screen")  # Title for the home screen
    
    # Button to navigate to the dashboard with a unique key
    if st.button("Go to Dashboard", key=f"dashboard_button{unique_key_suffix}"):
        # Logic for transitioning to the dashboard
        return "dashboard"  # Indicate transition to the dashboard

    # Display additional content on the home screen
    st.write("Welcome to the Castara AgroEconomy application!")

# Function to display the dashboard
def dashboard_screen(counter):
    unique_key_suffix = f"_{counter}"
    
    st.title("Dashboard")  # Title for the dashboard
    
    # Button to return to the home screen with a unique key
    if st.button("Back to Home", key=f"back_home_button{unique_key_suffix}"):
        return "home"  # Indicate transition back to the home screen

    # Display dashboard content
    st.write("Here is your dashboard with relevant data and insights.")

# Main function to control the application flow
def main():
    global screen_counter  # Access the global counter
    
    # Main loop to handle screen transitions
    while True:
        if screen_counter == 0:  # Initial screen
            logged_in = login_screen(screen_counter)
            if logged_in:
                screen_counter += 1  # Increment counter on successful login

        elif screen_counter == 1:  # Home screen after login
            next_screen = home_screen(screen_counter)
            if next_screen == "dashboard":
                screen_counter += 1  # Move to dashboard screen

        elif screen_counter == 2:  # Dashboard screen
            next_screen = dashboard_screen(screen_counter)
            if next_screen == "home":
                screen_counter -= 1  # Return to home screen

        # To exit the loop, consider adding a condition to break (like a logout option)

if __name__ == "__main__":
    main()  # Run the main function to start the application
