import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sydney Events", layout="wide")

st.title("🎶 Sydney Events")
st.write("Live events happening in Sydney, Australia")

df = pd.read_csv("events.csv")

for _, row in df.iterrows():
    with st.container():
        st.subheader(row["title"])
        st.write(f"📅 {row['date']}")

        with st.form(key=row["title"]):
            email = st.text_input("Enter your email to get tickets")
            opt_in = st.checkbox("Notify me about similar events")
            submitted = st.form_submit_button("GET TICKETS")

            if submitted:
                st.success("Redirecting you to ticket page...")
                st.markdown(
                    f"[Click here if not redirected]({row['link']})",
                    unsafe_allow_html=True
                )

        st.divider()
