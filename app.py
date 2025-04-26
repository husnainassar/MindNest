import streamlit as st
import openai

# Load OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Streamlit page configuration
st.set_page_config(page_title="MindNest", layout="centered")
st.title("🧠 MindNest - Story Generator for Kids")
st.subheader("Let your imagination come to life!")

# Prompt input
prompt = st.text_input("Enter a fun idea for a story", "A robot who learns ballet")

if st.button("Generate Story"):
    with st.spinner("Creating your story..."):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Write a fun, 3-sentence story for kids based on: {prompt}"}
            ]
        )
        story = response.choices[0].message.content.strip()
        st.success("Here’s your story!")
        st.markdown("### 📖 Story")
        st.write(story)
