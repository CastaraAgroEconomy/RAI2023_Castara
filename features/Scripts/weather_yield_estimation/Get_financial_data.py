import streamlit as st
import pandas as pd

# Example financial data for franchises
def get_financial_data():
    data = {
        'Franchise': ['Franchise A', 'Franchise B', 'Franchise C', 'Franchise D', 'Franchise E','Franchise F'],
        'Revenue ($)': [50000, 62000, 55000, 57000, 59000, 63000],
        'Profit ($)': [12000, 15000, 13000, 14500, 15000, 16000],
        'Profit Share (%)': [24, 25, 23, 24, 24, 25]
    }
    df = pd.DataFrame(data)
    return df

# Financial dashboard for management
def financial_data():
    st.header("Financial Data")
    
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
def management_dashboard_external(user_role):
    """ Display the management dashboard based on the given user role. """
    st.header(f"{user_role} Dashboard")
    
    if user_role == "Management":
        financial_data()  # Management function's display of financial data
    else:
        st.write("Welcome to the Castara AgroEconomy dashboard.")
