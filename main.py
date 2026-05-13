import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

import streamlit as st

def main_page():

    # =========================
    # タイトル
    # =========================

    st.title(
        "げんしけんにじさんじ共通テスト2026 in 清陵祭"
    )

    # =========================
    # 説明文
    # =========================

    st.markdown("""
    ## 企画詳細

    このサイトは、2026年清陵祭企画「げんしけん博覧会」で実施した
                ###「にじさんじ共通テスト(仮)」
    の統計やランキングが閲覧できるサイトです！
    
    - 回答者全体の統計データ
    - 問題別の選択率
    - ランキング
    - 正答率や得点分布

    などをリアルタイムで閲覧できます！
                
    """)

    st.divider()

    # =========================
    # 遷移ボタン
    # =========================

    st.subheader("ページ一覧")

    col1, col2 = st.columns(2)

    # -------------------------
    # 統計データ
    # -------------------------

    with col1:

        st.markdown("### 📊 統計データ")

        st.write(
            "平均点・標準偏差・正答率などを表示します。"
        )

        if st.button(
            "統計データを見る",
            use_container_width=True
        ):

            st.switch_page("統計データ")

    # -------------------------
    # 問題別データ
    # -------------------------

    with col2:

        st.markdown("### 📝 問題別データ")

        st.write(
            "各問題の選択肢選択率を表示します。"
        )

        if st.button(
            "問題別データを見る",
            use_container_width=True
        ):

            st.switch_page("問題別データ")

    st.write("")

    col3, col4 = st.columns(2)

    # -------------------------
    # ランキング
    # -------------------------

    with col3:

        st.markdown("### 🏆 ランキング")

        st.write(
            "ランキングを表示します。目指せ1位！！！"
        )

        if st.button(
            "ランキングを見る",
            use_container_width=True
        ):

            st.switch_page("ランキング")

    # -------------------------
    # おまけ
    # -------------------------

    with col4:

        st.markdown("### ℹ️ システム情報")

        st.write(
            "Streamlit + Google Sheets により動作しています。"
        )

        st.info(
            "回答は約60秒ごとに自動更新されます。"
        )