import streamlit as st

st.set_page_config(
    layout="centered",
    page_title="Sign in",
    page_icon=":material/person:",
)

st.title("manyhouses")
st.caption("Find your dream home in Egypt")

with st.container(border=True):
    email = st.text_input(":material/email: Email", placeholder="you@example.com")
    password = st.text_input(":material/lock: Password", type="password", placeholder="Enter your password")

    # Nothing is checked or saved. We only make sure the boxes are not empty.
    if st.button("Sign in", type="primary", width="stretch"):
        if not email.strip():
            st.error("Please enter your email.")
        elif not password.strip():
            st.error("Please enter your password.")
        else:
            st.switch_page("app_pages/home.py")

    st.divider()
    st.caption("Don't have an account?")
    if st.button("Create an account", width="stretch"):
        st.switch_page("app_pages/register.py")

    st.divider()
    st.caption("Already have an account?")
    if st.button(":material/favorite: View Favorites", width="stretch"):
        st.switch_page("app_pages/favorites.py")
