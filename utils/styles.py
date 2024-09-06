import streamlit as st
from .config import COLORS

def apply_styles():
    st.markdown(
        f"""
        <style>
        /* Set the entire app background color */
        .stApp {{
            background-color: {COLORS['lichtblauw']};  /* Light Blue Background */
        }}

        /* Set the main container's background color */
        .main {{
            background-color: {COLORS['lichtblauw']};  /* Light Blue Background */
            padding: 0 !important;
        }}

        /* Set text colors */
        .css-1v0mbdj a {{
            color: {COLORS['donkerblauw']};  /* Dark Blue Links */
        }}
        .css-1q1n0ol {{
            color: {COLORS['donkerblauw']};  /* Dark Blue Text */
        }}
        .stMarkdown h2, .stMarkdown h4 {{
            color: {COLORS['donkerblauw']};  /* Dark Blue for headers */
        }}
        .stSlider {{
            color: {COLORS['oranje']};  /* Orange for slider */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def dynamic_style(element_id, color):
    st.markdown(
        f"""
        <style>
        #{element_id} {{
            color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
