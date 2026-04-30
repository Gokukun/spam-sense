import streamlit as st
import pickle

st.set_page_config(
    page_title="SpamSense",
    page_icon="🛡️",
    layout="centered"
)

@st.cache_resource
def load_model():
    with open("spam_detection.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main-card {
    background: #161b22;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 0 25px rgba(0,0,0,0.4);
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    background: linear-gradient(90deg,#00c6ff,#0072ff);
    -webkit-background-clip: text;
    color: transparent;
}
.subtitle {
    text-align: center;
    color: #9ba3af;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🛡️ SpamSense</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-powered Spam Message Detection</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)

    user_input = st.text_area(
        "✉️ Enter your message",
        height=150,
        placeholder="Type or paste your message here..."
    )

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        predict = st.button("🔍 Analyze Message", use_container_width=True)

    if predict:
        if user_input.strip():
            prediction = model.predict([user_input])[0]
            if prediction == "spam":
                st.error("🚨 **SPAM DETECTED**\n\nThis message looks suspicious.")
            else:
                st.success("✅ **SAFE MESSAGE**\n\nThis message is not spam.")
        else:
            st.warning("⚠️ Please enter a message first.")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center;color:#6b7280;margin-top:20px;'>Built with ❤️ using Streamlit & ML</p>",
    unsafe_allow_html=True
)
