
import streamlit as st
import random
import string

st.title("PASSWORD GENERATOR")
st.text("This is an app that generates a strong password for your internet purposes:")
char = []
limit = int(st.text_input("What is the length of ur alphanumeric password ?"))
if st.button("Generate!"):
  if i in limit:
    gen = random.choice(string.ascii_letters + string.digits)
    char.append(gen)

  word = "".join(char)
  st.subheader(f"Your generated password is {word}")
