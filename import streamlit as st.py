import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="F1 Stream Fix", layout="wide")

st.title("🏎️ F1 Live Stream")

# This script creates an inline Blob document on your actual Streamlit domain,
# forcing the browser to send a valid HTTP Referer header instead of 'null'.
blob_bypass_script = """
<div id="stream-target" style="width:100%; height:650px; background:#000;"></div>

<script>
    const htmlContent = `
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                html, body { margin:0; padding:0; width:100%; height:100%; overflow:hidden; background:#000; }
                iframe { width:100%; height:100%; border:none; }
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
    `;

    // Create a data blob with a valid text/html mime-type
    const blob = new Blob([htmlContent], { type: 'text/html' });
    const blobURL = URL.createObjectURL(blob);

    // Build the container iframe that targets our new valid blob URL
    const finalIframe = document.createElement('iframe');
    finalIframe.src = blobURL;
    finalIframe.style.width = '100%';
    finalIframe.style.height = '100%';
    finalIframe.style.border = 'none';
    
    // Append it straight to the target div
    document.getElementById('stream-target').appendChild(finalIframe);
</script>
"""

# Render the script block
components.html(blob_bypass_script, height=660, scrolling=False)