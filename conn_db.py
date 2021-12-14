import sqlite3
import base64
from io import BytesIO
import pandas as pd

conn = sqlite3.connect('data_hcbp1.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS data_idp(nik INTEGER, ambition TEXT, strength TEXT, weakness TEXT, cuti_start_1 DATE, lama_cuti_1 TEXT, alasan_cuti_1 TEXT,  cuti_start_2 DATE, lama_cuti_2 TEXT, alasan_cuti_2 TEXT, cuti_start_3 DATE, lama_cuti_3 TEXT, alasan_cuti_3 TEXT, competencies_1 TEXT, dev_type_1 TEXT, dev_desc_1 TEXT, dev_date_1 DATE, competencies_2 TEXT, dev_type_2 TEXT, dev_desc_2 TEXT, dev_date_2 DATE, competencies_3 TEXT, dev_type_3 TEXT, dev_desc_3 TEXT, dev_date_3 DATE, competencies_4 TEXT, dev_type_4 TEXT, dev_desc_4 TEXT, dev_date_4 DATE, competencies_5 TEXT, dev_type_5 TEXT, dev_desc_5 TEXT, dev_date_5 DATE, recommendation TEXT)')

def add_data(nik, ambition, strength, weakness, cuti_start_1, lama_cuti_1, alasan_cuti_1, cuti_start_2, lama_cuti_2, alasan_cuti_2, cuti_start_3, lama_cuti_3, alasan_cuti_3, competencies_1, dev_type_1, dev_desc_1, dev_date_1, competencies_2, dev_type_2, dev_desc_2, dev_date_2, competencies_3, dev_type_3, dev_desc_3, dev_date_3, competencies_4, dev_type_4, dev_desc_4, dev_date_4, competencies_5, dev_type_5, dev_desc_5, dev_date_5, recommendation):
    c.execute('INSERT INTO data_idp(nik, ambition, strength, weakness, cuti_start_1, lama_cuti_1, alasan_cuti_1, cuti_start_2, lama_cuti_2, alasan_cuti_2, cuti_start_3, lama_cuti_3, alasan_cuti_3, competencies_1, dev_type_1, dev_desc_1, dev_date_1, competencies_2, dev_type_2, dev_desc_2, dev_date_2, competencies_3, dev_type_3, dev_desc_3, dev_date_3, competencies_4, dev_type_4, dev_desc_4, dev_date_4, competencies_5, dev_type_5, dev_desc_5, dev_date_5, recommendation) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )', (nik, ambition, strength, weakness, cuti_start_1, lama_cuti_1, alasan_cuti_1, cuti_start_2, lama_cuti_2, alasan_cuti_2, cuti_start_3, lama_cuti_3, alasan_cuti_3, competencies_1, dev_type_1, dev_desc_1, dev_date_1, competencies_2, dev_type_2, dev_desc_2, dev_date_2, competencies_3, dev_type_3, dev_desc_3, dev_date_3, competencies_4, dev_type_4, dev_desc_4, dev_date_4, competencies_5, dev_type_5, dev_desc_5, dev_date_5, recommendation))
    conn.commit()

def view_all_data():
    c.execute('SELECT * FROM data_idp')
    data = c.fetchall()
    return data

def filter_data(nik):
    c.execute('SELECT * FROM data_idp WHERE nik={}'.format(nik))
    data = c.fetchall()
    return data

def edit_data(new_ambition, new_strength, new_weakness, new_cuti_start_1, new_lama_cuti_1, new_alasan_cuti_1, new_cuti_start_2, new_lama_cuti_2, new_alasan_cuti_2, new_cuti_start_3, new_lama_cuti_3, new_alasan_cuti_3, new_competencies_1, new_dev_type_1, new_dev_desc_1, new_dev_date_1, new_competencies_2, new_dev_type_2, new_dev_desc_2, new_dev_date_2, new_competencies_3, new_dev_type_3, new_dev_desc_3, new_dev_date_3, new_competencies_4, new_dev_type_4, new_dev_desc_4, new_dev_date_4, new_competencies_5, new_dev_type_5, new_dev_desc_5, new_dev_date_5, new_recommendation, ambition, strength, weakness, cuti_start_1, lama_cuti_1, alasan_cuti_1, cuti_start_2, lama_cuti_2, alasan_cuti_2, cuti_start_3, lama_cuti_3, alasan_cuti_3, competencies_1, dev_type_1, dev_desc_1, dev_date_1, competencies_2, dev_type_2, dev_desc_2, dev_date_2, competencies_3, dev_type_3, dev_desc_3, dev_date_3, competencies_4, dev_type_4, dev_desc_4, dev_date_4, competencies_5, dev_type_5, dev_desc_5, dev_date_5, recommendation):
    c.execute('UPDATE data_idp SET ambition=?, strength=?, weakness=?, cuti_start_1=?, lama_cuti_1=?, alasan_cuti_1=?, cuti_start_2=?, lama_cuti_2=?, alasan_cuti_2=?, cuti_start_3=?, lama_cuti_3=?, alasan_cuti_3=?, competencies_1=?, dev_type_1=?, dev_desc_1=?, dev_date_1=?, competencies_2=?, dev_type_2=?, dev_desc_2=?, dev_date_2=?, competencies_3=?, dev_type_3=?, dev_desc_3=?, dev_date_3=?, competencies_4=?, dev_type_4=?, dev_desc_4=?, dev_date_4=?, competencies_5=?, dev_type_5=?, dev_desc_5=?, dev_date_5=?, recommendation=? where ambition=? AND strength=? AND weakness=? AND cuti_start_1=? AND lama_cuti_1=? AND alasan_cuti_1=? AND cuti_start_2=? AND lama_cuti_2=? AND alasan_cuti_2=? AND cuti_start_3=? AND lama_cuti_3=? AND alasan_cuti_3=? AND competencies_1=? AND dev_type_1=? AND dev_desc_1=? AND dev_date_1=? AND competencies_2=? AND dev_type_2=? AND dev_desc_2=? AND dev_date_2=? AND competencies_3=? AND dev_type_3=? AND dev_desc_3=? AND dev_date_3=? AND competencies_4=? AND dev_type_4=? AND dev_desc_4=? AND dev_date_4=? AND competencies_5=? AND dev_type_5=? AND dev_desc_5=? AND dev_date_5=? AND recommendation=?', (new_ambition, new_strength, new_weakness, new_cuti_start_1, new_lama_cuti_1, new_alasan_cuti_1, new_cuti_start_2, new_lama_cuti_2, new_alasan_cuti_2, new_cuti_start_3, new_lama_cuti_3, new_alasan_cuti_3, new_competencies_1, new_dev_type_1, new_dev_desc_1, new_dev_date_1, new_competencies_2, new_dev_type_2, new_dev_desc_2, new_dev_date_2, new_competencies_3, new_dev_type_3, new_dev_desc_3, new_dev_date_3, new_competencies_4, new_dev_type_4, new_dev_desc_4, new_dev_date_4, new_competencies_5, new_dev_type_5, new_dev_desc_5, new_dev_date_5, new_recommendation, ambition, strength, weakness, cuti_start_1, lama_cuti_1, alasan_cuti_1, cuti_start_2, lama_cuti_2, alasan_cuti_2, cuti_start_3, lama_cuti_3, alasan_cuti_3, competencies_1, dev_type_1, dev_desc_1, dev_date_1, competencies_2, dev_type_2, dev_desc_2, dev_date_2, competencies_3, dev_type_3, dev_desc_3, dev_date_3, competencies_4, dev_type_4, dev_desc_4, dev_date_4, competencies_5, dev_type_5, dev_desc_5, dev_date_5, recommendation))
    conn.commit()
    data = c.fetchall()
    return data

def delete_data(nik):
    c.execute('DELETE FROM data_idp WHERE nik={}'.format(nik))
    conn.commit()

#Function to download as excel
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def get_table_download_link(df, output_file):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    val = to_excel(df)
    b64 = base64.b64encode(val)  # val looks like b'..,.'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download={output_file}>Download Data</a>' # decode b'abc' => abc