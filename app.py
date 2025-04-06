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
        "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    },
    "Sci-Fi": {
        "questions": [
            "Is this future believable or too distant?",
            "How do the technologies reflect human fears?",
            "Would you live in this timeline?"
        ],
        "image": "https://images.pexels.com/photos/256369/pexels-photo-256369.jpeg",
        "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
    },
    "Fantasy": {
        "questions": [
            "Which magical element felt most creative?",
            "Would you ally with the protagonist or villain?",
            "How was world-building handled?"
        ],
        "image": "https://images.pexels.com/photos/417074/pexels-photo-417074.jpeg",
        "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"
    },
    "Romance": {
        "questions": [
            "Were the emotions realistic or exaggerated?",
            "Did the story rely on clichés?",
            "How did the romance evolve over time?"
        ],
        "image": "https://images.pexels.com/photos/1020895/pexels-photo-1020895.jpeg",
        "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"
    },
    "Dystopian": {
        "questions": [
            "What aspect of the dystopia felt closest to reality?",
            "Could this society arise today?",
            "Who was the most rebellious character?"
        ],
        "image": "https://images.pexels.com/photos/919734/pexels-photo-919734.jpeg",
        "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3"
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
    st.image(img, caption=f"{genre} mood", use_column_width=True)
except Exception as e:
    st.warning("⚠️ Couldn't load image. Try another genre.")
    st.error(str(e))

# --------------------------- AUDIOBOOK SECTION --------------------------
st.markdown("### 🎧 Audiobook Sample")
audio_url = genres[genre]["audio"]
st.audio(audio_url)

# --------------------------- AI QUESTION GENERATOR --------------------------
st.markdown("## 🤖 AI Discussion Prompt")
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

# --------------------------- VIRTUAL GROUP DISCUSSION --------------------------
st.markdown("### 👥 Virtual Group Discussion")

if "group_chat" not in st.session_state:
    st.session_state["group_chat"] = []

user_name = st.text_input("Your Name", value="Reader")
new_msg = st.text_input("Type your message and press Enter")

if new_msg:
    st.session_state["group_chat"].append(f"**{user_name}**: {new_msg}")
    st.experimental_rerun()

for msg in reversed(st.session_state["group_chat"][-10:]):
    st.markdown(msg)

# --------------------------- END --------------------------
st.markdown("---")
st.caption("✨ Designed for immersive & futuristic reading experiences.")
