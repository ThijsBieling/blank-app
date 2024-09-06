# config.py

# Color scheme
COLORS = {
    "lichtblauw": "#d6e6ed",      # Light Blue
    "donkerblauw": "#164050",     # Dark Blue
    "oranje": "#d68437",          # Orange
    "white": "#ffffff"            # White
}

# Default values for sliders, dropdowns, etc.
DEFAULTS = {
    "satisfaction_score": 50,
    "focus_areas": ["Leaf", "Truss"],
    "indicators": ["Amount of leaves", "Flower colour"]
}

# Other configurations
PAGE_CONFIG = {
    "page_title": "Crop Monitoring Dashboard",
    "layout": "wide",
    "initial_sidebar_state": "collapsed",
    "color_scheme": {
        "topbar_bg": COLORS["donkerblauw"],  # Topbar background
        "topbar_text": COLORS["white"]       # Topbar text
    }
}
