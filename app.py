import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('INvideos.csv', encoding='latin1')
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['publish_hour'] = df['publish_time'].dt.hour

# Optional: Map category_id to names
category_map = {
    1: "Film & Animation", 10: "Music", 23: "Comedy", 24: "Entertainment", 25: "News & Politics"
}
df['category_name'] = df['category_id'].map(category_map)

# App layout
st.set_page_config(page_title="YouTube India Trends", layout="wide")
st.title("🇮🇳 YouTube Trending Insights - India")

# Category chart
st.subheader("Top Categories by Views")
category_views = df.groupby('category_name')['views'].sum().sort_values()
st.bar_chart(category_views)

# Publish hour chart
st.subheader("Engagement by Publish Hour")
hourly = df.groupby('publish_hour')[['likes', 'comment_count']].mean()
st.line_chart(hourly)

# Top videos
st.subheader("Top 10 Most Liked Videos")
top_liked = df.sort_values('likes', ascending=False).head(10)
st.write(top_liked[['title', 'channel_title', 'likes', 'views']])
