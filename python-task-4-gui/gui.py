import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox

# CLASS UNTUK MENGAKSES DAN MENGKALISIFASIKAN JENIS MENU
class Meals(Menu):
    meals_menu = []

class Drinks(Menu):
    drinks_menu = []

class Sides(Menu):
    sides_menu = []

# CLASS WINDOW UTAMA
class Main(tk.Frame):
    list_menu = {}
    def __init__(self, master = None):
        super().__init__(master)
        # setting utama main window
        self.master.geometry("400x200")
        self.pack()
        master.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.master.resizable(False, False)

        # widget button main window
        self.button1 = tk.Button(self, text="Buat Pesanan", width=30, command=self.buat_pesanan, bg="#4472C4", fg="white")\
                .grid(row=1, column=1, padx=10, pady=40)
        self.button2 = tk.Button(self, text="Selesai Gunakan Meja", width=30, command=self.selesai_gunakan_meja, bg="#4472C4", fg="white")\
                .grid(row=2, column=1)

    def buat_pesanan(self):
        BuatPesanan(self.master)

    def selesai_gunakan_meja(self):
        SelesaiGunakanMeja(self.master)

# CLASS WINDOW INPUT NAMA PELANGGAN
class BuatPesanan(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        # setting awal window
        self.geometry("")
        self.grid()
        self.resizable(False, False)

        # widget label dan entry "input nama"
        self.lbl_nama = tk.Label(self, text="Siapa nama Anda?")\
                .grid(row=1, column=1, padx=(45,5), pady=(70,20))
        Meja.nama = tk.StringVar()      # menyimpan nama pelanggan
        self.ent_nama = tk.Entry(self, textvariable= Meja.nama)\
                .grid(row=1, column=2, padx=(10,55), pady=(70,20))
        
        # widget tombol "lanjut" dan "kembali"
        self.button1 = tk.Button(self, text="Lanjut", width=20, command=self.tabel_buat_pesanan, bg="#4472C4", fg="white")\
            .grid(row=2, column=2, padx=(5,45), pady=40)
        self.button2 = tk.Button(self, text="Kembali", width=20, command=self.destroy, bg="#4472C4", fg="white")\
            .grid(row=2, column=1, padx=(45,5), pady=40)        
    
    def tabel_buat_pesanan(self):
        # jika meja sudah penuh
        if len(Meja.no_meja_terisi) == 10:
            messagebox.showinfo("Kafe Daun-Daun Pacilkom v2.0 🌿", "Mohon maaf, meja sedang penuh. Silakan datang kembali di lain kesempatan.")
            self.destroy()
        else:
            Tabel(self.master)
            self.destroy()
    
# CLASS WINDOW MEMESAN MENU
class Tabel(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        # setting awal window
        self.geometry("") 
        self.grid()
        self.resizable(False, False) 

        # nilai awal
        self.start_baris = 0        # menyimpan nilai barisan widget
        self.harga = 0  # menyimpan total harga
        self.dict = {}  # menyimpan banyak pesanan
        self.dict2 = {} # menyimpan harga pesanan
        Meja.dict_pesanan[Meja.no_meja_now] = []    # menyimpan semua data pelanggan

        self.upper_menu()   # widget

        # widget tabel menu
        self.lbl_menu("MEALS")
        self.tabel_info("Kegurihan")
        self.tabel_menu(Meals.meals_menu) 

        self.lbl_menu("DRINKS")
        self.tabel_info("Kemanisan")
        self.tabel_menu(Drinks.drinks_menu) 

        self.lbl_menu("SIDES")
        self.tabel_info("Keviralan")
        self.tabel_menu(Sides.sides_menu)        

        # widget harga menu
        self.teks_harga()

        # widget button "kembali" dan konfirmasi pesanan
        self.button1 = tk.Button(self, text="Kembali", width=15, bg="#4472C4", fg="white", command= self.destroy)\
                .grid(row=self.start_baris, column=1, columnspan=2, pady=(30,10))
        self.button2 = tk.Button(self, text="OK", width=15, bg="#4472C4", fg="white", command= self.selesai)\
                .grid(row=self.start_baris, column=2, columnspan=2, pady=(30,10))

    # konfigurasi label menu
    def lbl_menu(self, input_text):
        tk.Label(self, text=input_text).grid(row = self.start_baris, column = 0, padx=(40,40))
        self.start_baris += 1
    
    # konfigurasi heading tabel
    def tabel_info(self, input_text):
        teks_info_tabel = ["Kode", "Nama", "Harga", input_text, "Jumlah"]
        for kolom in range(5):
            if kolom == 0:
                padx = (30,0)   # pad pada ujung kiri tabel
            elif kolom == 4:
                padx = (0,30)   # pad pada ujung kanan tabel
            else:
                padx = (0,0)
            entry = tk.Entry(self, width = 20, fg = 'black')
            entry.grid(row = self.start_baris, column = kolom, padx=padx)
            entry.insert(tk.END, teks_info_tabel[kolom])
            entry['state'] = 'readonly'
        self.start_baris += 1

    def upper_menu(self):
        # label nama dan no meja pelanggan
        self.nama_pemesan = tk.Label(self, text=f"Nama pemesan: {Meja.nama.get()}")\
                .grid(row = 0, column = 0, columnspan=2, sticky="w", padx=(40,0), pady=(0,20))
        self.no_meja = tk.Label(self, text=f"No Meja: {Meja.no_meja_now}")\
                .grid(row = 0, column = 3, sticky="e", pady=(0,30))
        # button ubah meja
        self.ubah_meja = tk.Button(self, text="Ubah", bg="#4472C4", fg="white", command=self.ubah_meja)\
                .grid(row = 0, column = 4, sticky="w", pady=(0,30))
        self.start_baris += 1
        
    def teks_harga(self):
        self.lbl_harga = tk.Label(self, text=f"Total harga: {self.harga}", font=("Arial Bold", 10))
        self.lbl_harga.grid(row=self.start_baris, column=4, sticky="w")
        self.start_baris += 1

    def ubah_meja(self):
        self.destroy()       
        UbahMeja(self.master)
        
    # konfigurasi isi tabel
    def tabel_menu(self, list_menu):
        self.total_baris = len(list_menu)
        self.total_kolom = len(list_menu[0])

        for baris in range(self.total_baris):
            for kolom in range(self.total_kolom - 1):
                if kolom == 0:
                    padx = (30,0)   # pad pada kiri tabel
                else:
                    padx = (0,0)
                entry = tk.Entry(self, width = 20, fg = 'black')
                entry.grid(row = self.start_baris + baris, column = kolom, padx= padx)
                entry.insert(tk.END, list_menu[baris][kolom])
                entry['state'] = 'readonly'

            self.dict2[f"combobox{self.start_baris + baris}"] = list_menu[baris][2] # harga menu
            Meja.dict_pesanan[Meja.no_meja_now].append(0)   # nilai awal banyak menu

            # konfigurasi kolom paling kanan (combobox)
            values = tuple([k for k in range(10)])  # nilai yang tertera pada combobox
            self.dict[f"combobox{self.start_baris + baris}"]= ttk.Combobox(self, values = values)
            self.dict[f"combobox{self.start_baris + baris}"].set(0)  
            self.dict[f"combobox{self.start_baris + baris}"].grid(row = self.start_baris + baris, column = 4, padx=(0,30))
            

            # combobox terhubung dengan fungsi menghitung harga
            self.dict[f"combobox{self.start_baris + baris}"].bind("<<ComboboxSelected>>", self.total_harga)

            count_baris = baris + 1
        self.start_baris += count_baris

    # meghitung total harga
    def total_harga(self, event= None):
        Meja.dict_pesanan[Meja.no_meja_now] = []
        self.harga = 0
        for key in self.dict.keys():
            # menyimpan harga sesuat no meja pelanggan
            self.harga += int(self.dict[key].get()) * int(self.dict2[key])
            Meja.dict_pesanan[Meja.no_meja_now].append(int(self.dict[key].get()))
        self.lbl_harga["text"]=f"Total harga: {self.harga}"     # mengubah label total harga
        
    # menyimpan data pelanggan
    def selesai(self):
        Meja.dict_pesanan[Meja.no_meja_now].append(Meja.nama.get())
        Meja.dict_pesanan[Meja.no_meja_now].append(self.harga)

        # mereset harga untuk pelanggan selanjutnya
        self.harga = 0
        Meja.no_meja_terisi.append(Meja.no_meja_now)
              
        if len(Meja.no_meja_terisi) == 10:
            pass       
        else:
            Meja.no_meja_now = Meja.no_meja_kosong.pop() # mengeset no meja pelanggan selanjutnya
        self.destroy()

# CLASS MENYIMPAN DATA MEJA DAN PESANAN
class Meja():
    dict_button = {}
    dict_pesanan = {}
    no_meja_kosong = [9,8,7,6,5,4,3,2,1]
    no_meja_terisi = []
    no_meja_now = 0
    meja_selesai = 0
    nama = ""

# CLASS WINDOW MENGUBAH MEJA
class UbahMeja(tk.Toplevel):   
    def __init__(self, master = None):
        super().__init__(master)
        # setting awal window
        self.geometry("")
        self.resizable(False, False)
        self.grid()

        # nilai awal
        self.start_baris = 0
        self.count_meja = 0
        self.no_meja_now = Meja.no_meja_now
        
        # widget label keterangan meja
        tk.Label(self, text="Silakan klik meja kosong yang diinginkan")\
                .grid(row=0, column=0, pady=(0,30), columnspan=4)
        self.interface_meja()   # widget tombol meja
        tk.Label(self, text="Info", font=("Arial Bold", 10))\
                .grid(row=self.start_baris, column=0, sticky="w", pady=(20,0), padx=30)
        self.start_baris += 1
        tk.Label(self, text="Merah: Terisi")\
                .grid(row=self.start_baris, column=0, sticky="w", columnspan=2, padx=30)
        self.start_baris += 1
        tk.Label(self, text="Abu-abu: Kosong")\
                .grid(row=self.start_baris, column=0, sticky="w", columnspan=2, padx=30)
        self.start_baris += 1
        tk.Label(self, text="Biru: Meja Anda")\
                .grid(row=self.start_baris, column=0, sticky="w", columnspan=2, padx=30)
        self.start_baris += 1

        # widget button
        self.button1 = tk.Button(self, text="Kembali", bg="#4472C4", fg="white", width=20, command=self.destroy)\
            .grid(row=self.start_baris, column=0, columnspan=2, padx=(50,10), pady=(20,30))
        self.button2 = tk.Button(self, text="OK", bg="#4472C4", fg="white", width=20, command= self.konfirmasi_no_meja)\
            .grid(row=self.start_baris, column=2, columnspan=2, padx=(10,50), pady=(20,30))        

        # mengatur ukuran kolom window
        self.columnconfigure(0, minsize=50)
        self.columnconfigure(3, minsize=90)
    
    # membuat tombol meja
    def interface_meja(self):
        for baris in range(5):
            for kolom in range(1, 3):                  
                Meja.dict_button[self.count_meja] = tk.Button(self, width = 10, fg = 'white',
                    bg= "#a8a4a4", text=self.count_meja, font=('Arial 10'),
                    command= lambda no_meja=self.count_meja : self.ganti_no_meja(no_meja))
                # mengatur posisi tombol
                if kolom == 1:
                    sticky = "e"
                else:
                    sticky = "w"
                Meja.dict_button[self.count_meja].grid(row = baris+1, column = kolom, pady=(5,5), padx=(5,5), sticky=sticky)

                self.count_meja += 1
                self.start_baris += 1
            self.start_baris += 1

        # mengeset warna tombol meja sesuai keterangan meja
        for key in Meja.dict_button.keys():     
          if key == self.no_meja_now:
            Meja.dict_button[key].configure(bg = "blue")
          elif key in Meja.no_meja_terisi:
            Meja.dict_button[key].configure(bg = "#ff0404")

    # mengambil nilai dan mengatur warna tombol meja yang dipilih
    def ganti_no_meja(self, no_meja):
        if no_meja in Meja.no_meja_terisi:
            pass
        else:
            Meja.dict_button[self.no_meja_now].configure(bg="#a8a4a4")
            Meja.dict_button[no_meja].configure(bg="blue")
            self.no_meja_now = no_meja

    # mengeset nomor meja yang baru
    def konfirmasi_no_meja(self):
        Meja.no_meja_kosong.append(Meja.no_meja_now)
        Meja.no_meja_now = self.no_meja_now       

        self.destroy()
        Tabel(self.master)  # kembali ke window tabel menu

# CLASS WINDOW SELESAI MENGGUNAKAN MEJA
class SelesaiGunakanMeja(tk.Toplevel):   
    def __init__(self, master = None):
        super().__init__(master)
        # setting awal window
        self.geometry("")
        self.resizable(False, False)
        self.grid()

        # nilai awal
        self.start_baris = 0
        self.count_meja = 0
        self.no_meja_now = Meja.no_meja_now

        # widget label keterangan meja
        tk.Label(self, text="Silakan klik meja kosong yang selesai digunakan")\
                .grid(row=0, column=0, pady=(0,30), columnspan=4)

        UbahMeja.interface_meja(self)

        tk.Label(self, text="Info", font=("Arial Bold", 10))\
                .grid(row=self.start_baris, column=0, sticky="w", pady=(20,0), padx=30)
        self.start_baris += 1
        tk.Label(self, text="Abu-abu: Kosong")\
                .grid(row=self.start_baris, column=0, sticky="w", columnspan=2, padx=30)
        self.start_baris += 1
        tk.Label(self, text="Merah: Terisi")\
                .grid(row=self.start_baris, column=0, sticky="w", columnspan=2, padx=30)
        self.start_baris += 1
        self.button1 = tk.Button(self, text="Kembali", bg="#4472C4", fg="white", width=20, command=self.destroy)\
                .grid(row=self.start_baris, column=0, columnspan=4, pady=(20,30))
        
        # konfigurasi kolom window
        self.columnconfigure(0, minsize=50)
        self.columnconfigure(3, minsize=90)

        # mengeset warna tombol meja sesuai keterangan
        for key in Meja.dict_button.keys():                 
            if key in Meja.no_meja_terisi:
                Meja.dict_button[key].configure(bg = "#ff0404")
                Meja.dict_button[key].configure(command= lambda no_meja=key : self.tabel_pesanan(no_meja))
            else:
                Meja.dict_button[key].configure(bg = "#a8a4a4")
                Meja.dict_button[key].configure(command=None)
    
    # membuka window pesanan no meja yang dipilih
    def tabel_pesanan(self, no_meja):
        SelesaiGunakanMeja.destroy(self)
        Meja.meja_selesai = no_meja
        TabelPesanan(self.master)
        
    # agar inheritance method tidak melakukan apapun
    def ganti_no_meja(self, event):
        pass

# CLASS WINDOW TABEL MENU PESANAN PELANGGAN
class TabelPesanan(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        # setting awal window
        self.geometry("")
        self.resizable(False, False)
        self.grid()   

        # nilai awal    
        self.start_baris = 0
        self.start_menu = 0
        self.meja_selesai = Meja.meja_selesai

        self.nama_pemesan = tk.Label(self, text=f"Nama pemesan: {Meja.dict_pesanan[self.meja_selesai][-2]}")\
                .grid(row = 0, column = 0, columnspan=2, sticky="w", padx=(40,0), pady=(0,20))
        self.no_meja = tk.Label(self, text=f"No Meja: {self.meja_selesai}")\
                .grid(row = 0, column = 3, sticky="e", pady=(0,30))
        self.start_baris += 1

        # inheritance widget class Tabel
        Tabel.lbl_menu(self, "MEALS")
        Tabel.tabel_info(self, "Kegurihan")
        self.tabel_pesanan(Meals.meals_menu) 
        self.start_baris +=1

        Tabel.lbl_menu(self, "DRINKS")
        Tabel.tabel_info(self, "Kemanisan")
        self.tabel_pesanan(Drinks.drinks_menu) 
        self.start_baris +=1

        Tabel.lbl_menu(self, "SIDES")
        Tabel.tabel_info(self, "Keviralan")
        self.tabel_pesanan(Sides.sides_menu)
        self.start_baris +=1        

        self.lbl_harga = tk.Label(self, text=f"Total harga: {Meja.dict_pesanan[self.meja_selesai][-1]}", font=("Arial Bold", 10))
        self.lbl_harga.grid(row=self.start_baris, column=4, sticky="w")
        self.start_baris += 1

        self.button1 = tk.Button(self, text="Kembali", width=17, bg="#4472C4", fg="white", command= self.kembali)\
            .grid(row=self.start_baris, column=1, columnspan=2, pady=(30,10), padx=(50,0), sticky="w")
        self.button2 = tk.Button(self, text="Selesai Gunakan Meja", width=17, bg="#4472C4", fg="white", command= self.pesanan_selesai)\
            .grid(row=self.start_baris, column=2, columnspan=2, pady=(30,10), padx=(0,50), sticky="e")

    # kembali ke window selesai gunakan meja
    def kembali(self):
        SelesaiGunakanMeja(self.master)
        self.destroy()
    
    # konfirmasi pesanan pelangan sudah selesai
    def pesanan_selesai(self):
        print(Meja.no_meja_now)
        print(Meja.no_meja_terisi)
        print(Meja.no_meja_kosong)
        print(self.meja_selesai)
        if len(Meja.no_meja_terisi) == 10:
            Meja.no_meja_now = self.meja_selesai
        else:
            Meja.no_meja_kosong.append(self.meja_selesai)   # mengembalikan meja menjadi kosong
        Meja.no_meja_terisi.remove(self.meja_selesai)
        Meja.dict_pesanan[self.meja_selesai] = []           # menghapus data pelanggan yang selesai

        SelesaiGunakanMeja(self.master)
        self.destroy()

    # menampilkan tabel pesanan pelanggan
    def tabel_pesanan(self, list_menu):
        self.total_baris = len(list_menu)
        self.total_kolom = len(list_menu[0])

        for baris in range(self.total_baris):
            for kolom in range(self.total_kolom):   
                # konfigurasi pad           
                if kolom == 4:
                    padx = (0,30)
                    entry = tk.Entry(self, width = 20, fg = 'black')
                    entry.grid(row = self.start_baris + baris, column = kolom, padx= padx)
                    entry.insert(tk.END, Meja.dict_pesanan[Meja.meja_selesai][self.start_menu])
                    entry['state'] = 'readonly'
                    self.start_menu += 1
                else:
                    if kolom == 0:
                        padx = (30,0)
                    else:
                        padx = (0,0)
                    entry = tk.Entry(self, width = 20, fg = 'black')
                    entry.grid(row = self.start_baris + baris, column = kolom, padx= padx)
                    entry.insert(tk.END, list_menu[baris][kolom])
                    entry['state'] = 'readonly'
        self.start_baris +=1

# membuka menu dari teks
open_menu = open("menu.txt", "r")
read_menu = open_menu.readlines()

# iterasi menu
for menu in read_menu:
    if menu.startswith("==="):
        jenis = menu.replace("===", "").strip("\n")
    else:
        menu = menu.split(";")
        # menyimpan data menu dalam variabel
        kode_menu = menu[0]
        nama_menu = menu[1]
        harga_menu = int(menu[2])
        info_menu = menu[3].strip("\n")

        # menyimpan data menu dalam class
        if jenis == "MEALS":
            Meals.meals_menu.append([kode_menu, nama_menu, harga_menu, info_menu, 0])    
        elif jenis == "DRINKS":
            Drinks.drinks_menu.append([kode_menu, nama_menu, harga_menu, info_menu, 0]) 
        elif jenis == "SIDES":
            Sides.sides_menu.append([kode_menu, nama_menu, harga_menu, info_menu, 0]) 

# variabel utama pemanggil class
window = tk.Tk()
cafe = Main(window)
window.mainloop()