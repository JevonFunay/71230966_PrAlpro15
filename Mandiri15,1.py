import re
from datetime import datetime

text = """
Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02).
"""
def caritanggal(text):
    cari_tanggal = re.findall(r'\d{4}-\d{2}-\d{2}', text)
    tanggal = []
    for i in cari_tanggal:
        formattanggal = datetime.strptime(i, '%Y-%m-%d')
        gantiformatT = formattanggal.strftime('%d-%m-%Y')
        tanggalsekarang = datetime.now()
        perbandingan = tanggalsekarang - formattanggal
        tanggal.append(f"{i} {gantiformatT}, selisih {perbandingan.days} hari")
    return tanggal

hasil = caritanggal(text)
for r in hasil:
    print(r)
