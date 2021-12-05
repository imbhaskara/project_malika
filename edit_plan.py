import streamlit as st
import pandas as pd
from conn_db import filter_data, edit_data
import datetime as dt
 
def edit_plan():
    st.subheader('Edit Data Individual Plan 2022')
    nik = st.number_input('NIK Karyawan')
    data = filter_data(nik)
    if data:
        ambition = data[0][1]
        strength = data[0][2]
        weakness = data[0][3]
        competencies_1 = data[0][4]
        dev_type_1 = data[0][5]
        dev_desc_1 = data[0][6]
        dev_date_1 = data[0][7]
        competencies_2 = data[0][8]
        dev_type_2 = data[0][9]
        dev_desc_2 = data[0][10]
        dev_date_2 = data[0][11]
        competencies_3 = data[0][12]
        dev_type_3 = data[0][13]
        dev_desc_3 = data[0][14]
        dev_date_3 = data[0][15]
        competencies_4 = data[0][16]
        dev_type_4 = data[0][16]
        dev_desc_4 = data[0][17]
        dev_date_4 = data[0][18]
        competencies_5 = data[0][19]
        dev_type_5 = data[0][20]
        dev_desc_5 = data[0][21]
        dev_date_5 = data[0][22]
        recommendation = data[0][23]
            
        new_ambition = st.text_area('Ambisi/Obsesi Karir di 2022', value=ambition)
        st.caption('Ceritakan hal-hal yang ingin Anda capai terkait Karir dan Pengembangan di tahun 2022')
        strength_cols, weakness_cols = st.columns((2,2))
        new_strength = strength_cols.text_area('Employee Strength', strength)
        strength_cols.caption('Ceritakan tentang kompetensi yang menjadi kekuatan dari karyawan Anda')
        new_weakness = weakness_cols.text_area('Employee Weakness', weakness)
        weakness_cols.caption('Ceritakan tentang kompetensi yang masih kurang dari karyawan Anda')
        st.write('Jenis Development yang ingin dilakukan')
        st.caption('Ceritakan maksimal 5 Jenis Development yang ingin Anda ambil di tahun 2022 untuk meningkatkan kompetensi Anda')
        activity1, jenis_dev1, deskripsi_dev1, tgl_dev1 = st.columns((2,2,2,1))
        new_competencies_1 = activity1.text_input('Nama Kompetensi', competencies_1, key=1)
        new_dev_type_1 = jenis_dev1.selectbox('Jenis Development', ['Development 70', 'Development 20', 'Development 10'], key=1)
        new_dev_desc_1 = deskripsi_dev1.text_area('Deskripsi Development yang akan dilakukan', dev_desc_1, key=1)
        new_dev_date_1 = tgl_dev1.date_input('Deadline Realisasi',value=dt.datetime.strptime(dev_date_1, '%Y-%m-%d'), key=1)
        activity2, jenis_dev2, deskripsi_dev2, tgl_dev2 = st.columns((2,2,2,1))
        new_competencies_2 = activity2.text_input('Nama Kompetensi', competencies_2, key=2)
        new_dev_type_2 = jenis_dev2.selectbox('Jenis Development', ['Development 70', 'Development 20', 'Development 10'], key=2)
        new_dev_desc_2 = deskripsi_dev2.text_area('Deskripsi Development yang akan dilakukan', dev_desc_2, key=2)
        new_dev_date_2 = tgl_dev2.date_input('Deadline Realisasi',value=dt.datetime.strptime(dev_date_2, '%Y-%m-%d'), key=2)
        activity3, jenis_dev3, deskripsi_dev3, tgl_dev3 = st.columns((2,2,2,1))
        new_competencies_3 = activity3.text_input('Nama Kompetensi', competencies_3, key=3)
        new_dev_type_3 = jenis_dev3.selectbox('Jenis Development', ['Development 70', 'Development 20', 'Development 10'], key=3)
        new_dev_desc_3 = deskripsi_dev3.text_area('Deskripsi Development yang akan dilakukan', dev_desc_3, key=3)
        new_dev_date_3 = tgl_dev3.date_input('Deadline Realisasi',value=dt.datetime.strptime(dev_date_3, '%Y-%m-%d'), key=3)
        activity4, jenis_dev4, deskripsi_dev4, tgl_dev4 = st.columns((2,2,2,1))
        new_competencies_4 = activity4.text_input('Nama Kompetensi', competencies_4, key=4)
        new_dev_type_4 = jenis_dev4.selectbox('Jenis Development', ['Development 70', 'Development 20', 'Development 10'], key=4)
        new_dev_desc_4 = deskripsi_dev4.text_area('Deskripsi Development yang akan dilakukan', dev_desc_4, key=4)
        new_dev_date_4 = tgl_dev4.date_input('Deadline Realisasi',value=dt.datetime.strptime(dev_date_4, '%Y-%m-%d'), key=4)
        activity5, jenis_dev5, deskripsi_dev5, tgl_dev5 = st.columns((2,2,2,1))
        new_competencies_5 = activity5.text_input('Nama Kompetensi', competencies_5, key=5)
        new_dev_type_5 = jenis_dev5.selectbox('Jenis Development', ['Development 70', 'Development 20', 'Development 10'], key=5)
        new_dev_desc_5 = deskripsi_dev5.text_area('Deskripsi Development yang akan dilakukan', dev_desc_5, key=5)
        new_dev_date_5 = tgl_dev5.date_input('Deadline Realisasi',value=dt.datetime.strptime(dev_date_5, '%Y-%m-%d'), key=5)
        new_recommendation = st.text_area('Catatan / Rekomendasi', recommendation)
        st.caption('Tuliskan kesimpulan akhir, catatan, dan rekomendasi dari hasil diskusi dengan karyawan Anda ')
        if st.button('Update Data'):
            edit_data(new_ambition, new_strength, new_weakness, new_competencies_1, new_dev_type_1, new_dev_desc_1, new_dev_date_1, new_competencies_2, new_dev_type_2, new_dev_desc_2, new_dev_date_2, new_competencies_3, new_dev_type_3, new_dev_desc_3, new_dev_date_3, new_competencies_4, new_dev_type_4, new_dev_desc_4, new_dev_date_4, new_competencies_5, new_dev_type_5, new_dev_desc_5, new_dev_date_5, new_recommendation, ambition, strength, weakness, competencies_1, dev_type_1, dev_desc_1, dev_date_1, competencies_2, dev_type_2, dev_desc_2, dev_date_2, competencies_3, dev_type_3, dev_desc_3, dev_date_3, competencies_4, dev_type_4, dev_desc_4, dev_date_4, competencies_5, dev_type_5, dev_desc_5, dev_date_5, recommendation)
            st.success(f'Data {nik} telah berhasil diupdate')
       