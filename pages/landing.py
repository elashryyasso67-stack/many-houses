import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="manyhouses — Egyptian Real Estate",
    page_icon=":material/home:",
)

st.logo("images/many_houses_logo.jpeg")

st.markdown(
    """
    <style>
    .hero-title {
        font-family: 'Playfair Display', serif;
        font-weight: 700;
        font-size: 3.5rem;
        line-height: 1.1;
        color: #111111;
        margin-bottom: 1rem;
    }
    .hero-subtitle {
        font-family: 'Inter', sans-serif;
        font-weight: 400;
        font-size: 1.25rem;
        color: #444444;
        margin-bottom: 2rem;
        max-width: 600px;
    }
    .gold-accent {
        color: #D4AF37;
    }
    .feature-card {
        border: 1px solid #D4AF37;
        border-radius: 12px;
        padding: 1.5rem;
        height: 100%;
        background: #FFF8E7;
        transition: all 0.2s ease;
    }
    .feature-card:hover {
        background: #D4AF37;
        color: #111111;
    }
    .feature-title {
        font-family: 'Playfair Display', serif;
        font-weight: 600;
        font-size: 1.25rem;
        margin-bottom: 0.5rem;
    }
    .feature-desc {
        font-family: 'Inter', sans-serif;
        font-size: 0.95rem;
        color: #555555;
    }
    .stat-number {
        font-family: 'Playfair Display', serif;
        font-weight: 700;
        font-size: 3rem;
        color: #D4AF37;
        line-height: 1;
    }
    .stat-label {
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        color: #666666;
        margin-top: 0.25rem;
    }
    .cta-button {
        background: #D4AF37 !important;
        color: #111111 !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
        font-size: 1.1rem !important;
    }
    .cta-button:hover {
        background: #C4A030 !important;
    }
    .section-title {
        font-family: 'Playfair Display', serif;
        font-weight: 700;
        font-size: 2.5rem;
        color: #111111;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .section-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        color: #666666;
        text-align: center;
        margin-bottom: 3rem;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }
    .city-badge {
        background: #111111;
        color: #D4AF37;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        font-size: 0.9rem;
        display: inline-block;
        margin: 0.25rem;
    }
    .footer-link {
        color: #D4AF37;
        text-decoration: none;
    }
    .footer-link:hover {
        text-decoration: underline;
    }
    .icon-large {
        font-size: 2.5rem;
        display: block;
        text-align: center;
        margin-bottom: 0.75rem;
    }
    .icon-city {
        font-size: 2.5rem;
        display: block;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============ HERO SECTION ============
with st.container():
    col1, col2 = st.columns([1.2, 1], gap="large")

    with col1:
        st.markdown('<div class="hero-title">Find Your Home<br>in <span class="gold-accent">Egypt</span></div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="hero-subtitle">Verified listings. Transparent pricing. '
            'From Cairo to the Red Sea, Luxor to the New Capital — '
            'your dream property is one search away.</div>',
            unsafe_allow_html=True,
        )

        cta_col1, cta_col2 = st.columns([1, 1], gap="medium")
        with cta_col1:
            if st.button(":material/search: Explore Properties", type="primary", use_container_width=True):
                st.switch_page("pages/home.py")
        with cta_col2:
            if st.button(":material/person_add: List Your Property", type="secondary", use_container_width=True):
                st.switch_page("pages/register.py")

        st.space("small")
        st.caption(":material/lock: No login required to browse  •  :material/favorite: Save favorites across sessions  •  :material/description: Generate contracts in-app")

    with col2:
        st.image("images/manyhouses_baner.png", width="stretch")

# ============ TRUST INDICATORS ============
st.space("large")
st.divider()
st.space("medium")

stats_cols = st.columns(4, gap="medium")
stats = [
    ("10+", "Cities Covered"),
    ("12", "Property Types"),
    ("100%", "Verified Listings"),
    ("0", "Hidden Fees"),
]
for col, (num, label) in zip(stats_cols, stats):
    with col:
        st.markdown(f'<div class="stat-number">{num}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="stat-label">{label}</div>', unsafe_allow_html=True)

# ============ FEATURES ============
st.space("large")
st.markdown('<div class="section-title">Why Choose manyhouses?</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Built for how Egyptians actually buy and rent property</div>', unsafe_allow_html=True)
st.space("medium")

features = [
    (":material/shield:", "Verified Listings", "Every property is photographed, ownership-confirmed, and priced transparently — no surprises at signing."),
    (":material/public:", "National Coverage", "Search across 10+ Egyptian cities: Cairo, Alexandria, Red Sea, Upper Egypt, and the New Capital."),
    (":material/favorite:", "Smart Favorites", "Save properties across cities, compare side-by-side, share with family — no account needed."),
    (":material/description:", "Instant Contracts", "Generate ready-to-sign agreements directly in the app. Legal review optional."),
    (":material/attach_money:", "Zero Hidden Fees", "What you see is what you pay. No service fees, no agent surprises, no fine print."),
    (":material/support_agent:", "Dedicated Support", "Real humans, Saturday–Thursday, 9–6. WhatsApp, email, or call — we answer."),
]

feat_cols = st.columns(3, gap="medium")
for idx, (icon, title, desc) in enumerate(features):
    with feat_cols[idx % 3]:
        with st.container(border=True):
            st.markdown(f'<div class="icon-large">{icon}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="feature-title">{title}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="feature-desc">{desc}</div>', unsafe_allow_html=True)

# ============ CITIES WE SERVE ============
st.space("large")
st.divider()
st.space("medium")

st.markdown('<div class="section-title">We Cover All of Egypt</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">From Mediterranean coast to Red Sea resorts, ancient cities to the new capital</div>', unsafe_allow_html=True)
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
            st.markdown(f"<div class='icon-city'>{icon}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align:center; font-weight:600; color:#111111;'>{city}</div>", unsafe_allow_html=True)
            st.caption("Verified listings available")

# ============ TESTIMONIALS ============
st.space("large")
st.divider()
st.space("medium")

st.markdown('<div class="section-title">What Our Clients Say</div>', unsafe_allow_html=True)
st.space("medium")

testimonials = [
    ("Amina K.", "Cairo", "Found our dream villa in 3 days. The team was incredibly professional and transparent throughout."),
    ("Omar S.", "Hurghada", "Best real estate platform I've used. Verified listings saved me from two scams. Highly recommend."),
    ("Fatima R.", "Alexandria", "Smooth process from viewing to contract. Five stars! :material/star:"),
]

test_cols = st.columns(3, gap="medium")
for col, (name, city, text) in zip(test_cols, testimonials):
    with col:
        with st.container(border=True):
            st.markdown(f"**{name}** — {city}")
            st.caption(f"\"{text}\"")
            st.divider()
            st.write(":material/star: :material/star: :material/star: :material/star: :material/star:")

# ============ CTA SECTION ============
st.space("large")
with st.container(border=True):
    st.markdown(
        """
        <div style="text-align:center; padding: 2rem;">
            <h2 style="font-family:'Playfair Display',serif; font-weight:700; color:#111111; margin-bottom:1rem;">
                Ready to Find Your Home?
            </h2>
            <p style="font-family:'Inter',sans-serif; color:#555555; font-size:1.1rem; margin-bottom:2rem; max-width:600px; margin-left:auto; margin-right:auto;">
                Start searching verified properties across Egypt today. No account needed to browse.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    cta1, cta2, cta3 = st.columns([1, 1, 1], gap="medium")
    with cta1:
        if st.button(":material/search: Browse Properties", type="primary", use_container_width=True):
            st.switch_page("pages/home.py")
    with cta2:
        if st.button(":material/person_add: Register as Agent", type="secondary", use_container_width=True):
            st.switch_page("pages/register.py")
    with cta3:
        if st.button(":material/info: Learn More", type="secondary", use_container_width=True):
            st.switch_page("pages/about.py")

# ============ FOOTER ============
st.space("large")
st.divider()
st.space("small")

footer_cols = st.columns(4, gap="large")
with footer_cols[0]:
    st.markdown("**manyhouses**")
    st.caption("Your trusted partner for Egyptian real estate")
with footer_cols[1]:
    st.markdown("**Quick Links**")
    st.caption("[Properties](pages/home.py)  |  [About](pages/about.py)  |  [FAQ](pages/faq.py)")
    st.caption("[Contact Us](pages/contact_us.py)  |  [Register](pages/register.py)")
with footer_cols[2]:
    st.markdown("**Contact**")
    st.caption(":material/location_on: Cairo, Egypt")
    st.caption(":material/phone: +20 100 000 0000")
    st.caption(":material/email: support@manyhouses.com")
with footer_cols[3]:
    st.markdown("**Follow Us**")
    st.caption("LinkedIn  |  Facebook  |  Instagram  |  Twitter")

st.space("small")
st.caption("© 2025 manyhouses. All rights reserved. | Built with Streamlit")