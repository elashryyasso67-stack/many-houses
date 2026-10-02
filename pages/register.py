import streamlit as st

st.set_page_config(
    layout="centered",
    page_title="Register",
    page_icon=":material/person_add:",
)

st.logo("images/many_houses_logo.jpeg")
st.title("manyhouses")
st.caption("Create your account to get started")

with st.container(border=True):
    email = st.text_input(":material/email: Email", placeholder="you@example.com")
    password = st.text_input(":material/lock: Password", type="password", placeholder="Create a password")
    age = st.number_input(":material/calendar_today: Age", min_value=18, max_value=120, value=25)
    address = st.text_input(":material/location_on: Address", placeholder="Your city")
    birth_date = st.date_input(":material/calendar_today: Date of birth")

    register_btn = st.button("Register", use_container_width=True)

    if register_btn:
        if not email.strip():
            st.error("Please enter your email.")
        elif not password.strip():
            st.error("Please enter a password.")
        else:
            st.success("Account created!")
            st.switch_page("pages/home.py")

    st.divider()
    st.caption("Already have an account?")
    if  st.button("Sign in", use_container_width=True):
           st.switch_page("pages/login.py")

    st.divider()
    st.caption("View saved properties?")
    st.button(":material/favorite: View Favorites", use_container_width=True, on_click=lambda: st.switch_page("pages/favorites.py"))
