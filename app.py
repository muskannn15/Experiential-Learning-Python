import time
import streamlit as st

st.set_page_config(page_title="Stopwatch Web App", page_icon="⏱️")
st.title("⏱️ Simple Stopwatch")

# Session state initialize karein
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "elapsed_time" not in st.session_state:
    st.session_state.elapsed_time = 0.0
if "laps" not in st.session_state:
    st.session_state.laps = []


def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:05.2f}"


# Elapsed time calculate karein
current_time = st.session_state.elapsed_time
if st.session_state.start_time is not None:
    current_time += time.perf_counter() - st.session_state.start_time

st.header(format_time(current_time))

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("▶️ Start"):
        if st.session_state.start_time is None:
            st.session_state.start_time = time.perf_counter()
            st.rerun()

with col2:
    if st.button("⏹️ Stop"):
        if st.session_state.start_time is not None:
            st.session_state.elapsed_time += (
                time.perf_counter() - st.session_state.start_time
            )
            st.session_state.start_time = None
            st.rerun()

with col3:
    if st.button("🔄 Reset"):
        st.session_state.start_time = None
        st.session_state.elapsed_time = 0.0
        st.session_state.laps = []
        st.rerun()

with col4:
    if st.button("🚩 Lap"):
        if st.session_state.start_time is not None:
            st.session_state.laps.append(format_time(current_time))
            st.rerun()
        else:
            st.warning("Stopwatch start karein pehle!")

if st.session_state.laps:
    st.subheader("Laps")
    for idx, lap in enumerate(st.session_state.laps, 1):
        st.write(f"Lap {idx}: {lap}")