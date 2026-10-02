import streamlit as st
from data import properties

st.set_page_config(
    layout="wide",
    page_title="Create contract",
    page_icon=":material/description:",
)

st.logo("images/many_houses_logo.jpeg")
st.title(":material/description: Create a Property Contract")
st.caption("Complete the details below to prepare a contract draft.")

property_names = [item["name"] for item in properties]
selected_name = st.session_state.get("selected_property")
selected_index = property_names.index(selected_name) if selected_name in property_names else 0

selected_property_name = st.selectbox("Select Property", property_names, index=selected_index)
property_data = next(item for item in properties if item["name"] == selected_property_name)

sidebar_col, main_col = st.columns([1, 4], gap="medium")

with sidebar_col:
    if property_data.get("image"):
        st.image(property_data["image"], width="stretch")
    with st.container(border=True):
        st.subheader(":material/home: Property Summary")
        st.write(f"**{property_data['type']}**")
        st.caption(property_data["place"])
        st.write(f":material/bed: {property_data['rooms']} rooms")
        st.write(f":material/bathtub: {property_data['bathrooms']} bathrooms")
        st.write(f":material/expand: {property_data['area']} sq ft")
        st.write(f":material/attach_money: ${property_data['price']:,}")

    with st.container(border=True):
        st.subheader(":material/person: Customer")
        customer_name = st.text_input("Full name", key="sidebar_name")

with main_col:
    with st.form("contract_form"):
        st.subheader(":material/home: Property details")
        contract_type = st.selectbox("Contract type", ["Sale", "Rent"])

        st.write(
            f"**{property_data['type']}** in {property_data['place']} · "
            f"{property_data['area']} sq ft · {property_data['rooms']} rooms · "
            f"Listed price: ${property_data['price']:,}"
        )

        st.divider()

        st.subheader(":material/person: Customer details")
        national_id = st.text_input("National ID")
        phone = st.text_input("Phone number")
        address = st.text_input("Address")

        st.divider()

        st.subheader(":material/payments: Payment and dates")
        total_price = st.number_input("Agreed price", min_value=0.0, value=float(property_data["price"]), step=1000.0)
        deposit = st.number_input("Deposit", min_value=0.0, max_value=total_price, step=1000.0)
        start_date = st.date_input("Contract start date")
        end_date = st.date_input("Contract end date")
        payment_method = st.selectbox("Payment method", ["Cash", "Bank transfer", "Installments"])

        st.divider()

        st.subheader(":material/rule: Terms")
        extra_terms = st.text_area("Additional terms")
        accepted = st.checkbox("I confirm that the information entered is correct.")
        create_button = st.form_submit_button("Create contract draft", use_container_width=True)

if create_button:
    if not customer_name.strip() or not national_id.strip() or not phone.strip():
        st.error("Please enter the full name, national ID, and phone number.")
    elif end_date < start_date:
        st.error("The contract end date cannot be before the start date.")
    elif not accepted:
        st.error("Please confirm that the entered information is correct.")
    else:
        contract_text = f"""PROPERTY CONTRACT DRAFT

Customer: {customer_name}
National ID: {national_id}
Phone: {phone}
Address: {address}

Property: {property_data['name']}
Type: {property_data['type']}
Location: {property_data['place']}
Contract type: {contract_type}
Agreed price: ${total_price:,.2f}
Deposit: ${deposit:,.2f}
Payment method: {payment_method}
Start date: {start_date}
End date: {end_date}

Additional terms:
{extra_terms or 'None'}

This is a draft and should be reviewed by a legal professional before signing.
"""
        st.success("Contract draft created successfully.")
        st.download_button(
            "Download contract draft",
            contract_text,
            file_name="property_contract.txt",
            mime="text/plain",
            use_container_width=True,
        )
