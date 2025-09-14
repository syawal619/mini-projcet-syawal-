#nama:Muhammad Syawal Samir
#kelas:B
#nim:2509116079

ngecek_gudang_internet = ["kabel utp", "kabel dropcore", "kabel lan", "kabel stp"]
print("Selamat Datang di gudang kabel telkom")
print("\n=== Daftar kabel saat ini ===")
for i, kabel in enumerate(ngecek_gudang_internet, start=1):
    print(f"{i}. {kabel}")
    
#pengertian kabel
while True:
    hasil_pengertian = int(input("masukkan nomor kabel yang ingin kamu pahami (1-4):")) 

    if hasil_pengertian== 1:
        print("\npengertian kabel utp adalah jenis kabel yang terdiri dari pasangan.")
        break
    elif hasil_pengertian == 2:
        print("\npengertian kabel dropcore adalah kabel serat optik tunggal yang digunakan untuk jaringan internet.")
        break
    elif hasil_pengertian == 3:
        print("\npengertian Kabel lan adalah jaringan fisik yang digunakan untuk menghubungkan perangkat seperti switch,router")
        break
    elif hasil_pengertian == 4:
        print("\npengertian kabel stp adalah jenis kabel pasangan terpilih yang memiliki lapisan pelindung tambahan")
        break
    else:
        print("\nData tidak tersedia, Coba lagi")
        continue

#kegunaan kabel
print("\n=== Daftar kabel saat ini ===")
for i, kabel in enumerate(ngecek_gudang_internet, start=1):
    print(f"{i}. {kabel}")

while True:
    hasil_kegunaan = int (input("\nmasukkan no kabel yang ingin kamu tau kegunaanya (1-4):"))  

    if hasil_kegunaan == 1:
        print("kabel utp kegunannya sebagai media tranmisi data dalam jaringan komputer khususnya unntuk membangun jaringan area lokal.")
        break
    elif hasil_kegunaan == 2:
        print("Kabel dropcore kegunannya menghubungkan jaringan utama(distribusi)ke pelanggan akhir,seperti rumah atau gedung.")
        break
    elif hasil_kegunaan == 3:
        print("kabel lan kegunannya sebagai tulang punggung jaringan untuk menghubungkan berbagai perangkat seperti komputer,router,dan printer.")
        break
    elif hasil_kegunaan == 4:
        print("kabel stp kegunannya melindungi tranmisi data dari gangguan sinyal(interferensi elektromagnetik)berkat lapisan pelindungnya yang ekstra.")
        break
    else:
        print("Data tidak tersedia, coba lagi")
        continue        


#pengapusan Data Kabel

print("\n=== Daftar kabel saat ini ===")

for i, kabel in enumerate(ngecek_gudang_internet, start=1):
    print(f"{i}. {kabel}")

while True:   
 try:
   hapus_kabel = int(input("Masukkan nomor kabel yang ingin dihapus: "))

   if 1 <= hapus_kabel <= len(ngecek_gudang_internet):
    kabel_yang_dihapus = ngecek_gudang_internet.pop(hapus_kabel - 1)
    print(f"\nkabel '{kabel_yang_dihapus}' berhasil dihapus.")  
   else:
    print("\nNomor kabel tidak valid")
 except ValueError:
    print("\nInput harus berupa angkat!")

print("\n=== Daftar kabel setelah penghapusan ===")
for i, kabel in enumerate(ngecek_gudang_internet, start = 1):
    print(f"{i}. {kabel}")
    
#riwayat pilihan
print("\n=== Riwayat Pilihanmu ===")
print("Nomor kabel (pengertian):", hasil_pengertian)
print("Nomor kabel (kegunaan):", hasil_kegunaan)
print("Nomor kabel yang dihapus:", hapus_kabel)


 