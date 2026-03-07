import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Netflix Data Analysis", layout="wide")

# Load dataset
df = pd.read_csv("data/netflix_titles.csv")

df["date_added"] = df["date_added"].str.strip()
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

df["year_added"] = df["date_added"].dt.year

# Sidebar
st.sidebar.title("Netflix Dashboard")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dataset Overview",
        "Movies vs TV Shows",
        "Top Countries",
        "Content Growth",
        "Release Year Distribution"
    ]
)

# Page 1
if page == "Dataset Overview":

    st.title("Netflix Dataset Overview")

    st.write("Dataset Shape:", df.shape)

    st.dataframe(df.head())

# Page 2
elif page == "Movies vs TV Shows":

    st.title("Movies vs TV Shows")

    fig, ax = plt.subplots()

    sns.countplot(data=df, x="type", ax=ax)

    st.pyplot(fig)

# Page 3
elif page == "Top Countries":

    st.title("Top Producing Countries")

    top_countries = df["country"].value_counts().head(10)

    fig, ax = plt.subplots()

    top_countries.plot(kind="bar", ax=ax)

    ax.set_ylabel("Number of Titles")

    st.pyplot(fig)

# Page 4
elif page == "Content Growth":

    st.title("Content Added Over Time")

    yearly = df["year_added"].value_counts().sort_index()

    fig, ax = plt.subplots()

    yearly.plot(ax=ax)

    ax.set_ylabel("Number of Titles")

    st.pyplot(fig)

# Page 5
elif page == "Release Year Distribution":

    st.title("Distribution of Release Years")

    fig, ax = plt.subplots()

    sns.histplot(df["release_year"], bins=30, ax=ax)

    st.pyplot(fig)