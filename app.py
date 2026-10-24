
import streamlit as st
from transformers import pipeline

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="IntelliText AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS - COLOURFUL DASHBOARD
# ==========================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f1029, #1e1b4b, #312e81);
    color: white;
}
[data-testid="stHeader"] {
    background: transparent;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #171538, #312e81);
    border-right: 1px solid #6366f1;
}
[data-testid="stSidebar"] * {
    color: white !important;
}
.main-title {
    font-size: 46px;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(90deg, #22d3ee, #c084fc, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    padding: 10px;
}
.subtitle {
    text-align: center;
    color: #d1d5db;
    font-size: 18px;
    margin-bottom: 30px;
}
.feature-card {
    background: linear-gradient(135deg, #312e81, #4c1d95);
    border: 1px solid #818cf8;
    border-radius: 18px;
    padding: 22px;
    min-height: 155px;
    margin-bottom: 15px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.20);
}
.feature-card h3 {
    color: #67e8f9;
    margin-bottom: 10px;
}
.feature-card p {
    color: #e5e7eb;
    font-size: 15px;
}
.section-title {
    color: #67e8f9;
    font-size: 28px;
    font-weight: bold;
    margin-top: 15px;
}
.result-card {
    background: linear-gradient(135deg, #164e63, #312e81);
    border: 1px solid #22d3ee;
    border-radius: 15px;
    padding: 22px;
    margin-top: 20px;
    color: white;
}
.stButton > button {
    background: linear-gradient(90deg, #7c3aed, #db2777);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 24px;
    font-weight: bold;
    width: 100%;
    transition: 0.3s;
}
.stButton > button:hover {
    background: linear-gradient(90deg, #0891b2, #7c3aed);
    color: white;
    border: 1px solid #67e8f9;
}
.stTextArea textarea, .stTextInput input {
    background-color: #f8fafc;
    color: #111827;
    border-radius: 10px;
}
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #312e81, #581c87);
    border: 1px solid #818cf8;
    padding: 18px;
    border-radius: 15px;
}
div[data-testid="stMetric"] label {
    color: #c4b5fd !important;
}
div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: #67e8f9 !important;
}
hr {
    border-color: #6366f1;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# MODEL LOADING
# ==========================================
@st.cache_resource
def load_summarizer():
    return pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )


@st.cache_resource
def load_translator():
    return pipeline(
        "translation_en_to_fr",
        model="Helsinki-NLP/opus-mt-en-fr"
    )


@st.cache_resource
def load_sentiment():
    return pipeline(
        "sentiment-analysis",
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    )


@st.cache_resource
def load_qa():
    return pipeline(
        "question-answering",
        model="distilbert/distilbert-base-cased-distilled-squad"
    )


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
with st.sidebar:
    st.markdown("# ✨ IntelliText AI")
    st.markdown("---")
    st.markdown("### 🧭 Navigation")

    page = st.radio(
        "Choose a feature",
        [
            "🏠 Home Dashboard",
            "📝 Text Summarization",
            "🌍 Language Translation",
            "😊 Sentiment Analysis",
            "❓ Question Answering"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("### 🤖 Technology")
    st.markdown("💜 Hugging Face")
    st.markdown("💙 Transformers")
    st.markdown("🩷 Streamlit")
    st.markdown("💚 Python")
    st.markdown("---")
    st.caption("LLM Week 7 Project")
    st.caption("Made with ❤️ using AI")


# ==========================================
# HOME DASHBOARD
# ==========================================
if page == "🏠 Home Dashboard":

    st.markdown(
        '<div class="main-title">✨ IntelliText AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Your Smart AI-Powered Language & Text Assistant'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="result-card">
        <h2>👋 Welcome to IntelliText AI!</h2>
        <p>
        Explore the power of Artificial Intelligence with four
        intelligent NLP tools. Summarize long documents, translate
        languages, analyze sentiment, and find answers from text.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📝 AI Tools", "04")

    with col2:
        st.metric("🌍 Translation", "EN → FR")

    with col3:
        st.metric("😊 Sentiments", "2 Classes")

    with col4:
        st.metric("🤖 Platform", "Hugging Face")

    st.markdown(
        '<div class="section-title">🚀 Explore AI Features</div>',
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>📝 Text Summarization</h3>
            <p>Convert long paragraphs into short,
            meaningful summaries using AI.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
            <h3>😊 Sentiment Analysis</h3>
            <p>Discover whether a sentence or review
            expresses positive or negative sentiment.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🌍 Language Translation</h3>
            <p>Translate English text into French
            using a pretrained translation model.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
            <h3>❓ Question Answering</h3>
            <p>Ask questions and find answers
            directly from the context you provide.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info(
        "👈 Select an AI feature from the sidebar to get started. "
        "The first use of each feature may take time while its model loads."
    )


# ==========================================
# TEXT SUMMARIZATION
# ==========================================
elif page == "📝 Text Summarization":

    st.markdown(
        '<div class="main-title">📝 Text Summarization</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Transform lengthy text into concise summaries</div>',
        unsafe_allow_html=True
    )

    text = st.text_area(
        "📄 Enter your text",
        height=230,
        placeholder="Paste your paragraph or article here..."
    )

    if st.button("✨ Generate Summary"):

        if len(text.split()) < 10:
            st.warning("Please enter at least 10 words to summarize.")

        else:
            try:
                with st.spinner("🤖 AI is generating your summary..."):
                    summarizer = load_summarizer()

                    result = summarizer(
                        text,
                        max_length=100,
                        min_length=15,
                        do_sample=False,
                        truncation=True
                    )

                st.markdown(
                    '<div class="result-card">'
                    '<h3>✨ Generated Summary</h3></div>',
                    unsafe_allow_html=True
                )

                st.success(result[0]["summary_text"])

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Original Words", len(text.split()))

                with col2:
                    st.metric(
                        "Summary Words",
                        len(result[0]["summary_text"].split())
                    )

            except Exception as e:
                st.error(f"Unable to summarize: {e}")


# ==========================================
# LANGUAGE TRANSLATION
# ==========================================
elif page == "🌍 Language Translation":

    st.markdown(
        '<div class="main-title">🌍 Language Translation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Translate English sentences into French with AI</div>',
        unsafe_allow_html=True
    )

    st.markdown("### 🇬🇧 English Input")

    text = st.text_area(
        "Enter English text",
        height=170,
        placeholder="Artificial intelligence is changing the world."
    )

    if st.button("🌐 Translate Text"):

        if text.strip():
            try:
                with st.spinner("🌍 Translating your text..."):
                    translator = load_translator()
                    result = translator(text, truncation=True)

                st.markdown(
                    '<div class="result-card">'
                    '<h3>🇫🇷 French Translation</h3></div>',
                    unsafe_allow_html=True
                )

                st.success(result[0]["translation_text"])

            except Exception as e:
                st.error(f"Translation failed: {e}")

        else:
            st.warning("Please enter English text first.")


# ==========================================
# SENTIMENT ANALYSIS
# ==========================================
elif page == "😊 Sentiment Analysis":

    st.markdown(
        '<div class="main-title">😊 Sentiment Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Understand the emotion behind your text</div>',
        unsafe_allow_html=True
    )

    text = st.text_area(
        "💬 Enter a review or sentence",
        height=150,
        placeholder="I love this product. It is amazing!"
    )

    if st.button("🔍 Analyze Sentiment"):

        if text.strip():
            try:
                with st.spinner("🧠 Analyzing sentiment..."):
                    analyzer = load_sentiment()
                    result = analyzer(text)

                label = result[0]["label"]
                score = result[0]["score"]

                st.markdown(
                    '<div class="result-card">'
                    '<h3>📊 Analysis Result</h3></div>',
                    unsafe_allow_html=True
                )

                col1, col2 = st.columns(2)

                with col1:
                    if label == "POSITIVE":
                        st.success("😊 POSITIVE SENTIMENT")
                    else:
                        st.error("😞 NEGATIVE SENTIMENT")

                with col2:
                    st.metric("Confidence Score", f"{score:.2%}")

                st.progress(float(score))

                st.caption(
                    "The confidence score is the model's estimate, "
                    "not a guarantee that the prediction is correct."
                )

            except Exception as e:
                st.error(f"Analysis failed: {e}")

        else:
            st.warning("Please enter some text to analyze.")


# ==========================================
# QUESTION ANSWERING
# ==========================================
elif page == "❓ Question Answering":

    st.markdown(
        '<div class="main-title">❓ Question Answering</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Ask questions and get answers from your text</div>',
        unsafe_allow_html=True
    )

    context = st.text_area(
        "📚 Enter the context",
        height=220,
        value=(
            "Python is a popular programming language created by "
            "Guido van Rossum. It is widely used in web development, "
            "data science, artificial intelligence, and machine "
            "learning. Python is known for its simple syntax and readability."
        )
    )

    question = st.text_input(
        "❓ Ask a question",
        placeholder="Who created Python?"
    )

    if st.button("💡 Find Answer"):

        if context.strip() and question.strip():
            try:
                with st.spinner("🔎 Finding the answer..."):
                    qa = load_qa()
                    result = qa(question=question, context=context)

                st.markdown(
                    '<div class="result-card">'
                    '<h3>💡 Answer</h3></div>',
                    unsafe_allow_html=True
                )

                st.success(result["answer"])

                st.metric(
                    "Answer Confidence",
                    f'{result["score"]:.2%}'
                )

            except Exception as e:
                st.error(f"Question answering failed: {e}")

        else:
            st.warning("Please enter both the context and question.")


# ==========================================
# FOOTER
# ==========================================
st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#c4b5fd; padding:15px;">
        <h4>✨ IntelliText AI</h4>
        <p>Smart Language & Text Assistant</p>
        <p>Powered by Python • Streamlit • Hugging Face</p>
        <p>LLM Week 7 Project</p>
    </div>
    """,
    unsafe_allow_html=True
)
