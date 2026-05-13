import base64
import streamlit as st

def set_bg_image(image_file):

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