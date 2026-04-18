import streamlit as st

st.set_page_config(page_title="AI Art Generator", layout="wide")

st.title("🎨 Instant AI Image Generator")
st.write("Professional AI Art - Fast & Free")

# Sidebar for tips
st.sidebar.header("💡 Tips for better Art")
st.sidebar.info("Use descriptive words like 'Hyper-realistic', '4k', 'Cinematic lighting', or 'Digital art'.")

# User Input
prompt = st.text_input("Enter your prompt:", placeholder="e.g. A futuristic car on Mars, high detail, 4k")

if st.button("✨ Generate Image", use_container_width=True):
    if prompt:
        with st.spinner("🎨 Creating..."):
            # We will use a more robust image engine
            # Adding a random seed automatically to avoid 'Server Busy' text
            import random
            seed = random.randint(1, 99999)
            
            # This is the direct image generation URL
            clean_prompt = prompt.replace(" ", "%20")
            image_url = f"https://image.pollinations.ai/prompt/{clean_prompt}?width=1024&height=1024&seed={seed}&nologo=true"
            
            # Instead of downloading and opening, we directly show the URL
            # Streamlit is smart enough to fetch it as an image
            try:
                st.image(image_url, caption=f"AI Generated: {prompt}", use_container_width=True)
                
                st.markdown(f"[🔗 Direct Link to Image]({image_url})")
                st.info("Right-click on the image and 'Save Image As' to download.")
                
            except Exception as e:
                st.error(f"Error: {e}. Please try a simpler prompt.")
    else:
        st.warning("Please type something first!")

st.write("---")
st.caption("Note: This uses a public AI engine. If it fails, try changing the words in your prompt.")