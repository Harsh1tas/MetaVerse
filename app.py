import streamlit as st
import random

st.set_page_config(page_title="Metaverse Book Club", layout="centered")

st.title("📖 Metaverse Book Club")
st.markdown("A virtual, immersive listening & journaling experience.")

# ------------------- Sidebar -------------------
st.sidebar.header("Select Book Genre")

# Predefined genres and corresponding image backgrounds
background_images = {
    "Fantasy": "https://images.pexels.com/photos/35600/road-sun-rays-path.jpg",
    "Sci-Fi": "https://images.pexels.com/photos/256369/pexels-photo-256369.jpeg",
    "Mystery": "https://images.pexels.com/photos/792381/pexels-photo-792381.jpeg",
    "Romance": "https://images.pexels.com/photos/1020895/pexels-photo-1020895.jpeg",
    "Historical": "https://images.pexels.com/photos/698500/pexels-photo-698500.jpeg",
    "Horror": "https://images.pexels.com/photos/167964/pexels-photo-167964.jpeg",
    "Adventure": "https://images.pexels.com/photos/1125274/pexels-photo-1125274.jpeg",
    "Dystopian": "https://images.pexels.com/photos/919734/pexels-photo-919734.jpeg",
    "Biography": "https://images.pexels.com/photos/2376751/pexels-photo-2376751.jpeg",
    "Self-help": "https://images.pexels.com/photos/694740/pexels-photo-694740.jpeg"
}

genre = st.sidebar.selectbox("Choose your genre", list(background_images.keys()))
bg_url = background_images[genre]
st.sidebar.image(bg_url, caption=f"{genre} Vibe", use_column_width=True)

# ------------------- GPT-powered Questions -------------------
st.subheader("🤖 Real-time Book Discussion Questions")

question_bank = {
    "Fantasy": [
        "What magical element intrigued you the most?",
        "Would you live in this fantasy world?",
        "Which mythical character stood out?"
    ],
    "Sci-Fi": [
        "Is the technology believable?",
        "How does the setting reflect society?",
        "Could this be Earth’s future?"
    ],
    "Mystery": [
        "What clues were hidden in plain sight?",
        "Did you predict the twist?",
        "Who is the most suspicious character?"
    ],
    "Romance": [
        "How authentic was the chemistry?",
        "Were the love conflicts relatable?",
        "Would you root for the couple?"
    ],
    "Historical": [
        "Did it align with real history?",
        "What was the most surprising historical detail?",
        "Did it inspire you to learn more?"
    ],
    "Horror": [
        "What moment chilled you the most?",
        "Was the fear psychological or supernatural?",
        "Did you feel immersed in the horror setting?"
    ],
    "Adventure": [
        "What was the most thrilling moment?",
        "Would you survive the same journey?",
        "Did the pacing enhance the excitement?"
    ],
    "Dystopian": [
        "What’s the scariest part of the world built?",
        "Could this dystopia happen in real life?",
        "Who rebelled best against the system?"
    ],
    "Biography": [
        "What inspired you the most about their life?",
        "Were there moments you related to?",
        "How would you summarize their legacy?"
    ],
    "Self-help": [
        "Which tip felt most useful to you?",
        "Would you recommend this to a friend?",
        "What mindset shift did this book encourage?"
    ]
}

if genre in question_bank:
    question = random.choice(question_bank[genre])
    st.info(f"💬 **Discussion Question:** {question}")

# ------------------- Doodle/Journal Pad -------------------
st.subheader("🖋️ Your Private Doodle/Journal Pad")

default_notes = st.session_state.get("user_notes", "")

user_notes = st.text_area("Write your thoughts, ideas, or doodles here...", value=default_notes, height=250)

if st.button("💾 Save Notes"):
    st.session_state.user_notes = user_notes
    st.success("Notes saved for this session!")

# ------------------- Background Preview -------------------
st.markdown("---")
st.markdown(f"### 🌌 Visual Vibe: {genre}")
st.image(bg_url, use_column_width=True)
