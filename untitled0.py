# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/136z4NW1bdAgz-4y2sXEJGZKNoVEELXEH
"""

import streamlit as st
import pandas as pd

# Title of the app
st.title('Interactive Data Visualization App')

# Pre-loaded dataset
data = {
    'Country': ['USA', 'China', 'India', 'Japan', 'Germany'],
    'GDP (Trillions USD)': [21.43, 14.34, 2.87, 5.08, 3.86],
    'Population (Millions)': [331, 1441, 1380, 126, 83]
}

df = pd.DataFrame(data)

# Show the data
st.write("Dataset:")
st.write(df)

# Let user select columns for visualization
columns = df.columns.tolist()

# Dropdowns for X and Y axes
x_axis = st.selectbox('Select column for X-axis', columns)
y_axis = st.selectbox('Select column for Y-axis', columns)

# Choose chart type: Bar or Line
chart_type = st.selectbox('Select chart type', ['Bar Chart', 'Line Chart'])

# Display chart based on user selections
if chart_type == 'Bar Chart':
    st.bar_chart(df[[x_axis, y_axis]].set_index(x_axis))
elif chart_type == 'Line Chart':
    st.line_chart(df[[x_axis, y_axis]].set_index(x_axis))

