import streamlit as st
import pandas
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

st.set_page_config(layout="wide")

st.header("The Best Company")
byline = """
proin sed libero enim sed faucibus turpis in eu mi bibendum neque egestas congue quisque egestas diam in
arcu cursus euismod quis viverra nibh cras pulvinar mattis nunc sed blandit libero volutpat sed cras ornare
arcu dui vivamus arcu felis bibendum ut tristique et egestas quis ipsum suspendisse ultrices gravida dictum
fusce ut placerat orci nulla pellentesque dignissim enim sit amet venenatis urna cursus eget nunc scelerisque
viverra mauris in aliquam sem fringilla ut morbi tincidunt augue interdum velit euismod
"""
st.write(byline)
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)
dataframe = pandas.read_csv("data.csv")

with col1:
    for index, row in dataframe[:4].iterrows():
        name = f"{row['first name'].capitalize()} {row['last name'].capitalize()}"
        st.subheader(name)
        st.write(row['role'])
        st.image("images/" + row['image'])

with col2:
    for index, row in dataframe[4:8].iterrows():
        name = f"{row['first name'].capitalize()} {row['last name'].capitalize()}"
        st.subheader(name)
        st.write(row['role'])
        st.image("images/" + row['image'])

with col3:
    for index, row in dataframe[8:].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image("images/" + row['image'])
