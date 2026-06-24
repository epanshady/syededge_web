import streamlit as st

# ==========================================
# 1. PAGE CONFIGURATION & FIXING THE WHITE THEME CSS
# ==========================================
st.set_page_config(
    page_title="SYEDEDGE PLUS (SE+) | Corporate Portal",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a Clean White Theme WITHOUT blinding out the text and expanders
st.markdown("""
    <style>
    /* Main body background to clean white */
    .stApp {
        background-color: #ffffff;
    }
    
    /* 🚨 MEMAKSA SEMUA TAJUK BESAR (st.title / h1) MENJADI WARNA NAVY BLUE PEKAT 🚨 */
    h1, [data-testid="stHeader"] h1 {
        color: #1A365D !important;
        font-weight: bold !important;
    }
    
    /* Sidebar background setup */
    [data-testid="stSidebar"] {
        background-color: #f8fafc !important;
        border-right: 1px solid #e2e8f0;
    }
    
    /* FIXING SIDEBAR TEXT COLOR: Make navigation text clearly visible in Navy Blue */
    [data-testid="stSidebar"] .stRadio div label p {
        color: #1A365D !important;
        font-weight: 500 !important;
        font-size: 15px !important;
    }
    [data-testid="stSidebar"] h3, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #1A365D !important;
    }
    
    /* FIXING EXPANDER / DROPDOWN: Ensure header and internal content remain fully visible */
    .stExpander {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
        margin-bottom: 15px !important;
    }
    .stExpander details summary p {
        color: #1A365D !important;
        font-weight: bold !important;
        font-size: 16px !important;
    }
    .stExpander div[data-testid="stMarkdownContainer"] p, 
    .stExpander div[data-testid="stMarkdownContainer"] li {
        color: #333333 !important;
    }
    
    /* Styled Corporate Cards - Electric Blue Left Border */
    .corporate-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 12px;
        border-left: 6px solid #00A3E0;
        border-top: 1px solid #e2e8f0;
        border-right: 1px solid #e2e8f0;
        border-bottom: 1px solid #e2e8f0;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }
    .corporate-card h4, .corporate-card h5 {
        color: #1A365D !important;
        font-weight: bold;
    }
    .corporate-card p {
        color: #333333 !important;
    }
    
    /* Certificate Cards (SSM & MOF) */
    .cert-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #e2e8f0;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.01);
    }
    .cert-header {
        color: #1A365D !important;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    /* Banner/Header Text Styling from image_4541e1.png */
    .home-header {
        color: #1A365D;
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        margin-top: 15px;
        margin-bottom: 20px;
        letter-spacing: 0.5px;
    }
    .home-subheader {
        color: #1A365D;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin-top: 25px;
        margin-bottom: 15px;
    }
    .footer-slogan {
        color: #1A365D;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SIDEBAR NAVIGATION
# ==========================================
try:
    st.sidebar.image("logo_short.png", use_container_width=True)
except:
    st.sidebar.subheader("[ SE+ LOGO ]")

st.sidebar.markdown("<h3 style='text-align: center; margin-top:-10px; color: #1A365D;'>%s</h3>" % "SYEDEDGE PLUS", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #00A3E0; font-style: italic; font-size:13px;'>\"From Components to Creativity\"</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "PORTAL NAVIGATION",
    ["Home", "About Us", "Our Products", "Certificates", "Contact Us"]
)

st.sidebar.markdown("---")
st.sidebar.caption("📍 HQ: Kota Tinggi, Johor")
st.sidebar.caption("© 2026 SYEDEDGE PLUS (SE+). All Rights Reserved.")

# ==========================================
# 3. MENU CONTENT: HOME
# ==========================================
if menu == "Home":
    col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
    with col_l2:
        try:
            st.image("logo_long.png", use_container_width=True)
        except:
            st.warning("⚠️ [logo_long.png file not found in directory]")

    st.markdown("<div class='home-header'>CONNECTING IDEAS WITH TECHNOLOGY</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 800px; margin: 0 auto; text-align: center; font-size: 16px; line-height: 1.8; color: #333333;">
        <p>SyedEdge Plus is dedicated to providing quality electronic components that empower innovation, education, and technological growth.</p>
        <p>Through reliable products, professional service, and a passion for technology, we continue to support the next generation of creators, developers, and innovators.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='home-subheader'>Building Connections. Driving Innovation. Creating Possibilities.</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 800px; margin: 25px auto 10px auto;">
        <div style="background-color: #1A365D; color: white; padding: 12px; border-radius: 6px; text-align: center; margin-bottom: 10px; font-weight: 500;">
            📍 &nbsp; Kota Tinggi, Johor, Malaysia
        </div>
        <div style="background-color: #7A92B5; color: white; padding: 12px; border-radius: 6px; text-align: center; margin-bottom: 10px; font-weight: 500;">
            ✉️ &nbsp; hq_2026@syededgempire
        </div>
        <div style="background-color: #6C7D93; color: white; padding: 12px; border-radius: 6px; text-align: center; font-weight: 500;">
            🌐 &nbsp; www.syededgeplus.com
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='footer-slogan'>Powering Ideas, Enabling Innovation.</div>", unsafe_allow_html=True)

# ==========================================
# 4. MENU CONTENT: ABOUT US
# ==========================================
elif menu == "About Us":
    st.title("🏢 About Us")
    st.markdown("Please use the dropdowns below to explore our official corporate structure and identity:")
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.expander("📖 About Company & Background", expanded=True):
        st.markdown("""
        <div class="corporate-card">
            <h4 style="margin-top:0;">SyedEdge Plus</h4>
            <p style="text-align: justify; line-height: 1.6;">
                SyedEdge Plus was established in May 2026 in Kota Tinggi, Johor by two young entrepreneurs, 
                Syed Muhammad Irfan Bin Syed Abd Razib and Muhammad Imran Hakim Bin Latif.
            </p>
            <p style="text-align: justify; line-height: 1.6;">
                The company specializes in supplying high quality microcontrollers and electronic development 
                boards to students, hobbyists, educators, and technology enthusiasts throughout Malaysia.
            </p>
            <p style="text-align: justify; line-height: 1.6;">
                With a commitment to quality, reliability, and customer satisfaction, SyedEdge Plus provides 
                genuine products at competitive prices while ensuring excellent customer service and support.
            </p>
            <p style="text-align: justify; line-height: 1.6;">
                Our primary focus is on supplying popular development platforms such as ESP32, Arduino Uno, 
                Raspberry Pi, and Wemos boards, enabling customers to access the technology they need for 
                learning, experimentation, and project development.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🎯 Our Vision & Mission", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background-color: #ffffff; padding: 20px; border-radius: 8px; border-top: 4px solid #1A365D; border-left: 1px solid #e2e8f0; border-right: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0; box-shadow: 0 2px 4px rgba(0,0,0,0.01);">
                <h4 style="color: #1A365D; margin-top:0;">👁️ Vision</h4>
                <p style="text-align: justify; font-size: 15px; line-height: 1.6;">
                    To be the leading supplier of microcontrollers and electronic development boards in Malaysia, 
                    empowering the next generation of innovators and creators through accessible and high-quality technology.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div style="background-color: #ffffff; padding: 20px; border-radius: 8px; border-top: 4px solid #00A3E0; border-left: 1px solid #e2e8f0; border-right: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0; box-shadow: 0 2px 4px rgba(0,0,0,0.01);">
                <h4 style="color: #00A3E0; margin-top:0;">🚀 Mission</h4>
                <ul style="padding-left: 20px; font-size: 15px; line-height: 1.6; margin-bottom:0;">
                    <li>To provide a comprehensive range of genuine microcontrollers and electronic development boards at competitive prices.</li>
                    <li>To deliver exceptional customer service, technical support, and guidance to ensure customer success.</li>
                    <li>To foster a culture of creativity, learning, and innovation among students, hobbyists, and educators.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("👥 Executive Team & Organization Chart", expanded=False):
        st.markdown("<h4 style='color: #1A365D; text-align: center; margin-bottom: 25px;'>Organization Structure</h4>", unsafe_allow_html=True)
        
        st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center; font-family: sans-serif; margin-bottom: 30px;">
            <div style="background-color: #1A365D; color: white; padding: 12px 25px; border-radius: 6px; text-align: center; width: 80%; max-width: 450px;">
                <b style="font-size: 14px; color: white !important;">SYED MUHAMMAD IRFAN BIN SYED ABD RAZIB</b><br><span style="color: #00A3E0; font-size: 12.5px;">Co-Founder & Chief Executive Officer (CEO)</span>
            </div>
            <div style="font-size: 18px; color: #1A365D; margin: 5px 0;">⬇️</div>
            <div style="background-color: #1A365D; color: white; padding: 12px 25px; border-radius: 6px; text-align: center; width: 80%; max-width: 450px;">
                <b style="font-size: 14px; color: white !important;">MUHAMMAD IMRAN HAKIM BIN LATIF</b><br><span style="color: #00A3E0; font-size: 12.5px;">Co-Founder & Operations Manager</span>
            </div>
            <div style="font-size: 18px; color: #1A365D; margin: 5px 0;">⬇️</div>
            <div style="display: flex; gap: 10px; justify-content: center; width: 100%; max-width: 800px; flex-wrap: wrap;">
                <div style="background-color: #f1f5f9; border: 1px solid #cbd5e1; color: #1A365D; padding: 10px; border-radius: 6px; text-align: center; flex: 1; min-width: 200px; font-weight: bold; font-size: 12px;">SALES & MARKETING DIVISION</div>
                <div style="background-color: #f1f5f9; border: 1px solid #cbd5e1; color: #1A365D; padding: 10px; border-radius: 6px; text-align: center; flex: 1; min-width: 200px; font-weight: bold; font-size: 12px;">CUSTOMER SERVICE DIVISION</div>
                <div style="background-color: #f1f5f9; border: 1px solid #cbd5e1; color: #1A365D; padding: 10px; border-radius: 6px; text-align: center; flex: 1; min-width: 200px; font-weight: bold; font-size: 12px;">INVENTORY & LOGISTICS DIVISION</div>
            </div>
        </div>
        <hr style="border-top: 1px solid #e2e8f0; margin-bottom:25px;">
        """, unsafe_allow_html=True)
        
        st.markdown("<h4 style='color: #1A365D; margin-bottom:15px;'>1. CEO Portfolio Summary</h4>", unsafe_allow_html=True)
        ceo_col1, ceo_col2 = st.columns([1, 3])
        with ceo_col1:
            try: st.image("ceo.png", use_container_width=True)
            except: st.info("👤 [ceo.png Image]")
        with ceo_col2:
            st.markdown("<h5 style='color:#1A365D;'>SYED MUHAMMAD IRFAN BIN SYED ABD RAZIB</h5>", unsafe_allow_html=True)
            st.markdown("<p style='color: #00A3E0; font-weight: bold; margin-top:-10px;'>Co-Founder & Chief Executive Officer (CEO)</p>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**🎓 Education:**\n* Bachelor of Technology in Industrial Electronic Automation with Honours (2024-2028)\n* Diploma in Electronic Technology (2023)\n* Malaysian Skills Certificate Level 3 in Electronic Technology (2022)")
            with c2:
                st.markdown("**🎯 Roles:**\n* Lead the company's strategic direction and growth.\n* Represent the company in business meetings and partnerships.\n* Oversee overall business operations and decision making.")
        st.markdown("""
        <div style="background-color: #f8fafc; padding: 12px; border-left: 4px solid #1A365D; margin-top: 10px; margin-bottom: 25px; font-size:13.5px; color:#333333;">
            <b>💼 Key Responsibilities:</b> Develop business plans and objectives • Manage company finances and budgeting • Build supplier & stakeholder relationships • Monitor performance & identify growth • Ensure service quality & customer satisfaction.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<h4 style='color: #1A365D; margin-bottom:15px;'>2. Operations Manager Portfolio Summary</h4>", unsafe_allow_html=True)
        coo_col1, coo_col2 = st.columns([1, 3])
        with coo_col1:
            try: st.image("coo.png", use_container_width=True)
            except: st.info("👤 [coo.png Image]")
        with coo_col2:
            st.markdown("<h5 style='color:#1A365D;'>MUHAMMAD IMRAN HAKIM BIN LATIF</h5>", unsafe_allow_html=True)
            st.markdown("<p style='color: #00A3E0; font-weight: bold; margin-top:-10px;'>Co-Founder & Operations Manager</p>", unsafe_allow_html=True)
            cx1, cx2 = st.columns(2)
            with cx1:
                st.markdown("**🎓 Education:**\n* Bachelor of Technology in Industrial Electronic Automation with Honours (2024-2028)\n* Diploma in Electronic Technology (2023)\n* Malaysian Skills Certificate Level 3 in Electronic Technology (2022)")
            with cx2:
                st.markdown("**🎯 Roles:**\n* Manage the daily operations of the company.\n* Coordinate product sourcing, inventory, and logistics.\n* Support technical and customer service activities.")
        st.markdown("""
        <div style="background-color: #f8fafc; padding: 12px; border-left: 4px solid #00A3E0; margin-top: 10px; font-size:13.5px; color:#333333;">
            <b>💼 Key Responsibilities:</b> Maintain stock levels and inventory records • Ensure timely order processing and delivery • Handle customer inquiries and technical support • Coordinate with suppliers for quality • Assist in marketing & promotions.
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 5. MENU CONTENT: OUR PRODUCTS
# ==========================================
elif menu == "Our Products":
    st.title("📦 Our Products & Hardware Catalog")
    st.markdown("Explore our range of premium hardware components supplied across Malaysia:")
    st.markdown("<br>", unsafe_allow_html=True)
    
    products = [
        ("esp32.png", "ESP32 Development Boards", "Our flagship product and best selling microcontroller, widely used for IoT, smart devices, and embedded system applications due to its powerful performance and built in WiFi and Bluetooth connectivity."),
        ("raspi.png", "Raspberry Pi", "Compact single board computer designed for programming, educational projects, and advanced computing applications."),
        ("arduino.png", "Arduino Uno R3", "User friendly microcontroller board suitable for beginners, students, and electronics enthusiasts, making it one of the most popular development platforms worldwide."),
        ("wemos.png", "Wemos D1 Mini", "Compact and affordable WiFi enabled development board that provides an efficient solution for wireless electronic projects.")
    ]
    
    for filename, title, desc in products:
        with st.container():
            img_col, txt_col = st.columns([1, 3])
            with img_col:
                try: st.image(filename, use_container_width=True)
                except: st.warning(f"⚠️ [{filename} missing]")
            with txt_col:
                st.markdown(f"""
                <div class="corporate-card">
                    <h4>{title}</h4>
                    <p style="text-align: justify; font-size: 15px; line-height: 1.6;">{desc}</p>
                    <span style="color: #00A3E0; font-weight: bold; font-size: 14px;">✓ Authentic & Original Stock Guarantee</span>
                </div>
                """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 6. MENU CONTENT: CERTIFICATES
# ==========================================
elif menu == "Certificates":
    st.title("🗂️ Company Sijil & Certificates")
    st.markdown("Official corporate verification and future compliance framework for **SyedEdge Plus**:")
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.expander("🏢 Suruhanjaya Syarikat Malaysia (SSM) Certificate", expanded=True):
        sc1, sc2 = st.columns([1.5, 1])
        with sc1:
            try: st.image("ssm.png", caption="SSM Corporate Registration Certificate", use_container_width=True)
            except: st.error("⚠️ Fail 'ssm.png' not found in project directory.")
        with sc2:
            st.markdown("""
            <div style="background-color: #ffffff; padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0; border-top: 4px solid #1A365D;">
                <h5 style="color: #1A365D; margin-top:0; font-weight:bold;">Entity Verification:</h5>
                <p style="font-size: 14px; margin-bottom: 8px;"><b>Company Name:</b> SyedEdge Plus</p>
                <p style="font-size: 14px; margin-bottom: 8px;"><b>Registration Status:</b> Active Legal Entity</p>
                <p style="font-size: 14px; margin-bottom: 8px;"><b>Incorporation Date:</b> May 2026</p>
                <span style="color: #48BB78; font-weight:bold; font-size:14px;">● Verifiable Corporate Supplier</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("🏛️ Ministry of Finance (MOF) Registration Roadmap", expanded=False):
        st.markdown("<h3 style='color: #1A365D; margin-top:0;'>Ministry of Finance (MOF)</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color:#333333;'>To enable SyedEdge Plus to participate in government procurement opportunities and expand its business network, the company plans to register with the Ministry of Finance (MOF) through the ePerolehan system.</p>", unsafe_allow_html=True)
        
        st.markdown("<h4 style='color: #1A365D; margin-top:20px;'>Registration Process Steps</h4>", unsafe_allow_html=True)
        mof_steps = [
            ("Step 1: Access the ePerolehan Portal", "Visit the official ePerolehan website and select the New supplier registration option to begin the registration process."),
            ("Step 2: Choose MOF Account Registration", "Select MOF Account as the registration type and proceed to the next step."),
            ("Step 3: Agree to the Terms and Conditions", "Read and accept the terms and conditions and fill the captcha provided by the Ministry of Finance before continuing."),
            ("Step 4: Enter Company Information", "Fill in the company's business details, including business registration information and contact details."),
            ("Step 5: Enter Account Information", "Provide the required account information and complete all registration fields accurately."),
            ("Step 6: Enter Supplier Administrator Information", "Assign a supplier administrator who will be responsible for managing account access."),
            ("Step 7: Accept Declarations", "Read and accept the terms and conditions for final activation."),
            ("Step 8: Registration Approval", "After submission, the Ministry of Finance will review the application and supporting documents. Upon successful approval, the company will receive the MOF Registration Certificate, allowing participation in government procurement and tender opportunities.")
        ]
        for title, step_desc in mof_steps:
            st.markdown(f"""
            <div style="margin-left: 10px; padding-left: 15px; border-left: 3px solid #00A3E0; margin-bottom: 12px;">
                <b style="color: #1A365D; font-size: 14.5px;">{title}</b><br><span style="color: #4a5568; font-size: 13.5px;">{step_desc}</span>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<h4 style='color: #1A365D; margin-top:20px;'>Benefits of MOF Registration</h4>", unsafe_allow_html=True)
        b_col1, b_col2 = st.columns(2)
        with b_col1:
            st.markdown("""
            * Eligibility to participate in government tenders.
            * Increased business credibility and professionalism.
            * Access to government procurement opportunities.
            """)
        with b_col2:
            st.markdown("""
            * Enhanced visibility among government agencies and public sector organizations.
            * Potential business growth through public sector partnerships.
            """)

# ==========================================
# MENU CONTENT: CONTACT US (FULLY FIXED TEXT COLORS)
# ==========================================
elif menu == "Contact Us":
    # Tambahan CSS khusus untuk hitamkan tulisan label input borang
    st.markdown("""
        <style>
        /* Memaksa warna tulisan label input menjadi hitam pekat dan jelas */
        div[data-testid="stForm"] label p {
            color: #000000 !important;
            font-weight: 600 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("📞 Contact Our Team")
    
    # FIX: Menggunakan HTML style untuk memastikan ayat sub-header ini berwarna gelap/jelas
    st.markdown(
        "<p style='color: #1A365D; font-weight: 500; font-size: 15px; margin-bottom: 20px;'>"
        "Have an RFQ or wholesale component order? Reach out to us directly:"
        "</p>", 
        unsafe_allow_html=True
    )
    
    col_c1, col_c2 = st.columns([2, 1])
    with col_c1:
        with st.form("contact", clear_on_submit=True):
            # Semua label di bawah ini kekal hitam pekat
            name = st.text_input("Name / Procurement Organization")
            email = st.text_input("Official Email Address")
            subject = st.selectbox("Inquiry Type", ["Request for Quotation (RFQ)", "Bulk Hardware Purchase", "Academic Collaboration", "Technical Product Support"])
            message = st.text_area("Inquiry Details / List of Component Quantities Needed")
            
            if st.form_submit_button("Submit Inquiry"):
                st.success(f"Thank you, {name}. Your inquiry regarding '{subject}' has been recorded. Our Johor sales office will contact you within 24 hours.")
                
    with col_c2:
        st.markdown("""
        <div style="background-color: #f8fafc; padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0; color: #333333;">
            <h5 style="color: #1A365D; margin-top:0; font-weight:bold;">Corporate Desk</h5>
            <p style="font-size:14px;"><b>📍 Headquarters:</b><br>Kota Tinggi, Johor, Malaysia.</p>
            <p style="font-size:14px;"><b>✉️ Email Contact:</b><br>hq_2026@syededgempire</p>
            <p style="font-size:14px;"><b>🌐 Web Domain:</b><br>www.syededgeplus.com</p>
            <hr style="margin: 10px 0;">
            <p style="font-size:12.5px; color:#666666;"><b>Operations Hours:</b><br>Sunday - Thursday<br>9:00 AM - 5:00 PM (Johor Working Days)</p>
        </div>
        """, unsafe_allow_html=True)