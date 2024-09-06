import streamlit as st

def create_support_section():
    # Initialize session state if not already set
    if 'show_feedback_input' not in st.session_state:
        st.session_state.show_feedback_input = False

    # Custom HTML/CSS for the support section and plus button
    st.markdown(
        """
        <style>
        .support-section {
            background-color: #164050;
            padding: 20px;
            border-radius: 0px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            position: relative;  /* Make sure to position relative for absolute positioning of the button */
        }

        .support-text {
            color: #d6e6ed;
        }

        .support-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 5px;
        }

        .support-subtitle {
            font-size: 16px;
            margin-bottom: 0;
        }

        .plus-button {
            background-color: #d6e6ed;
            color: #164050;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            border: none;
            font-size: 36px;
            font-weight: bold;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
        }

        .plus-button:hover {
            background-color: #b0c4ce;
        }

        .hidden-streamlit-button {
            position: absolute;
            top: -100px;  /* Adjust positioning based on your layout */
            right: 20px;  /* Align with the plus button */
            width: 50px;
            height: 50px;
            opacity: 0;  /* Make the button invisible */
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Layout to ensure proper alignment and avoid unwanted buttons
    st.markdown(
        """
        <div class="support-section">
            <div class="support-text">
                <div class="support-title">Support</div>
                <div class="support-subtitle">Do you need more data on the context?</div>
            </div>
            <button class="plus-button">+</button>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Invisible button positioned over the fake button
    button_clicked = st.button(" ", key="hidden_plus_button", help="Click to provide feedback")
    
    if button_clicked:
        st.session_state.show_feedback_input = not st.session_state.show_feedback_input

    # Display the feedback input if the plus button was clicked
    if st.session_state.show_feedback_input:
        st.text_input("Please provide your feedback here:")

