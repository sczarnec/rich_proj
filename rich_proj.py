import streamlit as st
import pandas as pd
import numpy as np
import csv

st.title("Here you go, Rich:")

st.write(" ")
st.write(" ")

schedule = pd.read_csv("schedule.csv")
schedule["total_pts"] = schedule["away_score"] + schedule["home_score"]

schedule_grouped = (
    schedule
    .groupby(["season", "week", "game_type"])["total_pts"]
    .sum()
    .reset_index()
    .sort_values(["season", "week"], ascending=False)
)
schedule_grouped = schedule_grouped.loc[schedule_grouped["total_pts"]!=0]



st.dataframe(schedule_grouped)

st.write(" ")

@st.cache_data
def df_to_csv_bytes(df):
    return df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇️ Download as CSV",
    data=df_to_csv_bytes(schedule_grouped),
    file_name="richs_cool_data.csv",
    mime="text/csv",
)


