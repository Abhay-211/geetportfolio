import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# --- CORRECTION 1: set_page_config must be the first st command ---
st.set_page_config(layout="wide", page_title="Geetanjali Portfolio")

# --- Display the image ---
# Make sure you have a folder named 'images' with 'geet.jpg' inside it
try:
    st.image("images/geet.jpg") 
except FileNotFoundError:
    st.error("Image file not found. Please check 'images/geet.jpg' exists.")

# --- CORRECTION 2: Fixed the broken 'utf-8' string ---
# Read the HTML file
try:
    with open("index.html", 'r', encoding='utf-8') as f:
        html_string = f.read()

    # Render the HTML
    components.html(html_string, height=1500, scrolling=True)

except FileNotFoundError:
    st.error("The file 'index.html' was not found in the directory.")
