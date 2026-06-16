import streamlit as st

# ==========================================
# 1. KONFIGURASI PREMIUM & THEME COLOUR (NAVY & ELECTRIC BLUE)
# ==========================================
st.set_page_config(
    page_title="SYEDEDGE PLUS (SE+) | Corporate Portal",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk menyamakan warna dengan image_5a1366.png
st.markdown("""
    <style>
    /* Latar belakang Sidebar - Deep Navy Blue */
    [data-testid="stSidebar"] {
        background-color: #1A365D;
    }
    /* Warna teks di Sidebar menjadi putih */
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    /* Warna aktif menu radio */
    div.row-widget.stRadio > div {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 8px;
        padding: 10px;
    }
    /* Kad Korporat - Sisi kiri menggunakan warna Electric Blue */
    .corporate-card {
        background-color: #f8fafc;
        padding: 25px;
        border-radius: 12px;
        border-left: 6px solid #00A3E0;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .corporate-card h4, .corporate-card h5 {
        color: #1A365D;
        font-weight: bold;
    }
    /* Kad Sijil (SSM & MOF) */
    .cert-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #e2e8f0;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .cert-header {
        color: #1A365D;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    /* Gaya subheader dan teks */
    .slogan-text {
        font-style: italic;
        color: #00A3E0;
        font-size: 18px;
        margin-top: -10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SIDEBAR NAVIGATION & LOGO (.PNG)
# ==========================================
# Memanggil logo telus anda: logo_short.png
st.sidebar.image("logo_short.png", use_container_width=True)

st.sidebar.markdown("<h2 style='text-align: center; margin-top:-10px;'>SYEDEDGE PLUS</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #00A3E0; font-style: italic;'>\"From Components to Creativity\"</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

# Menu Navigasi Korporat
menu = st.sidebar.radio(
    "NAVIGASI PORTAL",
    ["Halaman Utama", "Profil Syarikat", "Katalog Produk", "Sijil & Pendaftaran (Certificates)", "Hubungi Kami"]
)

st.sidebar.markdown("---")
st.sidebar.caption("📍 HQ: Kota Tinggi, Johor")
st.sidebar.caption("© 2026 SYEDEDGE PLUS (SE+). All Rights Reserved.")

# ==========================================
# 3. KANDUNGAN MENU: HALAMAN UTAMA
# ==========================================
if menu == "Halaman Utama":
    st.title("Welcome to SYEDEDGE PLUS (SE+)")
    st.markdown("<p class='slogan-text'>\"From Components to Creativity\"</p>", unsafe_allow_html=True)
    
    # Gambar Banner Elektronik/IoT Profesional
    st.image("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="corporate-card">
        <h4>Peneraju Solusi Elektronik & Mikrokontroler Anda</h4>
        <p>Ditubuhkan pada tahun 2026, SYEDEDGE PLUS (SE+) komited untuk membekalkan komponen perkakasan gred industri dan pendidikan berkualiti tinggi di Malaysia. Kami memperkasakan para inovator, pelajar Capstone, dan industri daripada peringkat komponen asas sehingga mencetuskan kreativiti tanpa had.</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 4. KANDUNGAN MENU: PROFIL SYARIKAT (DROPDOWN ABOUT US)
# ==========================================
elif menu == "Profil Syarikat":
    st.title("🏢 Profil Korporat Syarikat")
    st.markdown("Sila buka *dropdown* di bawah untuk melihat maklumat rasmi agensi:")
    
    with st.expander("📖 Pengenalan & Latar Belakang", expanded=True):
        st.markdown("""
        **SYEDEDGE PLUS (SE+)** merupakan sebuah syarikat milikan Bumiputera sepenuhnya yang beroperasi di **Kota Tinggi, Johor**. 
        Fokus utama kami adalah menjadi hub pembekalan komponen mikrokontroler terpantas dan menyediakan ekosistem sokongan teknikal bersepadu untuk projek berteknologi tinggi (IoT, Automasi, dan Robotik).
        """)
        
    with st.expander("🎯 Visi & Misi Syarikat"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h4 style='color: #1A365D;'>👁️ Visi</h4>", unsafe_allow_html=True)
            st.info("Menjadi pemangkin utama revolusi IR 4.0 dalam sektor pendidikan teknik dan industri mikro di Malaysia menjelang tahun 2030.")
        with col2:
            st.markdown("<h4 style='color: #1A365D;'>🚀 Misi</h4>", unsafe_allow_html=True)
            st.success("1. Membantu mempercepatkan fasa pembangunan R&D melalui pembekalan komponen yang efisien.\n2. Menyediakan khidmat rundingan teknikal bernilai tinggi untuk projek komuniti dan industri.\n3. Memastikan standard produk sentiasa berada di tahap tertinggi.")

    with st.expander("👥 Struktur Organisasi & Pasukan Eksekutif"):
        st.markdown("Barisan kepimpinan utama SYEDEDGE PLUS:")
        st.markdown("""
        * **Pengarah Urusan / CEO:** Syed Irfan
        * **Ketua Pegawai Operasi (COO):** Bahagian Pengurusan Fail & Logistik
        * **Ketua Jurutera Sistem (Chief Engineer):** Bahagian Penyelidikan & Pembangunan (R&D)
        """)

# ==========================================
# 5. KANDUNGAN MENU: KATALOG PRODUK (DROPDOWN OUR PRODUCT)
# ==========================================
elif menu == "Katalog Produk":
    st.title("📦 Produk & Portfolio Perkhidmatan")
    st.markdown("Terokai penawaran komersial kami menerusi kategori di bawah:")
    
    with st.expander("⚡ Papan Mikrokontroler & Komputer Mini", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="corporate-card">
                <h5>ESP32 Wi-Fi + Bluetooth Board</h5>
                <p>Sangat ideal untuk aplikasi Smart Home dan projek pemantauan data IoT secara wireless (awan).</p>
                <span style="color: #00A3E0; font-weight: bold;">Status: Ready Stock (Johor Warehouse)</span>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="corporate-card">
                <h5>Raspberry Pi 4 (4GB/8GB RAM)</h5>
                <p>Komputer papan tunggal berkuasa tinggi untuk pemprosesan AI, pangkalan data tempatan, dan Edge Computing.</p>
                <span style="color: #1A365D; font-weight: bold;">Status: Pre-Order Available</span>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("🔌 Komponen Pasif, Sensor & Aktuator"):
        st.markdown("""
        Kami menawarkan lebih 500 jenis sensor aktif dan komponen diskret:
        * **Modul Sensor:** Sensor Gas (MQ series), Sensor Jarak (Ultrasonic/Lidar), Penderia Suhu Industri.
        * **Komponen Robotik:** Motor Servo, Driver Motor (L298N), Solenoid Valve.
        * **Aksesori Perkakasan:** Breadboard, Wayar Jumper Premium, Bekalan Kuasa (Power Adapter 5V/12V).
        """)

    with st.expander("🛠️ Perkhidmatan Kejuruteraan Kontrak (Contract Engineering)"):
        st.markdown("""
        Di samping pembekalan fizikal, kami turut menerima kontrak reka bentuk industri:
        1. **Rapid Prototyping:** Cetakan 3D (3D Printing) & Reka bentuk Casing Produk.
        2. **Custom PCB Design:** Pembuatan litar tersuai dua lapisan (2-Layer Industrial PCB).
        3. **Firmware Programming:** Pembangunan algoritma sistem menggunakan C/C++ dan MicroPython.
        """)

# ==========================================
# 6. KANDUNGAN MENU: SIJIL (CERTIFICATES DROPDOWN)
# ==========================================
elif menu == "Sijil & Pendaftaran (Certificates)":
    st.title("🗂️ Sijil Kebenaran & Akreditasi")
    st.markdown("Pihak pengurusan SYEDEDGE PLUS sentiasa patuh pada regulasi perniagaan tempatan:")
    
    # Permintaan khas: SSM dan MOF digabungkan dalam 1 dropdown bertajuk "Certificates"
    with st.expander("🪪 Certificates (SSM & MOF Registrations)", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="cert-card">
                <div class="cert-header">🏢 SSM</div>
                <p><b>Suruhanjaya Syarikat Malaysia</b></p>
                <p>Pendaftaran Entiti Perniagaan Sah</p>
                <p style="color: #1A365D; font-weight: bold;">Ref: 202603XXXXXX</p>
                <span style="color: #48BB78; font-weight: bold;">● Patuh & Aktif</span>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div class="cert-card">
                <div class="cert-header">🏛️ MOF</div>
                <p><b>Kementerian Kewangan Malaysia</b></p>
                <p>Sijil Akuan Pendaftaran Kontraktor Kerajaan</p>
                <p style="color: #1A365D; font-weight: bold;">Kod Bidang: Alat Perhubungan & Elektronik</p>
                <span style="color: #48BB78; font-weight: bold;">● Diluluskan</span>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# 7. KANDUNGAN MENU: HUBUNGI KAMI
# ==========================================
elif menu == "Hubungi Kami":
    st.title("📞 Hubungi Rangkaian Kami")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### Borang Interaktif Pertanyaan Harga / RFQ")
        with st.form("corporate_contact", clear_on_submit=True):
            nama_org = st.text_input("Nama Penuh / Nama Agensi Korporat")
            emel_org = st.text_input("Alamat E-mel Rasmi")
            subjek = st.selectbox("Tujuan Urusan", ["Sebut Harga Projek (RFQ)", "Pembelian Pukal Komponen", "Kolaborasi Akademik", "Sokongan Teknikal"])
            mesej = st.text_area("Butiran Mesej / Senarai Semak Komponen Perkakasan")
            
            hantar = st.form_submit_button("Hantar Ke Urus Setia")
            if hantar:
                st.success(f"Mesej anda berkenaan '{subjek}' berjaya dihantar. Pegawai jualan kami di Johor akan menghubungi anda secepat mungkin.")
                
    with col2:
        st.markdown("#### Maklumat Korporat")
        st.markdown("""
        * 📍 **Alamat Ibu Pejabat:**  
          Kota Tinggi, Johor, Malaysia.
        * ✉️ **E-mel Pertanyaan:**  
          hq_2026@syededgempire
        * 🌐 **Portal Rasmi:**  
          [www.syedgeplus.com](https://syededgeplus.streamlit.app)
        """)
        
        st.info("🕒 **Waktu Operasi Kaunter:**\n\nAhad - Khamis (Waktu Johor)\n9:00 AM - 5:00 PM")