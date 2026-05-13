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
    ### 「にじさんじ共通テスト(仮)」
    の統計やランキングが閲覧できるサイトです！
    
    - 回答者全体の統計データ
    - 問題別の選択率
    - ランキング
    - 正答率や得点分布

    などをリアルタイムで閲覧できます！
                
    """)

    st.divider()

    st.subheader("ページ一覧")

    col1, col2 = st.columns(2)

    # =========================
    # 統計
    # =========================

    with col1:

        st.markdown("### 📊 統計データ")

        st.write(
            "平均点・標準偏差などを表示します。"
        )

        if st.button(
            "統計データへ",
            use_container_width=True
        ):

            st.query_params["page"] = "page2"

            st.rerun()

    # =========================
    # 問題別
    # =========================

    with col2:

        st.markdown("### 📝 問題別データ")

        st.write(
            "問題ごとの選択率を表示します。"
        )

        if st.button(
            "問題別データへ",
            use_container_width=True
        ):

            st.query_params["page"] = "page3"

            st.rerun()

    st.write("")

    col3, col4 = st.columns(2)

    # =========================
    # ランキング
    # =========================

    with col3:

        st.markdown("### 🏆 ランキング")

        st.write(
            "ランキングと偏差値を表示します。"
        )

        if st.button(
            "ランキングへ",
            use_container_width=True
        ):

            st.query_params["page"] = "page4"

            st.rerun()

    # =========================
    # システム情報
    # =========================

    with col4:

        st.markdown("### ℹ️ システム情報")

        st.info(
            "データは60秒ごとに更新されます。"
        )