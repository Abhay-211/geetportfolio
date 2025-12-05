import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(layout="wide", page_title="Geetanjali Portfolio")

# --- 1. Function to convert any file (img/video) to Base64 ---
def get_base64_file(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

# --- 2. List of files to replace ---
# FORMAT: "The path inside HTML" : "Real path on computer"
# You must list every file you want to load here.
files_to_process = {
    # Images
    "images/geet.jpg": "images/geet.jpg",
    "images/poster1.jpg": "images/poster1.jpg",
    "images/poster2.jpg": "images/poster2.jpg",
    
    # Videos (Note: Keep these small for best performance!)
    "images/QUACI.mp4": "images/QUACI.mp4",
    "images/diego.mp4": "images/diego.mp4"
}

# --- 3. Read HTML ---
try:
    with open("index.html", 'r', encoding='utf-8') as f:
        html_string = f.read()

    # --- 4. Loop through the list and replace them all ---
    for html_path, local_path in files_to_process.items():
        b64_data = get_base64_file(local_path)
        
        if b64_data:
            # Determine the file type (MIME type)
            if local_path.endswith(".mp4"):
                mime = "data:video/mp4;base64,"
            elif local_path.endswith(".jpg") or local_path.endswith(".jpeg"):
                mime = "data:image/jpeg;base64,"
            elif local_path.endswith(".png"):
                mime = "data:image/png;base64,"
            else:
                mime = "" # Fallback
            
            # Create the full source string
            new_src = mime + b64_data
            
            # Replace it in the HTML string
            html_string = html_string.replace(html_path, new_src)
            print(f"Successfully loaded: {local_path}")
        else:
            print(f"⚠️ Warning: Could not find file {local_path}")

    # --- 5. Render ---
    components.html(html_string, height=3000, scrolling=True)

except FileNotFoundError:
    st.error("Could not find index.html")

