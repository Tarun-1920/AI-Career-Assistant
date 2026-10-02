import streamlit as st

from backend.pdf_reader import extract_text_from_pdf
from backend.resume_analyzer import analyze_resume


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# =========================================================
# GLOBAL CSS
# =========================================================

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
    margin-bottom: 10px;
}

.page-description {
    color: #dbeafe;
    font-size: 15px;
    line-height: 1.7;
    max-width: 760px;
}


/* ========================================================
   FEATURE CARDS
   ======================================================== */

.feature-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 17px;

    padding: 22px;
    min-height: 135px;

    box-shadow:
        0 5px 18px rgba(15, 23, 42, 0.04);
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


/* ========================================================
   SECTION HEADINGS
   ======================================================== */

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


/* ========================================================
   UPLOAD AREA
   ======================================================== */

.upload-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 18px;

    padding: 25px;
    margin-top: 20px;

    box-shadow:
        0 5px 18px rgba(15, 23, 42, 0.04);
}

.upload-title {
    color: #111827;
    font-size: 19px;
    font-weight: 750;
    margin-bottom: 6px;
}

.upload-description {
    color: #6b7280;
    font-size: 13px;
    line-height: 1.6;
}


/* ========================================================
   RESUME STATUS
   ======================================================== */

.resume-status {
    background: #f0fdf4;

    border: 1px solid #bbf7d0;

    border-radius: 14px;

    padding: 15px 18px;

    margin-top: 15px;
}

.resume-name {
    color: #166534;
    font-size: 14px;
    font-weight: 700;
}

.resume-size {
    color: #15803d;
    font-size: 12px;
    margin-top: 4px;
}


/* ========================================================
   ANALYSIS AREA
   ======================================================== */

.analysis-card {
    background: #ffffff;

    border: 1px solid #e5e7eb;

    border-radius: 18px;

    padding: 25px;

    margin-top: 18px;

    box-shadow:
        0 5px 18px rgba(15, 23, 42, 0.04);
}


/* ========================================================
   EMPTY STATE
   ======================================================== */

.empty-state {
    background: #ffffff;

    border: 1px solid #e5e7eb;

    border-radius: 20px;

    padding: 55px 25px;

    margin-top: 25px;

    text-align: center;

    box-shadow:
        0 5px 18px rgba(15, 23, 42, 0.04);
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


# =========================================================
# PAGE HEADER
# =========================================================

st.html("""
<div class="page-header">

    <div class="page-label">
        AI-POWERED RESUME INTELLIGENCE
    </div>

    <div class="page-title">
        AI Resume Analyzer
    </div>

    <div class="page-description">
        Upload your resume and let AI analyze your
        skills, experience, strengths, and areas
        for improvement.
    </div>

</div>
""")


# =========================================================
# FEATURE CARDS
# =========================================================

col1, col2, col3 = st.columns(3)


with col1:

    st.html("""
    <div class="feature-card">

        <div class="feature-icon">
            🔍
        </div>

        <div class="feature-title">
            Resume Analysis
        </div>

        <div class="feature-description">
            Extract and analyze important information
            from your resume.
        </div>

    </div>
    """)


with col2:

    st.html("""
    <div class="feature-card">

        <div class="feature-icon">
            💡
        </div>

        <div class="feature-title">
            AI Insights
        </div>

        <div class="feature-description">
            Get AI-powered insights about your skills,
            experience and profile.
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
            Career Improvement
        </div>

        <div class="feature-description">
            Discover areas where your resume can
            be strengthened.
        </div>

    </div>
    """)


# =========================================================
# UPLOAD SECTION
# =========================================================

st.html("""
<div class="section-title">
    Upload Your Resume
</div>

<div class="section-description">
    Upload your resume as a PDF to begin the AI analysis.
</div>
""")


st.html("""
<div class="upload-card">

    <div class="upload-title">
        Resume Upload
    </div>

    <div class="upload-description">
        Select your latest resume in PDF format.
        The document will be processed by the AI analyzer.
    </div>

</div>
""")


# =========================================================
# FILE UPLOADER
# =========================================================

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"],
    label_visibility="collapsed"
)


# =========================================================
# PROCESS UPLOADED RESUME
# =========================================================

if uploaded_file:

    st.html(f"""
    <div class="resume-status">

        <div class="resume-name">
            {uploaded_file.name}
        </div>

        <div class="resume-size">
            Resume uploaded successfully •
            {round(uploaded_file.size / 1024, 2)} KB
        </div>

    </div>
    """)


    # -----------------------------------------------------
    # EXTRACT TEXT
    # -----------------------------------------------------

    resume_text = extract_text_from_pdf(
        uploaded_file
    )


    # -----------------------------------------------------
    # EXTRACTED RESUME
    # -----------------------------------------------------

    st.html("""
    <div class="section-title">
        Resume Content
    </div>

    <div class="section-description">
        Review the text extracted from your uploaded resume.
    </div>
    """)


    with st.expander(
        "View Extracted Resume",
        expanded=False
    ):

        st.text(resume_text)


    # -----------------------------------------------------
    # ANALYZE BUTTON
    # -----------------------------------------------------

    if st.button(
        "Analyze Resume",
        use_container_width=True,
        type="primary"
    ):

        with st.spinner(
            "AI is analyzing your resume..."
        ):

            result = analyze_resume(
                resume_text
            )


        # -------------------------------------------------
        # RESULT
        # -------------------------------------------------

        st.html("""
        <div class="section-title">
            AI Resume Analysis
        </div>

        <div class="section-description">
            Insights generated from your uploaded resume.
        </div>
        """)


        st.html("""
        <div class="analysis-card">
        """)

        st.markdown(result)

        st.html("""
        </div>
        """)


# =========================================================
# EMPTY STATE
# =========================================================

else:

    st.html("""
    <div class="empty-state">

        <div class="empty-icon">
            📄
        </div>

        <div class="empty-title">
            No resume uploaded yet
        </div>

        <div class="empty-description">
            Upload your PDF resume above to start
            your AI-powered resume analysis.
        </div>

    </div>
    """)


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="page-footer">
    AI Career Assistant &nbsp;•&nbsp; Powered by Google Gemini
</div>
""")