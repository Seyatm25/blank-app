elif pilihan_halaman == "📘 BAB I. HIDROKARBON":
    st.title("📘 BAB I. HIDROKARBON")
    st.write("---")
    
    # 1. MEMBUAT TABS (Sesuai referensi gambar)
    tab_teori, tab_reaksi, tab_visual = st.tabs([
        "📖 Referensi Standar & Sifat", 
        "📊 Analisis Parameter Reaksi", 
        "📈 Visualisasi 2D"
    ])
    
    # ==========================================
    # TAB 1: TEORI DASAR
    # ==========================================
    with tab_teori:
        st.subheader("Landasan Teori Hidrokarbon")
        st.markdown("""
        Hidrokarbon adalah senyawa organik yang seluruh strukturnya hanya tersusun atas unsur karbon (C) dan hidrogen (H). Berdasarkan jenis ikatannya, hidrokarbon alifatik dibagi menjadi hidrokarbon jenuh (alkana) dan tidak jenuh (alkena dan alkuna). Sementara itu, hidrokarbon aromatik memiliki rantai siklik konjugasi yang sangat stabil.

        #### **A. Sifat Fisika Hidrokarbon**
        * **Wujud Zat (pada suhu kamar):**
          * Suhu rendah ($C_1 - C_4$) berwujud gas (contoh: metana, etana, etena, etuna).
          * Suhu sedang ($C_5 - C_{17}$) berwujud cair (contoh: pentana, heksana, benzena).
          * Suhu tinggi ($\ge C_{18}$) berwujud padat (contoh: parafin padat).
        * **Kelarutan:** Bersifat nonpolar, sehingga tidak larut dalam air (pelarut polar). Hidrokarbon larut dengan baik dalam sesama pelarut organik nonpolar seperti kloroform ($CHCl_3$), karbon tetraklorida ($CCl_4$), atau eter.
        * **Titik Didih dan Titik Leleh:** Meningkat seiring bertambahnya massa molekul.
        * **Densitas:** Memiliki massa jenis yang lebih kecil daripada air.
        """)

    # ==========================================
    # TAB 2: ANALISIS REAKSI
    # ==========================================
    with tab_reaksi:
        st.subheader("Sifat Kimia & Reaksi Identifikasi")
        
        st.markdown("**1. Alkana (Hidrokarbon Jenuh)**")
        st.markdown("Disebut juga parafin (afinitas kecil). Alkana dapat bereaksi dengan halogen melalui reaksi substitusi radikal bebas dengan bantuan sinar UV.")
        st.latex(r"\text{CH}_4 + \text{I}_2 \xrightarrow{\text{Sinar UV} / \Delta} \text{CH}_3\text{I} + \text{HI}")
        
        st.divider()
        
        st.markdown("**2. Alkena dan Alkuna (Hidrokarbon Tidak Jenuh)**")
        st.markdown("**Uji Adisi Iodium:** Mengadisi halogen pada ikatan rangkap seketika tanpa UV.")
        st.latex(r"\text{R-CH}=\text{CH-R} + \text{I}_2 \rightarrow \text{R-CH(I)-CH(I)-R}")
        
        st.markdown("**Uji Baeyer (Oksidasi $KMnO_4$):** Dioksidasi menghasilkan senyawa glikol dan endapan cokelat $MnO_2$.")
        st.latex(r"3\text{CH}_2=\text{CH}_2 + 2\text{KMnO}_4 + 4\text{H}_2\text{O} \rightarrow 3\text{HO-CH}_2\text{-CH}_2\text{-OH} + 2\text{MnO}_2\downarrow + 2\text{KOH}")
        
        st.divider()
        
        st.markdown("**3. Benzena (Hidrokarbon Aromatik)**")
        st.markdown("**Reaksi Substitusi Elektrofilik:** Benzena cenderung mengalami reaksi substitusi, seperti Nitrasi.")
        st.latex(r"\
