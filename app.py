import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
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
    max-width: 1400px;
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
    padding-bottom: 4rem;
}


/* ========================================================
   HIDE DEFAULT PAGE NAVIGATION
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
   SIDEBAR NAVIGATION TITLE
   ======================================================== */

.sidebar-nav-title {
    color: #9ca3af !important;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.2px;
    padding: 6px 12px 10px;
}


/* ========================================================
   SIDEBAR NAVIGATION
   ======================================================== */

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

    transition: background 0.2s ease;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] a span {
    color: #e5e7eb !important;
}


/* Material icons */

[data-testid="stSidebar"] [data-testid="stPageLink"] a svg {
    color: #93c5fd !important;
}


/* Navigation hover */

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


/* Active page */

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


/* ========================================================
   SIDEBAR DIVIDER
   ======================================================== */

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
   HERO
   ======================================================== */

.hero {
    background: linear-gradient(
        135deg,
        #111827 0%,
        #1e3a8a 100%
    );

    border-radius: 24px;

    padding: 48px;

    margin-bottom: 35px;

    color: white;

    box-shadow:
        0 15px 35px rgba(15, 23, 42, 0.12);
}

.hero-label {
    color: #bfdbfe;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 12px;
}

.hero-title {
    color: #ffffff;
    font-size: 42px;
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 15px;
}

.hero-description {
    color: #dbeafe;
    font-size: 16px;
    line-height: 1.7;
    max-width: 780px;
}


/* ========================================================
   SECTION HEADINGS
   ======================================================== */

.section-title {
    color: #111827;
    font-size: 27px;
    font-weight: 750;
    margin-top: 20px;
    margin-bottom: 6px;
}

.section-description {
    color: #6b7280;
    font-size: 14px;
    margin-bottom: 22px;
}


/* ========================================================
   CLICKABLE CAREER CARDS
   ======================================================== */

/*
   The entire st.page_link becomes the card.
   Clicking anywhere inside the card navigates to the page.
*/

[data-testid="stPageLink"].career-card {
    height: 190px;
    margin-bottom: 25px;
}

[data-testid="stPageLink"].career-card a {
    height: 190px !important;

    display: flex !important;

    flex-direction: column !important;

    align-items: flex-start !important;

    justify-content: flex-start !important;

    padding: 27px !important;

    background: #ffffff !important;

    border: 1px solid #e5e7eb !important;

    border-radius: 18px !important;

    color: #111827 !important;

    text-decoration: none !important;

    box-shadow:
        0 5px 18px rgba(15, 23, 42, 0.04);

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease,
        border-color 0.2s ease;
}


/* Card icon */

[data-testid="stPageLink"].career-card a svg {
    width: 30px !important;
    height: 30px !important;

    color: #2563eb !important;

    margin-bottom: 14px !important;
}


/* Card title */

[data-testid="stPageLink"].career-card a span {
    color: #111827 !important;

    font-size: 18px !important;

    font-weight: 700 !important;

    line-height: 1.4 !important;
}


/* Card hover */

[data-testid="stPageLink"].career-card a:hover {
    transform: translateY(-4px);

    border-color: #93c5fd !important;

    box-shadow:
        0 14px 30px rgba(15, 23, 42, 0.10);

    background: #ffffff !important;
}

[data-testid="stPageLink"].career-card a:hover svg {
    color: #1d4ed8 !important;
}


/* ========================================================
   JOURNEY CARD
   ======================================================== */

.journey-container {
    background: #ffffff;

    border: 1px solid #e5e7eb;

    border-radius: 18px;

    padding: 28px;

    margin-top: 10px;

    box-shadow:
        0 5px 18px rgba(15, 23, 42, 0.04);
}

.journey-title {
    color: #111827;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 22px;
}

.step {
    text-align: center;
    padding: 10px;
}

.step-icon {
    font-size: 28px;
    margin-bottom: 8px;
}

.step-title {
    color: #111827;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 4px;
}

.step-description {
    color: #6b7280;
    font-size: 12px;
}


/* ========================================================
   FOOTER
   ======================================================== */

.footer {
    text-align: center;

    color: #9ca3af;

    font-size: 12px;

    margin-top: 45px;

    padding: 20px 0;
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
    # NAVIGATION LINKS
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
# HERO SECTION
# =========================================================

st.html("""
<div class="hero">

    <div class="hero-label">
        YOUR AI-POWERED CAREER COMPANION
    </div>

    <div class="hero-title">
        Build Your Career With AI
    </div>

    <div class="hero-description">
        Analyze your resume, match jobs, practice interviews,
        chat with AI, and work with career documents —
        all in one place.
    </div>

</div>
""")


# =========================================================
# CAREER TOOLS
# =========================================================

st.html("""
<div class="section-title">
    Explore Your Career Tools
</div>

<div class="section-description">
    Choose a tool below to continue your career journey.
</div>
""")


# =========================================================
# ROW 1
# =========================================================

col1, col2, col3 = st.columns(3)


with col1:

    st.page_link(
        "pages/1_Chat.py",
        label="AI Career Chat",
        icon=":material/chat:",
        help="Chat with your AI career assistant",
        width="stretch"
    )


with col2:

    st.page_link(
        "pages/2_Resume_Analyzer.py",
        label="Resume Analyzer",
        icon=":material/description:",
        help="Analyze your resume with AI",
        width="stretch"
    )


with col3:

    st.page_link(
        "pages/5_Job_Matcher.py",
        label="Job Matcher",
        icon=":material/track_changes:",
        help="Compare your resume with a job",
        width="stretch"
    )


# =========================================================
# ROW 2
# =========================================================

col4, col5, col6 = st.columns(3)


with col4:

    st.page_link(
        "pages/3_Interview_Coach.py",
        label="Interview Coach",
        icon=":material/mic:",
        help="Practice interviews with AI",
        width="stretch"
    )


with col5:

    st.page_link(
        "pages/4_PDF_Chat.py",
        label="PDF Chat",
        icon=":material/menu_book:",
        help="Ask questions about your PDF",
        width="stretch"
    )


with col6:

    st.page_link(
        "pages/2_Resume_Analyzer.py",
        label="Career Journey",
        icon=":material/rocket_launch:",
        help="Start your AI-powered career journey",
        width="stretch"
    )


# =========================================================
# CAREER JOURNEY
# =========================================================

st.html("""
<div class="section-title">
    Your Career Journey
</div>

<div class="section-description">
    Follow a simple path from resume analysis to interview preparation.
</div>
""")


st.html("""
<div class="journey-container">

    <div class="journey-title">
        From Skills to Career
    </div>

</div>
""")


j1, j2, j3, j4 = st.columns(4)


with j1:

    st.html("""
    <div class="step">

        <div class="step-icon">
            📄
        </div>

        <div class="step-title">
            Analyze Resume
        </div>

        <div class="step-description">
            Understand your profile
        </div>

    </div>
    """)


with j2:

    st.html("""
    <div class="step">

        <div class="step-icon">
            🎯
        </div>

        <div class="step-title">
            Match Jobs
        </div>

        <div class="step-description">
            Find relevant opportunities
        </div>

    </div>
    """)


with j3:

    st.html("""
    <div class="step">

        <div class="step-icon">
            🎤
        </div>

        <div class="step-title">
            Practice
        </div>

        <div class="step-description">
            Prepare for interviews
        </div>

    </div>
    """)


with j4:

    st.html("""
    <div class="step">

        <div class="step-icon">
            🚀
        </div>

        <div class="step-title">
            Get Career Ready
        </div>

        <div class="step-description">
            Improve and move forward
        </div>

    </div>
    """)


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer">
    AI Career Assistant &nbsp;•&nbsp; Powered by Google Gemini
</div>
""")