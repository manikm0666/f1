import streamlit as st
import streamlit.components.v1 as components

# Set up the page configuration
st.set_page_config(
    page_title="F1 Stream Player",
    page_icon="🏎️",
    layout="wide"  # Uses the full width of the screen
)

st.title("🏎️ Live Stream Player")
st.caption("Watching: F1 on Apple")

# Define the iframe HTML string
iframe_html = """
<iframe 
    src="https://junkieembeds.pages.dev/embed/f1-on-apple" 
    width="100%" 
    height="100%" 
    frameborder="0" 
    scrolling="no" 
    allow="autoplay; encrypted-media; picture-in-picture; fullscreen" 
    allowfullscreen>
</iframe>
"""

# Render the iframe component
# We set a fixed height (e.g., 600px) so the video player has enough vertical space
components.html(iframe_html, height=600, scrolling=False)