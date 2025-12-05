import streamlit as st
import streamlit.components.v1 as components

from PIL import Image

# This works locally AND on deployment without changing anything
st.image("images/geet.jpg")
# Set page configuration to wide mode
st.set_page_config(layout="wide", page_title="Geetanjali Portfolio")

# Read the HTML file (assuming you saved the HTML as index.html)
# OR you can paste the HTML string directly into a variable
with open("index.html", 'r', encoding='utf-8') as f:
    html_string = f.read()

# Render the HTML
# height needs to be adjusted based on content length

components.html(html_string, height=1500, scrolling=True)
