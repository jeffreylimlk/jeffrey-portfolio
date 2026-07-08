import streamlit as st
from openai import OpenAI, APIError, AuthenticationError, RateLimitError
import os
from dotenv import load_dotenv

# ============================================================
# CONFIGURATION CONSTANTS
# ============================================================
MODEL_NAME = "gpt-4o-mini"
PROFILE_FILE = "profile.md"
PHOTO_FILE = "assets/jeffrey.jpg"
PAGE_TITLE = "Jeffrey Lim | Technical Leader & Applied AI"
PAGE_ICON = None
MAX_HISTORY_MESSAGES = 20
MAX_MESSAGES_PER_SESSION = 25

STARTER_QUESTIONS = [
    "What are Jeffrey's AI projects?",
    "Tell me about his coaching experience",
    "What certifications does he hold?",
]

SYSTEM_PROMPT_TEMPLATE = (
    "You are a professional, down-to-earth AI assistant for Lim Lee Keong, Jeffrey. "
    "Your job is to answer professional queries about his career, certifications, projects, and capabilities. "
    "Base your answers strictly on the following factual context:\n\n{context}\n\n"
    "Guidelines:\n"
    "- Stay grounded and factual. Do not use hyperbole or empty buzzwords.\n"
    "- Keep answers concise — aim for 2-4 short paragraphs unless the user asks for detail.\n"
    "- If a user asks about unrelated topics (politics, religion, or personal life), "
    "politely guide them back to Jeffrey's professional credentials.\n"
    "- When referencing projects or certifications, be specific about names and details from the context."
)

WELCOME_MESSAGE = (
    "Hello! I'm Jeffrey's AI profile assistant. I can answer questions about his "
    "technical projects, leadership background, certifications, or coaching philosophies. "
    "Try one of the suggestions below, or ask your own question!"
)


# ============================================================
# PAGE SETUP & API CONFIGURATION
# ============================================================
load_dotenv()
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None


# ============================================================
# DATA LOADING
# ============================================================
@st.cache_data
def load_profile_context():
    """Load the profile markdown file as the RAG knowledge base."""
    try:
        with open(PROFILE_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None


profile_context = load_profile_context()
if not profile_context:
    st.error("Warning: `profile.md` not found. The AI assistant will not have access to your context data.")
    profile_context = "Profile data is currently unavailable."

if not api_key:
    st.warning("Warning: `OPENAI_API_KEY` is not set in your environment. Chatbot features will be disabled.")


# ============================================================
# CUSTOM CSS — Modern Premium Light Theme
# ============================================================
def load_css(file_name):
    try:
        with open(file_name, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Warning: Custom stylesheet not found. Using default Streamlit theme.")

load_css("assets/style.css")


# ============================================================
# SIDEBAR
# ============================================================
def render_sidebar():
    """Render the sidebar with profile info and navigation."""
    with st.sidebar:
        st.title("Lim Lee Keong, Jeffrey")

        # Status badge
        st.markdown(
            '<div class="status-badge"><span class="status-dot"></span> Open to Opportunities</div>',
            unsafe_allow_html=True,
        )

        # Profile photo
        if os.path.exists(PHOTO_FILE):
            st.image(PHOTO_FILE, width="stretch")
        else:
            st.info("Add your headshot as 'jeffrey.jpg'")

        st.markdown(
            """
        **Technical Operations Leader & Applied AI Developer**

        Email: lim_lee_keong@yahoo.com
        Phone: 97967375
        LinkedIn: [LinkedIn](https://linkedin.com/in/jeffrey-lim-22174841)
        GitHub: [GitHub - Data Science](https://github.com/jeffreylimlk/Data-Science-Project)
        GitHub: [GitHub - Capstone](https://github.com/jeffreylimlk/Data-Science-Capstone-Project)
        Location: Singapore
        """,
            unsafe_allow_html=True,
        )

        st.markdown("---")
        st.markdown("### Core Domains")
        domains = [
            "Technical Coaching",
            "Agentic RAG AI",
            "Python Automation",
            "Power BI Dashboards",
            "Operations Leadership",
            "Machine Learning",
        ]
        domain_html = "".join(
            [f'<span class="domain-tag">{d}</span>' for d in domains]
        )
        st.markdown(domain_html, unsafe_allow_html=True)


render_sidebar()


# ============================================================
# HERO SECTION
# ============================================================
st.markdown(
    """
    <div class="hero-container">
        <div class="hero-title">Professional Portfolio</div>
        <div class="hero-subtitle">30 years of engineering leadership, now building with AI</div>
        <span class="hero-tagline">AI-Powered Profile — Ask the chatbot anything →</span>
    </div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# MAIN LAYOUT — Two Columns
# ============================================================
col_left, col_right = st.columns([1.1, 0.9], gap="large")


# ============================================================
# LEFT COLUMN — Professional Portfolio
# ============================================================
def render_portfolio():
    """Render the left-column portfolio content."""
    with col_left:
        # --- Summary & Experience ---
        with st.expander("Summary & Experience Highlights", expanded=True):
            st.markdown(
                """
            **Technical Operations Leader and Applied AI Developer** with 30 years of
            industry experience driving operational efficiency and mentoring technical teams.

            * **Cymer Singapore (2011–Present):** Site Operations Manager / Senior Engineer
              executing digital process automation via Python and enterprise Power BI tracking.
            * **RSAF (1996–2011):** Air Force Engineer (Master Sergeant) directing F16
              maintenance squads and executing statistical data modeling (FMEA/RCA).
            """
            )

        # --- Applied AI Portfolio ---
        with st.expander("Applied AI & Software Portfolio", expanded=True):
            st.markdown(
                """
            <div class="project-card">
                <h4>FSE Assistant — Agentic RAG AI Virtual Tech Support</h4>
                <p>Built a localized generative AI support framework utilizing Gemini APIs
                to parse multi-block technical flowcharts and diagnose machine error codes
                on standard CPU-bound workplace computers.</p>
                <div class="project-impact">Runs on CPU-only hardware — no GPU required</div>
                <span class="tech-badge">Gemini API</span>
                <span class="tech-badge">RAG</span>
                <span class="tech-badge">Python</span>
                <span class="tech-badge">Agentic AI</span>
            </div>
            <div class="project-card">
                <h4>FSE Assistant — RAG AI E-Library Manual</h4>
                <p>Developed an AI knowledge retrieval system using advanced semantic text
                chunking and localized database indexing to dynamically query thousands of
                pages of technical hardware manuals.</p>
                <div class="project-impact">Processes 1000s of pages of technical docs</div>
                <span class="tech-badge">Semantic Chunking</span>
                <span class="tech-badge">Embeddings</span>
                <span class="tech-badge">Vector DB</span>
                <span class="tech-badge">Python</span>
            </div>
            <div class="project-card">
                <h4>SpaceX Operations Capstone</h4>
                <p>Programmed an end-to-end Python and SQL data pipeline to clean, process,
                and dynamically visualize aerospace metrics and train predictive success models.</p>
                <div class="project-impact">End-to-end ML pipeline with predictive modeling</div>
                <span class="tech-badge">Python</span>
                <span class="tech-badge">SQL</span>
                <span class="tech-badge">Scikit-learn</span>
                <span class="tech-badge">Data Viz</span>
            </div>
            <div class="project-card">
                <h4>Applied ML Portfolio Projects</h4>
                <p>Implemented deep learning CNNs for medical imaging tasks (COVID detection,
                breast cancer prediction) and built regression/classification pipelines for
                real estate pricing, climate modeling, and big data user classification.</p>
                <div class="project-impact">Deep Learning + Traditional ML</div>
                <span class="tech-badge">TensorFlow</span>
                <span class="tech-badge">CNN</span>
                <span class="tech-badge">Regression</span>
                <span class="tech-badge">Classification</span>
            </div>
            """,
                unsafe_allow_html=True,
            )

        # --- Skills Visualization ---
        with st.expander("Technical Skills", expanded=True):
            skills = [
                ("AI & RAG Systems", 92),
                ("Python Development", 90),
                ("Power BI & Analytics", 88),
                ("Machine Learning", 85),
                ("Technical Coaching", 95),
                ("Operations Leadership", 93),
            ]
            skills_html = ""
            for label, pct in skills:
                skills_html += f"""
                <div class="skill-category">
                    <div class="skill-label">{label}</div>
                    <div class="skill-bar-bg">
                        <div class="skill-bar-fill" style="width: {pct}%;"></div>
                    </div>
                </div>
                """
            st.markdown(skills_html, unsafe_allow_html=True)

        # --- Education & Certifications ---
        with st.expander("Education & Key Certifications", expanded=True):
            st.markdown(
                """
            **Academic Credentials**
            * **Bachelor of Engineering (Honours Class 1)** — University of Newcastle, Australia
            * **Diploma with Merit (Electrical Engineering)** — Ngee Ann Polytechnic, Singapore

            **Professional Certifications**
            * AI Coder: Complete Claude Code & Coding Agents Course (Udemy, 2026)
            * Google TensorFlow Developer Certificate
            * Multi-Agent RAG with Gemini & LangChain
            * IBM AI Engineering Professional Certificate
            * Microsoft Certified: Power BI Data Analyst
            * DeepLearning.AI TensorFlow Developer Professional Certificate
            * IBM Data Science Professional Certificate
            * Generative AI for Data Scientists Specialization
            """
            )


render_portfolio()


# ============================================================
# RIGHT COLUMN — AI RAG Chatbot
# ============================================================
def render_chatbot():
    """Render the right-column AI chatbot interface."""
    with col_right:
        st.header("Ask My AI Assistant")
        st.caption(
            "This chatbot uses a context-augmented pipeline on Jeffrey's profile document "
            "to answer your career, project, or training questions."
        )

        # --- Initialize chat state ---
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": WELCOME_MESSAGE}
            ]

        # --- Clear Chat Button ---
        if st.button("Clear Chat", key="clear_chat"):
            st.session_state.messages = [
                {"role": "assistant", "content": WELCOME_MESSAGE}
            ]
            st.rerun()

        # --- Display chat history ---
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # --- Rate limit check ---
        user_msg_count = sum(
            1 for m in st.session_state.messages if m["role"] == "user"
        )
        remaining = MAX_MESSAGES_PER_SESSION - user_msg_count

        if remaining <= 0:
            st.info(
                "You've reached the message limit for this session. "
                "Click **Clear Chat** above to start a new conversation."
            )
            return

        if remaining <= 5:
            st.caption(
                f"{remaining} message{'s' if remaining != 1 else ''} remaining in this session"
            )

        # --- Starter Question Buttons ---
        starter_query = None
        if len(st.session_state.messages) <= 1:
            st.markdown("**Try asking:**")
            cols = st.columns(len(STARTER_QUESTIONS))
            for i, question in enumerate(STARTER_QUESTIONS):
                with cols[i]:
                    if st.button(question, key=f"starter_{i}", use_container_width=True):
                        starter_query = question

        # --- Chat input ---
        user_query = st.chat_input(
            "e.g., What is Jeffrey's experience with Python automation?"
        )

        # --- Process query from either source ---
        active_query = starter_query or user_query
        if active_query:
            # Display user message immediately
            with st.chat_message("user"):
                st.markdown(active_query)
            st.session_state.messages.append(
                {"role": "user", "content": active_query}
            )

            # Get and display AI response with visible spinner
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response_text = _get_ai_response()
                st.markdown(response_text)
            st.session_state.messages.append(
                {"role": "assistant", "content": response_text}
            )

            st.rerun()


def _get_ai_response():
    """Call the OpenAI API with conversation context and return the response text."""
    if not client:
        return (
            "I'm sorry, the OpenAI API key is not configured. "
            "Please set it up in the backend environment."
        )

    try:
        system_instruction = SYSTEM_PROMPT_TEMPLATE.format(
            context=profile_context
        )

        # Build conversation history with sliding window
        history = st.session_state.messages[1:]  # Skip welcome msg
        if len(history) > MAX_HISTORY_MESSAGES:
            history = history[-MAX_HISTORY_MESSAGES:]

        messages = [{"role": "system", "content": system_instruction}]
        for msg in history:
            messages.append({"role": msg["role"], "content": msg["content"]})

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
        )
        return response.choices[0].message.content

    except AuthenticationError:
        return "Warning: API authentication failed. Please check the API key configuration."
    except RateLimitError:
        return "Warning: API rate limit reached. Please try again in a moment."
    except APIError as e:
        return (
            f"Warning: The AI service returned an error (code {e.status_code}). "
            "Please try again."
        )
    except Exception:
        return "Warning: An unexpected error occurred. Please try again later."


render_chatbot()