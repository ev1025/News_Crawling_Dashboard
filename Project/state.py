import streamlit as st

def initialize_state():
    """초기 상태를 설정합니다."""
    for key, value in {
        "data": [],
        "message": None,
        "message_time": None,
        "current_name": "",
        "current_age": 0,
        "current_score": 0.0,
    }.items():
        if key not in st.session_state:
            st.session_state[key] = value