import streamlit as st
from data import find_property

st.set_page_config(
    layout="wide",
    page_title="manyhouses",
    page_icon=":material/home:",
)

selected_name = st.session_state.get("selected_property")
if not selected_name:
    st.warning("No property selected.")
    st.stop()

item = find_property(selected_name)
if item is None:
    st.warning("Selected property was not found.")
    st.stop()

st.image(item["image"], width=500)

st.title(item["name"])
st.caption(f":material/location_on: {item['place']} · :material/house: {item['type']}")

is_fav = item["name"] in st.session_state.favorites
if is_fav:
    fav_label = ":material/favorite: Favorites"
else:
    fav_label = ":material/favorite_border: Add to Favorites"
if st.button(fav_label, key="fav_detail"):
    if is_fav:
        st.session_state.favorites.remove(item["name"])
    else:
        st.session_state.favorites.append(item["name"])
    st.rerun()

st.space("small")

with st.container(horizontal=True, border=True):
    c1, c2, c3, c4 = st.columns(4, gap="medium")
    with c1:
        st.metric(":material/attach_money:", f"${item['price']:,}")
    with c2:
        st.metric(":material/bed:", str(item["rooms"]))
    with c3:
        st.metric(":material/bathtub:", str(item["bathrooms"]))
    with c4:
        st.metric(":material/expand:", f"{item['area']} sq ft")

st.space("small")

# Only one listing has a second photo, so this box is empty for most properties.
with st.expander(":material/image: Gallery", expanded=False):
    if item.get("image2"):
        st.image(item["image2"], width=400)

st.space("small")

with st.expander(":material/analytics: Property Details", expanded=False):
    with st.container(border=True):
        st.write(f":material/label: **Type:** {item['type']}")
        st.write(f":material/location_on: **City:** {item['place']}")
        st.write(f":material/expand: **Area:** {item['area']} sq ft")
        st.write(f":material/bed: **Rooms:** {item['rooms']}")
        st.write(f":material/bathtub: **Bathrooms:** {item['bathrooms']}")

st.space("small")

with st.expander(":material/map: Location on Map", expanded=False):
    # st.map takes a plain dict with lat and lon lists, so pandas is not needed.
    st.map({"lat": [item["latitude"]], "lon": [item["longitude"]]}, zoom=12)
