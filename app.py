import streamlit as st
import streamlit.components.v1 as components
import base64

# 1. Set page config MUST be the first Streamlit command
st.set_page_config(layout="wide", page_title="Geetanjali Portfolio")

# Function to convert image to base64 so HTML can read it
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

# 2. Get the Base64 string of your image
image_path = "images/geet.jpg" 
img_base64 = get_base64_image(image_path)

if img_base64:
    img_src = f"data:image/jpg;base64,{img_base64}"
else:
    # Fallback if image isn't found
    img_src = "https://via.placeholder.com/400" 
    st.error("Could not find 'images/geet.jpg'. Check your folder structure.")

# 3. Read the HTML file
try:
    with open("index.html", 'r', encoding='utf-8') as f:
        html_string = f.read()

    # 4. MAGIC STEP: Replace the local path in HTML with the Base64 data
    # This finds "images/geet.jpg" in your HTML and swaps it for the actual image data
    html_string = html_string.replace("images/geet.jpg", img_src)

    # 5. Render the HTML
    components.html(html_string, height=1500, scrolling=True)

except FileNotFoundError:
    st.error("The file 'index.html' was not found.")
