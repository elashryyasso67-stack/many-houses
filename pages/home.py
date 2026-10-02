import streamlit as st
from data import properties

st.set_page_config(
    layout = "wide",
    page_title = "manyhouses",
    page_icon=":material/home:"
)

st.logo("images/many_houses_logo.jpeg")
st.image("images/manyhouses_baner.png", width="stretch")

search = st.text_input("Search properties", placeholder="Search by name, city, or type")

filtered_properties = properties
if search:
    search_term = search.lower()
    filtered_properties = [
        item for item in properties
        if search_term in item["name"].lower()
        or search_term in item["place"].lower()
        or search_term in item["type"].lower()
    ]

if not filtered_properties:
    st.warning("No properties match your search.")
    st.stop()

for i in range(0, len(filtered_properties), 3):
    row_items = filtered_properties[i:i + 3]

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

                    is_fav = item["name"] in st.session_state.favorites
                    fav_icon = ":material/favorite:" if is_fav else ":material/favorite_border:"
                    if st.button(f"{fav_icon} {'' if is_fav else 'Add to'} Favorites", key=f"fav_{item['name']}"):
                        if is_fav:
                            st.session_state.favorites.remove(item["name"])
                        else:
                            st.session_state.favorites.append(item["name"])
                        st.rerun()

                    if st.button("View Details" , use_container_width=True  , key=f"details_{item['name']}"):
                        st.session_state.selected_property = item["name"]
                        st.switch_page("pages/details.py")
