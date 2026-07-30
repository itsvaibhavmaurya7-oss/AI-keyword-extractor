import streamlit as st
import pandas as pd
import yake

st.set_page_config(
    page_title="Keyword Extractor",
    page_icon="🔑",
    layout="wide"
)

st.title("🔑 AI Keyword Extractor")
st.write("Extract the most important keywords from your text.")

# Sidebar
st.sidebar.header("Settings")

num_keywords = st.sidebar.slider(
    "Number of Keywords",
    min_value=5,
    max_value=30,
    value=10
)

language = st.sidebar.selectbox(
    "Language",
    ["en", "hi", "fr", "de", "es"]
)

max_ngram = st.sidebar.slider(
    "Maximum Keyword Length",
    1,
    3,
    2
)

# Input option
option = st.radio(
    "Choose Input Method",
    ["Paste Text", "Upload TXT File"]
)

text = ""

if option == "Paste Text":
    text = st.text_area(
        "Enter your text",
        height=250,
        placeholder="Paste your paragraph here..."
    )

else:
    uploaded_file = st.file_uploader(
        "Upload a TXT file",
        type=["txt"]
    )

    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")

if st.button("Extract Keywords"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:

        extractor = yake.KeywordExtractor(
            lan=language,
            n=max_ngram,
            top=num_keywords
        )

        keywords = extractor.extract_keywords(text)

        df = pd.DataFrame(
            keywords,
            columns=["Keyword", "Score"]
        )

        st.success("Keywords Extracted Successfully!")

        st.subheader("Extracted Keywords")
        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "Download CSV",
            csv,
            "keywords.csv",
            "text/csv"
        )

        st.subheader("Top Keywords")

        for keyword, score in keywords:
            st.write(f"**{keyword}**  → Score: {score:.5f}")