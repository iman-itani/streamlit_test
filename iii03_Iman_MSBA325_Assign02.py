import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

governorate_totals=pd.read_csv("governorate_totals.csv")

# Title of the dashboard
st.title("Governorate Institution Totals Dashboard")

# Introduction
st.markdown("""
## Introduction

The analysis of the provided graphs highlights a significant gap in data concerning Beirut, the most crucial governorate in the tourism sector.
""")

# Distribution of Institutions
st.markdown("""
## Distribution of Institutions

Despite this absence, it is evident that across all available governorates, the number of cafes and restaurants substantially exceeds the counts of other types of institutions. This trend indicates a strong emphasis on dining and social spaces within the tourism landscape.
""")

# Select institution types to show
st.sidebar.subheader("Select Institution Types")
selected_types = st.sidebar.multiselect(
    label="Choose institution types",
    options=[
        'Total number of cafes', 
        'Total number of hotels', 
        'Total number of restaurants', 
        'Total number of guest houses'
    ],
    default=['Total number of cafes', 'Total number of hotels', 'Total number of restaurants', 'Total number of guest houses']
)

# Filter data based on selected institution types
filtered_data = governorate_totals[['Governorate'] + selected_types]

# Plot for institution totals by governorate
st.subheader("Institution Totals by Governorate")
if not filtered_data.empty:
    fig1 = px.bar(
        filtered_data,
        x='Governorate',
        y=selected_types,
        barmode='group',
        title='Institution Totals by Governorate'
    )
    st.plotly_chart(fig1)

# Slider for selecting tourism index range
st.sidebar.subheader("Tourism Index Filter")
tourism_range = st.sidebar.slider(
    "Select Tourism Index range:",
    min_value=0.0, max_value=10.0, value=(0.0, 10.0), step=0.1
)

# Filter data based on tourism index range
filtered_tourism_data = governorate_totals[
    (governorate_totals['Average Tourism Index'] >= tourism_range[0]) &
    (governorate_totals['Average Tourism Index'] <= tourism_range[1])
]

# Insights from the Tourism Index
st.markdown("""
## Insights from the Tourism Index

The second graph enhances our understanding by enabling filters based on the tourism index. This feature allows us to delve deeper into the relationships between the tourism index and various institution types within specific governorates.
""")

# Plot for tourism index vs institution totals
st.subheader("Total Number of Institutions for Selected Tourism Index Range")
if not filtered_tourism_data.empty:
    fig2 = px.bar(
        filtered_tourism_data,
        x='Governorate',
        y=['Total number of cafes', 'Total number of hotels', 'Total number of restaurants', 'Total number of guest houses'],
        barmode='group',
        title='Institutions by Governorate (Filtered by Tourism Index)'
    )
    st.plotly_chart(fig2)

# Conclusion
st.markdown("""
## Conclusion

This analysis reveals how different governorates align with tourism performance indicators, providing valuable insights into the dynamics of the tourism sector.
""")
