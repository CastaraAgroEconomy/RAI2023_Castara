import streamlit as st
import pandas as pd

# Example performance data for four franchises
def get_performance_data():
    data = {
        'Franchise': ['Franchise A', 'Franchise B', 'Franchise C', 'Franchise D'],
        'Yield (kg)': [18000, 20000, 19500, 21000],
        'Operational Efficiency (%)': [85, 90, 88, 92],
        'Revenue ($)': [50000, 62000, 55000, 67000]
    }
    df = pd.DataFrame(data)
    return df

# Franchise performance dashboard for management
def franchise_performance():
    st.header("Franchise Performance Dashboard")
    
    # Display performance data
    st.subheader("Franchise Performance Overview")
    performance_df = get_performance_data()
    st.dataframe(performance_df)
    
    # Show bar chart for yield comparison
    st.subheader("Yield Comparison")
    st.bar_chart(performance_df.set_index('Franchise')['Yield (kg)'])
    
    # Show line chart for operational efficiency
    st.subheader("Operational Efficiency Trends")
    st.line_chart(performance_df.set_index('Franchise')['Operational Efficiency (%)'])

# Sidebar menu function
def main_menu(user_role):
    st.sidebar.title("Navigation")
    
    if user_role == "Franchisee":
        option = st.sidebar.selectbox("Choose Action", ["Yield Management", "Financial Performance"])
        if option == "Yield Management":
            yield_tracking()  # Assuming this function exists for franchisees
        elif option == "Financial Performance":
            st.write("Financial performance coming soon.")
    
    elif user_role == "Management":
        option = st.sidebar.selectbox("Choose Action", ["Franchise Performance", "Strategic Planning"])
        if option == "Franchise Performance":
            franchise_performance()  # Show franchise performance tracking
        elif option == "Strategic Planning":
            st.write("Strategic planning coming soon.")
    
    elif user_role == "Investor":
        option = st.sidebar.selectbox("Choose Action", ["Financial Overview", "Sustainability Impact"])
        st.write(f"{option} coming soon.")
    
    elif user_role == "Technical Staff":
        option = st.sidebar.selectbox("Choose Action", ["Equipment Monitoring", "Maintenance Logs"])
        st.write(f"{option} coming soon.")
    
    else:
        st.sidebar.write("Select a valid user role.")

# Main function
def main():
    # Placeholder for authentication
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if username and password:  # Simple placeholder for authentication
        user_role = st.selectbox("Select your role", ["Franchisee", "Management", "Investor", "Technical Staff"])
        main_menu(user_role)  # Call the sidebar menu after role selection
        display_dashboard(user_role)  # Display the dashboard content for the user role
    else:
        st.error("Please enter your username and password.")

# Run app
if __name__ == "__main__":
    main()
