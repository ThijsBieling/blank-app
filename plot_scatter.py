import streamlit as st
import matplotlib.pyplot as plt

def plot_scatter(points):
    """
    Plots multiple points on a customized scatter plot.
    Each point is a dictionary with 'x', 'y', 'label', and 'symbol' keys.
    
    Args:
        points (list): A list of dictionaries where each dictionary represents a point with:
                       - 'x' (int/float): X-axis value
                       - 'y' (int/float): Y-axis value
                       - 'label' (str): Text label to display below the point
                       - 'symbol' (str): Symbol to display inside the point (e.g., "T", "N", "D")
    """
    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(5, 5))  # Adjust figsize to control plot size

    # Set the background color to light blue
    fig.patch.set_facecolor('#d6e6ed')
    ax.set_facecolor('#d6e6ed')

    # Set the limits for the axes
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)

    # Hide the default axis labels
    ax.set_xticks([])
    ax.set_yticks([])

    # Draw the center lines
    line_width = 3  # Set the same thickness for inner and outer lines
    ax.axhline(0, color='#d68437', linewidth=line_width)
    ax.axvline(0, color='#d68437', linewidth=line_width)

    # Add the custom quadrant labels with bold text and rounded corners
    ax.text(-110, 0, 'Vegetative', va='center', ha='right', fontsize=11, color='#d68437', weight='bold',
            bbox=dict(facecolor='#d6e6ed', edgecolor='#d68437', boxstyle='round,pad=0.5'))
    ax.text(110, 0, 'Generative', va='center', ha='left', fontsize=11, color='#d68437', weight='bold',
            bbox=dict(facecolor='#d6e6ed', edgecolor='#d68437', boxstyle='round,pad=0.5'))
    ax.text(0, 110, 'Strong', va='bottom', ha='center', fontsize=11, color='#d68437', weight='bold',
            bbox=dict(facecolor='#d6e6ed', edgecolor='#d68437', boxstyle='round,pad=0.5'))
    ax.text(0, -110, 'Weak', va='top', ha='center', fontsize=11, color='#d68437', weight='bold',
            bbox=dict(facecolor='#d6e6ed', edgecolor='#d68437', boxstyle='round,pad=0.5'))

    # Add a label for the center point ("Balance") with bold text and a rounded corner box
    ax.text(0, 0, 'Balance', va='center', ha='center', fontsize=11, color='#d6e6ed', weight='bold',
            bbox=dict(facecolor='#d68437', edgecolor='none', boxstyle='round,pad=0.5'))

    # Plot each point with its corresponding symbol and label
    circle_size = 300  # Set the size of the circle
    for point in points:
        ax.scatter(point['x'], point['y'], color='#d68437', s=circle_size)  # Larger circle
        ax.text(point['x'], point['y'] - 1.5, point['symbol'], va='center', ha='center', fontsize=12, color='#d6e6ed', weight='bold')
        ax.text(point['x'], point['y'] - 12.5, point['label'], va='top', ha='center', fontsize=11, color='#d68437')

    # Customize grid and frame
    ax.grid(False)  # Turn off the grid
    for spine in ax.spines.values():
        spine.set_color('#d68437')
        spine.set_linewidth(line_width)

    # Display the plot in Streamlit
    st.pyplot(fig)
