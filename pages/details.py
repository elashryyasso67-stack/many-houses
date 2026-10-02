import pandas as pd
import streamlit as st
from data import properties

st.set_page_config(
    layout="wide",
    page_title="manyhouses",
    page_icon=":material/home:",
)

st.logo("images/many_houses_logo.jpeg")

selected_property = st.session_state.get("selected_property")
if not selected_property:
    st.warning("No property selected.")
    st.stop()

item = next((p for p in properties if p["name"] == selected_property), None)
if not item:
    st.warning("Selected property was not found.")
    st.stop()

st.image(item["image"], width=500)

st.title(item["name"])
st.caption(f":material/location_on: {item['place']} · :material/house: {item['type']}")

is_fav = item["name"] in st.session_state.favorites
fav_icon = ":material/favorite:" if is_fav else ":material/favorite_border:"
if st.button(f"{fav_icon} {'' if is_fav else 'Add to'} Favorites", key="fav_detail"):
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
        st.metric(":material/bed:", str(item['rooms']))
    with c3:
        st.metric(":material/bathtub:", str(item['bathrooms']))
    with c4:
        st.metric(":material/expand:", f"{item['area']} sq ft")

st.space("small")

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

if "latitude" in item and "longitude" in item:
    with st.expander(":material/map: Location on Map", expanded=False):
        map_data = pd.DataFrame([{"lat": item["latitude"], "lon": item["longitude"]}])
        st.map(map_data, zoom=12)
