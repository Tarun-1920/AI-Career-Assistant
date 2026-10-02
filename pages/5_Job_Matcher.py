import streamlit as st
import json
import ast
import html

from backend.pdf_reader import extract_text_from_pdf
from backend.job_matcher import analyze_job_match


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Job Matcher",
    page_icon="💼",
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
   HIDE DEFAULT STREAMLIT NAVIGATION
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
   INPUT CARD
   ============================================================ */

.input-card {
    background: #ffffff;

    border: 1px solid #e5e7eb;

    border-radius: 18px;

    padding: 25px;

    margin-top: 20px;

    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
}

.input-card-title {
    color: #111827;

    font-size: 19px;
    font-weight: 750;

    margin-bottom: 6px;
}

.input-card-description {
    color: #6b7280;

    font-size: 13px;

    line-height: 1.6;

    margin-bottom: 15px;
}


/* ============================================================
   RESUME STATUS
   ============================================================ */

.resume-status {
    background: #eff6ff;

    border: 1px solid #bfdbfe;

    border-radius: 14px;

    padding: 15px 18px;

    margin-top: 15px;
}

.resume-name {
    color: #1e40af;

    font-size: 14px;

    font-weight: 700;
}

.resume-size {
    color: #2563eb;

    font-size: 12px;

    margin-top: 4px;
}


/* ============================================================
   MATCH SCORE
   ============================================================ */

.match-score-card {
    background: linear-gradient(
        135deg,
        #eff6ff,
        #dbeafe
    );

    border: 1px solid #bfdbfe;

    border-radius: 20px;

    padding: 30px;

    text-align: center;

    margin-top: 20px;

    box-shadow: 0 5px 18px rgba(37, 99, 235, 0.08);
}

.match-score-number {
    color: #1d4ed8;

    font-size: 52px;

    font-weight: 800;

    line-height: 1;
}

.match-score-label {
    color: #475569;

    font-size: 13px;

    font-weight: 600;

    margin-top: 9px;
}


/* ============================================================
   RESULT SECTIONS
   ============================================================ */

.result-section {
    background: #ffffff;

    border: 1px solid #e5e7eb;

    border-radius: 18px;

    padding: 24px;

    margin-top: 18px;

    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
}

.result-section-title {
    color: #111827;

    font-size: 18px;

    font-weight: 750;

    margin-bottom: 15px;
}


/* ============================================================
   SKILL TAGS
   ============================================================ */

.skill-tag {
    display: inline-block;

    background: #eff6ff;

    color: #1d4ed8;

    border: 1px solid #bfdbfe;

    border-radius: 20px;

    padding: 7px 13px;

    margin: 4px 5px 4px 0;

    font-size: 12px;

    font-weight: 600;
}

.missing-tag {
    display: inline-block;

    background: #fff7ed;

    color: #c2410c;

    border: 1px solid #fed7aa;

    border-radius: 20px;

    padding: 7px 13px;

    margin: 4px 5px 4px 0;

    font-size: 12px;

    font-weight: 600;
}


/* ============================================================
   RESULT ITEMS
   ============================================================ */

.result-item {
    color: #475569;

    font-size: 13px;

    line-height: 1.65;

    padding: 10px 0;

    border-bottom: 1px solid #f1f5f9;
}

.result-item:last-child {
    border-bottom: none;
}


/* ============================================================
   ROADMAP
   ============================================================ */

.roadmap-item {
    display: flex;

    gap: 12px;

    align-items: flex-start;

    padding: 12px 0;

    border-bottom: 1px solid #f1f5f9;
}

.roadmap-item:last-child {
    border-bottom: none;
}

.roadmap-number {
    min-width: 30px;

    height: 30px;

    border-radius: 50%;

    background: #2563eb;

    color: #ffffff;

    display: flex;

    align-items: center;
    justify-content: center;

    font-size: 12px;

    font-weight: 700;
}

.roadmap-text {
    color: #475569;

    font-size: 13px;

    line-height: 1.55;

    padding-top: 5px;
}


/* ============================================================
   INTERVIEW TOPICS
   ============================================================ */

.interview-topic {
    background: #f8fafc;

    border: 1px solid #e2e8f0;

    border-radius: 12px;

    padding: 13px 15px;

    margin-bottom: 9px;

    color: #334155;

    font-size: 13px;
}


/* ============================================================
   INFORMATION CARD
   ============================================================ */

.match-info {
    background: #f8fafc;

    border: 1px solid #e2e8f0;

    border-radius: 16px;

    padding: 20px;

    margin-top: 25px;
}

.match-info-title {
    color: #111827;

    font-size: 15px;

    font-weight: 700;

    margin-bottom: 6px;
}

.match-info-text {
    color: #64748b;

    font-size: 12px;

    line-height: 1.6;
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
   TEXT AREA
   ============================================================ */

textarea {
    border-radius: 12px !important;
}


/* ============================================================
   BUTTON
   ============================================================ */

.stButton > button {
    border-radius: 10px !important;

    min-height: 42px;

    font-weight: 650 !important;
}


/* Primary button */

.stButton > button[kind="primary"] {
    background: #2563eb !important;

    border: 1px solid #2563eb !important;

    color: #ffffff !important;
}

.stButton > button[kind="primary"]:hover {
    background: #1d4ed8 !important;

    border-color: #1d4ed8 !important;

    color: #ffffff !important;
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
# SESSION STATE
# ============================================================

if "job_match_result" not in st.session_state:
    st.session_state.job_match_result = None


# ============================================================
# PAGE HEADER
# ============================================================

st.html("""
<div class="page-header">

    <div class="page-label">
        AI-POWERED JOB COMPATIBILITY
    </div>

    <div class="page-title">
        AI Job Matcher
    </div>

    <div class="page-description">
        Compare your resume with a job description and
        discover how your skills and experience align
        with the requirements of the role.
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
            Skill Matching
        </div>

        <div class="feature-description">
            Identify the skills from your resume that
            match the requirements of the job.
        </div>

    </div>
    """)


with col2:

    st.html("""
    <div class="feature-card">

        <div class="feature-icon">
            🔎
        </div>

        <div class="feature-title">
            Gap Analysis
        </div>

        <div class="feature-description">
            Discover important skills and requirements
            that may be missing from your profile.
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
            Career Insights
        </div>

        <div class="feature-description">
            Get AI-generated suggestions for improving
            your profile for the selected role.
        </div>

    </div>
    """)


# ============================================================
# RESUME SECTION
# ============================================================

st.html("""
<div class="section-title">
    Your Resume
</div>

<div class="section-description">
    Upload your resume so the AI can compare your profile
    with the target job.
</div>
""")


st.html("""
<div class="input-card">

    <div class="input-card-title">
        Upload Resume
    </div>

    <div class="input-card-description">
        Upload your latest resume in PDF format.
    </div>

</div>
""")


uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"],
    key="job_matcher_resume",
    label_visibility="collapsed"
)


resume_text = None


# ============================================================
# PROCESS RESUME
# ============================================================

if uploaded_resume:

    st.html(f"""
    <div class="resume-status">

        <div class="resume-name">
            📄 {html.escape(uploaded_resume.name)}
        </div>

        <div class="resume-size">
            Resume uploaded successfully
            • {round(uploaded_resume.size / 1024, 2)} KB
        </div>

    </div>
    """)

    try:

        resume_text = extract_text_from_pdf(
            uploaded_resume
        )

    except Exception as e:

        st.error(
            f"Unable to read the resume: {str(e)}"
        )


# ============================================================
# JOB DESCRIPTION SECTION
# ============================================================

st.html("""
<div class="section-title">
    Job Description
</div>

<div class="section-description">
    Paste the job description of the position you want
    to compare with your resume.
</div>
""")


st.html("""
<div class="input-card">

    <div class="input-card-title">
        Target Job
    </div>

    <div class="input-card-description">
        Include the role, responsibilities, required skills,
        qualifications, and other relevant information.
    </div>

</div>
""")


job_description = st.text_area(
    "Job Description",

    placeholder=(
        "Paste the complete job description here...\n\n"
        "Example:\n"
        "We are looking for a Python Developer with experience "
        "in machine learning, Flask, SQL and REST APIs..."
    ),

    height=280,

    label_visibility="collapsed"
)


# ============================================================
# ANALYZE BUTTON
# ============================================================

st.write("")

if st.button(
    "Analyze Job Match",
    type="primary",
    use_container_width=True
):

    if not uploaded_resume:

        st.warning(
            "Please upload your resume before analyzing the job match."
        )

    elif not resume_text:

        st.warning(
            "Unable to extract text from the uploaded resume."
        )

    elif not job_description.strip():

        st.warning(
            "Please paste a job description before analyzing."
        )

    else:

        with st.spinner(
            "AI is analyzing your resume against the job description..."
        ):

            try:

                result = analyze_job_match(
                    resume_text,
                    job_description
                )

                st.session_state.job_match_result = result

            except Exception as e:

                st.session_state.job_match_result = None

                st.error(
                    f"Unable to analyze the job match: {str(e)}"
                )


# ============================================================
# DISPLAY RESULT
# ============================================================

result = st.session_state.job_match_result


if result:

    # --------------------------------------------------------
    # Convert result to dictionary
    # --------------------------------------------------------

    result_data = None

    if isinstance(result, dict):

        result_data = result

    elif isinstance(result, str):

        try:

            result_data = json.loads(result)

        except Exception:

            try:

                result_data = ast.literal_eval(result)

            except Exception:

                result_data = None


    # ========================================================
    # STRUCTURED RESULT
    # ========================================================

    if isinstance(result_data, dict):

        match_score = result_data.get(
            "match_score",
            0
        )

        matching_skills = result_data.get(
            "matching_skills",
            []
        )

        missing_skills = result_data.get(
            "missing_skills",
            []
        )

        strengths = result_data.get(
            "strengths",
            []
        )

        improvements = result_data.get(
            "improvements",
            []
        )

        learning_roadmap = result_data.get(
            "learning_roadmap",
            []
        )

        interview_topics = result_data.get(
            "interview_topics",
            []
        )


        # ----------------------------------------------------
        # RESULT HEADER
        # ----------------------------------------------------

        st.html("""
        <div class="section-title">
            AI Job Match Analysis
        </div>

        <div class="section-description">
            AI-powered comparison of your resume with
            the selected job description.
        </div>
        """)


        # ----------------------------------------------------
        # MATCH SCORE
        # ----------------------------------------------------

        try:

            score_value = int(
                float(match_score)
            )

        except Exception:

            score_value = 0


        st.html(f"""
        <div class="match-score-card">

            <div class="match-score-number">
                {score_value}%
            </div>

            <div class="match-score-label">
                Resume &amp; Job Compatibility
            </div>

        </div>
        """)


        # ----------------------------------------------------
        # MATCHING SKILLS
        # ----------------------------------------------------

        if matching_skills:

            skill_html = ""

            for skill in matching_skills:

                skill_html += f"""
                <span class="skill-tag">
                    {html.escape(str(skill))}
                </span>
                """

            st.html(f"""
            <div class="result-section">

                <div class="result-section-title">
                    ✅ Matching Skills
                </div>

                <div>
                    {skill_html}
                </div>

            </div>
            """)


        # ----------------------------------------------------
        # MISSING SKILLS
        # ----------------------------------------------------

        if missing_skills:

            missing_html = ""

            for skill in missing_skills:

                missing_html += f"""
                <span class="missing-tag">
                    {html.escape(str(skill))}
                </span>
                """

            st.html(f"""
            <div class="result-section">

                <div class="result-section-title">
                    ⚠️ Skills to Develop
                </div>

                <div>
                    {missing_html}
                </div>

            </div>
            """)


        # ----------------------------------------------------
        # STRENGTHS
        # ----------------------------------------------------

        if strengths:

            strengths_html = ""

            for item in strengths:

                strengths_html += f"""
                <div class="result-item">
                    ✓ {html.escape(str(item))}
                </div>
                """

            st.html(f"""
            <div class="result-section">

                <div class="result-section-title">
                    💪 Your Strengths
                </div>

                {strengths_html}

            </div>
            """)


        # ----------------------------------------------------
        # IMPROVEMENTS
        # ----------------------------------------------------

        if improvements:

            improvements_html = ""

            for item in improvements:

                improvements_html += f"""
                <div class="result-item">
                    → {html.escape(str(item))}
                </div>
                """

            st.html(f"""
            <div class="result-section">

                <div class="result-section-title">
                    📈 Areas to Improve
                </div>

                {improvements_html}

            </div>
            """)


        # ----------------------------------------------------
        # LEARNING ROADMAP
        # ----------------------------------------------------

        if learning_roadmap:

            roadmap_html = ""

            for index, item in enumerate(
                learning_roadmap,
                start=1
            ):

                roadmap_html += f"""
                <div class="roadmap-item">

                    <div class="roadmap-number">
                        {index}
                    </div>

                    <div class="roadmap-text">
                        {html.escape(str(item))}
                    </div>

                </div>
                """

            st.html(f"""
            <div class="result-section">

                <div class="result-section-title">
                    🚀 Recommended Learning Roadmap
                </div>

                {roadmap_html}

            </div>
            """)


        # ----------------------------------------------------
        # INTERVIEW TOPICS
        # ----------------------------------------------------

        if interview_topics:

            topics_html = ""

            for topic in interview_topics:

                topics_html += f"""
                <div class="interview-topic">
                    💬 {html.escape(str(topic))}
                </div>
                """

            st.html(f"""
            <div class="result-section">

                <div class="result-section-title">
                    🎤 Suggested Interview Topics
                </div>

                {topics_html}

            </div>
            """)


    # ========================================================
    # FALLBACK FOR PLAIN TEXT RESPONSE
    # ========================================================

    else:

        st.html("""
        <div class="section-title">
            AI Job Match Analysis
        </div>

        <div class="section-description">
            AI-generated analysis of your resume and target job.
        </div>
        """)

        st.markdown(result)


# ============================================================
# INFORMATION CARD
# ============================================================

st.html("""
<div class="match-info">

    <div class="match-info-title">
        💡 How Job Matching Works
    </div>

    <div class="match-info-text">
        The AI compares information from your resume with
        the job description to identify relevant skills,
        experience, requirements, and potential gaps.
        Use the results as guidance when improving your
        resume and preparing for the role.
    </div>

</div>
""")


# ============================================================
# EMPTY STATE
# ============================================================

if not uploaded_resume and not job_description.strip():

    st.html("""
    <div class="empty-state">

        <div class="empty-icon">
            💼
        </div>

        <div class="empty-title">
            Ready to find your job match?
        </div>

        <div class="empty-description">
            Upload your resume and paste a job description
            above to start your AI-powered job compatibility
            analysis.
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