import base64
import streamlit as st

def backimg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()

    encoded = base64.b64encode(data).decode()

    page_bg_img = f"""
    <style>

    .stApp {{
        background-image:
            linear-gradient(
                rgba(0,0,0,0.5),
                rgba(0,0,0,0.5)
            ),
            url("data:image/png;base64,{encoded}");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    </style>
    """

    st.markdown(
        page_bg_img,
        unsafe_allow_html=True
    )

def font():
    st.markdown("""
        <style>

        /* Google Fonts 読み込み */
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

        /* 全体へ適用 */
        html, body, [class*="css"] {

            font-family: 'Noto Sans JP', sans-serif;
        }

        </style>
        """, unsafe_allow_html=True)

def bgm(bgm_file):

    with open(bgm_file, "rb") as f:
        data = f.read()

    b64 = base64.b64encode(data).decode()

    md = f"""
    <audio autoplay loop>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    st.markdown(
        md,
        unsafe_allow_html=True
    )



def setting(image_file, bgm_file):

    backimg(image_file)
    font()
    bgm(bgm_file)