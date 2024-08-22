import streamlit as st 
import google.generativeai as genai


st.title("Welcome to Explore Chat")

genai.configure(api_key="AIzaSyDe9N_olcsYrQktlgGraHJSbt5MIkUE65I")

text = st.text_input("ASK ME A QUESTION?")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("SUMBIT"):
    response = chat.send_message(text)
    st.write(response.text)