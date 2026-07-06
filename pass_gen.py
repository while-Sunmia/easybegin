
import streamlit as st
import random

st.title("PASSWORD GENERATOR")
st.text("This is an app that generates a strong password for your internet purposes:")
limit = int(st.text_input("What is the length of ur alphanumeric password ?"))
gen = random(size = limit)
st.subheader(f"Your generated password is {gen}")
