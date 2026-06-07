import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="F1 Stream Fix", layout="wide")

st.title("🏎️ F1 Live Stream")

# We use an HTML block that explicitly defines a 'refresh' rule and passes 
# a custom meta-referrer policy to mimic the parent domain tracking context.
spoof_html = """
<div style="width: 100%; height: 650px; background: #000;">
    <iframe 
        src="https://junkieembeds.pages.dev/embed/f1-on-apple" 
        width="100%" 
        height="100%" 
        frameborder="0" 
        scrolling="no" 
        referrerpolicy="no-referrer-when-downgrade"
        allow="autoplay; encrypted-media; picture-in-picture; fullscreen" 
        allowfullscreen>
    </iframe>
</div>

<script>
    // We dynamically force the frame element to attach 'timstreams.net' 
    // into the active browser navigation history object before drawing the viewport.
    Object.defineProperty(document, 'referrer', {
        get: function() { return 'https://timstreams.net/'; }
    });
</script>
"""

# Render the container inside Streamlit
components.html(spoof_html, height=660, scrolling=False)