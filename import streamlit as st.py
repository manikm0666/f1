import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="F1 Stream Player",
    page_icon="🏎️",
    layout="wide"
)

st.title("🏎️ Live Stream Player")
st.caption("Watching: F1 on Apple")

# We use raw HTML inside st.markdown to prevent Streamlit from forcing a sandbox.
# This uses a standard flex container to keep it responsive.
iframe_html = """
<div style="width: 100%; height: 650px; overflow: hidden;">
    <iframe 
        src="https://junkieembeds.pages.dev/embed/f1-on-apple" 
        width="100%" 
        height="100%" 
        frameborder="0" 
        scrolling="no" 
        allow="autoplay; encrypted-media; picture-in-picture; fullscreen" 
        allowfullscreen>
    </iframe>
</div>
"""

# Render using markdown with unsafe HTML allowed
st.markdown(iframe_html, unsafe_allow_html=True)