import streamlit as st
from data import properties


st.set_page_config(
    layout="wide",
    page_icon=":material/email:",
    page_title="Contact us",
)

st.logo("images/many_houses_logo.jpeg")
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

        property_names = ["No specific property"] + [item["name"] for item in properties]
        selected_property = st.session_state.get("selected_property")
        default_property = selected_property if selected_property in property_names else property_names[0]
        property_index = property_names.index(default_property)
        property_name = st.selectbox("Property", property_names, index=property_index)

        preferred_contact = st.radio(
            "Preferred way to contact you",
            ["Email", "Phone", "WhatsApp"],
            horizontal=True,
        )
        message = st.text_area("Message", height=150, placeholder="Write your question here...")
        submitted = st.form_submit_button("Send message", width="stretch")

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
    st.write(":material/email: **Email**")
    st.write("support@manyhouses.com")
    st.write(":material/phone: **Phone**")
    st.write("+20 100 000 0000")
    st.write(":material/location_on: **Office**")
    st.write("Cairo, Egypt")

    with st.expander("Before you contact us"):
        st.write("For a faster response, include the property name, your preferred viewing date, and your budget.")