from transformers import pipeline
import streamlit as st

# Load the summarization pipeline
try:
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
except Exception as e:
    st.error(f"Error loading summarization model: {e}")
    st.stop()

# Function to summarize text
def summarize_text(text, max_length=130, min_length=30, do_sample=False):
    try:
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
        return summary[0]['summary_text']
    except Exception as e:
        st.error(f"Error during summarization: {e}")
        return ""

# Set the title and add an image
st.set_page_config(page_title="AI Text Summarizer", page_icon="📝")
st.image("https://source.unsplash.com/random/800x200?text", use_column_width=True)

# Sidebar for customization
st.sidebar.header("Customize Summary")
max_length = st.sidebar.slider("Max Length of Summary", 50, 300, 130, 10)
min_length = st.sidebar.slider("Min Length of Summary", 10, 100, 30, 5)
do_sample = st.sidebar.checkbox("Use Sampling", False)

# Main interface
st.title("AI Text Summarizer 📝")
st.markdown(
    """
    <style>
    .summary-box {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.write(
    "Welcome to the AI Text Summarizer! Paste your text below, adjust the settings in the sidebar, and click **Summarize** to see a concise summary."
)

# Input text
input_text = st.text_area("Enter the text to summarize", height=200)

# Summarize button
if st.button("Summarize"):
    if input_text:
        summary = summarize_text(input_text, max_length=max_length, min_length=min_length, do_sample=do_sample)
        if summary:
            st.markdown("**Summary:**", unsafe_allow_html=True)
            st.markdown(f'<div class="summary-box">{summary}</div>', unsafe_allow_html=True)
    else:
        st.error("Please enter some text to summarize.")
else:
    st.write("Enter the text and press **Summarize** to generate a summary.")

# Footer
st.markdown("---")
st.markdown("**Developed with ❤️ using Hugging Face Transformers and Streamlit**")
