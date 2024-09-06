import streamlit as st
import base64

# Adds whitspace
def add_margin(margin_px):
    """
    Adds a custom margin in pixels.

    Args:
        margin_px (int): The size of the margin in pixels.
    """
    st.markdown(
        f"""
        <div style="margin-top: {margin_px}px;"></div>
        """,
        unsafe_allow_html=True
    )

# Makes images centered and a certain size
def display_centered_image(image_path, width=400):
    """
    Displays an image centered with a specified width.

    Args:
        image_path (str): The path to the image file.
        width (int): The width of the image in pixels. Defaults to 400.
    """
    # Encode the image to base64
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()

    # Create the HTML to display the image centered without a caption
    st.markdown(
        f"""
        <style>
        .centered-image {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: {width}px;
        }}
        .stImage > div {{
            text-align: center;
        }}
        .stImage > div:after {{
            content: none;
        }}
        </style>

        <div class="centered-image">
            <img src="data:image/png;base64,{encoded_image}" alt="Image" />
        </div>
        """,
        unsafe_allow_html=True
    )

# Makes the buttons our custom color
def create_custom_button(button_text="Continue"):
    """
    Creates a custom-styled button with the provided text.

    Args:
        button_text (str): The text to display on the button. Defaults to "Continue".
    """
    st.markdown(
        """
        <style>
        .custom-button {
            background-color: #d68437;  /* Orange background */
            color: #d6e6ed;  /* Light blue text */
            padding: 50px 150px;  /* Increase padding for a larger button */
            font-size: 36px;  /* Larger font size */
            font-weight: bold;
            border-radius: 100px;  /* Rounded corners */
            border: none;
            cursor: pointer;
        }

        .custom-button:hover {
            background-color: #c76a2f;  /* Slightly darker orange on hover */
        }

        .center {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="center">
            <button class="custom-button">{button_text}</button>
        </div>
        """,
        unsafe_allow_html=True
    )

def add_custom_button_css():
    st.markdown(
        """
        <style>
        .stButton > button {
            padding: 10px 20px;
            font-size: 20px;
            font-weight: bold;
            background-color: #d68437;
            color: #d6e6ed;
            border-radius: 10px;
            border: none;
        }

        .stButton > button:hover {
            background-color: #c76a2f;
            color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Makes a slider using our style
def apply_slider_style():
    """
    Applies custom CSS to style the slider with a triangle thumb and orange track.
    The slider values (0 and 100) are hidden, and the percentage display is aligned.
    """
    # CSS to hide the background of min and max labels and change their text color to light blue
    st.markdown('''
        <style>
        /* Hide the background of min and max labels */
        div.stSlider > div[data-baseweb="slider"] > div[data-testid="stTickBar"] > div {
            background: rgb(1 1 1 / 0%) !important;  /* Make the background transparent */
        }
        /* Change the color of the min, max, and value labels to light blue */
        div.stSlider > div[data-baseweb="slider"] > div > div > div > div {
            color: #d6e6ed !important;  /* Light blue color for the labels */
        }
        </style>
    ''', unsafe_allow_html=True)
    
    st.markdown(
        """
        <style>
        [data-testid="stTickBar"] > div {
            color: #d6e6ed !important;  /* Light blue color for tick labels */
        }
   
        /* Slider thumb customization to make it a triangle */
        div[data-baseweb="slider"] > div > div > div > div {
            width: 0 !important;
            height: 0 !important;
            border-left: 30px solid transparent !important;
            border-right: 30px solid transparent !important;
            border-top: 54px solid #d68437 !important;  /* Orange triangle */
            top: -17px !important;  /* Move the triangle upwards */
            margin-left: 0px !important;  /* Center the triangle thumb */
        }

        /* Slider value label (percentage display) */
        div[data-baseweb="slider"] > div > div > div > div > div {
            display: none;  /* Hide the default value label */
        }

        /* Adjust the slider width and align to the left */
        div[data-baseweb="slider"] > div {
            width: 80% !important;  /* Set the slider width
            margin: 0 0 0 0;  /* Align the slider to the left */
        }

        /* Custom percentage display on the right */
        .custom-slider-value {
            position: absolute;
            right: 10px;  /* Position it right next to the slider */
            top: -75px;  /* Align it vertically with the slider */
            background-color: #d68437;
            color: white;
            padding:  8px 16px;
            border-radius: 40px;
            font-size: 24px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def display_custom_slider(label, min_value, max_value, default_value, left_label, right_label):
    """
    Displays a custom slider with labels on the left and right side and a percentage label on the right.
    
    Parameters:
    label (str): The label for the slider.
    min_value (int/float): The minimum value of the slider.
    max_value (int/float): The maximum value of the slider.
    default_value (int/float): The default value of the slider.
    left_label (str): The label to display on the left side of the slider.
    right_label (str): The label to display on the right side of the slider.
    
    Returns:
    int/float: The current value of the slider.
    """
    # Display the labels above the slider
    st.markdown(
        f"""
        <div style="display: flex; justify-content: space-between; width: 80%;">
            <span style="color: #d68437;">{left_label}</span>
            <span style="color: #d68437;">{right_label}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # The slider itself
    value = st.slider(label, min_value, max_value, default_value, label_visibility="hidden")

    # Display the percentage value on the right
    st.markdown(f'<div class="custom-slider-value">{int(value)}</div>', unsafe_allow_html=True)

    return value
