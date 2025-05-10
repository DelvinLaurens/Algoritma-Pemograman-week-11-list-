# def angka_terbaik(data):
#     urutan = sorted(data, reverse=True)
#     return urutan[:3]

# print(angka_terbaik([10, 25, 7, 72, 34, 67]))



#soal 2
# simpan = []
# while True:
#     jumlahngka = input("Masukan angka (Ketikkan 'done' jika selesai): ")
#     if jumlahngka.lower() == 'done':
#         break 
#     angka = float(jumlahngka)
#     simpan.append(angka)
# if simpan:
#     ratarata = sum(simpan) / len(simpan)
#     print(f'Nilai rata - rata adalah: {ratarata}')
# else:
#     print("Tidak ada bilangan yang dimasukkan")

#Soal 3
def tampilkata(namafile):
    try:
        with open(namafile, 'r') as file:
            isi = file.read()
            isi = isi.lower()
            isi = isi.replace(',','')
            isi = isi.replace('.','')
            pisah = isi.split()
            simpan = []
            for i in pisah:
                if i not in simpan:
                    simpan.append(i)
            for j in simpan:
                print(j)
            print(f'Jumlah kata unik: {len(simpan)}')
    except FileNotFoundError:
        print("file tidak ada")

tampilkata('artikel.txt')