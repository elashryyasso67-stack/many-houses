import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="about",
    page_icon=":material/info:",
)

st.title(":material/home: About manyhouses")
st.caption("Your trusted partner for Egyptian real estate")

st.divider()

st.subheader(":material/account_balance: Our Mission")
st.write(
    "At manyhouses, we connect you with the best properties across Egypt. "
    "Whether you're looking for a luxury apartment in Cairo or a beach house "
    "in Sharm El Sheikh, we make finding your dream home simple and stress-free."
)

st.subheader(":material/location_on: Market Coverage")
st.caption("Serving buyers and renters across all major Egyptian cities.")

cities = [
    ("Cairo", ":material/home:"),
    ("Giza", ":material/house:"),
    ("Alexandria", ":material/waves:"),
    ("Hurghada", ":material/beach_access:"),
    ("Sharm El Sheikh", ":material/sunny:"),
    ("Luxor", ":material/eco:"),
    ("Aswan", ":material/water:"),
    ("Marsa Alam", ":material/water_drop:"),
    ("Siwa", ":material/landscape:"),
    ("New Administrative Capital", ":material/construction:"),
]

# Show the cities five to a row.
cols = st.columns(5, gap="medium")
for idx, (city, icon) in enumerate(cities):
    with cols[idx % 5]:
        with st.container(border=True):
            st.write(f"{icon} {city}")

st.space("small")

st.subheader(":material/support: Why Choose Us")
cols = st.columns(3, gap="medium")
with cols[0]:
    with st.container(border=True):
        st.write(":material/shield: Verified Listings")
        st.caption("Every property is verified and photographed.")
with cols[1]:
    with st.container(border=True):
        st.write(":material/payment: No Hidden Fees")
        st.caption("Transparent pricing from start to finish.")
with cols[2]:
    with st.container(border=True):
        st.write(":material/support_agent: Dedicated Support")
        st.caption("Our team is here for you, Saturday to Thursday.")

st.space("small")

# These quotes are sample placeholders, not real client reviews. Replace them before launch.
st.subheader(":material/star: Sample Client Feedback")
testimonials = [
    ("Amina K.", "Cairo", "Found our dream villa in 3 days. The team was incredibly professional."),
    ("Omar S.", "Hurghada", "Best real estate platform I've used. Highly recommend it."),
    ("Fatima R.", "Alexandria", "Smooth process from viewing to contract. Five stars! ⭐"),
]
for name, city, text in testimonials:
    with st.container(border=True):
        st.write(f"**{name}** — {city}")
        st.caption(f"“{text}”")
        st.divider()

st.space("small")

st.subheader(":material/location_on: Our Office")
st.caption("📍 Cairo, Egypt")
st.caption("📞 +20 100 000 0000")
st.caption("📧 support@manyhouses.com")
st.caption("🕐 Saturday to Thursday, 9:00 AM — 6:00 PM")
