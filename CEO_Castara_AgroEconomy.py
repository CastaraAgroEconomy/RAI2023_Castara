import streamlit as st

# Placeholder text for navigation instructions
st.write("⚠️ - Note: use the navigation icons ‘>’ & ‘<‘ at the top left-hand and right-hand side of your screen in portrait mode to navigate between menus and sub-menus.")

# Main header
st.title("Castara AgroEconomy")

# Main menu options for user roles
user_role = st.radio("Select your user role:", ['Franchisee', 'Administrator', 'Researcher', 'Consultant'])

# Conditional menus based on the selected user role
if user_role == 'Franchisee':
    st.header("Franchisee Dashboard")
    franchisee_option = st.radio("Choose an action:", ['Yield Estimation', 'Weather Analysis', 'Inventory Management'])

    if franchisee_option == 'Yield Estimation':
        st.header("Yield Estimation")
        st.write("This feature allows you to estimate crop yield based on historical data and current weather trends.")
        # Media asset call (example, uncomment when the file is ready)
        st.image('features/Media/Images/Yield_Estimation.jpg')
        # Add the yield estimation script or logic here

    elif franchisee_option == 'Weather Analysis':
        st.header("Weather Analysis")
        st.write("Analyze weather patterns affecting your farm.")
        # Media asset call (example, uncomment when the file is ready)
        # st.image('features/Media/Images/Weather_Analysis.png')
        # Add the weather analysis script or API call here

    elif franchisee_option == 'Inventory Management':
        st.header("Inventory Management")
        st.write("Manage your farm inventory including seeds, fertilizers, and tools.")
        # Media asset call (example, uncomment when the file is ready)
        # st.image('features/Media/Images/Inventory_Management.png')
        # Add the inventory management script or logic here

elif user_role == 'Administrator':
    st.header("Administrator Dashboard")
    admin_option = st.radio("Choose an action:", ['User Management', 'System Logs', 'Data Export'])

    if admin_option == 'User Management':
        st.header("User Management")
        st.write("Manage the system's user accounts and permissions.")
        # Media asset call (example, uncomment when the file is ready)
        # st.image('features/Media/Images/User_Management.png')
        # Add the user management script or logic here

    elif admin_option == 'System Logs':
        st.header("System Logs")
        st.write("View system logs and activity for troubleshooting.")
        # Media asset call (example, uncomment when the file is ready)
        # st.image('features/Media/Images/System_Logs.png')
        # Add the system logs script or logic here

    elif admin_option == 'Data Export':
        st.header("Data Export")
        st.write("Export system data for backup or analysis.")
        # Media asset call (example, uncomment when the file is ready)
        # st.image('features/Media/Images/Data_Export.png')
        # Add the data export script or logic here

elif user_role == 'Researcher':
    st.header("Researcher Dashboard")
    researcher_option = st.radio("Choose an action:", ['Field Studies', 'Data Analysis', 'External Data Integration'])

    if researcher_option == 'Field Studies':
        st.header("Field Studies")
        st.write("Access and manage field study data.")
        # Media asset call (example, uncomment when the file is ready)
        # st.image('features/Media/Images/Field_Studies.png')
        # Add the field studies script or logic here

    elif researcher_option == 'Data Analysis':
        st.header("Data Analysis")
        st.write("Analyze agricultural data for insights.")
        # Media asset call (example, uncomment when the file is ready)
        # st.image('features/Media/Images/Data_Analysis.png')
        # Add the data analysis script or logic here

    elif researcher_option == 'External Data Integration':
        st.header("External Data Integration")
        st.write("Integrate data from external platforms for advanced research.")
        # Media asset call (example, uncomment when the file is ready)
        # st.image('features/Media/Images/External_Data_Integration.png')
        # Add the API integration or script here

elif user_role == 'Consultant':
    st.header("Consultant Dashboard")
    consultant_option = st.radio("Choose an action:", ['Client Reports', 'Market Trends', 'Project Management'])

    if consultant_option == 'Client Reports':
        st.header("Client Reports")
        st.write("Generate and review reports for your clients.")
        # Media asset call (example, uncomment when the file is ready)
        # st.image('features/Media/Images/Client_Reports.png')
        # Add the client report script or logic here

    elif consultant_option == 'Market Trends':
        st.header("Market Trends")
        st.write("Analyze current market trends for crops and commodities.")
        # Media asset call (example, uncomment when the file is ready)
        # st.image('features/Media/Images/Market_Trends.png')
        # Add the market trend script or logic here

    elif consultant_option == 'Project Management':
        st.header("Project Management")
        st.write("Manage ongoing projects and tasks.")
        # Media asset call (example, uncomment when the file is ready)
        # st.image('features/Media/Images/Project_Management.png')
        # Add the project management script or logic here

# Note: Implement navigation shortcuts for logging out or jumping between sub-features when needed.
