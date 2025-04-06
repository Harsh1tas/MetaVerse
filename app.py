import streamlit as st
import random
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="📚 Metaverse Book Club", layout="centered")

st.markdown("<h1 style='text-align: center;'>📚 Metaverse Book Club</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter immersive genres, AI questions & a creative journal space.</p>", unsafe_allow_html=True)


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


# --------------------------- GENRES --------------------------
genres = {
    "Mystery": {
        "questions": [
            "What clues were subtly placed throughout the story?",
            "Was the ending satisfying or too abrupt?",
            "Which character do you suspect the most and why?"
        ],
        "image": "https://images.pexels.com/photos/792381/pexels-photo-792381.jpeg"
    },
    "Sci-Fi": {
        "questions": [
            "Is this future believable or too distant?",
            "How do the technologies reflect human fears?",
            "Would you live in this timeline?"
        ],
        "image": "https://images.pexels.com/photos/256369/pexels-photo-256369.jpeg"
    },
    "Fantasy": {
        "questions": [
            "Which magical element felt most creative?",
            "Would you ally with the protagonist or villain?",
            "How was world-building handled?"
        ],
        "image": "https://images.pexels.com/photos/417074/pexels-photo-417074.jpeg"
    },
    "Romance": {
        "questions": [
            "Were the emotions realistic or exaggerated?",
            "Did the story rely on clichés?",
            "How did the romance evolve over time?"
        ],
        "image": "https://images.pexels.com/photos/1020895/pexels-photo-1020895.jpeg"
    },
    "Dystopian": {
        "questions": [
            "What aspect of the dystopia felt closest to reality?",
            "Could this society arise today?",
            "Who was the most rebellious character?"
        ],
        "image": "https://images.pexels.com/photos/919734/pexels-photo-919734.jpeg"
    }
}

# --------------------------- SELECT GENRE --------------------------
genre = st.selectbox("🎧 Select Book Genre", list(genres.keys()))

# --------------------------- BACKGROUND IMAGE --------------------------
st.markdown(f"### 🌌 {genre} Book Vibe")

try:
    img_url = genres[genre]["image"]
    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))
    st.image(img, caption=f"{genre} mood", width=700)
except Exception as e:
    st.warning("⚠️ Couldn't load image. Try another genre.")
    st.error(str(e))

# --------------------------- AI QUESTION --------------------------
st.markdown("### 🤖 AI Prompted Discussion")
question = random.choice(genres[genre]["questions"])
st.success(f"💬 {question}")

# --------------------------- JOURNAL PAD --------------------------
st.markdown("### 📝 Private Journal Pad")

default_notes = st.session_state.get("notes", "")
notes = st.text_area("Write your reflections or insights...", value=default_notes, height=200)

if st.button("💾 Save Thoughts"):
    st.session_state["notes"] = notes
    st.success("Saved locally in session.")

# --------------------------- CONDITIONAL DOODLE --------------------------
if genre in ["Fantasy", "Sci-Fi", "Mystery"]:
    st.markdown("### 🎨 Doodle Pad (Genre-Based Unlock)")
    st.markdown("Unleash your imagination with a simple sketchpad (external).")
    st.markdown("[Launch Doodle Pad](https://jspaint.app) 🌐", unsafe_allow_html=True)

st.markdown("---")
st.caption("✨ Designed for immersive & futuristic reading experiences.")
