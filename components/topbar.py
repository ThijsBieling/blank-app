import streamlit as st
from datetime import datetime
from utils.config import COLORS, PAGE_CONFIG

def topbar():
    today_date = datetime.now().strftime("%B %d, %Y")
    st.markdown(
        f"""
        <div style='background-color: {PAGE_CONFIG['color_scheme']['topbar_bg']}; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center;'>
            <div style='flex: 1;'>
                <h1 style='color: {COLORS['lichtblauw']}; margin: 0;'>Today</h1>
                <h3 style='color: {COLORS['lichtblauw']}; margin: 0;'>{today_date}</h3>
            </div>
            <div style='flex: 1; text-align: center;'>
                <h1 style='margin: 0;'>&nbsp;</h1>  <!-- Empty H1 for spacing -->
                <h3 style='color: {COLORS['lichtblauw']}; margin: 0;'>Data entry</h3>
            </div>
            <div style='flex: 1; text-align: right;'>
                <h1 style='margin: 0;'>&nbsp;</h1>  <!-- Empty H1 for spacing -->
                <h3 style='color: {COLORS['lichtblauw']}; margin: 0;'>Week 10</h3>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
