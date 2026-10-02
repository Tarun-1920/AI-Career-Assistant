import streamlit as st
from backend.gemini_client import ask_gemini


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Career Chat",
    page_icon="💬",
    layout="wide"
)


# =========================================================
# GLOBAL CSS
# =========================================================

st.html("""
<style>

/* ========================================================
   MAIN APPLICATION
   ======================================================== */

.stApp {
    background: #f7f8fc;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* ========================================================
   HIDE DEFAULT NAVIGATION
   ======================================================== */

[data-testid="stSidebarNav"] {
    display: none !important;
}


/* ========================================================
   SIDEBAR
   ======================================================== */

[data-testid="stSidebar"] {
    background: #111827 !important;
    border-right: 1px solid #1f2937;
}


/* ========================================================
   SIDEBAR BRAND
   ======================================================== */

.sidebar-brand {
    text-align: center;
    padding: 18px 8px 25px;
}

.sidebar-logo {
    width: 58px;
    height: 58px;

    margin: 0 auto 14px auto;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #2563eb;
    border-radius: 14px;

    color: #ffffff !important;
    font-size: 19px;
    font-weight: 800;
    letter-spacing: 1px;

    box-shadow: 0 8px 20px rgba(37, 99, 235, 0.25);
}

.sidebar-title {
    color: #ffffff !important;
    font-size: 20px;
    font-weight: 700;
    line-height: 1.3;
}

.sidebar-subtitle {
    color: #9ca3af !important;
    font-size: 12px;
    margin-top: 7px;
}


/* ========================================================
   SIDEBAR NAVIGATION
   ======================================================== */

.sidebar-nav-title {
    color: #9ca3af !important;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.2px;
    padding: 6px 12px 10px;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] {
    margin: 3px 0;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a {
    color: #e5e7eb !important;
    background: transparent !important;

    border-radius: 9px !important;

    padding: 10px 12px !important;

    min-height: 42px;

    font-size: 14px !important;
    font-weight: 500 !important;

    text-decoration: none !important;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a span {
    color: #e5e7eb !important;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a svg {
    color: #93c5fd !important;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {
    background: #1f2937 !important;
    color: #ffffff !important;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover span {
    color: #ffffff !important;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover svg {
    color: #60a5fa !important;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a[aria-current="page"] {
    background: #273449 !important;
    color: #ffffff !important;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a[aria-current="page"] span {
    color: #ffffff !important;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a[aria-current="page"] svg {
    color: #60a5fa !important;
}

[data-testid="stSidebar"] hr {
    border-color: #273244 !important;
    margin: 15px 0;
}


/* ========================================================
   POWERED BY
   ======================================================== */

.sidebar-powered {
    text-align: center;
    padding: 12px 5px;
}

.powered-label {
    color: #6b7280;
    font-size: 9px;
    letter-spacing: 1px;
    margin-bottom: 4px;
}

.powered-name {
    color: #dbeafe;
    font-size: 13px;
    font-weight: 700;
}


/* ========================================================
   PAGE HEADER
   ======================================================== */

.page-header {
    background: linear-gradient(
        135deg,
        #111827 0%,
        #1e3a8a 100%
    );

    border-radius: 24px;

    padding: 40px;

    margin-bottom: 28px;

    box-shadow:
        0 12px 30px rgba(15, 23, 42, 0.10);
}

.page-label {
    color: #bfdbfe;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 10px;
}

.page-title {
    color: #ffffff;
    font-size: 36px;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 10px;
}

.page-description {
    color: #dbeafe;
    font-size: 15px;
    line-height: 1.7;
    max-width: 760px;
}


/* ========================================================
   INFORMATION CARDS
   ======================================================== */

.info-card {
    background: #ffffff;

    border: 1px solid #e5e7eb;

    border-radius: 17px;

    padding: 22px;

    min-height: 135px;

    box-shadow:
        0 5px 18px rgba(15, 23, 42, 0.04);
}

.info-icon {
    font-size: 26px;
    margin-bottom: 9px;
}

.info-title {
    color: #111827;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 6px;
}

.info-description {
    color: #6b7280;
    font-size: 12px;
    line-height: 1.55;
}


/* ========================================================
   CHAT AREA
   ======================================================== */

.chat-section-title {
    color: #111827;
    font-size: 24px;
    font-weight: 750;

    margin-top: 32px;
    margin-bottom: 5px;
}

.chat-section-description {
    color: #6b7280;
    font-size: 13px;
    margin-bottom: 15px;
}


/* ========================================================
   EMPTY CHAT
   ======================================================== */

.empty-chat {
    background: #ffffff;

    border: 1px solid #e5e7eb;

    border-radius: 20px;

    padding: 55px 25px;

    margin-top: 20px;

    text-align: center;

    box-shadow:
        0 5px 18px rgba(15, 23, 42, 0.04);
}

.empty-chat-icon {
    font-size: 48px;
    margin-bottom: 14px;
}

.empty-chat-title {
    color: #111827;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 8px;
}

.empty-chat-description {
    color: #6b7280;
    font-size: 13px;
    line-height: 1.6;

    max-width: 600px;

    margin: auto;
}


/* ========================================================
   CHAT MESSAGES
   ======================================================== */

[data-testid="stChatMessage"] {
    border-radius: 14px;
}


/* ========================================================
   FOOTER
   ======================================================== */

.page-footer {
    text-align: center;

    color: #9ca3af;

    font-size: 12px;

    margin-top: 40px;

    padding: 20px;
}

</style>
""")


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    # -----------------------------------------------------
    # BRAND
    # -----------------------------------------------------

    st.html("""
    <div class="sidebar-brand">

        <div class="sidebar-logo">
            AI
        </div>

        <div class="sidebar-title">
            AI Career Assistant
        </div>

        <div class="sidebar-subtitle">
            Your AI-powered career companion
        </div>

    </div>
    """)

    st.divider()

    # -----------------------------------------------------
    # NAVIGATION TITLE
    # -----------------------------------------------------

    st.html("""
    <div class="sidebar-nav-title">
        NAVIGATION
    </div>
    """)

    # -----------------------------------------------------
    # NAVIGATION
    # -----------------------------------------------------

    st.page_link(
        "app.py",
        label="Dashboard",
        icon=":material/dashboard:",
        width="stretch"
    )

    st.page_link(
        "pages/1_Chat.py",
        label="AI Chat",
        icon=":material/chat:",
        width="stretch"
    )

    st.page_link(
        "pages/2_Resume_Analyzer.py",
        label="Resume Analyzer",
        icon=":material/description:",
        width="stretch"
    )

    st.page_link(
        "pages/5_Job_Matcher.py",
        label="Job Matcher",
        icon=":material/work:",
        width="stretch"
    )

    st.page_link(
        "pages/3_Interview_Coach.py",
        label="Interview Coach",
        icon=":material/mic:",
        width="stretch"
    )

    st.page_link(
        "pages/4_PDF_Chat.py",
        label="PDF Chat",
        icon=":material/menu_book:",
        width="stretch"
    )

    st.divider()

    # -----------------------------------------------------
    # POWERED BY
    # -----------------------------------------------------

    st.html("""
    <div class="sidebar-powered">

        <div class="powered-label">
            POWERED BY
        </div>

        <div class="powered-name">
            Google Gemini
        </div>

    </div>
    """)


# =========================================================
# PAGE HEADER
# =========================================================

st.html("""
<div class="page-header">

    <div class="page-label">
        AI-POWERED CAREER ASSISTANCE
    </div>

    <div class="page-title">
        AI Career Chat
    </div>

    <div class="page-description">
        Ask questions about careers, programming, AI/ML,
        technologies, learning paths, projects, interviews,
        and job preparation.
    </div>

</div>
""")


# =========================================================
# INFORMATION CARDS
# =========================================================

col1, col2, col3 = st.columns(3)


with col1:

    st.html("""
    <div class="info-card">

        <div class="info-icon">
            💡
        </div>

        <div class="info-title">
            Career Guidance
        </div>

        <div class="info-description">
            Get guidance on career paths, skills,
            technologies and learning strategies.
        </div>

    </div>
    """)


with col2:

    st.html("""
    <div class="info-card">

        <div class="info-icon">
            💻
        </div>

        <div class="info-title">
            Technical Help
        </div>

        <div class="info-description">
            Ask programming, AI/ML, Python,
            web development and project questions.
        </div>

    </div>
    """)


with col3:

    st.html("""
    <div class="info-card">

        <div class="info-icon">
            🎯
        </div>

        <div class="info-title">
            Interview Preparation
        </div>

        <div class="info-description">
            Prepare for technical interviews,
            HR questions and placement discussions.
        </div>

    </div>
    """)


# =========================================================
# CHAT SECTION
# =========================================================

st.html("""
<div class="chat-section-title">
    💬 Start a Conversation
</div>

<div class="chat-section-description">
    Ask your AI career assistant anything related to your career journey.
</div>
""")


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================================================
# EMPTY CHAT STATE
# =========================================================

if not st.session_state.messages:

    st.html("""
    <div class="empty-chat">

        <div class="empty-chat-icon">
            🤖
        </div>

        <div class="empty-chat-title">
            How can I help you today?
        </div>

        <div class="empty-chat-description">
            Start a conversation with your AI career assistant.
            You can ask about programming, AI/ML, resumes,
            projects, interviews, career paths, and more.
        </div>

    </div>
    """)


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"]
        )


# =========================================================
# CHAT INPUT
# =========================================================

prompt = st.chat_input(
    "Ask about careers, coding, AI/ML, interviews..."
)


# =========================================================
# PROCESS USER MESSAGE
# =========================================================

if prompt:

    # -----------------------------------------------------
    # SAVE USER MESSAGE
    # -----------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    # -----------------------------------------------------
    # DISPLAY USER MESSAGE
    # -----------------------------------------------------

    with st.chat_message("user"):

        st.markdown(prompt)


    # -----------------------------------------------------
    # GENERATE AI RESPONSE
    # -----------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = ask_gemini(
                st.session_state.messages
            )

        st.markdown(response)


    # -----------------------------------------------------
    # SAVE AI RESPONSE
    # -----------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="page-footer">
    AI Career Assistant &nbsp;•&nbsp; Powered by Google Gemini
</div>
""")