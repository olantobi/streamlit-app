import streamlit as st
import pandas as pd
import numpy as np

with st.sidebar:
    st.title("About App")
    st.write("This is a sidebar where you can add additional information or controls.")
    st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
    st.slider("Adjust a value", 0, 100, 50)

st.title("Streamlit App Example")
st.header("Welcome to the Streamlit App", divider="rainbow")

st.markdown("""
This is a simple Streamlit application that demonstrates how to use headers and titles.
You can use various components to build interactive web applications with Python.
- Use `st.title()` for the main title of your app.
""")

st.subheader("St Columns")
col1, col2 = st.columns(2)

with col1:
  x = st.slider("Select a value", 0, 100, 50)
with col2:
    st.write("You selected :blue[***x***]", x)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.subheader("Line Chart")
st.line_chart(chart_data)

st.subheader("Area Chart")
st.area_chart(chart_data)


st.subheader("Data Table")
st.dataframe(chart_data)
st.subheader("Interactive Widgets")
st.button("Click Me")
st.checkbox("Check Me")
st.radio("Choose an option", ["Option 1", "Option 2", "Option3"])
st.selectbox("Select a value", ["A", "B", "C"])
st.text_input("Enter some text")
st.text_area("Enter more text")
st.file_uploader("Upload a file", type=["csv", "xlsx"])
st.download_button("Download Data", data=chart_data.to_csv(), file_name="data.csv", mime="text/csv")
# st.sidebar.header("Sidebar")
# st.sidebar.selectbox("Sidebar Option", ["Option A", "Option B", "Option C"])
# st.sidebar.slider("Sidebar Slider", 0, 100, 50)   
# st.sidebar.checkbox("Sidebar Checkbox")
# st.sidebar.radio("Sidebar Radio", ["Choice 1", "Choice 2", "Choice 3"])