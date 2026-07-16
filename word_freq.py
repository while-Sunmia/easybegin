import string
import streamlit as st
st.title("Word frequency App")
st.write("This is an app that shows you many times a word has appeared and also highlights the specified word in the paragraph")
pas = st.text_input("Enter your paragraph/text/article: ")
word = st.text_input("Enter the word: ")

count = 0
if st.button("Show me the frequency:"):
  for i in pas.split():
    wo = i.lower().strip(".,/?!'-")
    if(wo==word):
     count = count + 1
  st.subheader(f"The word '{word}' has been used {count} times")
