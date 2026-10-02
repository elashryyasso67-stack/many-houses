import streamlit as st

if "favorites" not in st.session_state:
    st.session_state.favorites = []

import pages.login
