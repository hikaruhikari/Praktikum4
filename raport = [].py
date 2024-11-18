raport = []
while True:
    Nama     = input("Masukkan Nama: ")
    NIM      = int(input("Masukkan NIM (e.g. 123456789): "))
    Tugas    = int(input("Masukkan Nilai Tugas: "))
    UTS      = int(input("Masukkan Nilai UTS: "))
    UAS      = int(input("Masukkan Nilai UAS: "))
    Akhir    = ((Tugas*0.3) + (UTS*0.35) + (UAS*0.35))
    raport.append({
        "Nama": Nama, 
        "NIM": NIM, 
        "Nilai Tugas": Tugas, 
        "Nilai UTS": UTS, 
        "Nilai UAS": UAS, 
        "Nilai Akhir": Akhir
        })    
    lanjut    = input("Tambah data lagi? (y/t): ").lower()
    if lanjut == "t":
        break
print('_'*70)
print(f"| {'No':^3} | {'Nama':^10} | {'NIM':^10} | {'Tugas':^6} | {'UTS':^6} | {'UAS':^6} | {'Akhir':^6} |")
print('='*70)
for i, data in enumerate(r, start=1):
    print(f"| {i:^3} | {data['Nama']:^10} | {data['NIM']:^10} | {data['Nilai Tugas']:^6.1f} | {data['Nilai UTS']:^6.1f} | {data['Nilai UAS']:^6.1f} | {data['Nilai Akhir']:^6.1f} |")
print('‾'*70)