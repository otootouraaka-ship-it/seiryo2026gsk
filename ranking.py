import streamlit as st

def ranking_page(df):
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