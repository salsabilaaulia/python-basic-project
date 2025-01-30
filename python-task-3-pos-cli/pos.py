import copy
# membuka file teks berisi menu
open_menu = open("menu.txt", "r")
read_menu = open_menu.readlines()

# nilai awal
text_menu = []
dict_menu_kode = {}     
dict_menu_nama = {}     
dict_pesanan_kode = {}  
dict_pesanan_nama = {}  
pesanan = {}
total_harga = 0

# menyimpan data menu
for menu in read_menu:
    if menu[:3] == "===":
        if menu[3:-2].isalpha() == False: # validasi teks jenis menu sesudah "===" hingga sebelum "\n"
            print("Daftar menu tidak valid, cek kembali menu.txt!")
            exit()
        text_menu.append(menu.replace("===","").replace("\n",":\n"))    # menyimpan teks menu per baris ke dalam list
        pass
    else:
        if menu.count(";") != 2 or menu.startswith(";") or menu.count(";;") > 0:    # validasi teks data menu
            print("Daftar menu tidak valid, cek kembali menu.txt!")
            exit()
        else:
            try:
                menu = menu.split(";")
                # menyimpan data menu dalam variabel
                kode_menu = menu[0]
                nama_menu = menu[1]
                harga_menu = int(menu[2].strip("\n"))
                if harga_menu < 0 : # mencegah harga bernilai negatif
                    raise Exception
            except: # mencegah index error dan isi variabel yang tidak sesuai
                print("Daftar menu tidak valid, cek kembali menu.txt!")             # validasi teks data menu
                exit()

            # validasi kode menu tidak sama dengan nama menu dan tidak duplikat
            if kode_menu not in dict_menu_kode.keys() and nama_menu not in dict_menu_nama.keys()\
            and kode_menu not in dict_menu_nama.keys() and nama_menu not in dict_menu_kode.keys():
                dict_menu_kode[kode_menu] = [kode_menu, nama_menu, harga_menu, 0]   # dict untuk menyimpan data menu
                dict_menu_nama[nama_menu] = kode_menu   # dict untuk mengakses data menu melalui nama menu

                text_menu.append(f"{kode_menu} {nama_menu}, " + f"Rp{harga_menu:,}\n".replace(",", "."))  # menyimpan teks menu per baris ke dalam list

            else:
                print("Daftar menu tidak valid, cek kembali menu.txt!")

# IMPLEMENTASI PEMESANAN
banyak_meja = list(range(10 , 0, -1))
while True:
    print("Selamat datang di Kafe Daun Daun Pacilkom")
    input_mode = input("Apa yang ingin Anda lakukan? ")

    #1 MODE BUAT PESANAN
    if input_mode == "BUAT PESANAN":
        if banyak_meja == []:   # tidak ada nomor meja yang tersisa
            print("Mohon maaf meja sudah penuh, silakan kembali nanti.")

        else:
            nomor_meja = banyak_meja.pop()  # menyimpan nomor meja pelanggan
            nama_pelanggan = input("Siapa nama Anda? ")
            # mengeprint menu
            print("\nBerikut ini adalah menu yang kami sediakan:")
            print("".join(text_menu)) 

            while True:
                input_pesanan = input("Masukkan menu yang ingin Anda pesan: ")     

                # menyimpan data pesanan melalui kode menu
                if input_pesanan in dict_menu_kode.keys():
                    if input_pesanan not in dict_pesanan_kode.keys():
                        dict_pesanan_kode[input_pesanan] = copy.deepcopy(dict_menu_kode[input_pesanan])  
                        dict_pesanan_nama[dict_menu_kode[input_pesanan][1]] = input_pesanan                      
                    dict_pesanan_kode[input_pesanan][-1] += 1                   # menghitung banyak pesanan
                    print(f"Berhasil memesan {dict_menu_kode[input_pesanan][1]}.", end= " ")

                # menyimpan data pesanan melalui nama menu
                elif input_pesanan in dict_menu_nama.keys():
                    if input_pesanan not in dict_pesanan_nama.keys():
                        dict_pesanan_kode[dict_menu_nama[input_pesanan]] = copy.deepcopy(dict_menu_kode[dict_menu_nama[input_pesanan]])
                        dict_pesanan_nama[input_pesanan] = dict_menu_nama[input_pesanan]
                    dict_pesanan_kode[dict_menu_nama[input_pesanan]][-1] += 1   # menghitung banyak pesanan
                    print(f"Berhasil memesan {input_pesanan}.", end= " ")

                elif input_pesanan == "SELESAI":                    
                    pesanan[nomor_meja] = dict_pesanan_kode, dict_pesanan_nama, nama_pelanggan  # untuk menyimpan data pelanggan melalui key nomor meja

                    print("\nBerikut adalah pesanan Anda:")
                    for i in pesanan[nomor_meja][0]:
                        banyak_pesanan = pesanan[nomor_meja][0][i][-1]
                        harga = pesanan[nomor_meja][0][i][2]
                        harga = harga * banyak_pesanan
                        print(f"{pesanan[nomor_meja][0][i][1]} {banyak_pesanan} buah, " + f"total Rp{harga:,}".replace(",", "."))
                        total_harga += harga
                    print(f"\nTotal pesanan: Rp{total_harga:,}".replace(",", "."))
                    print(f"Pesanan akan kami proses, Anda bisa menggunakan meja nomor {nomor_meja}. Terima kasih.")
                    
                    # agar data kereset untuk pelanggan selanjutnya
                    total_harga = 0 
                    dict_pesanan_kode = {}
                    dict_pesanan_nama = {}
                    break

                else:
                    print(f"Menu {input_pesanan} tidak ditemukan.", end= " ")
                
    #2 MODE UBAH PESANAN
    if input_mode == "UBAH PESANAN":
        try:
            input_nomor_meja = int(input("Nomor meja berapa? "))
            if input_nomor_meja in pesanan.keys():
                # mengeprint menu
                print("\nBerikut ini adalah menu yang kami sediakan:")
                print("".join(text_menu))

                # mengeprint pesanan
                print("Berikut adalah pesanan Anda:")
                for i in pesanan[input_nomor_meja][0]:
                    banyak_pesanan = pesanan[input_nomor_meja][0][i][-1] # menghitung counter pada list
                    harga = pesanan[input_nomor_meja][0][i][2]
                    harga = harga * banyak_pesanan
                    print(f"{pesanan[input_nomor_meja][0][i][1]} {banyak_pesanan} buah, " + f"total Rp{harga:,}".replace(",", "."))
                print(" ")

                while True:
                    mode_ubah_pesanan = input("Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
                    #A GANTI JUMLAH PESANAN
                    if mode_ubah_pesanan == "GANTI JUMLAH":
                        ganti_jumlah_pesanan = input("Menu apa yang ingin Anda ganti jumlahnya: ")

                        # mengubah jumlah pesanan melalui kode menu
                        if ganti_jumlah_pesanan in pesanan[input_nomor_meja][0].keys():
                            jumlah_baru = int(input("Masukkan jumlah pesanan yang baru: "))
                            if jumlah_baru < 1:
                                print("Jumlah harus bilangan positif!", end= " ")
                            else:
                                pesanan[input_nomor_meja][0][ganti_jumlah_pesanan][-1] = jumlah_baru
                                print(f"Berhasil mengubah pesanan {dict_menu_kode[ganti_jumlah_pesanan][1]} {jumlah_baru} buah.", end= " ")

                        # mengubah jumlah pesanan melalui nama menu
                        elif ganti_jumlah_pesanan in pesanan[input_nomor_meja][1].keys():
                            jumlah_baru = int(input("Masukkan jumlah pesanan yang baru: "))
                            if jumlah_baru < 1:
                                print("Jumlah harus bilangan positif!", end= " ")
                            else:
                                pesanan[input_nomor_meja][0][dict_menu_nama[ganti_jumlah_pesanan]][-1] = jumlah_baru
                                print(f"Berhasil mengubah pesanan {ganti_jumlah_pesanan} {jumlah_baru} buah.", end= " ")

                        else:
                            if ganti_jumlah_pesanan in dict_menu_kode.keys() \
                            or ganti_jumlah_pesanan in dict_menu_nama.keys():
                                print(f"Menu {ganti_jumlah_pesanan} tidak Anda pesan sebelumnya.", end= " ")
                            else:
                                print(f"Menu {ganti_jumlah_pesanan} tidak ditemukan!", end= " ")
            
                    #B HAPUS PESANAN    
                    if mode_ubah_pesanan == "HAPUS":                   
                        hapus_pesanan = input("Menu apa yang ingin Anda hapus dari pesanan: ")
                        # menghapus jumlah pesanan melalui kode menu
                        if hapus_pesanan in pesanan[input_nomor_meja][0].keys():
                            hapus_pesanan = pesanan[input_nomor_meja][0].pop(hapus_pesanan)
                            print(f"{hapus_pesanan[-1]} buah {hapus_pesanan[1]} dihapus dari pesanan.", end= " ")                        
                            hapus_pesanan = pesanan[input_nomor_meja][1].pop(hapus_pesanan[1])
                        
                        # menghapus jumlah pesanan melalui nama menu
                        elif hapus_pesanan in pesanan[input_nomor_meja][1].keys():
                            hapus_pesanan = pesanan[input_nomor_meja][1].pop(hapus_pesanan)
                            hapus_pesanan = pesanan[input_nomor_meja][0].pop(hapus_pesanan)
                            print(f"{hapus_pesanan[-1]} buah {hapus_pesanan[1]} dihapus dari pesanan.", end= " ")

                        else:
                            if hapus_pesanan in dict_menu_kode.keys() \
                            or hapus_pesanan in dict_menu_nama.keys():
                                print(f"Menu {hapus_pesanan} tidak Anda pesan sebelumnya.", end= " ")
                            else:
                                print(f"Menu {hapus_pesanan} tidak ditemukan!", end= " ")
                            
                    #C TAMBAH PESANAN    
                    if mode_ubah_pesanan == "TAMBAH PESANAN":
                        tambah_pesanan = input("Menu apa yang ingin Anda pesan: ")
                        # menu sudah pernah dipesan
                        if tambah_pesanan in pesanan[input_nomor_meja][0].keys():
                            pesanan[input_nomor_meja][0][tambah_pesanan][-1] += 1
                            print(f"Berhasil memesan {dict_menu_kode[tambah_pesanan][1]}.", end= " ")
                        
                        elif tambah_pesanan in pesanan[input_nomor_meja][1].keys():
                            pesanan[input_nomor_meja][0][dict_menu_nama[tambah_pesanan]][-1] += 1
                            print(f"Berhasil memesan {tambah_pesanan}.", end= " ")

                        # menu belum pernah dipesan
                        else:                       
                            if tambah_pesanan in dict_menu_kode.keys():     # menambah pesanan melalui kode menu
                                pesanan[input_nomor_meja][0][tambah_pesanan] = copy.deepcopy(dict_menu_kode[tambah_pesanan])
                                pesanan[input_nomor_meja][1][dict_menu_kode[tambah_pesanan][1]] = tambah_pesanan
                                pesanan[input_nomor_meja][0][tambah_pesanan][-1] += 1
                                print(f"Berhasil memesan {dict_menu_kode[tambah_pesanan][1]}.", end= " ")

                            elif tambah_pesanan in dict_menu_nama.keys():   # menambah pesanan melalui nama menu
                                pesanan[input_nomor_meja][0][dict_menu_nama[tambah_pesanan]] = copy.deepcopy(dict_menu_kode[dict_menu_nama[tambah_pesanan]])
                                pesanan[input_nomor_meja][1][tambah_pesanan] = dict_menu_nama[tambah_pesanan]
                                pesanan[input_nomor_meja][0][dict_menu_nama[tambah_pesanan]][-1] += 1
                                print(f"Berhasil memesan {tambah_pesanan}.", end= " ")
                            
                            else:
                                print(f"Menu {tambah_pesanan} tidak ditemukan!", end= " ")

                    #D STOP MENGGUNAKAN MODE UBAH PESANAN   
                    if mode_ubah_pesanan == "SELESAI":
                        print("\nBerikut adalah pesanan terbaru Anda:")
                        # menghitung pesanan baru
                        for i in pesanan[input_nomor_meja][0]:
                            banyak_pesanan = pesanan[input_nomor_meja][0][i][-1]
                            harga = pesanan[input_nomor_meja][0][i][2]
                            harga = harga * banyak_pesanan
                            print(f"{pesanan[input_nomor_meja][0][i][1]} {banyak_pesanan} buah, " + f"total Rp{harga:,}".replace(",", "."))
                            total_harga += harga
                        print(f"\nTotal pesanan: {total_harga:,}".replace(",", "."))
                        total_harga = 0
        
                        break   

            #E JIKA MEJA TIDAK SESUAI        
            else:
                print("Nomor meja kosong atau tidak sesuai!")
        except:
            print("Nomor meja kosong atau tidak sesuai!")
    #3 MODE SELESAI MENGGUNAKAN MEJA
    if input_mode == "SELESAI MENGGUNAKAN MEJA":
        input_nomor_meja = int(input("Nomor meja berapa? "))
        if input_nomor_meja in pesanan.keys():
            struk = open(f"receipt_{pesanan[input_nomor_meja][-1]}.txt", "w")
            # mengeprint dalam file struk
            for i in pesanan[input_nomor_meja][0].keys():
                kode_pesanan = pesanan[input_nomor_meja][0][i][0]
                nama_pesanan = pesanan[input_nomor_meja][0][i][1]
                banyak_pesanan = pesanan[input_nomor_meja][0][i][-1]
                harga_pesanan = pesanan[input_nomor_meja][0][i][2]
                total_harga_pesanan = harga_pesanan * banyak_pesanan
                print(f"{kode_pesanan};{nama_pesanan};{banyak_pesanan};{harga_pesanan};{total_harga_pesanan}",file= struk)
                total_harga += total_harga_pesanan
            print(f"\nTotal {total_harga}", file= struk)
            total_harga = 0

            print(f"Pelanggan atas nama {pesanan[input_nomor_meja][-1]} selesai menggunakan meja {input_nomor_meja}.")
            
            # mengembalikan nomor meja
            pesanan.pop(input_nomor_meja)   # menghapus data pelanggan yang sudah selesai
            banyak_meja.append(input_nomor_meja)
            banyak_meja.sort(reverse= True)

            struk.flush()
            struk.close()

        else:
            print("Nomor meja kosong atau tidak sesuai!")
    
    print("\n---")
    
open_menu.close()