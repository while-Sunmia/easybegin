
import streamlit as st
import random
import string

st.title("PASSWORD GENERATOR")
st.text("This is an app that generates a strong password for your internet purposes:")
char = []
lim = st.text_input("What is the length of ur alphanumeric password ?")
limit = int(lim)
if st.button("Generate!"):
  for i in range(limit):
    gen = random.choice(string.ascii_letters + string.digits)
    char.append(gen)

  word = "".join(char)
  st.subheader(f"Your generated password is {word}")
st.markdown(
    """
    <style>
    h1{color: black; text-align: center; font-size: 100px;font-style: italic;font-family: Aerial}
    h3{color: black; text-align: center;}
    .stApp{
        background-color: pink;
    }
    p{color: black;font-size: 18px;}
    .stButton>button{
        background-color: red;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)
