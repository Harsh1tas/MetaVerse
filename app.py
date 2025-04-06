import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random

st.set_page_config(
    page_title="📚 Metaverse Book Club",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session states
if "note" not in st.session_state:
    st.session_state.note = ""
if "question" not in st.session_state:
    st.session_state.question = ""
if "canvas_data" not in st.session_state:
    st.session_state.canvas_data = None

# Sample AI-generated prompts
ai_prompts = [
    "🧠 What motivates the main character right now?",
    "🌌 How does this fictional world connect with ours?",
    "💭 What symbolism do you notice in the setting?",
    "🔮 If you could ask a character one question, what would it be?",
    "📚 How would you rewrite the ending of this chapter?"
]

# Sample AI-art backdrops (you can add your own URLs)
background_images = {
    "Fantasy": "https://images.unsplash.com/photo-1581091012184-7f1c7f3a87a7",
    "Sci-Fi": "https://images.unsplash.com/photo-1581322333069-4e4e479d9de2",
    "Mystery": "https://images.unsplash.com/photo-1519985176271-adb1088fa94c",
}

# Sidebar
st.sidebar.title("🎨 Backdrop Selector")
genre = st.sidebar.selectbox("Select Book Genre", list(background_images.keys()))
bg_url = background_images[genre]

# Display background image
st.image(bg_url, caption=f"{genre} World", use_column_width=True)

# App Title
st.title("📚 Metaverse Book Club")
st.caption("An immersive, AI-powered listening and journaling experience")

# Audio Player
st.subheader("🎧 Virtual Listening Room")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# Real-time AI Question
st.subheader("🤖 AI-Generated Real-time Question")
if st.button("🔄 Generate Question"):
    st.session_state.question = random.choice(ai_prompts)
if st.session_state.question:
    st.info(st.session_state.question)

# Notes Section
st.subheader("📝 Private Journal")
note = st.text_area("Your thoughts while listening...", value=st.session_state.note, height=150)
if st.button("💾 Save Note"):
    st.session_state.note = note
    st.success("Saved in session!")

# Sketchpad
st.subheader("🎨 AI-Augmented Doodle Pad")
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0.3)",
    stroke_width=3,
    stroke_color="#000000",
    background_color="#f0f0f0",
    update_streamlit=True,
    height=300,
    drawing_mode="freedraw",
    key="canvas"
)
