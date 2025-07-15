import streamlit as st
from data_selector import FewShotPosts
from post_builder import generate_post

# App config
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="✍️", layout="centered")

# Options
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# Main layout
def main():
    st.markdown("""
    <h1 style='text-align: center;'>✍️ LinkedIn Post Generator</h1>
    <p style='text-align: center; font-size: 18px;'>Generate content inspired by your own style using LLMs 🤖</p>
    <hr>
    """, unsafe_allow_html=True)

    fs = FewShotPosts()
    tags = fs.get_tags()

    # User inputs
    selected_tag = st.selectbox("📌 Select a topic", options=tags)
    selected_length = st.selectbox("📝 Select post length", options=length_options)
    selected_language = st.selectbox("🌐 Select language", options=language_options)

    st.markdown("---")

    # Generate button
    if st.button("🚀 Generate Post"):
        with st.spinner("Crafting your post..."):
            post = generate_post(selected_length, selected_language, selected_tag)
            st.success("Post generated successfully!")
            st.text_area("🧠 Your Generated Post", value=post, height=250)

            # Copy button
            st.code(post, language='markdown')

            # Download button
            st.download_button(
                label="💾 Download as .txt",
                data=post,
                file_name="linkedin_post.txt",
                mime="text/plain"
            )

    # Footer
    st.markdown("""
    <hr>
    <div style='text-align: center;'>
        <p>Built with ❤️ using Streamlit & LangChain | <a href="https://github.com/YOUR_GITHUB" target="_blank">View on GitHub</a></p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
