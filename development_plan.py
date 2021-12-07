from delete_plan import delete_plan
from edit_plan import edit_plan
import streamlit as st
import pandas as pd
from new_plan import create_new_plan
from conn_db import view_all_data, get_table_download_link

today = pd.Timestamp('today')

#Page Configuration
st.set_page_config(page_title='Malika', layout='wide', initial_sidebar_state='collapsed')

menu = ['Home','Create New Development Plan', 'View Development Database', 'Edit or Manage Development Plan', 'Delete Development Plan']
choice = st.sidebar.selectbox('Pilih menu yang ingin dikunjungi', menu)

def development_plan():
    if choice=='Home':
        st.title(f'Individual Development Plan Tahun 2022')
        st.write(f'Tanggal akses anda: {today:%d %B %Y}')
    elif choice=='Create New Development Plan':
        create_new_plan()
    elif choice=='Edit or Manage Development Plan':
        edit_plan()
    elif choice=='Delete Development Plan':
        delete_plan()
    elif choice=='View Development Database':
        st.subheader('Rekapitulasi Data Development Plan 2022')
        output_name=f'Data_IDP_2022_{today:%d_%B_%Y}.xlsx'
        result = view_all_data()
        data = pd.DataFrame(result, columns=['NIK', 'Career Ambition', 'Employee Strength', 'Employee Weakness', 'Tgl Mulai Cuti 1', 'Lama Cuti 1', 'Alasan Cuti 1', 'Tgl Mulai Cuti 2', 'Lama Cuti 2', 'Alasan Cuti 2', 'Tgl Mulai Cuti 3', 'Lama Cuti 3', 'Alasan Cuti 3', 'Kompetensi 1', 'Jenis Development 1', 'Deskripsi Development 1', 'Deadline Development 1', 'Kompetensi 2', 'Jenis Development 2', 'Deskripsi Development 2', 'Deadline Development 2', 'Kompetensi 3', 'Jenis Development 3', 'Deskripsi Development 3', 'Deadline Development 3', 'Kompetensi 4', 'Jenis Development 4', 'Deskripsi Development 4', 'Deadline Development 4', 'Kompetensi 5', 'Jenis Development 5', 'Deskripsi Development 5', 'Deadline Development 5', 'Rekomendasi / Catatan'])
        st.write(data)
        st.markdown(get_table_download_link(data, output_file=output_name), unsafe_allow_html=True)

if __name__ == '__main__':
    development_plan()