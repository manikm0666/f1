import streamlit as st

st.set_page_config(page_title="F1 Launcher", layout="wide")

st.title("🏎️ F1 Live Stream")

# A pure, unstyled markdown link that forces a new tab.
# No CSS, no iframe containers, zero chance of a sandbox block.
st.markdown(
    '### 👉 [CLICK HERE TO LAUNCH STREAM (NEW TAB)](https://junkieembeds.pages.dev/embed/f1-on-apple)', 
    unsafe_allow_html=True
)