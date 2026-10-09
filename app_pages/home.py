import streamlit as st
from data import PROPERTIES

# How many property cards sit side by side in one row. Three fits a wide screen.
CARDS_PER_ROW = 3

st.set_page_config(
    layout="wide",
    page_title="manyhouses",
    page_icon=":material/home:",
)

st.image("images/manyhouses_baner.png", width="stretch")


def pick_property(name):
    # Remember which property was picked, so the Details page knows what to show.
    st.session_state.selected_property = name


search = st.text_input("Search properties", placeholder="Search by name, city, or type")

# Keep a property if the search words appear in its name, city or type.
shown = PROPERTIES
if search:
    search_term = search.lower()
    shown = []
    for item in PROPERTIES:
        name = item["name"].lower()
        place = item["place"].lower()
        kind = item["type"].lower()
        if search_term in name or search_term in place or search_term in kind:
            shown.append(item)

if not shown:
    st.warning("No properties match your search.")
    st.stop()

for start in range(0, len(shown), CARDS_PER_ROW):
    row_items = shown[start:start + CARDS_PER_ROW]

    with st.container(horizontal=True, border=True):
        cols = st.columns(len(row_items))
        for col, item in zip(cols, row_items):
            with col:
                with st.container(border=True):
                    st.image(item["image"], width="stretch")
                    st.subheader(item["name"])
                    st.caption(f"{item['type']} • {item['place']}")
                    st.write(f":material/attach_money: Price: ${item['price']:,}")
                    st.write(f":material/bed: Rooms: {item['rooms']}")
                    st.write(f":material/bathtub: Bathrooms: {item['bathrooms']}")
                    st.write(f":material/expand: Area: {item['area']} sq ft")

                    # The heart adds the property to favorites, or removes it if it is already there.
                    is_fav = item["name"] in st.session_state.favorites
                    if is_fav:
                        fav_label = ":material/favorite: Favorites"
                    else:
                        fav_label = ":material/favorite_border: Add to Favorites"
                    if st.button(fav_label, key=f"fav_{item['name']}"):
                        if is_fav:
                            st.session_state.favorites.remove(item["name"])
                        else:
                            st.session_state.favorites.append(item["name"])
                        st.rerun()

                    # The callback runs before this page redraws, so the menu already has Details when we switch.
                    if st.button("View Details", key=f"details_{item['name']}", on_click=pick_property, args=(item["name"],)):
                        st.switch_page("app_pages/details.py")
