import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def whole_analysis_page(df, mean_score, std_score, max_score, accuracy, ANSWER_KEY):

    st.title(
        "統計データ"
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

    col5, col6 = st.columns(2)

    # =====================
    # 得点分布
    # =====================

    with col5:

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

    with col6:

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

    