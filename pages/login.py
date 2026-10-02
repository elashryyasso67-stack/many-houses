import streamlit as st

st.set_page_config(
    layout="centered",
    page_title="Login",
    page_icon=":material/person:",
)

st.logo("images/many_houses_logo.jpeg")
st.title("manyhouses")
st.caption("Find your dream home in Egypt")

with st.container(border=True):
    email = st.text_input(":material/email: Email", placeholder="you@example.com")
    password = st.text_input(":material/lock: Password", type="password", placeholder="Enter your password")

    login_btn = st.button("Sign in", use_container_width=True)

    if login_btn:
        if not email.strip():
            st.error("Please enter your email.")
        elif not password.strip():
            st.error("Please enter your password.")
        else:
            st.switch_page("pages/home.py")

    st.divider()
    st.caption("Don't have an account?")
    st.button("Create an account", use_container_width=True, on_click=lambda: st.switch_page("pages/register.py"))

    st.divider()
    st.caption("Already have an account?")
    st.button(":material/favorite: View Favorites", use_container_width=True, on_click=lambda: st.switch_page("pages/favorites.py"))
