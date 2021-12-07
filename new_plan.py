from typing import runtime_checkable
import streamlit as st
import pandas as pd
from conn_db import create_table, add_data
 
def create_new_plan():
    st.subheader('Buat Individual Development Plan 2022')
    create_table()
    nik = st.number_input('NIK Karyawan')
    ambition = st.text_area('Ambisi/Obsesi Karir Anda di 2022', placeholder = 'Ceritakan hal-hal yang ingin Anda capai terkait Karir dan Pengembangan di tahun 2022')
    strength = 'Diisikan oleh atasan terkait kelebihan karyawan'
    weakness = 'Diisikan oleh atasan terkait kekurangan karyawan'
    st.write('Rencana Cuti Anda di 2022')
    st.caption('Rencanakan jatah cuti tahunan Anda maksimal 50% (6 hari) dari Jatah Cuti Tahunan Anda')
    cuti_start_cols1, lama_cuti_cols1, alasan_cuti_cols1 = st.columns((2,2,2))
    cuti_start_1 = cuti_start_cols1.date_input('Tanggal Pengajuan Cuti', key=1)
    lama_cuti_1 = lama_cuti_cols1.selectbox('Durasi Cuti', ['1 Hari','2 Hari','3 Hari','4 Hari','5 Hari','6 Hari',], key=1)
    alasan_cuti_1 = alasan_cuti_cols1.text_area('Alasan Cuti', placeholder='Ceritakan alasan Anda mengambil cuti ini', key=1)
    cuti_start_cols2, lama_cuti_cols2, alasan_cuti_cols2 = st.columns((2,2,2))
    cuti_start_2 = cuti_start_cols2.date_input('Tanggal Pengajuan Cuti', key=2)
    lama_cuti_2 = lama_cuti_cols2.selectbox('Durasi Cuti', ['1 Hari','2 Hari','3 Hari','4 Hari','5 Hari','6 Hari',], key=2)
    alasan_cuti_2 = alasan_cuti_cols2.text_area('Alasan Cuti', placeholder='Ceritakan alasan Anda mengambil cuti ini', key=2)
    cuti_start_cols3, lama_cuti_cols3, alasan_cuti_cols3 = st.columns((2,2,2))
    cuti_start_3 = cuti_start_cols3.date_input('Tanggal Pengajuan Cuti', key=3)
    lama_cuti_3 = lama_cuti_cols3.selectbox('Durasi Cuti', ['1 Hari','2 Hari','3 Hari','4 Hari','5 Hari','6 Hari',], key=3)
    alasan_cuti_3 = alasan_cuti_cols3.text_area('Alasan Cuti', placeholder='Ceritakan alasan Anda mengambil cuti ini', key=3)
    st.write('Jenis Development yang ingin dilakukan')
    st.caption('Ceritakan maksimal 5 Jenis Development yang ingin Anda ambil di tahun 2022 untuk meningkatkan kompetensi Anda')
    activity1, jenis_dev1, deskripsi_dev1, tgl_dev1 = st.columns((2,2,2,1))
    competencies_1 = activity1.text_input('Nama Kompetensi', key=1)
    dev_type_1 = jenis_dev1.selectbox('Jenis Development', ['Development 70', 'Development 20', 'Development 10'], key=1)
    dev_desc_1 = deskripsi_dev1.text_area('Deskripsi Development', placeholder='Ceritakan deskripsi development apa yang ingin Anda ambil di 2022', key=1)
    dev_date_1 = tgl_dev1.date_input('Deadline Realisasi', key=1)
    activity2, jenis_dev2, deskripsi_dev2, tgl_dev2 = st.columns((2,2,2,1))
    competencies_2 = activity2.text_input('Nama Kompetensi', key=2)
    dev_type_2 = jenis_dev2.selectbox('Jenis Development', ['Development 70', 'Development 20', 'Development 10'], key=2)
    dev_desc_2 = deskripsi_dev2.text_area('Deskripsi Development', placeholder='Ceritakan deskripsi development apa yang ingin Anda ambil di 2022', key=2)
    dev_date_2 = tgl_dev2.date_input('Deadline Realisasi', key=2)
    activity3, jenis_dev3, deskripsi_dev3, tgl_dev3 = st.columns((2,2,2,1))
    competencies_3 = activity3.text_input('Nama Kompetensi', key=3)
    dev_type_3 = jenis_dev3.selectbox('Jenis Development', ['Development 70', 'Development 20', 'Development 10'], key=3)
    dev_desc_3 = deskripsi_dev3.text_area('Deskripsi Development', placeholder='Ceritakan deskripsi development apa yang ingin Anda ambil di 2022', key=3)
    dev_date_3 = tgl_dev3.date_input('Deadline Realisasi', key=3)
    activity4, jenis_dev4, deskripsi_dev4, tgl_dev4 = st.columns((2,2,2,1))
    competencies_4 = activity4.text_input('Nama Kompetensi', key=4)
    dev_type_4 = jenis_dev4.selectbox('Jenis Development', ['Development 70', 'Development 20', 'Development 10'], key=4)
    dev_desc_4 = deskripsi_dev4.text_area('Deskripsi Development', placeholder='Ceritakan deskripsi development apa yang ingin Anda ambil di 2022', key=4)
    dev_date_4 = tgl_dev4.date_input('Deadline Realisasi', key=4)
    activity5, jenis_dev5, deskripsi_dev5, tgl_dev5 = st.columns((2,2,2,1))
    competencies_5 = activity5.text_input('Nama Kompetensi', key=5)
    dev_type_5 = jenis_dev5.selectbox('Jenis Development', ['Development 70', 'Development 20', 'Development 10'], key=5)
    dev_desc_5 = deskripsi_dev5.text_area('Deskripsi Development', placeholder='Ceritakan deskripsi development apa yang ingin Anda ambil di 2022', key=5)
    dev_date_5 = tgl_dev5.date_input('Deadline Realisasi', key=5)
    recommendation = 'Diisikan bersama atasan terkait terkait rekomendasi dan catatan'
    submit = st.button('Submit Data')

    if submit:
        add_data(nik, ambition, strength, weakness, cuti_start_1, lama_cuti_1, alasan_cuti_1, cuti_start_2, lama_cuti_2, alasan_cuti_2, cuti_start_3, lama_cuti_3, alasan_cuti_3, competencies_1, dev_type_1, dev_desc_1, dev_date_1, competencies_2, dev_type_2, dev_desc_2, dev_date_2, competencies_3, dev_type_3, dev_desc_3, dev_date_3, competencies_4, dev_type_4, dev_desc_4, dev_date_4, competencies_5, dev_type_5, dev_desc_5, dev_date_5, recommendation)
        st.success(f'Data Individual Plan {nik} sudah berhasil dimasukkan')
