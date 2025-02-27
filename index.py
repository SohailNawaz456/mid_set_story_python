import streamlit as st

# Streamlit app title
st.title("🎭 Mad Libs Game in Python")

# Taking user input through Streamlit
name = st.text_input("Enter the boy's name:")
programming_language = st.text_input("Enter a programming language (e.g., Python, Next.js, TypeScript, HTML, CSS):")
mentor = st.text_input("Enter a mentor's name:")
location = st.text_input("Enter a location:")

# Display the story when all inputs are filled
if name and programming_language and mentor and location:
    st.markdown("## 📖 Here is your Mad Libs Story!")
    st.markdown(f"🧒 Once upon a time, there was a boy named **{name}**.")
    st.markdown(f"🤔 **{name}** was very curious and always wanted to learn new things! 💡")
    st.markdown(f"📚 One day, he decided to learn **{programming_language}** at **{location}**! 🏛️")
    st.markdown(f"🎓 Luckily, **{name}** found a great mentor named **{mentor}** who was an expert in **{programming_language}**. 👨‍🏫")
    st.markdown("🚀 And so, his journey continues...! ✨")

# Footer
st.markdown("<div style='text-align: center; margin-top: 50px; font-size: 14px;'> Created with ❤️ by Sohail Nawaz </div>", unsafe_allow_html=True)
