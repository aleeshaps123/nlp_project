from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def summarize_text(text, max_length=130, min_length=30, do_sample=False):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
    return summary[0]['summary_text']


import streamlit as st

st.title("Text Summarizer")

# Input text
input_text = st.text_area("Enter the text to summarize")

# Summarize button
if st.button("Summarize"):
    if input_text:
        summary = summarize_text(input_text)
        st.write("**Summary:**", summary)
    else:
        st.write("Please enter some text to summarize.")

