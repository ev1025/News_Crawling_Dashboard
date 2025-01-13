import streamlit as st
import pandas as pd

def render():
    """생활/문화 탭을 렌더링합니다."""
    st.header("생활/문화")
    if st.session_state.data:
        st.table(pd.DataFrame(st.session_state.data))
    else:
        st.write("No data available.")