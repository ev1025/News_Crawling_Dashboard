import streamlit as st
import pandas as pd

def render():
    """경제 탭을 렌더링합니다."""
    st.header("경제")
    if st.session_state.data:
        st.table(pd.DataFrame(st.session_state.data))
    else:
        st.write("No data available.")