import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="F1 Stream Bypass", layout="wide")

st.title("🏎️ F1 Live Stream")

# This script runs inside Streamlit's sandbox but uses window.top to completely 
# overwrite the page container with a native, unrestricted iframe.
bypass_html = """
<script>
    // Build the clean iframe string
    const iframeCode = `
        <body style="margin:0;padding:0;background:#000;overflow:hidden;">
            <iframe 
                src="https://junkieembeds.pages.dev/embed/f1-on-apple" 
                width="100%" 
                height="100vh" 
                style="width:100vw; height:100vh; border:none; margin:0; padding:0;"
                scrolling="no" 
                allow="autoplay; encrypted-media; picture-in-picture; fullscreen" 
                allowfullscreen>
            </iframe>
        </body>
    `;

    // Force the browser to inject this iframe outside of Streamlit's sandbox restrictions
    window.parent.document.open();
    window.parent.document.write(iframeCode);
    window.parent.document.close();
</script>
"""

# Execute the bypass script
components.html(bypass_html, height=0, width=0)