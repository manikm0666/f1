import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="F1 Stream Player",
    page_icon="🏎️",
    layout="wide"
)

st.title("🏎️ Live Stream Player")
st.caption("Watching: F1 on Apple")

# Create a placeholder div where our true iframe will live
st.markdown('<div id="player-container" style="width:100%; height:650px;"></div>', unsafe_allow_html=True)

# Inject custom JavaScript to dynamically create and append a completely unrestricted iframe
js_script = """
<script>
    // Find the container we just made in the parent window
    const container = window.parent.document.getElementById('player-container');
    
    if (container && !container.querySelector('iframe')) {
        // Create a pristine iframe element
        const iframe = window.parent.document.createElement('iframe');
        
        // Apply your video parameters
        iframe.src = "https://junkieembeds.pages.dev/embed/f1-on-apple";
        iframe.style.width = "100%";
        iframe.style.height = "100%";
        iframe.style.border = "none";
        iframe.scrolling = "no";
        iframe.setAttribute("allow", "autoplay; encrypted-media; picture-in-picture; fullscreen");
        iframe.setAttribute("allowfullscreen", "true");
        
        # Explicitly ensure no sandbox attribute exists anywhere near it
        iframe.removeAttribute("sandbox");
        
        // Inject it directly into the main, un-sandboxed Streamlit DOM
        container.appendChild(iframe);
    }
</script>
"""

# Execute the script (we keep the component height 0 so it's invisible)
components.html(js_script, height=0, width=0)