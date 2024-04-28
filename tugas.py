import streamlit as st
from streamlit_option_menu import option_menu

#navigasi sidebar
with st.sidebar :
    selected = option_menu ('Hitung Satuan Konsentrasi',
    ['Hitung Konsentrasi % b/b',
    'Hitung Konsentrasi % v/v',
    'Hitung Konsentrasi % b/v',
    'Hitung Konsentrasi Molaritas',
    'Hitung Konsentrasi Normalitas',
    'Hitung Konsentrasi PPM'],
    default_index=0)

#halaman hitung konsentrasi % b/b
if (selected == 'Hitung Konsentrasi % b/b') :
    st.header('Hitung Konsentrasi % b/b', divider='rainbow')

    zatterlarut = st.number_input("Masukkan Nilai Zat Terlarut(g)")
    zatpelarut = st.number_input("Masukkan Nilai Zat Pelarut(g)")
    zatlarutan = zatterlarut + zatpelarut
    hitung = st.button("Hitung Konsentrasi % b/b")

    if hitung :
        konsentrasi = zatterlarut / zatlarutan * 100
        konsentrasi_formated = round(konsentrasi, 2)
        st.write("Konsentrasinya adalah =", konsentrasi_formated)
        st.success(f"Konsentrasinya adalah = {konsentrasi_formated}% b/b")

#halaman hitung konsentrasi % v/v
if (selected == 'Hitung Konsentrasi % v/v') :
    st.header('Hitung Konsentrasi % v/v', divider='rainbow')

    zatterlarut = st.number_input("Masukkan Nilai Zat Terlarut(mL)")
    zatpelarut = st.number_input("Masukkan Nilai Zat Pelarut(mL)")
    zatlarutan = zatterlarut + zatpelarut
    hitung = st.button("Hitung Konsentrasi % v/v")

    if hitung :
        konsentrasi = zatterlarut / zatlarutan * 100
        konsentrasi_formated = round(konsentrasi, 2)
        st.write("Konsentrasinya adalah =", konsentrasi_formated)
        st.success(f"Konsentrasinya adalah = {konsentrasi_formated}% v/v")

#halaman hitung konsentrasi % b/v
if (selected == 'Hitung Konsentrasi % b/v') :
    st.header('Hitung Konsentrasi % b/v', divider='rainbow')

    zatterlarut = st.number_input("Masukkan Nilai Zat Terlarut(g)")
    zatpelarut = st.number_input("Masukkan Nilai Zat Pelarut(g)")
    zatlarutan = zatterlarut + zatpelarut
    hitung = st.button("Hitung Konsentrasi % b/v")

    if hitung :
        konsentrasi = zatterlarut / zatlarutan * 100
        konsentrasi_formated = round(konsentrasi, 2)
        st.write("Konsentrasinya adalah =", konsentrasi_formated)
        st.success(f"Konsentrasinya adalah = {konsentrasi_formated}% b/v")

#halaman hitung konsentrasi molaritas
if (selected == 'Hitung Konsentrasi Molaritas') :
    st.header('Hitung Konsentrasi Molaritas', divider='rainbow')

    massa = st.number_input("Masukkan Jumlah Massa(g)")
    bm = st.number_input("Masukkan Nilai BM(g/mol)")
    volume = st.number_input("Masukkan Jumlah Volume(mL)")
    vb = bm * volume
    hitung = st.button("Hitung Konsentrasi Molaritas")

    if hitung :
        konsentrasi = massa / vb
        konsentrasi_formated = round(konsentrasi, 4)
        st.write("Konsentrasinya adalah = ", konsentrasi_formated)
        st.success(f"Konsentrasinya adalah = {konsentrasi_formated} mol/L")

#halaman hitung konsentrasi normalitas
if (selected == 'Hitung Konsentrasi Normalitas') :
    st.header('Hitung Konsentrasi Normalitas', divider='rainbow')

    massa = st.number_input("Masukkan Jumlah Massa(g)")
    be = st.number_input("Masukkan Nilai BE(g/grek)")
    volume = st.number_input("Masukkan Jumlah Volume(mL)")
    vb = be * volume
    hitung = st.button("Hitung Konsentrasi Normalitas")

    if hitung :
        konsentrasi = massa / vb
        konsentrasi_formated = round(konsentrasi, 4)
        st.write("Konsentrasinya adalah =", konsentrasi_formated)
        st.success(f"Konsentrasinya adalah = {konsentrasi_formated} grek/L")

#halaman hitung konsentrasi PPM
if (selected == 'Hitung Konsentrasi PPM') :
    st.header('Hitung Konsentrasi PPM', divider='rainbow')

    massa = st.number_input("Masukkan Jumlah Massa(mg)")
    volume = st.number_input("Masukkan Jumlah Volume(L)")
    hitung = st.button("Hitung Konsentrasi PPM")

    if hitung :
        konsentrasi = massa / volume 
        konsentrasi_formated = round(konsentrasi, 2)
        st.write("Konsentrasinya adalah =", konsentrasi_formated)
        st.success(f"Konsentrasinya adalah = {konsentrasi_formated}PPM")