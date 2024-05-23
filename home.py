import streamlit as st
from backend.retrieve_response import get_llm_response

st.header("Varsity Query")

form_input = st.text_input('Enter Query')
submit = st.button("Generate")

if submit:
    with st.spinner("Processing"):
        #st.write(get_llm_response(form_input))
        st.write("get_llm_response(form_input)")