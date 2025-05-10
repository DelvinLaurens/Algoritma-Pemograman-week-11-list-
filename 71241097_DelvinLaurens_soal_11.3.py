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
