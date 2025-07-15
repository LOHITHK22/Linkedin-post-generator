 LinkedIn Post Generator

Generate engaging, personal, and professional LinkedIn posts using Large Language Models — right from your browser.

![Demo](https://img.shields.io/badge/Built%20with-Streamlit-red?style=flat&logo=streamlit)
![LLM](https://img.shields.io/badge/Powered%20by-LangChain-blueviolet?style=flat&logo=OpenAI)

---

## 🚀 Features

- Topic-based Generation — Select from a variety of predefined tags.
- Few-shot Prompting — Posts are modeled based on real examples for higher quality.
- LLM Integration — Built on top of [LangChain](https://www.langchain.com/) + Groq LLM.
- Multi-language Support — Choose between English and Telugu (more coming soon).
- Short, Medium, or Long Posts — Adjust the length as per your tone and audience.
- Download Posts — Save your generated post with a single click.

---

💻 Demo

To run locally:

bash
# Step 1: Clone this repo
git clone https://github.com/LOHITHK22/Linkedin-post-generator.git
cd Linkedin-post-generator

# Step 2: Create & activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Create a .env file
# Add your GROQ API key like this:
# GROQ_API_KEY=your_actual_key_here

# Step 5: Run the app
streamlit run main.py
