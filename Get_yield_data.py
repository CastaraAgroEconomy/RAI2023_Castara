import pandas as pd
import streamlit as st

# Example yield data
def get_yield_data():
    data = {
        'Date': ['2024-09-01', '2024-09-15', '2024-09-30', '2024-10-14'],
        'Yield (kg)': [1000, 1200, 1100, 1300]
    }
    df = pd.DataFrame(data)
    return df

# Yield tracking function for franchisees
def yield_tracking():
    st.header("Yield Tracking")

    # Display yield data
    st.subheader("Current Yield Data")
    st.write(" ")
    yield_df = get_yield_data()
    st.dataframe(yield_df)
    
    # Display a yield trend chart
    st.subheader("Yield Trend")
    st.line_chart(yield_df.set_index('Date')['Yield (kg)'])

