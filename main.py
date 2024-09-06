import streamlit as st
from components import topbar, main_content_section
from utils import apply_styles, PAGE_CONFIG, setup_logger

# App setup
st.set_page_config(
    page_title=PAGE_CONFIG["page_title"],
    layout="wide",  # No sidebar
    
    initial_sidebar_state="collapsed"
)

# Apply custom styles
apply_styles()

# Initialize logger
setup_logger()

# Main Content
def main():
    topbar()  # Add the topbar with today's date
    main_content_section()

if __name__ == "__main__":
    main()
