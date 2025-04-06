import streamlit as st
import random
from PIL import Image
import requests
from io import BytesIO

# --------------------------- CONFIG --------------------------
st.set_page_config(page_title="📚 Metaverse Book Club", layout="centered")

st.markdown("<h1 style='text-align: center;'>📚 Metaverse Book Club</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter immersive genres, AI questions & a creative journal space.</p>", unsafe_allow_html=True)

# --------------------------- GENRES --------------------------
genres = {
    "Mystery": {
        "questions": [
            "What clues were subtly placed throughout the story?",
            "Was the ending satisfying or too abrupt?",
            "Which character do you suspect the most and why?"
        ],
        "image": "https://images.pexels.com/photos/792381/pexels-photo-792381.jpeg",
        "audiobook": "https://www.youtube.com/watch?v=pKZc9iFvRF0"  # Example audiobook
    },
    "Sci-Fi": {
        "questions": [
            "Is this future believable or too distant?",
            "How do the technologies reflect human fears?",
            "Would you live in this timeline?"
        ],
        "image": "https://images.pexels.com/photos/256369/pexels-photo-256369.jpeg",
        "audiobook": "https://www.youtube.com/watch?v=8EmQFbFoK44"
    },
    "Fantasy": {
        "questions": [
            "Which magical element felt most creative?",
            "Would you ally with the protagonist or villain?",
            "How was world-building handled?"
        ],
        "image": "https://images.pexels.com/photos/417074/pexels-photo-417074.jpeg",
        "audiobook": "https://www.youtube.com/watch?v=d9Gu1PspA3Y"
    },
    "Romance": {
        "questions": [
            "Were the emotions realistic or exaggerated?",
            "Did the story rely on clichés?",
            "How did the romance evolve over time?"
        ],
        "image": "https://images.pexels.com/photos/1020895/pexels-photo-1020895.jpeg",
        "audiobook": "https://www.youtube.com/watch?v=mzo3GcGt9vU"
    },
    "Dystopian": {
        "questions": [
            "What aspect of the dystopia felt closest to reality?",
            "Could this society arise today?",
            "Who was the most rebellious character?"
        ],
        "image": "https://images.pexels.com/photos/919734/pexels-photo-919734.jpeg",
        "audiobook": "https://www.youtube.com/watch?v=OqKxMNkVHxE"
    }
}

# --------------------------- SELECT GENRE --------------------------
genre = st.selectbox("🎧 Select Book Genre", list(genres.keys()))

# --------------------------- REACTIONS --------------------------
genre_reactions = {
    "Mystery": "🕵️‍♀️ Get ready to solve some clues!",
    "Sci-Fi": "👽 Warp speed to another galaxy!",
    "Fantasy": "🧙‍♂️ Magic, dragons, and realms await!",
    "Romance": "💖 Love is in the air!",
    "Dystopian": "🔥 Brave the chaos of a crumbling world!"
}
reaction = genre_reactions.get(genre, "📚 Happy reading!")
st.markdown(f"### {reaction}")

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
    st.markdown("Unleash your imagination with a sketchpad (external tool).")
    st.markdown("[Launch Doodle Pad](https://jspaint.app) 🌐", unsafe_allow_html=True)

# --------------------------- AUDIOBOOK SECTION --------------------------
st.markdown("### 🎧 Listen to an Audiobook")
st.markdown("Here’s a sample audiobook to complement your genre:")
st.video(genres[genre]["audiobook"])

# --------------------------- GROUP DISCUSSION --------------------------
st.markdown("### 👥 Virtual Book Discussion")
st.markdown("Join a virtual room to chat with fellow book lovers!")
st.markdown("[Launch Google Meet](https://meet.google.com/) 📡", unsafe_allow_html=True)

# --------------------------- FOOTER --------------------------
st.markdown("---")
st.caption("✨ Designed for immersive & futuristic reading experiences.")
