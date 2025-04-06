import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random

# Page config
st.set_page_config(
    page_title="🎧 Metaverse Book Club by KukuFM",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Session Variables ---
if "note" not in st.session_state:
    st.session_state.note = ""
if "question" not in st.session_state:
    st.session_state.question = ""

# --- Genre-based Backgrounds ---
background_images = {
    "Fantasy": "https://images.unsplash.com/photo-1618221375018-68749dc17c5c",
    "Sci-Fi": "https://images.unsplash.com/photo-1581322333069-4e4e479d9de2",
    "Mystery": "https://images.unsplash.com/photo-1531266752238-8f129e1688ce",
    "Romance": "https://images.unsplash.com/photo-1519167811503-ec65ed9c7cdd",
    "Historical": "https://images.unsplash.com/photo-1583225272828-1cc0fbc5365c",
    "Horror": "https://images.unsplash.com/photo-1521295121783-8a321d551ad2",
    "Adventure": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
    "Dystopian": "https://images.unsplash.com/photo-1532676021073-4182b4ee8e2c",
    "Biography": "https://images.unsplash.com/photo-1609016701223-98a373fe6b37",
    "Self-help": "https://images.unsplash.com/photo-1580894894510-7e8b1f5d8d79",
}

ai_prompts = [
    "🧠 What motivates the main character right now?",
    "🌌 How does this fictional world connect with ours?",
    "💭 What symbolism do you notice in the setting?",
    "🔮 If you could ask a character one question, what would it be?",
    "📚 How would you rewrite the ending of this chapter?",
    "🤔 Which character do you relate to and why?",
    "🎭 What is the emotional tone of the chapter?",
    "🌱 What lessons can be learned from the story so far?",
]

# --- Sidebar ---
st.sidebar.title("🎨 Choose Book Genre")
genre = st.sidebar.selectbox("Select Book Genre", list(background_images.keys()))
bg_url = background_images[genre]
st.sidebar.image(bg_url, caption=f"{genre} Vibe", use_column_width=True)

# --- Main App ---
st.markdown(f"<h1 style='text-align: center;'>📚 Metaverse Book Club</h1>", unsafe_allow_html=True)
st.caption("🚀 Immerse yourself in a KukuFM-inspired AI listening and journaling experience")

# Listening Room
st.subheader("🎧 Virtual Listening Room")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# AI Prompts
st.subheader("🤖 Real-time Discussion Prompt")
col1, col2 = st.columns([1, 4])
with col1:
    if st.button("🔄 New Prompt"):
        st.session_state.question = random.choice(ai_prompts)
with col2:
    if st.session_state.question:
        st.info(st.session_state.question)

# Journal
st.subheader("📝 Private Journal (Local Only)")
note = st.text_area("Write your thoughts here...", value=st.session_state.note, height=150)
if st.button("💾 Save Note"):
    st.session_state.note = note
    st.success("Saved locally! (Session only)")

# Doodle Pad
st.subheader("🎨 Doodle Pad (sketch your ideas)")
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0.3)",
    stroke_width=3,
    stroke_color="#000000",
    background_color="#fffefc",
    update_streamlit=True,
    height=300,
    drawing_mode="freedraw",
    key="canvas"
)

# Footer
st.markdown("---")
st.caption("Made with ❤️ for KukuFM by Harshita Singh")
