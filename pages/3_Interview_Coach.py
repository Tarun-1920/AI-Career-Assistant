import streamlit as st

from backend.interview_coach import interview_response


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Interview Coach",
    page_icon="🎤",
    layout="wide"
)


# ============================================================
# GLOBAL UI / CSS
# ============================================================

st.html("""
<style>

.stApp {
    background: #f7f8fc;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* ============================================================
   HIDE DEFAULT STREAMLIT SIDEBAR NAVIGATION
   ============================================================ */

[data-testid="stSidebarNav"] {
    display: none !important;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

[data-testid="stSidebar"] {
    background: #111827 !important;
    border-right: 1px solid #1f2937;
}

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
}

.sidebar-subtitle {
    color: #9ca3af !important;
    font-size: 12px;
    margin-top: 7px;
}

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
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover span {
    color: #ffffff !important;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover svg {
    color: #60a5fa !important;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a[aria-current="page"] {
    background: #273449 !important;
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


/* ============================================================
   PAGE HEADER
   ============================================================ */

.page-header {
    background: linear-gradient(
        135deg,
        #111827 0%,
        #1e3a8a 100%
    );

    border-radius: 24px;

    padding: 40px;
    margin-bottom: 28px;

    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.10);
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
    margin-bottom: 10px;
}

.page-description {
    color: #dbeafe;
    font-size: 15px;
    line-height: 1.7;
    max-width: 760px;
}


/* ============================================================
   FEATURE CARDS
   ============================================================ */

.feature-card {
    background: #ffffff;

    border: 1px solid #e5e7eb;
    border-radius: 17px;

    padding: 22px;
    min-height: 135px;

    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
}

.feature-icon {
    font-size: 26px;
    margin-bottom: 9px;
}

.feature-title {
    color: #111827;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 6px;
}

.feature-description {
    color: #6b7280;
    font-size: 12px;
    line-height: 1.55;
}


/* ============================================================
   SECTION HEADINGS
   ============================================================ */

.section-title {
    color: #111827;
    font-size: 24px;
    font-weight: 750;

    margin-top: 32px;
    margin-bottom: 5px;
}

.section-description {
    color: #6b7280;
    font-size: 13px;
    margin-bottom: 18px;
}


/* ============================================================
   INTERVIEW SETUP
   ============================================================ */

.setup-card {
    background: #ffffff;

    border: 1px solid #e5e7eb;
    border-radius: 18px;

    padding: 25px;
    margin-top: 20px;

    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
}

.setup-title {
    color: #111827;
    font-size: 19px;
    font-weight: 750;

    margin-bottom: 6px;
}

.setup-description {
    color: #6b7280;
    font-size: 13px;
    line-height: 1.6;

    margin-bottom: 18px;
}


/* ============================================================
   CHAT AREA
   ============================================================ */

.chat-container {
    background: #ffffff;

    border: 1px solid #e5e7eb;
    border-radius: 20px;

    padding: 20px;

    margin-top: 25px;

    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
}


/* ============================================================
   WELCOME CARD
   ============================================================ */

.welcome-card {
    background: #eff6ff;

    border: 1px solid #bfdbfe;
    border-radius: 17px;

    padding: 24px;

    margin-bottom: 20px;
}

.welcome-title {
    color: #1e3a8a;
    font-size: 18px;
    font-weight: 750;

    margin-bottom: 7px;
}

.welcome-description {
    color: #475569;
    font-size: 13px;
    line-height: 1.6;
}


/* ============================================================
   INTERVIEW TIPS
   ============================================================ */

.tip-card {
    background: #f8fafc;

    border: 1px solid #e2e8f0;
    border-radius: 15px;

    padding: 17px;

    margin-top: 10px;
}

.tip-title {
    color: #111827;
    font-size: 14px;
    font-weight: 700;

    margin-bottom: 5px;
}

.tip-description {
    color: #64748b;
    font-size: 12px;
    line-height: 1.55;
}


/* ============================================================
   EMPTY STATE
   ============================================================ */

.empty-state {
    background: #ffffff;

    border: 1px solid #e5e7eb;
    border-radius: 20px;

    padding: 55px 25px;
    margin-top: 25px;

    text-align: center;

    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
}

.empty-icon {
    font-size: 50px;
    margin-bottom: 14px;
}

.empty-title {
    color: #111827;
    font-size: 21px;
    font-weight: 700;

    margin-bottom: 8px;
}

.empty-description {
    color: #6b7280;
    font-size: 13px;
    line-height: 1.6;
}


/* ============================================================
   CHAT MESSAGE STYLING
   ============================================================ */

[data-testid="stChatMessage"] {
    border-radius: 16px;
    margin-bottom: 12px;
}


/* ============================================================
   BUTTON
   ============================================================ */

.stButton > button {
    border-radius: 10px !important;

    min-height: 42px;

    font-weight: 650 !important;
}


/* ============================================================
   FOOTER
   ============================================================ */

.page-footer {
    text-align: center;

    color: #9ca3af;
    font-size: 12px;

    margin-top: 40px;
    padding: 20px;
}

</style>
""")


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

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

    st.html("""
    <div class="sidebar-nav-title">
        NAVIGATION
    </div>
    """)

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


# ============================================================
# PAGE HEADER
# ============================================================

st.html("""
<div class="page-header">

    <div class="page-label">
        AI-POWERED INTERVIEW PREPARATION
    </div>

    <div class="page-title">
        AI Interview Coach
    </div>

    <div class="page-description">
        Practice interview questions with your AI career coach.
        Improve your answers, build confidence, and prepare
        for real technical and HR interviews.
    </div>

</div>
""")


# ============================================================
# FEATURE CARDS
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.html("""
    <div class="feature-card">

        <div class="feature-icon">
            🎯
        </div>

        <div class="feature-title">
            Interview Practice
        </div>

        <div class="feature-description">
            Practice realistic technical and HR interview
            questions with an AI interviewer.
        </div>

    </div>
    """)


with col2:

    st.html("""
    <div class="feature-card">

        <div class="feature-icon">
            💬
        </div>

        <div class="feature-title">
            AI Feedback
        </div>

        <div class="feature-description">
            Receive useful feedback and suggestions
            to improve your interview answers.
        </div>

    </div>
    """)


with col3:

    st.html("""
    <div class="feature-card">

        <div class="feature-icon">
            🚀
        </div>

        <div class="feature-title">
            Build Confidence
        </div>

        <div class="feature-description">
            Practice repeatedly and become more confident
            before attending real interviews.
        </div>

    </div>
    """)


# ============================================================
# INTERVIEW SETUP
# ============================================================

st.html("""
<div class="section-title">
    Start Your Interview
</div>

<div class="section-description">
    Choose the type of interview you want to practice.
</div>
""")


st.html("""
<div class="setup-card">

    <div class="setup-title">
        Interview Configuration
    </div>

    <div class="setup-description">
        Select an interview category and start answering
        questions with your AI interview coach.
    </div>

</div>
""")


# ============================================================
# INTERVIEW TYPE
# ============================================================

interview_type = st.selectbox(
    "Interview Type",
    [
        "Technical Interview",
        "HR Interview",
        "Python Interview",
        "Java Interview",
        "AI / ML Interview",
        "Data Science Interview",
        "Web Development Interview",
        "Full Stack Development Interview"
    ]
)


# ============================================================
# DIFFICULTY
# ============================================================

difficulty = st.selectbox(
    "Difficulty Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)


# ============================================================
# SESSION STATE
# ============================================================

if "interview_messages" not in st.session_state:
    st.session_state.interview_messages = []


if "interview_started" not in st.session_state:
    st.session_state.interview_started = False


# ============================================================
# START INTERVIEW BUTTON
# ============================================================

if not st.session_state.interview_started:

    if st.button(
        "Start Interview",
        type="primary",
        use_container_width=True
    ):

        st.session_state.interview_started = True

        st.session_state.interview_messages = [
            {
                "role": "assistant",
                "content": (
                    f"Welcome to your **{interview_type}** practice interview! "
                    f"Your selected difficulty is **{difficulty}**.\n\n"
                    "Let's begin. Please introduce yourself."
                )
            }
        ]

        st.rerun()


# ============================================================
# INTERVIEW AREA
# ============================================================

if st.session_state.interview_started:

    st.html("""
    <div class="chat-container">

        <div class="welcome-card">

            <div class="welcome-title">
                🎤 Interview Session Active
            </div>

            <div class="welcome-description">
                Answer each question as if you were in a real interview.
                Your AI coach will continue the conversation based on
                your responses.
            </div>

        </div>

    </div>
    """)


    # --------------------------------------------------------
    # DISPLAY CHAT HISTORY
    # --------------------------------------------------------

    for message in st.session_state.interview_messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])


    # --------------------------------------------------------
    # CHAT INPUT
    # --------------------------------------------------------

    prompt = st.chat_input(
        "Type your interview answer..."
    )


    if prompt:

        # Add user response
        st.session_state.interview_messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)


        # AI response
        with st.chat_message("assistant"):

            with st.spinner("AI interviewer is thinking..."):

                try:

                    response = interview_response(
                        st.session_state.interview_messages
                    )

                except Exception as e:

                    response = (
                        "I couldn't generate the next interview "
                        "question right now.\n\n"
                        f"Error: `{str(e)}`"
                    )

            st.markdown(response)


        # Save AI response
        st.session_state.interview_messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )


    # --------------------------------------------------------
    # INTERVIEW TIPS
    # --------------------------------------------------------

    st.html("""
    <div class="section-title">
        Interview Tips
    </div>

    <div class="section-description">
        Keep these points in mind while answering.
    </div>
    """)


    tip1, tip2, tip3 = st.columns(3)


    with tip1:

        st.html("""
        <div class="tip-card">

            <div class="tip-title">
                Be Clear
            </div>

            <div class="tip-description">
                Explain your answer clearly and avoid unnecessary
                technical jargon.
            </div>

        </div>
        """)


    with tip2:

        st.html("""
        <div class="tip-card">

            <div class="tip-title">
                Give Examples
            </div>

            <div class="tip-description">
                Use practical examples from your projects,
                internships, or academic experience.
            </div>

        </div>
        """)


    with tip3:

        st.html("""
        <div class="tip-card">

            <div class="tip-title">
                Stay Confident
            </div>

            <div class="tip-description">
                Take a moment to think before answering and
                communicate your ideas confidently.
            </div>

        </div>
        """)


    # --------------------------------------------------------
    # END INTERVIEW
    # --------------------------------------------------------

    st.write("")

    if st.button(
        "End Interview & Start New Session",
        use_container_width=True
    ):

        st.session_state.interview_messages = []

        st.session_state.interview_started = False

        st.rerun()


# ============================================================
# EMPTY STATE
# ============================================================

else:

    st.html("""
    <div class="empty-state">

        <div class="empty-icon">
            🎤
        </div>

        <div class="empty-title">
            Ready for your interview?
        </div>

        <div class="empty-description">
            Select your interview type and difficulty level,
            then click <b>Start Interview</b> to begin
            your AI-powered practice session.
        </div>

    </div>
    """)


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="page-footer">

    AI Career Assistant
    &nbsp;•&nbsp;
    Powered by Google Gemini

</div>
""")