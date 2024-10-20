import streamlit as st

# Dummy database of users and roles
users = {"admin": {"password": "password", "role": "Admin"},
         "user1": {"password": "password1", "role": "Sub-Role 1"},
         "user2": {"password": "password2", "role": "Sub-Role 2"}}

# Placeholder actions and activities for different roles
actions = {"Admin": ["Manage Users", "View Reports"],
           "Sub-Role 1": ["Submit Report", "View Own Reports"],
           "Sub-Role 2": ["Submit Feedback", "View Feedback"]}

activities = {"Manage Users": ["Add User", "Delete User"],
              "View Reports": ["Daily Report", "Weekly Report"],
              "Submit Report": ["Submit Daily", "Submit Weekly"],
              "View Own Reports": ["Own Daily Report", "Own Weekly Report"],
              "Submit Feedback": ["Submit General Feedback", "Submit Specific Feedback"],
              "View Feedback": ["View All Feedback", "View Own Feedback"]}

# Function to clear the screen
def clear_screen():
    st.empty()

# Login function
def login(username, password):
    if username in users and users[username]["password"] == password:
        st.session_state['username'] = username
        st.session_state['role'] = users[username]["role"]
        st.success(f"Login successful! Welcome {username}.")
        return True
    else:
        st.error("Invalid credentials. Please try again.")
        return False

# Function to select role
def select_role():
    st.subheader(f"User Role: {st.session_state['role']}")
    st.write("Proceed to the next step by selecting an action.")
    if st.button("Next"):
        clear_screen()
        select_action()

# Function to select action
def select_action():
    st.subheader("Select an Action:")
    action = st.radio("Choose an action:", actions[st.session_state['role']])
    st.session_state['action'] = action
    if st.button("Proceed"):
        clear_screen()
        select_activity()

# Function to select activity
def select_activity():
    st.subheader(f"Select an Activity for {st.session_state['action']}:")
    activity = st.radio("Choose an activity:", activities[st.session_state['action']])
    st.session_state['activity'] = activity
    if st.button("Proceed to Action"):
        clear_screen()
        run_selected_function()

# Function to run the selected function/script
def run_selected_function():
    st.subheader(f"Running: {st.session_state['activity']}")
    st.write(f"Executing {st.session_state['activity']}... (Placeholder for real functionality)")
    # Add more specific functionality for each activity here as needed.

# Logout function
def logout():
    st.session_state.clear()
    st.success("You have been logged out.")

# Main app flow
def main():
    st.title("Castara AgroEconomy App")
    
    # If the user is logged in
    if 'username' in st.session_state:
        st.sidebar.write(f"Logged in as: {st.session_state['username']}")
        if st.sidebar.button("Logout"):
            logout()
            return

        # Navigate through the user's journey
        if 'action' in st.session_state:
            select_activity()
        elif 'role' in st.session_state:
            select_action()
        else:
            select_role()

    else:
        st.subheader("Login to continue")
        username = st.text_input("Enter your username")
        password = st.text_input("Enter your password", type="password")
        if st.button("Login"):
            if login(username, password):
                clear_screen()

if __name__ == "__main__":
    main()
