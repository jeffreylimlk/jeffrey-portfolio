import os
import sys
import pytest

# Ensure app can be imported
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import app

def test_constants():
    assert app.MODEL_NAME == "gpt-4o-mini"
    assert "Jeffrey Lim" in app.PAGE_TITLE

def test_load_profile_context(monkeypatch):
    # Clear streamlit cache
    import streamlit as st
    st.cache_data.clear()
    
    # Test valid file
    test_file = "temp_test_profile.md"
    with open(test_file, "w") as f:
        f.write("Test Profile Content")
    
    monkeypatch.setattr(app, "PROFILE_FILE", test_file)
    
    content = app.load_profile_context()
    assert content == "Test Profile Content"
    
    os.remove(test_file)

    # Test invalid file
    st.cache_data.clear()
    monkeypatch.setattr(app, "PROFILE_FILE", "non_existent_file_12345.md")
    content = app.load_profile_context()
    assert content is None
