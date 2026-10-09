import streamlit as st

# Favorites are a list of property names. They last only while this browser session lasts.
if "favorites" not in st.session_state:
    st.session_state.favorites = []

st.logo("images/many_houses_logo.jpeg")

# Every screen is one file in app_pages/.
sign_in_page = st.Page("app_pages/login.py", title="Sign in", icon=":material/person:", default=True)
register_page = st.Page("app_pages/register.py", title="Register", icon=":material/person_add:")
welcome_page = st.Page("app_pages/landing.py", title="Welcome", icon=":material/storefront:")
home_page = st.Page("app_pages/home.py", title="Properties", icon=":material/search:")
details_page = st.Page("app_pages/details.py", title="Property details", icon=":material/house:")
favorites_page = st.Page("app_pages/favorites.py", title="Favorites", icon=":material/favorite:")
contract_page = st.Page("app_pages/contract.py", title="Contract", icon=":material/description:")
faq_page = st.Page("app_pages/faq.py", title="FAQ", icon=":material/help:")
about_page = st.Page("app_pages/about.py", title="About", icon=":material/info:")
contact_page = st.Page("app_pages/contact_us.py", title="Contact us", icon=":material/email:")

# Property details only shows in the menu after a property has been picked,
# because the page has nothing to show before that.
menu_pages = [sign_in_page, register_page, welcome_page, home_page]
if st.session_state.get("selected_property"):
    menu_pages.append(details_page)
menu_pages += [favorites_page, contract_page, faq_page, about_page, contact_page]

menu = st.navigation(menu_pages)
menu.run()
