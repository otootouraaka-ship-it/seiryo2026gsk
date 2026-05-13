import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def question_analysis_page(QUESTIONS, df):

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

    col4, col5 = st.columns(2)

    with col4:

        st.dataframe(
            display_df,
            hide_index=True,
            use_container_width=True
        )

    with col5:

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