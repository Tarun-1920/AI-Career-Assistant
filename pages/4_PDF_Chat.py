import streamlit as st

from backend.pdf_reader import extract_text_from_pdf
from backend.chunker import chunk_text
from backend.vector_store import create_vector_store, search_pdf
from backend.pdf_chat import chat_with_pdf


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="PDF Chat",
    page_icon="📚",
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
   UPLOAD CARD
   ============================================================ */

.upload-card {
    background: #ffffff;

    border: 1px solid #e5e7eb;
    border-radius: 18px;

    padding: 25px;

    margin-top: 20px;

    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
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


/* ============================================================
   FILE STATUS
   ============================================================ */

.file-status {
    background: #eff6ff;

    border: 1px solid #bfdbfe;
    border-radius: 14px;

    padding: 15px 18px;

    margin-top: 15px;
}

.file-name {
    color: #1e40af;

    font-size: 14px;
    font-weight: 700;
}

.file-info {
    color: #2563eb;

    font-size: 12px;

    margin-top: 4px;
}


/* ============================================================
   PDF INFO CARD
   ============================================================ */

.pdf-info {
    background: #f8fafc;

    border: 1px solid #e2e8f0;

    border-radius: 16px;

    padding: 20px;

    margin-top: 18px;
}

.pdf-info-title {
    color: #111827;

    font-size: 15px;
    font-weight: 700;

    margin-bottom: 6px;
}

.pdf-info-text {
    color: #64748b;

    font-size: 12px;
    line-height: 1.6;
}


/* ============================================================
   CHAT AREA
   ============================================================ */

.chat-card {
    background: #ffffff;

    border: 1px solid #e5e7eb;

    border-radius: 20px;

    padding: 22px;

    margin-top: 25px;

    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
}


/* ============================================================
   CHAT WELCOME
   ============================================================ */

.chat-welcome {
    background: #eff6ff;

    border: 1px solid #bfdbfe;

    border-radius: 17px;

    padding: 23px;

    margin-bottom: 20px;
}

.chat-welcome-title {
    color: #1e3a8a;

    font-size: 18px;
    font-weight: 750;

    margin-bottom: 7px;
}

.chat-welcome-description {
    color: #475569;

    font-size: 13px;
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
   CHAT MESSAGES
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
# SESSION STATE
# ============================================================

if "pdf_messages" not in st.session_state:
    st.session_state.pdf_messages = []

if "pdf_vector_store" not in st.session_state:
    st.session_state.pdf_vector_store = None

if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = None

if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = None


# ============================================================
# PAGE HEADER
# ============================================================

st.html("""
<div class="page-header">

    <div class="page-label">
        AI-POWERED DOCUMENT INTELLIGENCE
    </div>

    <div class="page-title">
        Chat With Your PDF
    </div>

    <div class="page-description">
        Upload a PDF document and ask questions about
        its content using your AI-powered document assistant.
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
            📄
        </div>

        <div class="feature-title">
            Upload Documents
        </div>

        <div class="feature-description">
            Upload your resume, study material,
            reports, or other PDF documents.
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
            Smart Search
        </div>

        <div class="feature-description">
            Find relevant information from your document
            using semantic search.
        </div>

    </div>
    """)


with col3:

    st.html("""
    <div class="feature-card">

        <div class="feature-icon">
            💬
        </div>

        <div class="feature-title">
            Ask Questions
        </div>

        <div class="feature-description">
            Ask natural-language questions and receive
            AI-generated answers from your PDF.
        </div>

    </div>
    """)


# ============================================================
# UPLOAD SECTION
# ============================================================

st.html("""
<div class="section-title">
    Upload Your PDF
</div>

<div class="section-description">
    Select a PDF document to start chatting with its content.
</div>
""")


st.html("""
<div class="upload-card">

    <div class="upload-title">
        Document Upload
    </div>

    <div class="upload-description">
        Upload a PDF containing the information you want
        to analyze or discuss with the AI assistant.
    </div>

</div>
""")


uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"],
    label_visibility="collapsed"
)


# ============================================================
# PROCESS UPLOADED PDF
# ============================================================

if uploaded_file:

    # --------------------------------------------------------
    # Check if this is a new PDF
    # --------------------------------------------------------

    if st.session_state.pdf_name != uploaded_file.name:

        with st.spinner("Processing your PDF..."):

            try:

                # Extract text
                pdf_text = extract_text_from_pdf(
                    uploaded_file
                )

                # Split into chunks
                chunks = chunk_text(
                    pdf_text
                )

                # Create vector store
                vector_store = create_vector_store(
                    chunks
                )

                # Save in session
                st.session_state.pdf_text = pdf_text

                st.session_state.pdf_vector_store = vector_store

                st.session_state.pdf_name = uploaded_file.name

                st.session_state.pdf_messages = []

            except Exception as e:

                st.error(
                    f"Unable to process the PDF: {str(e)}"
                )

    # --------------------------------------------------------
    # File status
    # --------------------------------------------------------

    st.html(f"""
    <div class="file-status">

        <div class="file-name">
            📄 {uploaded_file.name}
        </div>

        <div class="file-info">
            PDF uploaded successfully
            • {round(uploaded_file.size / 1024, 2)} KB
        </div>

    </div>
    """)


    # ========================================================
    # PDF INFORMATION
    # ========================================================

    st.html("""
    <div class="pdf-info">

        <div class="pdf-info-title">
            Document Ready
        </div>

        <div class="pdf-info-text">
            Your PDF has been processed and is ready for
            questions. Ask anything related to the content
            of the uploaded document.
        </div>

    </div>
    """)


    # ========================================================
    # DOCUMENT PREVIEW
    # ========================================================

    st.html("""
    <div class="section-title">
        Document Content
    </div>

    <div class="section-description">
        Preview the text extracted from your PDF.
    </div>
    """)


    with st.expander(
        "View Extracted PDF Text",
        expanded=False
    ):

        st.text(
            st.session_state.pdf_text
            if st.session_state.pdf_text
            else "No text extracted."
        )


    # ========================================================
    # CHAT SECTION
    # ========================================================

    st.html("""
    <div class="section-title">
        Ask Your PDF
    </div>

    <div class="section-description">
        Ask questions and get answers based on the
        uploaded document.
    </div>
    """)


    st.html("""
    <div class="chat-card">

        <div class="chat-welcome">

            <div class="chat-welcome-title">
                💬 Your PDF Assistant Is Ready
            </div>

            <div class="chat-welcome-description">
                Ask questions about the uploaded document.
                The AI will search the relevant sections
                before generating an answer.
            </div>

        </div>

    </div>
    """)


    # --------------------------------------------------------
    # Display previous messages
    # --------------------------------------------------------

    for message in st.session_state.pdf_messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )


    # --------------------------------------------------------
    # Chat input
    # --------------------------------------------------------

    question = st.chat_input(
        "Ask a question about your PDF..."
    )


    if question:

        # ----------------------------------------------------
        # Add user question
        # ----------------------------------------------------

        st.session_state.pdf_messages.append(
            {
                "role": "user",
                "content": question
            }
        )


        with st.chat_message("user"):

            st.markdown(question)


        # ----------------------------------------------------
        # Search relevant PDF content
        # ----------------------------------------------------

        with st.chat_message("assistant"):

            with st.spinner(
                "Searching your PDF..."
            ):

                try:

                    relevant_docs = search_pdf(
                        st.session_state.pdf_vector_store,
                        question
                    )

                    response = chat_with_pdf(
                        relevant_docs,
                        question
                    )

                except Exception as e:

                    response = (
                        "I couldn't process that question "
                        "right now.\n\n"
                        f"Error: `{str(e)}`"
                    )


            st.markdown(response)


        # ----------------------------------------------------
        # Save response
        # ----------------------------------------------------

        st.session_state.pdf_messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )


    # ========================================================
    # CLEAR CHAT
    # ========================================================

    if st.session_state.pdf_messages:

        st.write("")

        if st.button(
            "Clear PDF Conversation",
            use_container_width=True
        ):

            st.session_state.pdf_messages = []

            st.rerun()


else:

    # ========================================================
    # EMPTY STATE
    # ========================================================

    st.html("""
    <div class="empty-state">

        <div class="empty-icon">
            📚
        </div>

        <div class="empty-title">
            No PDF uploaded yet
        </div>

        <div class="empty-description">
            Upload a PDF above to start asking questions
            and exploring its content with AI.
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