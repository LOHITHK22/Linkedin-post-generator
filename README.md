LinkedIn Post Generator

Generate human-like, topic-specific LinkedIn posts using LLMs like Groq's LLaMA via LangChain — all through a simple, elegant Streamlit interface.

 Features
Select a topic, length, and language
Generate posts using LangChain + Groq
Supports English and Telugu
Instant preview and copy/download options
Clean UI powered by Streamlit
How It Works
This app uses few-shot prompting to guide the LLM toward generating posts that match your selected topic and tone.

Under the hood:

LangChain routes your prompt to Groq’s LLaMA model
few_shot.py filters examples based on your selection
post_builder.py builds a prompt dynamically
llm_engine.py handles the actual LLM call
🖥️ Running Locally
1. Clone the repo
git clone https://github.com/LOHITHK22/linkedin-post-generator.git
cd linkedin-post-generator