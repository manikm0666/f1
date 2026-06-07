import streamlit as st
import base64

st.set_page_config(page_title="F1 Stream Player", layout="wide")

st.title("🏎️ F1 Live Stream")

# The clean HTML document that handles the iframe natively
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        html, body { margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden; background-color: #000; }
        iframe { width: 100%; height: 100%; border: none; }
    </style>
</head>
<body>
    <iframe 
        src="https://junkieembeds.pages.dev/embed/f1-on-apple" 
        scrolling="no" 
        allow="autoplay; encrypted-media; picture-in-picture; fullscreen" 
        allowfullscreen>
    </iframe>
</body>
</html>
"""

# Encode the HTML into a base64 Data URI to mask the cross-origin reference
b64_html = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
data_uri = f"data:text/html;base64,{b64_html}"

# Render using a standard native iframe markdown block
st.markdown(
    f'<iframe src="{data_uri}" style="width:100%; height:650px; border:none;"></iframe>', 
    unsafe_allow_html=True
)