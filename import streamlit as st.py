import streamlit as st
import streamlit.components.v1 as components
import requests

st.set_page_config(page_title="F1 Live Stream", layout="wide")
st.title("🏎️ F1 Live Stream")

@st.cache_data(ttl=3600)  # Cache the retrieval for performance
def get_modified_stream():
    url = "https://junkieembeds.pages.dev/embed/f1-on-apple"
    headers = {
        "Referer": "https://timstreams.net/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        html = response.text
        
        # Strip or bypass common anti-frame/sandbox detection scripts if present
        html = html.replace("window.top !== window.self", "false")
        html = html.replace("top.location", "self.location")
        
        return html
    except Exception as e:
        return f"<p style='color:red;'>Failed to fetch stream source: {str(e)}</p>"

# Fetch the raw code using the correct referrer header from the server backend
stream_html = get_modified_stream()

# Render the sanitized content inside an isolated component container
components.html(stream_html, height=650, scrolling=True)