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

unique_seasons = sorted(schedule_grouped['season'].unique(), reverse=True)
season_options = st.multiselect(
    "Season", 
    options=["All"] + unique_seasons,  
    default = ["All"] 
)

unique_weeks = sorted(schedule_grouped['week'].unique(), reverse=True)
week_options = st.multiselect(
    "Week", 
    options=["All"] + unique_weeks,  
    default = ["All"] 
)


st.write(" ")

schedule_grouped = schedule_grouped.loc[schedule_grouped["total_pts"]!=0]

if "All" not in season_options:
    schedule_grouped = schedule_grouped[schedule_grouped["season"].isin(season_options)]

if "All" not in week_options:
    schedule_grouped = schedule_grouped[schedule_grouped["week"].isin(week_options)]



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


