import streamlit as st
import pandas
from send_email import send_email

st.set_page_config(page_title="Contact Us", layout="wide")

df = pandas.read_csv("topics.csv", )

with st.form(key="email_form"):
    email_address = st.text_input("Your email address")
    topic = st.selectbox("What topic do you want to discuss?", df["topic"])
    text = st.text_area("Message")
    message = f"""\
Subject: Website form from {email_address}

From: {email_address}\n
Topic: {topic}
{text}
"""
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        send_email(message)
        st.info("Email send successfully.")