import streamlit as st
from main import validate_hsn

st.title("📦 HSN Code Validation Chatbot")

user_input = st.text_input("Enter HSN code(s), comma-separated (e.g., 01, 0101, 01011010)")

if st.button("Validate"):
    if user_input:
        codes = [code.strip() for code in user_input.split(",")]
        params = {"hsn_code": codes}
        response = validate_hsn(params)
        st.text_area("Validation Result", response["messages"][0]["text"], height=250)
    else:
        st.warning("Please enter one or more HSN codes.")
