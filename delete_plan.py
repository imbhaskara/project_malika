import streamlit as st
import pandas as pd
from conn_db import filter_data, delete_data
import datetime as dt
 
def delete_plan():
    st.subheader('Hapus Data Individual Plan 2022')
    nik = st.number_input('Masukkan data NIK Karyawan')
    data = filter_data(nik)
    if data:
        ambition = data[0][1]
        strength = data[0][2]
        weakness = data[0][3]
        cuti_start_1 = data[0][4]
        lama_cuti_1 = data[0][5]
        alasan_cuti_1 = data[0][6]
        cuti_start_2 = data[0][7]
        lama_cuti_2 = data[0][8]
        alasan_cuti_2 = data[0][9]
        cuti_start_3 = data[0][10]
        lama_cuti_3 = data[0][11]
        alasan_cuti_3 = data[0][12]
        competencies_1 = data[0][13]
        dev_type_1 = data[0][14]
        dev_desc_1 = data[0][15]
        dev_date_1 = data[0][16]
        competencies_2 = data[0][17]
        dev_type_2 = data[0][18]
        dev_desc_2 = data[0][19]
        dev_date_2 = data[0][20]
        competencies_3 = data[0][21]
        dev_type_3 = data[0][22]
        dev_desc_3 = data[0][23]
        dev_date_3 = data[0][24]
        competencies_4 = data[0][25]
        dev_type_4 = data[0][26]
        dev_desc_4 = data[0][27]
        dev_date_4 = data[0][28]
        competencies_5 = data[0][29]
        dev_type_5 = data[0][30]
        dev_desc_5 = data[0][31]
        dev_date_5 = data[0][32]
        recommendation = data[0][33]

        new_ambition = st.text_area('Ambisi/Obsesi Karir di 2022', value=ambition, placeholder='Ceritakan hal-hal yang ingin Anda capai terkait Karir dan Pengembangan di tahun 2022')
        strength_cols, weakness_cols = st.columns((2,2))
        new_strength = strength_cols.text_area('Employee Strength', strength, placeholder='Ceritakan tentang kompetensi yang menjadi kekuatan dari karyawan Anda')
        new_weakness = weakness_cols.text_area('Employee Weakness', weakness, placeholder='Ceritakan tentang kompetensi yang masih kurang dari karyawan Anda')
        st.write('Rencana Cuti Anda di 2022')
        st.caption('Rencanakan jatah cuti tahunan Anda maksimal 50% (6 hari) dari Jatah Cuti Tahunan Anda')
        cuti_start_cols1, lama_cuti_cols1, alasan_cuti_cols1 = st.columns((2,2,2))
        new_cuti_start_1 = cuti_start_cols1.date_input('Tanggal Pengajuan Cuti', value=dt.datetime.strptime(cuti_start_1, '%Y-%m-%d'), key=1)
        new_lama_cuti_1 = lama_cuti_cols1.selectbox('Durasi Cuti', ['1 Hari','2 Hari','3 Hari','4 Hari','5 Hari','6 Hari',], key=1)
        new_alasan_cuti_1 = alasan_cuti_cols1.text_area('Alasan Cuti', alasan_cuti_1, placeholder='Ceritakan alasan Anda mengambil cuti ini', key=1)
        cuti_start_cols2, lama_cuti_cols2, alasan_cuti_cols2 = st.columns((2,2,2))
        new_cuti_start_2 = cuti_start_cols2.date_input('Tanggal Pengajuan Cuti', value=dt.datetime.strptime(cuti_start_2, '%Y-%m-%d'), key=2)
        new_lama_cuti_2 = lama_cuti_cols2.selectbox('Durasi Cuti', ['1 Hari','2 Hari','3 Hari','4 Hari','5 Hari','6 Hari',], key=2)
        new_alasan_cuti_2 = alasan_cuti_cols2.text_area('Alasan Cuti', alasan_cuti_2, placeholder='Ceritakan alasan Anda mengambil cuti ini', key=2)
        cuti_start_cols3, lama_cuti_cols3, alasan_cuti_cols3 = st.columns((2,2,2))
        new_cuti_start_3 = cuti_start_cols3.date_input('Tanggal Pengajuan Cuti', value=dt.datetime.strptime(cuti_start_3, '%Y-%m-%d'), key=3)
        new_lama_cuti_3 = lama_cuti_cols3.selectbox('Durasi Cuti', ['1 Hari','2 Hari','3 Hari','4 Hari','5 Hari','6 Hari',], key=3)
        new_alasan_cuti_3 = alasan_cuti_cols3.text_area('Alasan Cuti', alasan_cuti_3, placeholder='Ceritakan alasan Anda mengambil cuti ini', key=3)
        st.write('Jenis Development yang ingin dilakukan')
        st.caption('Ceritakan maksimal 5 Jenis Development yang ingin Anda ambil di tahun 2022 untuk meningkatkan kompetensi Anda')
        activity, jenis_dev, deskripsi_dev, tgl_dev = st.columns((2,2,2,1))
        new_competencies_1 = activity.text_input('Nama Kompetensi', competencies_1, key=1)
        new_dev_type_1 = jenis_dev.selectbox('Jenis Development', ['Development 70', 'Development 20', 'Development 10'], key=1)
        new_dev_desc_1 = deskripsi_dev.text_area('Deskripsi Development', dev_desc_1, placeholder='Ceritakan deskripsi development apa yang ingin Anda ambil di 2022', key=1)
        new_dev_date_1 = tgl_dev.date_input('Deadline Realisasi',value=dt.datetime.strptime(dev_date_1, '%Y-%m-%d'), key=1)
        activity2, jenis_dev2, deskripsi_dev2, tgl_dev2 = st.columns((2,2,2,1))
        new_competencies_2 = activity2.text_input('Nama Kompetensi', competencies_2, key=2)
        new_dev_type_2 = jenis_dev2.selectbox('Jenis Development', ['Development 70', 'Development 20', 'Development 10'], key=2)
        new_dev_desc_2 = deskripsi_dev2.text_area('Deskripsi Development', dev_desc_2, placeholder='Ceritakan deskripsi development apa yang ingin Anda ambil di 2022', key=2)
        new_dev_date_2 = tgl_dev2.date_input('Deadline Realisasi',value=dt.datetime.strptime(dev_date_2, '%Y-%m-%d'), key=2)
        activity3, jenis_dev3, deskripsi_dev3, tgl_dev3 = st.columns((2,2,2,1))
        new_competencies_3 = activity3.text_input('Nama Kompetensi', competencies_3, key=3)
        new_dev_type_3 = jenis_dev3.selectbox('Jenis Development', ['Development 70', 'Development 20', 'Development 10'], key=3)
        new_dev_desc_3 = deskripsi_dev3.text_area('Deskripsi Development', dev_desc_3, placeholder='Ceritakan deskripsi development apa yang ingin Anda ambil di 2022', key=3)
        new_dev_date_3 = tgl_dev3.date_input('Deadline Realisasi',value=dt.datetime.strptime(dev_date_3, '%Y-%m-%d'), key=3)
        activity4, jenis_dev4, deskripsi_dev4, tgl_dev4 = st.columns((2,2,2,1))
        new_competencies_4 = activity4.text_input('Nama Kompetensi', competencies_4, key=4)
        new_dev_type_4 = jenis_dev4.selectbox('Jenis Development', ['Development 70', 'Development 20', 'Development 10'], key=4)
        new_dev_desc_4 = deskripsi_dev4.text_area('Deskripsi Development', dev_desc_4, placeholder='Ceritakan deskripsi development apa yang ingin Anda ambil di 2022', key=4)
        new_dev_date_4 = tgl_dev4.date_input('Deadline Realisasi',value=dt.datetime.strptime(dev_date_4, '%Y-%m-%d'), key=4)
        activity5, jenis_dev5, deskripsi_dev5, tgl_dev5 = st.columns((2,2,2,1))
        new_competencies_5 = activity5.text_input('Nama Kompetensi', competencies_5, key=5)
        new_dev_type_5 = jenis_dev5.selectbox('Jenis Development', ['Development 70', 'Development 20', 'Development 10'], key=5)
        new_dev_desc_5 = deskripsi_dev5.text_area('Deskripsi Development', dev_desc_5, placeholder='Ceritakan deskripsi development apa yang ingin Anda ambil di 2022', key=5)
        new_dev_date_5 = tgl_dev5.date_input('Deadline Realisasi',value=dt.datetime.strptime(dev_date_5, '%Y-%m-%d'), key=5)
        new_recommendation = st.text_area('Catatan / Rekomendasi', recommendation, placeholder='Tuliskan kesimpulan akhir, catatan, dan rekomendasi dari hasil diskusi dengan karyawan Anda ')
        delete = st.button('Delete Data')
        if delete:
           delete_data(nik)
           st.success(f'Data {nik} telah berhasil dihapus')