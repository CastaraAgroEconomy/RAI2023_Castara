import streamlit as st
import pandas as pd

# Example financial data for franchises
def get_financial_data():
    data = {
        'Franchise': ['Franchise A', 'Franchise B', 'Franchise C'],
        'Revenue ($)': [50000, 62000, 55000],
        'Profit ($)': [12000, 15000, 13000],
        'Profit Share (%)': [24, 25, 23]
    }
    df = pd.DataFrame(data)
    return df

# Financial dashboard for management
def financial_dashboard():
    st.header("Financial Dashboard")
    
    # Display financial data
    st.subheader("Franchise Financial Overview")
    financial_df = get_financial_data()
    st.dataframe(financial_df)
    
    # Show bar chart for revenue comparison
    st.subheader("Revenue Comparison")
    st.bar_chart(financial_df.set_index('Franchise')['Revenue ($)'])

    # Show line chart for profit trends
    st.subheader("Profit Trends")
    st.line_chart(financial_df.set_index('Franchise')['Profit ($)'])

# Update the management dashboard to include financial tracking
def display_dashboard(user_role):
    """ Display the dashboard based on user role. """
    st.header(f"{user_role} Dashboard")
    
    if user_role == "Management":
        financial_dashboard()  # Management function for financial data
    else:
        st.write("Welcome to the Castara AgroEconomy dashboard.")
