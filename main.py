import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def dashboard_page(df, mean_score, std_score, max_score, accuracy, ANSWER_KEY):

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