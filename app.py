import pathlib
import streamlit as st

st.set_page_config(page_title="Should the company buy more staff hours? · Farah", layout="wide", initial_sidebar_state="collapsed")
st.markdown(
    "<style>#MainMenu, header, footer {visibility: hidden;}"
    " .block-container {padding: 0.6rem 1rem 0 1rem; max-width: 100%;}</style>",
    unsafe_allow_html=True,
)

html = (pathlib.Path(__file__).parent / "presentation.html").read_text(encoding="utf-8")
st.iframe(html, height=780, tab_index=0)
st.caption("Click the slide, then use the arrow keys (or click) to move between slides. Press R to replay a slide's animation.")
