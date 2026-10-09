import streamlit as st
from data import find_property

st.set_page_config(
    layout="wide",
    page_title="favorites",
    page_icon=":material/favorite:",
)

st.title(":material/favorite: Your Favorites")
st.caption("Properties you've saved for later.")

favorites = st.session_state.favorites

if not favorites:
    st.info("You haven't saved any properties yet.")
    st.caption("Browse our listings and click the heart icon to save a property.")
else:
    st.write(f"**{len(favorites)}** property/favorites saved.")
    st.divider()

    for name in favorites:
        item = find_property(name)
        if item:
            with st.container(border=True):
                col1, col2 = st.columns([1, 3], gap="medium")
                with col1:
                    st.image(item["image"], width=150)
                with col2:
                    st.subheader(item["name"])
                    st.caption(f"{item['type']} • {item['place']}")
                    st.write(f":material/attach_money: ${item['price']:,}")
                    st.write(f":material/bed: {item['rooms']} rooms • :material/bathtub: {item['bathrooms']} • :material/expand: {item['area']} sq ft")
                    if st.button("View Details", key=f"fav_detail_{item['name']}"):
                        st.session_state.selected_property = item["name"]
                        st.switch_page("app_pages/details.py")
                if st.button(":material/favorite:", key=f"remove_fav_{item['name']}"):
                    st.session_state.favorites.remove(item["name"])
                    st.rerun()
