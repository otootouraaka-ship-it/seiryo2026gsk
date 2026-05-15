# =====================================
# import
# =====================================
import json
import streamlit as st

from streamlit_autorefresh import st_autorefresh

from setting import setting
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
    page_title="げんしけんにじさんじ共通テスト2026 in 清陵祭", # リンク先として表示される名前
    layout="wide", # 画面いっぱいにサイト内容を表示する
    initial_sidebar_state="expanded" # サイドバーを拡張して表示する
)

# =====================================
# 自動更新
# =====================================

st_autorefresh(
    interval=60000, # 60000ms(60s, すなわち一分)間隔でデータを自動更新する
    key="refresh" # 追加ではなくrefreshのみ
)

# =====================================
# サイト設定
# =====================================

setting("1765439594403.png", "Morning_2.mp3") # サイトの背景とかフォントとかを設定している

# =====================================
# Google Sheets
# =====================================

df = access_sheets() # Google APIを用いてGoogle Spreadsheetのデータを持ってきている

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

def main():

    main_page()

# =====================================
# ページ2
# =====================================

def whole_analysis():

    whole_analysis_page(df, mean_score, std_score, max_score, accuracy, ANSWER_KEY)

# =====================================
# ページ3
# =====================================

def question_analysis():

    question_analysis_page(QUESTIONS, df)

# =====================================
# ページ4
# =====================================

def ranking():

    ranking_page(df)

# =====================================
# Navigation
# =====================================

pages = [

    st.Page(
        main,
        title="ホーム"
    ),

    st.Page(
        whole_analysis,
        title="統計データ"
    ),

    st.Page(
        question_analysis,
        title="問題別データ"
    ),

    st.Page(
        ranking,
        title="ランキング"
    )
]

pg = st.navigation(pages)

pg.run()