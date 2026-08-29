import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(page_title="Multi-Agent Research System", page_icon="🔎", layout="wide")

st.title("🔎 Multi-Agent Research System")
st.caption("Search Agent → Reader Agent → Writer Chain → Critic Chain")

# Keep results across reruns (e.g. when switching tabs)
if "result" not in st.session_state:
    st.session_state.result = None

with st.form("research_form"):
    topic = st.text_input("Research topic", placeholder="e.g. Latest advances in solid-state batteries")
    submitted = st.form_submit_button("Run Research", type="primary")

if submitted:
    if not topic.strip():
        st.warning("Please enter a topic before running the pipeline.")
    else:
        status_box = st.status("Running multi-agent pipeline...", expanded=True)
        try:
            status_box.write("Step 1/4 — Search agent gathering information...")
            status_box.write("Step 2/4 — Reader agent scraping top source...")
            status_box.write("Step 3/4 — Writer drafting the report...")
            status_box.write("Step 4/4 — Critic reviewing the report...")

            # This call runs all 4 steps internally (pipeline.py also prints to the
            # terminal it's launched from, which is fine to ignore here).
            result = run_research_pipeline(topic)
            st.session_state.result = result
            st.session_state.topic = topic

            status_box.update(label="Pipeline complete ✅", state="complete", expanded=False)
        except Exception as e:
            status_box.update(label="Pipeline failed ❌", state="error", expanded=True)
            st.error(f"Something went wrong: {e}")

# Display results
if st.session_state.result:
    result = st.session_state.result
    st.divider()
    st.subheader(f"Results for: {st.session_state.get('topic', '')}")

    tab_report, tab_critic, tab_search, tab_scraped = st.tabs(
        ["📄 Final Report", "🧐 Critic Feedback", "🔍 Search Results", "📰 Scraped Content"]
    )

    with tab_report:
        st.markdown(result.get("report", "_No report generated._"))
        st.download_button(
            "Download report as .md",
            data=str(result.get("report", "")),
            file_name="research_report.md",
            mime="text/markdown",
        )

    with tab_critic:
        st.markdown(result.get("feedback", "_No feedback generated._"))

    with tab_search:
        st.text(result.get("search_results", "_No search results._"))

    with tab_scraped:
        st.text(result.get("scraped_content", "_No scraped content._"))
else:
    st.info("Enter a topic above and click **Run Research** to start.")