import streamlit as st
from google import genai

# Page setup
st.set_page_config(page_title="AI Chat", layout="wide", initial_sidebar_state="collapsed")

# Gemini client replace with your API key
client = genai.Client(api_key="your api key here")

# 🎨 Aesthetic dark UI
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #09090b;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #e4e4e7;
}

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 0;
    max-width: 740px;
}

[data-testid="stBottomBlockContainer"] {
    background: linear-gradient(to top, #09090b 80%, transparent);
    border-top: none;
    padding-top: 20px;
    padding-bottom: 20px;
}

/* Animations */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

@keyframes pulse-dot {
    0%, 80%, 100% { opacity: 0.3; transform: scale(0.8); }
    40% { opacity: 1; transform: scale(1); }
}

/* User message */
.msg-user {
    max-width: 70%;
    margin-left: auto;
    padding: 14px 20px;
    border-radius: 20px 20px 6px 20px;
    background: linear-gradient(135deg, #27272a, #1e1e22);
    color: #fafafa;
    margin-bottom: 16px;
    animation: fadeUp 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    font-size: 14.5px;
    line-height: 1.6;
    border: 1px solid rgba(255,255,255,0.04);
    box-shadow: 0 2px 12px rgba(0,0,0,0.3);
}

/* AI message */
.msg-ai {
    width: 100%;
    padding: 22px 26px;
    background: linear-gradient(135deg, #111113, #0f0f12);
    color: #d4d4d8;
    border-radius: 20px;
    margin-bottom: 20px;
    animation: fadeUp 0.45s cubic-bezier(0.16, 1, 0.3, 1);
    line-height: 1.75;
    font-size: 14.5px;
    border: 1px solid rgba(255,255,255,0.03);
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    position: relative;
}

.msg-ai::before {
    content: '';
    position: absolute;
    top: 14px;
    left: 14px;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #22c55e;
    box-shadow: 0 0 8px rgba(34, 197, 94, 0.4);
}

.msg-ai-inner {
    padding-left: 16px;
}

/* Code blocks */
.msg-ai code {
    background-color: #1c1c1f;
    padding: 3px 7px;
    border-radius: 5px;
    font-size: 13px;
    color: #a1a1aa;
    font-family: 'SF Mono', 'Fira Code', monospace;
}

.msg-ai pre {
    background-color: #111113;
    padding: 16px;
    border-radius: 12px;
    overflow-x: auto;
    border: 1px solid rgba(255,255,255,0.05);
    margin: 12px 0;
}

/* Hover effects */
.msg-user:hover {
    background: linear-gradient(135deg, #2d2d31, #242428);
    transition: all 0.3s ease;
    transform: translateY(-1px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.4);
}

/* Input styling */
[data-testid="stChatInput"] {
    max-width: 740px;
    margin: 0 auto;
}

textarea {
    border-radius: 18px !important;
    background-color: #111113 !important;
    color: #e4e4e7 !important;
    border: 1px solid #27272a !important;
    padding: 14px 20px !important;
    font-size: 14.5px !important;
    font-family: 'Inter', sans-serif !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 2px 12px rgba(0,0,0,0.2) !important;
}

textarea:focus {
    border-color: #3f3f46 !important;
    box-shadow: 0 0 0 3px rgba(63,63,70,0.2), 0 4px 20px rgba(0,0,0,0.3) !important;
    background-color: #131315 !important;
}

textarea::placeholder {
    color: #52525b !important;
    font-weight: 300 !important;
}

/* Send button */
[data-testid="stChatInputSubmitButton"] {
    border-radius: 14px !important;
    background: linear-gradient(135deg, #fafafa, #d4d4d8) !important;
    color: #09090b !important;
    border: none !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
}

[data-testid="stChatInputSubmitButton"]:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.4) !important;
}

[data-testid="stChatInputSubmitButton"] svg {
    fill: #09090b !important;
}

/* Hide branding */
#MainMenu, footer, header { visibility: hidden; }

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #27272a; border-radius: 2px; }

/* Empty state */
.empty-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 65vh;
    gap: 12px;
    animation: fadeUp 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.empty-icon {
    width: 48px;
    height: 48px;
    border-radius: 16px;
    background: linear-gradient(135deg, #18181b, #111113);
    border: 1px solid rgba(255,255,255,0.05);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    margin-bottom: 8px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

.empty-title {
    color: #a1a1aa;
    font-size: 16px;
    font-weight: 400;
    letter-spacing: -0.01em;
}

.empty-sub {
    color: #3f3f46;
    font-size: 13px;
    font-weight: 300;
}

/* Spinner override */
[data-testid="stSpinner"] {
    color: #52525b !important;
}
</style>
""", unsafe_allow_html=True)

#  Chat state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render messages
if not st.session_state.messages:
    st.markdown("""
    <div class="empty-state">
        <div class="empty-icon">✦</div>
        <div class="empty-title">What can I help you with?</div>
        <div class="empty-sub">Ask anything — I'm ready when you are.</div>
    </div>
    """, unsafe_allow_html=True)
else:
    for role, msg in st.session_state.messages:
        if role == "user":
            st.markdown(f'<div class="msg-user">{msg}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="msg-ai"><div class="msg-ai-inner">{msg}</div></div>', unsafe_allow_html=True)

# Input
user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.messages.append(("user", user_input))

    with st.spinner("Thinking..."):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input,
        )

    st.session_state.messages.append(("ai", response.text))
    st.rerun()
