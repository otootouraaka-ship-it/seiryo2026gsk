import json
import streamlit as st

# =====================================
# ページ
# =====================================

def omake_page():

    st.title("没問題一覧")

    st.markdown("""
    本番では採用されなかった問題を掲載しています。
    """)

    # =====================================
    # JSON読み込み
    # =====================================

    with open(
        "dropped_questions.json",
        "r",
        encoding="utf-8"
    ) as f:

        questions = json.load(f)

    question_keys = list(
        questions.keys()
    )

    # =====================================
    # session_state
    # =====================================

    if "drop_page" not in st.session_state:

        st.session_state.drop_page = 0

    # =====================================
    # 問題番号入力
    # =====================================

    question_num = st.number_input(
        "問題番号",
        min_value=1,
        max_value=len(question_keys),
        value=st.session_state.drop_page + 1
    )

    st.session_state.drop_page = (
        question_num - 1
    )

    # =====================================
    # 左右ボタン
    # =====================================

    col1, col2, col3 = st.columns([1,2,1])

    with col1:

        if st.button("◀ 前の問題"):

            if st.session_state.drop_page > 0:

                st.session_state.drop_page -= 1

                st.rerun()

    with col3:

        if st.button("次の問題 ▶"):

            if (
                st.session_state.drop_page
                < len(question_keys)-1
            ):

                st.session_state.drop_page += 1

                st.rerun()

    # =====================================
    # 現在問題
    # =====================================

    current_key = question_keys[
        st.session_state.drop_page
    ]

    q = questions[current_key]

    # =====================================
    # 表示
    # =====================================

    st.divider()

    st.subheader(current_key)

    st.markdown(
        f"## {q['question']}"
    )

    st.write("")

    # 選択肢

    for choice_key, choice_text in q["choices"].items():

        st.markdown(
            f"**{choice_key}.** {choice_text}"
        )

    st.write("")

    # 正答

    st.success(
        f"正答：{q['answer']}"
    )

    # 解説

    st.info(
        q["explanation"]
    )