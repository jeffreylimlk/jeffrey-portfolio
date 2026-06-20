# CLAUDE.md - Jeffrey's Portfolio & RAG Chatbot Project

## Project Overview
A modern, single-page professional portfolio web application with a premium dark sidebar + light main panel design. Features an interactive AI Chatbot running a live multi-turn RAG pipeline via the OpenAI API (gpt-4o-mini), using `profile.md` as its sole ground truth knowledge base.

## Tech Stack
- Frontend & UI: Python (Streamlit) with custom CSS (Inter font, animations, gradients)
- AI Model Integration: OpenAI API (`openai` SDK, `client.chat.completions.create()`) — model: `gpt-4o-mini`
- Data Source: Markdown Context (`profile.md`)
- Environment Config: `python-dotenv`, `.env` file with `OPENAI_API_KEY` (excluded from git)
- Theme Config: `.streamlit/config.toml`

## Core Commands
- Install All Dependencies: `pip install -r requirements.txt`
- Run Application Locally: `streamlit run app.py`
- Code Formatting: `black app.py` (optional)

## Architecture
The app is structured as modular functions in a single `app.py`:
- **Configuration constants** at the top (model name, prompts, starter questions)
- `load_profile_context()` — Cached data loader for the RAG knowledge base
- `render_sidebar()` — Sidebar layout with photo, contact info, domain tags
- `render_portfolio()` — Left column: experience, projects, skills bars, education
- `render_chatbot()` — Right column: multi-turn chat UI with starter buttons
- `_handle_user_query()` — OpenAI API call with conversation history via `client.chat.completions.create()`

## Code Style & Guidelines
- Write clean, modular, and human-readable Python code.
- Keep all custom CSS isolated in the designated `st.markdown` block at the top of `app.py`.
- Store sensitive configuration keys strictly in a local `.env` file; never hardcode the `OPENAI_API_KEY`.
- Use explicit try-except handling for file I/O operations and external API requests.
- Configuration constants (model name, prompts, etc.) live at the top of `app.py`.

## Chatbot Persona Guardrails
- **Tone:** Grounded, professional, down-to-earth, and approachable. Mirror Jeffrey's real-world engineering background and coaching mindset. Avoid empty AI hype.
- **Knowledge Base:** Rely strictly on the verified text inside `profile.md`.
- **Response Length:** Aim for 2-4 concise paragraphs unless the user asks for more detail.
- **Safety Boundaries:** If a user pivots to unrelated domains (politics, religion, or personal gossip), the bot must politely steer the user back to Jeffrey's technical projects, leadership background, and teaching capabilities.
- **Multi-Turn:** Conversation history is passed to the model so follow-up questions work naturally.