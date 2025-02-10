import streamlit as st
import time as t 

st.image(r'C:\Users\HP 745 G6\Downloads\intellipaat.png')
 
#title
st.title("Welcome to intellipat")

# Header
st.header("Machine Learning")

# sub header
st.subheader("Linear Regression")

# information details
st.info("Information details of a user")

# Warning message
st.warning("Come on time or else you will be marked absent")

# Error message
st.error("Wrong Password")

# sucess message
st.success("Congrats you have got A grade")

# write 
st.write("Employee name")
st.write(range(50))

# markdown
st.markdown("# Intellipaat")
st.markdown("## Intellipaat")
st.markdown("### Intellipaat")
st.markdown(":moon:")

st.text("Intellipaat learners")

# to write a caption
st.caption("Caption is here")

# to display a mathematics
st.latex(r''' a+b x^2+c''')

# WIDGETS
st.checkbox('Login')

# button
st.button("Click")

# Radio widget
st.radio("Pick your gender",["Male","Female","other"])

# select box
st.selectbox("Pick your course",["ML","Data science","Data Analytics","Cyber security"])

# multiselect
st.multiselect("Choose the dept",["Content","Sales","Marketing"])

# selectslider
st.select_slider("Rating",["Bad","Good","Excellent","Outstanding"])

# slider
st.slider("Enter your number",0,100)

# number_input
st.number_input("Pick a number",0,100)

# text input
st.text_input("Enter your email address")

# date input
st.date_input("Opening ceremony")

# time input
st.time_input("Hey whats the timing")

# text area
st.text_area("Welcome to the intellipaat website.Hello learners")

st.file_uploader("Upload your file/folder")

st.color_picker("color")

st.progress(90)

# spinner
with st.spinner("Just wait"):
    t.sleep(5)
    
# ballon
st.balloons() 

# side bar
st.sidebar.title("intellipaat")
st.sidebar.text_input("Mail Address")
st.sidebar.text_input("Password")
st.sidebar.button("Submit")
st.sidebar.radio("Professional Expert",["Student","Working","Others"])

# Data visualization
import pandas as pd
import numpy as np
st.title("Bar Chart")
data = pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)
st.title("Line Chart")
st.line_chart(data)
st.title("Area Chart")
st.line_chart(data)