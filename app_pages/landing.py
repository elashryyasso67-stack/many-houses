import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="manyhouses — Egyptian Real Estate",
    page_icon=":material/home:",
)

# Colours and fonts come from .streamlit/config.toml. Only these few layout rules need CSS.
st.markdown(
    """
    <style>
    .hero-title { font-size: 3.5rem; line-height: 1.1; margin-bottom: 1rem; }
    .gold-text { color: #D4AF37; }
    .stat-number { font-size: 3rem; font-weight: 700; color: #D4AF37; line-height: 1; }
    .centered { text-align: center; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============ HERO ============
hero_text, hero_image = st.columns([1.2, 1], gap="large")

with hero_text:
    st.markdown(
        '<h1 class="hero-title">Find Your Home<br>in <span class="gold-text">Egypt</span></h1>',
        unsafe_allow_html=True,
    )
    st.write(
        "Photos, prices and details for properties from Cairo to the Red Sea, "
        "Luxor to the New Capital. Your next home is one search away."
    )

    explore_col, list_col = st.columns(2, gap="medium")
    with explore_col:
        if st.button(":material/search: Explore Properties", type="primary", width="stretch"):
            st.switch_page("app_pages/home.py")
    with list_col:
        if st.button(":material/person_add: List Your Property", width="stretch"):
            st.switch_page("app_pages/register.py")

    st.space("small")
    st.caption(
        ":material/lock: No login required to browse  •  "
        ":material/favorite: Save favorites while you browse  •  "
        ":material/description: Make contract drafts in the app"
    )

with hero_image:
    st.image("images/manyhouses_baner.png", width="stretch")

# ============ TRUST NUMBERS ============
st.space("large")
st.divider()
st.space("medium")

# These numbers are counted from the property list in data.py.
stats = [
    ("10+", "Cities Covered"),
    ("4", "Property Types"),
    ("12", "Sample Listings"),
    ("0", "Hidden Fees"),
]
stat_cols = st.columns(4, gap="medium")
for col, (number, label) in zip(stat_cols, stats):
    with col:
        st.markdown(f'<div class="stat-number">{number}</div>', unsafe_allow_html=True)
        st.caption(label)

# ============ FEATURES ============
st.space("large")
st.markdown('<h2 class="centered">Why Choose manyhouses?</h2>', unsafe_allow_html=True)
st.caption("Built for how Egyptians actually buy and rent property")
st.space("medium")

features = [
    (":material/shield:", "Photos and Details", "Every property has a photo, a price, and its rooms, bathrooms and area."),
    (":material/public:", "National Coverage", "Search across 10+ Egyptian cities: Cairo, Alexandria, Red Sea, Upper Egypt, and the New Capital."),
    (":material/favorite:", "Favorites", "Save properties with the heart button. Your saved list lasts for this visit."),
    (":material/description:", "Contract Drafts", "Fill in a form and download a contract draft as a text file. Have a lawyer review it before signing."),
    (":material/attach_money:", "Zero Hidden Fees", "What you see is what you pay. No service fees, no agent surprises, no fine print."),
    (":material/support_agent:", "Contact Us", "Send a message from the Contact Us page. Our team's hours are Saturday to Thursday, 9 AM to 6 PM."),
]

feat_cols = st.columns(3, gap="medium")
for idx, (icon, title, desc) in enumerate(features):
    with feat_cols[idx % 3]:
        with st.container(border=True):
            st.markdown(f'<div class="centered stat-number">{icon}</div>', unsafe_allow_html=True)
            st.subheader(title)
            st.write(desc)

# ============ CITIES ============
st.space("large")
st.divider()
st.space("medium")

st.markdown('<h2 class="centered">We Cover All of Egypt</h2>', unsafe_allow_html=True)
st.caption("From the Mediterranean coast to Red Sea resorts, ancient cities to the new capital.")
st.space("medium")

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

city_cols = st.columns(5, gap="medium")
for idx, (city, icon) in enumerate(cities):
    with city_cols[idx % 5]:
        with st.container(border=True):
            st.markdown(f'<div class="centered stat-number" style="font-size:2rem;">{icon}</div>', unsafe_allow_html=True)
            st.markdown(f"<div class='centered'><b>{city}</b></div>", unsafe_allow_html=True)
            st.caption("Listings available")

# ============ SAMPLE FEEDBACK ============
st.space("large")
st.divider()
st.space("medium")

st.markdown('<h2 class="centered">Sample Client Feedback</h2>', unsafe_allow_html=True)
st.caption("Placeholder quotes. Replace them with real client feedback before launch.")
st.space("medium")

testimonials = [
    ("Amina K.", "Cairo", "Found our dream villa in 3 days. The team was incredibly professional."),
    ("Omar S.", "Hurghada", "Best real estate platform I've used. Highly recommend."),
    ("Fatima R.", "Alexandria", "Smooth process from viewing to contract. Five stars!"),
]

test_cols = st.columns(3, gap="medium")
for col, (name, city, text) in zip(test_cols, testimonials):
    with col:
        with st.container(border=True):
            st.markdown(f"**{name}** — {city}")
            st.caption(f"\"{text}\"")

# ============ CALL TO ACTION ============
st.space("large")
with st.container(border=True):
    st.markdown('<h2 class="centered">Ready to Find Your Home?</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="centered">Start searching properties across Egypt today. No account needed to browse.</p>',
        unsafe_allow_html=True,
    )
    browse_col, register_col, about_col = st.columns(3, gap="medium")
    with browse_col:
        if st.button(":material/search: Browse Properties", type="primary", width="stretch"):
            st.switch_page("app_pages/home.py")
    with register_col:
        if st.button(":material/person_add: Register", width="stretch"):
            st.switch_page("app_pages/register.py")
    with about_col:
        if st.button(":material/info: Learn More", width="stretch"):
            st.switch_page("app_pages/about.py")

# ============ FOOTER ============
st.space("large")
st.divider()
st.space("small")

footer_cols = st.columns(3, gap="large")
with footer_cols[0]:
    st.markdown("**manyhouses**")
    st.caption("Your trusted partner for Egyptian real estate")
with footer_cols[1]:
    st.markdown("**Quick Links**")
    st.page_link("app_pages/home.py", label="Properties")
    st.page_link("app_pages/about.py", label="About")
    st.page_link("app_pages/faq.py", label="FAQ")
    st.page_link("app_pages/contact_us.py", label="Contact Us")
with footer_cols[2]:
    st.markdown("**Contact**")
    st.caption(":material/location_on: Cairo, Egypt")
    st.caption(":material/phone: +20 100 000 0000")
    st.caption(":material/email: support@manyhouses.com")

st.space("small")
st.caption("© 2025 manyhouses. All rights reserved. | Built with Streamlit")
