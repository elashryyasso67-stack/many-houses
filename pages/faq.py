import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="faq",
    page_icon=":material/help:",
)

st.logo("images/many_houses_logo.jpeg")
st.title(":material/help: Frequently Asked Questions")
st.caption("Everything you need to know about manyhouses.")

st.divider()

faqs = [
    {
        "q": "How do I search for properties?",
        "a": "Use the search bar on the home page to find properties by name, city, or type. You can also browse all listings."
    },
    {
        "q": "Can I save properties for later?",
        "a": "Yes! Click the heart icon on any property card or detail page to add it to your favorites. You can view all saved properties on the Favorites page."
    },
    {
        "q": "Is there a cost to use manyhouses?",
        "a": "No. Our platform is free for buyers and renters. There are no hidden fees whatsoever."
    },
    {
        "q": "How can I schedule a viewing?",
        "a": "Contact us through the Contact Us page or use the property details page to request a viewing. Our team will respond within 24 hours."
    },
    {
        "q": "What cities do you cover?",
        "a": "We cover all major Egyptian cities including Cairo, Giza, Alexandria, Hurghada, Sharm El Sheikh, Luxor, Aswan, Marsa Alam, Siwa, and the New Administrative Capital."
    },
    {
        "q": "How do I create a contract?",
        "a": "Go to any property and click 'Create contract' from the contract page. Fill in your details and we'll prepare a draft for you."
    },
    {
        "q": "Do I need an account to view properties?",
        "a": "No, you can browse all listings without an account. However, creating an account lets you save favorites and manage your inquiries."
    },
    {
        "q": "Can I negotiate the price?",
        "a": "Yes! The listed price is a starting point. Use the contract form to propose your agreed price and terms."
    },
]

for faq in faqs:
    with st.expander(faq["q"], expanded=False):
        st.write(faq["a"])
        st.divider()

st.space("small")

st.subheader(":material/support_agent: Still have questions?")
st.caption("Reach out to us at support@manyhouses.com or call +20 100 000 0000.")
st.button("Contact Us", use_container_width=True, on_click=lambda: st.switch_page("pages/contact_us.py"))
