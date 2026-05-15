import pandas as pd
import streamlit as st
import json
import gspread

from google.oauth2.service_account import Credentials

def access_sheets():
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets"
    ]

    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=SCOPES
    )

    client = gspread.authorize(creds)

    SHEET_URL = "https://docs.google.com/spreadsheets/d/1tAHJJx2lAC0MFWzAMdkcd70RUBgCdn21zOAWhYs3rGo/edit?resourcekey=&gid=796447487#gid=796447487"

    sheet = client.open_by_url(
        SHEET_URL
    ).sheet1

    data = sheet.get_all_records()

    df = pd.DataFrame(data)

    return df