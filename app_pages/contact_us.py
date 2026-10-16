import streamlit as st
from data import PROPERTIES

st.set_page_config(
    layout="wide",
    page_icon=":material/email:",
    page_title="Contact us",
)

st.title("Contact us")
st.write("Tell us what you are looking for and our property team will get back to you.")

left_column, right_column = st.columns([2, 1], gap="large")

with left_column:
    with st.form("contact_form"):
        st.subheader("Send us a message")

        full_name = st.text_input("Full name")
        email = st.text_input("Email address")
        phone = st.text_input("Phone number")

        inquiry_type = st.selectbox(
            "How can we help?",
            ["Ask about a property", "Schedule a viewing", "Ask about a contract", "General question"],
        )

        # The dropdown starts with "No specific property", then lists every property name.
        property_names = ["No specific property"]
        for item in PROPERTIES:
            property_names.append(item["name"])

        # If the user came here from a property, start the dropdown on that property.
        selected_property = st.session_state.get("selected_property")
        default_property = property_names[0]
        if selected_property in property_names:
            default_property = selected_property
        property_index = property_names.index(default_property)
        property_name = st.selectbox("Property", property_names, index=property_index)

        preferred_contact = st.radio(
            "Preferred way to contact you",
            [ "Phone", "WhatsApp"],
            horizontal=True,
        )
        message = st.text_area("Message", height=150, placeholder="Write your question here...")
        submitted = st.form_submit_button("Send message", type="primary", width="stretch")

    # Nothing is sent anywhere. We only check the boxes and show a thank-you.
    if submitted:
        if not full_name.strip() or not email.strip() or not message.strip():
            st.error("Please enter your name, email address, and message.")
        else:
            st.success("Thanks! Your message has been received. We will contact you soon.")
            st.write(
                f"We will contact you by **{preferred_contact}** about "
                f"**{property_name}**."
            )

with right_column:
    st.subheader("Our contact details")
    st.info("Our team is available Saturday to Thursday, 9:00 AM to 6:00 PM.")
    st.write("support@manyhouses.com")
    st.write(":material/phone: **Phone**")
    st.write("+20 100 147 9499")
    st.write(":material/location_on: **Office**")
    st.write("kafr el sheikh, Egypt")

    with st.expander("Before you contact us"):
        st.write("For a faster response, include the property name, your preferred viewing date, and your budget...for better contact, use whatsapp")
