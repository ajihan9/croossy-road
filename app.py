import streamlit as st
import pathlib

st.set_page_config(page_title="길건너기 미니게임", layout="wide")

st.title("🚸 Simple Crossy Road Game")
st.write("방향키(↑ ↓ ← →)로 캐릭터를 움직여 자동차를 피해 길을 건너세요!")

# HTML 파일 읽기
html_file = pathlib.Path("static/game.html").read_text()

# HTML 삽입
st.components.v1.html(html_file, height=600, scrolling=False)
