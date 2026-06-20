# Code Review & Proposed Change Plan

I have reviewed the entire project directory. This is a very clean, well-structured Streamlit application that serves as an excellent interactive professional portfolio. Below is the code review and proposed change plan covering architectural discrepancies, code organization, and UX improvements.

## 1. Architectural Discrepancies (High Priority)
**Finding:** There is a major mismatch between the documentation and the actual code regarding the AI provider.
* The `README.md` explicitly claims the app uses the **Google Gemini API (`google-generativeai`)** and asks users to configure `GEMINI_API_KEY`.
* However, `app.py`, `claude.md`, and `requirements.txt` are all implemented using the **OpenAI API** (`gpt-4o-mini`) and expect an `OPENAI_API_KEY`.

**Proposed Change:** 
* Decide which LLM provider you prefer to use. We can either update `README.md` to accurately reflect the OpenAI usage, or we can refactor `app.py` to use `google-generativeai` as originally advertised.

## 2. Code Organization & Cleanliness (Medium Priority)
**Finding:** `app.py` contains nearly 240 lines of embedded CSS inside an `st.markdown` block. While standard practice for quick Streamlit prototyping, it clutters the application logic. 

**Proposed Change:**
* Extract the CSS into an external file (e.g., `assets/style.css` or `.streamlit/style.css`). 
* Create a simple loader function in `app.py` to inject the CSS. This will reduce your `app.py` size significantly and improve code readability.

## 3. RAG Architecture / Terminology (Low Priority / Conceptual)
**Finding:** The documentation frequently mentions a "Live RAG Pipeline." However, the current implementation strictly reads the entire `profile.md` and injects it into the system prompt window. 
* *Note:* Because `profile.md` is small (~6 KB), this approach is actually **more efficient** and cheaper than true RAG. But technically, there is no "Retrieval" (chunking, embeddings, vector DB) happening here; it's "Context Stuffing".

**Proposed Change:**
* If you want to keep the architecture as-is (recommended for simplicity and cost), we should slightly adjust the terminology in the `README` to something like "Context-Aware Prompt Injection."
* Alternatively, if you want this portfolio piece to demonstrate true RAG capabilities (perhaps to impress recruiters), we could implement a lightweight LangChain + FAISS/ChromaDB retrieval flow.

## 4. Application UX & Error Handling Enhancements (Medium Priority)
**Finding:** The app's error handling degrades gracefully but could be more informative.
* If `profile.md` is missing, `load_profile_context()` silently returns a string `"Profile data is currently unavailable."` which the AI will treat as its ground truth, leading to confusing chatbot answers. 
* If the API key is missing, it only warns the user *after* they attempt to chat.

**Proposed Change:**
* Add an explicit `st.error` banner at the top of the UI if `profile.md` fails to load.
* Add an `st.warning` banner near the chatbot UI if the `OPENAI_API_KEY` (or Gemini key) is missing, guiding the user to configure their `.env` file proactively.

## 5. Automated Testing (Low Priority)
**Finding:** There are currently no tests for the application. 

**Proposed Change:**
* Add a `tests/` directory with `pytest` covering basic functionalities like environment variable parsing, context file loading, and chat history management.
