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
    st.write(" ")
    st.header("Franchise Performance")
    
    # Display performance data
    st.subheader("FOverview")
    performance_df = get_performance_data()
    st.dataframe(performance_df)
    
    # Show bar chart for yield comparison
    st.subheader("Yield Comparison")
    st.bar_chart(performance_df.set_index('Franchise')['Yield (kg)'])
    
    # Show line chart for operational efficiency
    st.subheader("Operational Efficiency Trends")
    st.line_chart(performance_df.set_index('Franchise')['Operational Efficiency (%)'])

