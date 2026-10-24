
import streamlit as st

from datetime import date
from storage import load_invoices, save_invoice

st.set_page_config(
    page_title="Unified Business Hub",
    page_icon="🏢",
    layout="wide",
)

st.title("Unified Business Hub")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Businesses", "Invoices", "Reports", "Settings"],
)

if page == "Dashboard":
    st.header("Dashboard")

    business = st.selectbox(
        "Select Business",
        ["My Business"],
    )

    
    # Calculate dashboard totals from saved invoice records.
    invoices = load_invoices()

    invoice_count = len(invoices)

    expenses = sum(
        float(invoice.get("amount", 0))
        for invoice in invoices
    )

    # Revenue tracking is planned for a future module.
    revenue = 0.0
    profit = revenue - expenses


    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Revenue", f"${revenue:,.2f}")
    col2.metric("Expenses", f"${expenses:,.2f}")
    col3.metric("Profit", f"${profit:,.2f}")
    col4.metric("Invoices", invoice_count)

    st.subheader("Revenue Chart")
    st.info("Revenue data will appear here when records are available.")

    st.divider()

    st.subheader("Upload Invoice")
    uploaded_file = st.file_uploader(
        "Choose an invoice",
        type=["pdf", "png", "jpg", "jpeg"],
    )

    if uploaded_file:
        st.success(f"Selected file: {uploaded_file.name}")
        st.info("Automated invoice extraction is planned for a later module.")


elif page == "Invoices":
    st.header("Invoice Management")

    st.subheader("Add New Invoice")

    with st.form("invoice_form", clear_on_submit=True):
        vendor = st.text_input("Vendor / Supplier Name")
        invoice_number = st.text_input("Invoice Number")
        invoice_date = st.date_input("Invoice Date", value=date.today())
        amount = st.number_input(
            "Invoice Amount ($)",
            min_value=0.0,
            step=0.01,
            format="%.2f",
        )
        description = st.text_area("Description")

        submitted = st.form_submit_button("Save Invoice")

        if submitted:
            if not vendor.strip() or not invoice_number.strip():
                st.error("Vendor name and invoice number are required.")
            else:
                invoice = {
                    "business": "My Business",
                    "vendor": vendor.strip(),
                    "invoice_number": invoice_number.strip(),
                    "date": invoice_date.isoformat(),
                    "amount": amount,
                    "description": description.strip(),
                }

                try:
                    save_invoice(invoice)
                    st.success("Invoice saved successfully!")
                except OSError:
                    st.error("Could not save the invoice. Check file permissions.")

    st.divider()

    
    st.subheader("Saved Invoices")
    invoices = load_invoices()

    if invoices:
        search_term = st.text_input(
            "Search invoices",
            placeholder="Enter vendor name or invoice number",
        )

        filtered_invoices = [
            invoice
            for invoice in invoices
            if search_term.strip().lower()
            in str(invoice.get("vendor", "")).lower()
            or search_term.strip().lower()
            in str(invoice.get("invoice_number", "")).lower()
        ]

        st.caption(
            f"Showing {len(filtered_invoices)} of {len(invoices)} invoices"
        )

        if filtered_invoices:
            st.dataframe(
                filtered_invoices,
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.warning("No invoices match your search.")
    else:
        st.info("No invoices have been saved yet.")


elif page == "Businesses":
    st.header("Businesses")
    st.info("Business management is planned for a future module.")

elif page == "Reports":
    st.header("Reports")
    st.info("Reporting features are planned for a future module.")

elif page == "Settings":
    st.header("Settings")
    st.info("Settings will be added later.")
