# =====================================
# import
# =====================================
import json
import streamlit as st

from streamlit_autorefresh import st_autorefresh

from background import set_bg_image
from Google_Sheets import access_sheets
from calc import make_data
from main import main_page
from rate_question import question_analysis_page
from whole_analysis import whole_analysis_page
from ranking import ranking_page

# =====================================
# ページのコンフィグ設定
# =====================================

st.set_page_config(
    page_title="げんしけんにじさんじ共通テスト2026 in 清陵祭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# 自動更新
# =====================================

st_autorefresh(
    interval=60000,
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

# =====================================
# ページ1
# =====================================

def page1():

    main_page()

# =====================================
# ページ2
# =====================================

def page2():

    whole_analysis_page(df, mean_score, std_score, max_score, accuracy, ANSWER_KEY)

# =====================================
# ページ3
# =====================================

def page3():

    question_analysis_page(QUESTIONS, df)

# =====================================
# ページ4
# =====================================

def page4():

    ranking_page(df)

# =====================================
# Navigation
# =====================================

pg = st.navigation([
    st.Page(
        page1,
        title="ホーム"
    ),

    st.Page(
        page2,
        title="統計データ"
    ),

    st.Page(
        page3,
        title="問題別データ"
    ),

    st.Page(
        page4,
        title="ランキング"
    )
])

pg.run()