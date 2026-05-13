import streamlit as st

# =====================================
# 最優先
# =====================================

st.set_page_config(
    page_title="げんしけんにじさんじ共通テスト2026 in 清陵祭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# import
# =====================================

import pandas as pd
import matplotlib.pyplot as plt
import json

from google.oauth2.service_account import Credentials

from streamlit_autorefresh import st_autorefresh

from background import set_bg_image
from Google_Sheets import access_sheets
from calc import make_data
from main import dashboard_page
from rate_question import question_analysis_page

# =====================================
# 自動更新
# =====================================

st_autorefresh(
    interval=5000,
    key="refresh"
)

# =====================================
# 背景
# =====================================

set_bg_image("image.png")

# =====================================
# Google Sheets
# =====================================

df = access_sheets()

# =====================================
# 問題設定
# =====================================

with open('answer.json', 'r', encoding='utf-8') as f:
    ANSWER_KEY = json.load(f)

QUESTIONS = list(
    ANSWER_KEY.keys()
)

# =====================================
# 採点・統計
# =====================================

df, mean_score, std_score, max_score, accuracy = make_data(df, ANSWER_KEY)

page1 = dashboard_page(df, mean_score, std_score, max_score, accuracy, ANSWER_KEY)

# =====================================
# Navigation
# =====================================

pg = st.navigation([
    st.Page(
        page1,
        title="ランキング"
    ),
    st.Page(
        question_analysis_page(QUESTIONS, df),
        title="問題分析"
    )
])

pg.run()