import streamlit as st
import utils.layout_utils
import components


def main_content_section():
    utils.layout_utils.add_margin(40)

    # Add Crop Location section
    st.markdown("### Crop location")
    st.markdown("Which crop are you monitoring?")

    # Text input for crop location with a default value and hidden visibility
    crop_location = st.text_input("Enter crop location here:", placeholder="Department A, row 100",label_visibility='hidden')

    utils.layout_utils.add_margin(70)

    st.markdown("### General Crop Satisfaction Score")
    st.markdown("Shift the triangle to match how satisfied you feel in general about the crop’s health")
    utils.layout_utils.apply_slider_style()

    # Display the custom slider with a percentage value on the right
    satisfaction_value = utils.layout_utils.display_custom_slider("Satisfaction", 0, 100, 60, "Unsatisfied", "Satisfied")

    utils.layout_utils.add_margin(70)

    st.markdown("### Focus Areas")
    st.markdown("Select the areas of the plant that can be improved")
    focus_areas = st.multiselect("Select Focus Areas",
                                 ["Purple", "Colour", "Length", "Position", "Openness", "Flower", "Leaf", "Truss", "Stem", "Head"],
                                 label_visibility='hidden')

    utils.layout_utils.add_margin(70)

    st.markdown("### Growth status")
    st.markdown("Insert your growth status and view the progress using the buttons")

    utils.layout_utils.add_margin(20)

    # Initialize session state if not already set
    if "subpage" not in st.session_state:
        st.session_state.subpage = "Today"

    # Add custom CSS for larger buttons
    utils.layout_utils.add_custom_button_css()

    # Create columns to place buttons side by side and center them
    col1, col2, col3, col4, col5 = st.columns(5)  # Five columns for four buttons and centering

    with col1:
        if st.button("Today", key="today"):
            st.session_state.subpage = "Today"

    with col2:
        if st.button("Desired", key="desired"):
            st.session_state.subpage = "Desired"

    with col3:
        if st.button("Next Week", key="next_week"):
            st.session_state.subpage = "Next Week"

    with col4:
        if st.button("View Trend", key="view_trend"):
            st.session_state.subpage = "View Trend"

    utils.layout_utils.add_margin(20)

    # Display content based on the selected subpage
    if st.session_state.subpage in ["Today", "Desired", "Next Week"]:
        st.markdown(f"### {st.session_state.subpage} Status")
        st.markdown(f"Shift the triangle to match how vegetative or generative your crop is for {st.session_state.subpage}")
        
        veg_gen_value = utils.layout_utils.display_custom_slider("Vegetative", -100, 100, 
                                                                 st.session_state.get(f"{st.session_state.subpage.lower()}_veg_gen_value", 20), 
                                                                 "Vegetative", "Generative")

        utils.layout_utils.add_margin(20)

        st.markdown(f"Shift the triangle to match how weak or strong your crop is for {st.session_state.subpage}")
        
        weak_strong_value = utils.layout_utils.display_custom_slider("Strong", -100, 100, 
                                                                     st.session_state.get(f"{st.session_state.subpage.lower()}_weak_strong_value", 30), 
                                                                     "Weak", "Strong")

        utils.layout_utils.add_margin(40)

        # Store the values in the session state for later use
        st.session_state[f"{st.session_state.subpage.lower()}_veg_gen_value"] = veg_gen_value
        st.session_state[f"{st.session_state.subpage.lower()}_weak_strong_value"] = weak_strong_value

    elif st.session_state.subpage == "View Trend":
        # Display the plot with results from Today, Desired, and Next Week
        st.markdown("### View Trend")
        st.markdown("Below you can see your input results")

        # Retrieve stored values or use defaults if not yet set
        today_veg_gen = st.session_state.get("today_veg_gen_value", -20)
        today_weak_strong = st.session_state.get("today_weak_strong_value", 30)

        desired_veg_gen = st.session_state.get("desired_veg_gen_value", 40)
        desired_weak_strong = st.session_state.get("desired_weak_strong_value", -60)

        next_week_veg_gen = st.session_state.get("next_week_veg_gen_value", -10)
        next_week_weak_strong = st.session_state.get("next_week_weak_strong_value", 90)

        # Prepare the points for plotting
        points = [
            {"x": today_veg_gen, "y": today_weak_strong, "label": "Today", "symbol": "T"},
            {"x": desired_veg_gen, "y": desired_weak_strong, "label": "Desired", "symbol": "D"},
            {"x": next_week_veg_gen, "y": next_week_weak_strong, "label": "Next Week", "symbol": "N"}
        ]

        # Plot all points on the same scatter plot
        components.plot_scatter(points)

    utils.layout_utils.add_margin(70)

    components.create_support_section()

    utils.layout_utils.add_margin(40)

    st.markdown("### Indicators")
    st.markdown("Select the places that were most indicative for the current type of growth")

    # Display the image
    image_path = "figures/Flower_image.png"  # Replace with your actual image name
    utils.layout_utils.display_centered_image(image_path, width=500)

    utils.layout_utils.add_margin(10)

    # Add a multiselect box below the image
    options = ["Amount of leaves", "Place of flowering",
               "Purple colour", "Position truss-stem",
               "Flower colour", "Curling head", "Head thickness"]
    selected_options = st.multiselect("Select up to 3 options:", options)

    # Check if the number of selections exceeds the limit
    if len(selected_options) > 3:
        st.warning("You can only select up to 3 options.")

    utils.layout_utils.add_margin(70)

    # Create the custom button using the utility function
    utils.layout_utils.create_custom_button("Continue")

    utils.layout_utils.add_margin(40)

    # Add the powered by text below
    st.markdown(
        """
        <div class="center">
            <p style="font-size: 24px; color: #164050; font-weight: bold;">Powered by <br> Plense Technologies </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Print input to the terminal
    if crop_location:
        print(f"Crop location entered: {crop_location}")
