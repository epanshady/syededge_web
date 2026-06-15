import streamlit as st

# 1. Konfigurasi Halaman Web
st.set_page_config(
    page_title="SYEDEDGE PLUS (SE+) | Electronic Supplier",
    page_icon="⚡",
    layout="wide"
)

# 2. Sistem Navigasi (Sidebar)
st.sidebar.title("SE+ Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Company Profile", "Product Catalog", "Submit PO / RFQ"])

# Maklumat Syarikat (Footer / Contact Info)
st.sidebar.markdown("---")
st.sidebar.markdown("**Contact Us:**")
st.sidebar.markdown("📧 syededgeplus99@gmail.com")
st.sidebar.markdown("📍 809 Kuching Street, 26600 Pekan, Johor")

# ==========================================
# HALAMAN 1: HOME
# ==========================================
if page == "Home":
    st.title("⚡ SYEDEDGE PLUS (SE+)")
    st.subheader("Your Trusted Partner in Microcontrollers & Electronic Components")
    
    st.image("https://images.unsplash.com/photo-1608564697171-252559d5743c?auto=format&fit=crop&q=80&w=1200", 
             caption="Empowering Students, Hobbyists, and Industries with High-Quality Tech Hardware.")
    
    st.markdown("""
    ### Welcome to SYEDEDGE PLUS
    We bridge the gap between high-grade industrial hardware and accessible components for innovators. 
    Whether you are a university student working on your Final Year Project (FYP), a passionate hobbyist, 
    or a corporate buyer, we supply the exact tools you need to build the future.
    
    **Our Core Offerings:**
    * 🛠️ Microcontrollers & Development Boards (Arduino, ESP32, Raspberry Pi)
    * 🔌 Industrial Networking & Automation (Cisco Switches, PLCs)
    * ⚙️ Essential Electronic Components & Power Supplies
    """)
    
    st.info("💡 **Notice for Corporate Buyers:** We accept institutional Purchase Orders (PO) and support NET 30 payment terms.")

# ==========================================
# HALAMAN 2: COMPANY PROFILE
# ==========================================
elif page == "Company Profile":
    st.title("📁 Company Profile")
    st.write("Learn more about our vision, mission, and who we serve.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Our Mission")
        st.write("To provide seamless B2B procurement and accessible retail solutions for electronic prototyping, ensuring that creators at all levels have access to reliable components.")
        
    with col2:
        st.markdown("### Our Vision")
        st.write("To become the leading and most trusted electronic hardware supplier in the region, empowering the next generation of engineers and tech entrepreneurs.")

    st.markdown("---")
    st.markdown("### Why Settle for Less? Choose SE+")
    st.markdown("""
    * **Student & Hobbyist Friendly:** We sell in retail units for individual creators, but we maintain the infrastructure of a bulk supplier.
    * **Fast Shipment:** All domestic orders are dispatched rapidly via our trusted logistics partner, **DHL Express**.
    * **Rigorous Quality Check:** Every microcontroller, switch, and cable undergoes standard testing before dispatch.
    """)

# ==========================================
# HALAMAN 3: PRODUCT CATALOG
# ==========================================
elif page == "Product Catalog":
    st.title("📦 Supplier Catalog")
    st.write("Browse our available electronic devices. Click 'Submit PO / RFQ' in the sidebar to request a formal quotation.")
    
    # Kategori 1: Microcontrollers
    st.markdown("### 🤖 Microcontrollers & Proto-boards")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Arduino Opta Lite")
        st.caption("Item Code: W17 | Category: Industrial IoT")
        st.write("Price: **RM 690.00**")
    with c2:
        st.subheader("Arduino Giga R1")
        st.caption("Item Code: W11 | Category: Advanced Development")
        st.write("Price: **RM 399.00**")
        
    st.markdown("---")
    
    # Kategori 2: Networking & Infrastructure
    st.markdown("### 🔌 Networking & Power Infrastructure")
    c3, c4, c5 = st.columns(3)
    with c3:
        st.subheader("Cisco WS-C2960-48TC-L")
        st.caption("Item Code: MCL40 | Category: Network Switch")
        st.write("Price: **RM 750.00**")
    with c4:
        st.subheader("Corsair Power Supply CX750")
        st.caption("Item Code: SF25 | Category: Power Delivery")
        st.write("Price: **RM 305.00**")
    with c5:
        st.subheader("Vention Cat8 8M Cable")
        st.caption("Item Code: RB21 | Category: Cabling")
        st.write("Price: **RM 24.00**")

# ==========================================
# HALAMAN 4: SUBMIT PO / RFQ
# ==========================================
elif page == "Submit PO / RFQ":
    st.title("📝 Request for Quote (RFQ) / Submit Purchase Order")
    st.write("Are you representing a university club, industrial plant, or companies like **MFC Trading**? Submit your requirements below.")
    
    with st.form("procurement_form"):
        company_name = st.text_input("Company / Institution Name", placeholder="e.g., MFC Trading / Universiti Malaysia Pahang")
        contact_person = st.text_input("Contact Person Name")
        email = st.text_input("Email Address")
        
        po_number = st.text_input("Existing Purchase Order Number (If applicable)", placeholder="e.g., #1258820")
        
        items_needed = st.text_area("List down the items and quantity required", 
                                    placeholder="e.g.,\n1. Arduino Opta Lite - 5 units\n2. Cisco Switch - 4 units")
        
        submitted = st.form_submit_button("Submit Request to SE+ Sales Team")
        
        if submitted:
            if company_name and email and items_needed:
                st.success(f"Thank you, {contact_person}. Your request for {company_name} has been received. Our procurement team will contact you within 24 hours with a formal Invoice under Net 30 terms.")
            else:
                st.error("Please fill in all the required fields (Name, Email, and Items Needed).")