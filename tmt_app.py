import streamlit as st
import random

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="TMT - Teacher Manage Tasks",
    page_icon="TMTlogo.jpeg",  # Your original image icon
    layout="centered"
)

# --- CUSTOM CSS FOR CUTE THEME WITH BG GRADIENT AND EMOJIS ---
cute_css = """
<style>
/* Import font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
    color: #5A4E42;
    min-height: 100vh;
    margin: 0;
}

h1, h2, h3 {
    color: #A56C6C;
    text-shadow: 1px 1px 3px #FFD9D9;
}

.stTextInput input, .stTextArea textarea, .stNumberInput input {
    border-radius: 15px;
    border: 2px solid #FFB6B9;
    padding: 10px;
    box-shadow: 1px 1px 5px #FFD6D6;
    transition: border-color 0.3s ease;
    font-size: 16px;
}

.stTextInput input:focus, .stTextArea textarea:focus, .stNumberInput input:focus {
    border-color: #FF6F91;
    outline: none;
}

.stButton>button {
    background-color: #FF6F91;
    color: white;
    border-radius: 25px;
    padding: 12px 30px;
    font-weight: 700;
    font-size: 16px;
    box-shadow: 0 4px 12px rgba(255,111,145,0.5);
    transition: background-color 0.3s ease;
    cursor: pointer;
}

.stButton>button:hover {
