import streamlit as st
import random
from PIL import Image
import requests
from io import BytesIO

# --------------------------- CONFIG --------------------------
st.set_page_config(page_title="Metaverse Book Club", layout="centered")
st.markdown("<h1 style='text-align: center;'>📚 Metaverse Book Club</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>A futuristic listening room with AI prompts and visual journaling.</p>", unsafe_allow_html=True)

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

# Load background image
image_url = genres[genre]["image"]
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))

st.image(img, caption=f"{genre} Book Vibe", use_column_width=True)

# --------------------------- AI QUESTION GENERATOR --------------------------
st.markdown("## 🤖 AI Discussion Prompt")

question = random.choice(genres[genre]["questions"])
st.success(f"💬 {question}")

# --------------------------- SKETCHPAD / JOURNAL PAD --------------------------
st.markdown("## 🖌️ Private Doodle / Journal Pad")

default_notes = st.session_state.get("notes", "")
notes = st.text_area("Write or doodle your thoughts privately here...", value=default_notes, height=200)

if st.button("💾 Save"):
    st.session_state["notes"] = notes
    st.success("Saved in session (local only).")

# --------------------------- END --------------------------
st.markdown("---")
st.caption("✨ Designed for immersive and introspective reading experiences.")
