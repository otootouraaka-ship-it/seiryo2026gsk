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

# =====================================
# ページ1
# =====================================

def dashboard_page():

    st.title(
        "げんしけんにじさんじ共通テスト2026 in 清陵祭"
    )

    # =====================
    # メトリクス
    # =====================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "回答人数",
        len(df)
    )

    col2.metric(
        "平均点",
        round(mean_score, 2)
    )

    col3.metric(
        "標準偏差",
        round(std_score, 2)
    )

    col4.metric(
        "正答率",
        f"{accuracy:.1f}%"
    )

    # =====================
    # 得点分布
    # =====================

    st.subheader("得点分布")

    fig, ax = plt.subplots()

    fig.patch.set_alpha(0)

    ax.set_facecolor((0,0,0,0))

    ax.hist(
        df["score"],
        bins=range(max_score + 2),
        alpha=0.3
    )

    st.pyplot(fig)

    # =====================
    # 正答率
    # =====================

    st.subheader("問題別正答率")

    question_accuracy = {}

    for q, setting in ANSWER_KEY.items():

        ans = setting["answer"]

        correct = (
            df[q]
            .astype(str)
            .str.strip()
            == ans
        ).sum()

        rate = correct / len(df) * 100

        question_accuracy[q] = rate

    qa_df = pd.DataFrame({
        "Question": question_accuracy.keys(),
        "Accuracy": question_accuracy.values()
    })

    fig, ax = plt.subplots()

    fig.patch.set_alpha(0)

    ax.set_facecolor((0,0,0,0))

    bars = ax.bar(
        qa_df["Question"],
        qa_df["Accuracy"],
        alpha=0.3
    )

    ax.set_ylim(0, 100)

    for bar in bars:

        height = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width()/2,
            height + 1,
            f"{height:.1f}%",
            ha='center'
        )

    st.pyplot(fig)

    # =====================
    # ランキング
    # =====================

    st.subheader("ランキング")

    ranking_df = df[[
        "ハンドルネーム",
        "score",
        "hensachi",
        "rank"
    ]].copy()

    ranking_df = ranking_df.sort_values(
        by=["score", "hensachi"],
        ascending=False
    )

    ranking_df = ranking_df.reset_index(drop=True)

    ranking_df = ranking_df[[
        "rank",
        "ハンドルネーム",
        "score",
        "hensachi"
    ]]

    ranking_df.columns = [
        "順位",
        "名前",
        "得点",
        "偏差値"
    ]

    ITEMS_PER_PAGE = 10

    total_items = len(ranking_df)

    total_pages = (
        total_items - 1
    ) // ITEMS_PER_PAGE + 1

    if "page" not in st.session_state:
        st.session_state.page = 0

    col1, col2, col3 = st.columns([1,2,1])

    with col1:

        if st.button("◀ 前へ"):

            if st.session_state.page > 0:
                st.session_state.page -= 1

    with col3:

        if st.button("次へ ▶"):

            if st.session_state.page < total_pages - 1:
                st.session_state.page += 1

    start_idx = (
        st.session_state.page
        * ITEMS_PER_PAGE
    )

    end_idx = start_idx + ITEMS_PER_PAGE

    page_df = ranking_df.iloc[
        start_idx:end_idx
    ]

    st.write(
        f"ページ {st.session_state.page + 1} / {total_pages}"
    )

    st.dataframe(
        page_df,
        hide_index=True,
        use_container_width=True
    )

# =====================================
# ページ2
# =====================================

def question_analysis_page():

    st.title("問題別選択率")

    if "question_page" not in st.session_state:
        st.session_state.question_page = 0

    question_input = st.number_input(
        "問題番号",
        min_value=1,
        max_value=len(QUESTIONS),
        value=st.session_state.question_page + 1
    )

    st.session_state.question_page = (
        question_input - 1
    )

    col1, col2, col3 = st.columns([1,2,1])

    with col1:

        if st.button("◀ 前の問題"):

            if st.session_state.question_page > 0:
                st.session_state.question_page -= 1

    with col3:

        if st.button("次の問題 ▶"):

            if st.session_state.question_page < len(QUESTIONS)-1:
                st.session_state.question_page += 1

    current_question = QUESTIONS[
        st.session_state.question_page
    ]

    st.header(current_question)

    counts = (
        df[current_question]
        .astype(str)
        .value_counts()
    )

    percentages = (
        counts / counts.sum()
    ) * 100

    analysis_df = pd.DataFrame({
        "Choice": percentages.index,
        "Percentage": percentages.values
    })

    display_df = analysis_df.copy()

    display_df["Percentage"] = (
        display_df["Percentage"]
        .round(1)
        .astype(str)
        + "%"
    )

    st.dataframe(
        display_df,
        hide_index=True,
        use_container_width=True
    )

    fig, ax = plt.subplots()

    fig.patch.set_alpha(0)

    ax.set_facecolor((0,0,0,0))

    bars = ax.bar(
        analysis_df["Choice"],
        analysis_df["Percentage"],
        alpha=0.3
    )

    ax.set_ylim(0, 100)

    for bar in bars:

        height = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width()/2,
            height + 1,
            f"{height:.1f}%",
            ha='center'
        )

    st.pyplot(fig)

# =====================================
# Navigation
# =====================================

pg = st.navigation([
    st.Page(
        dashboard_page,
        title="ランキング"
    ),

    st.Page(
        question_analysis_page,
        title="問題分析"
    )
])

pg.run()