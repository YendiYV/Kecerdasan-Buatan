import json #Mengimpor ekstensi untuk membaca dan menulis suatu data ke dalam file yang berformat json (JavaScript Object Notation)
a = open('data.json') #Mendefinisikan a untuk membuka data.json
data = json.load(a) #Mendefinisikan data untuk membaca data.json

print('''
1. Melatih bot
2. Berbicara dengan bot
	''')

while True:
	input_awal = input("Masukkan kode : ")
	if input_awal == "1":
		while True:
			x = input("User\t: ")
			if x == "keluar":
				break
			else:
				y = input("Bot\t: ")
				data[x] = y #melakukan tugas pada data dengan mengatautkan input x dengan input y menggunakan variabel data.
				b 	 = open('data.json',"w")#Berfungsi untuk membuka file dengan nama data.json dan dalam mode write(menulis)
				json.dump(data,b) #Berfungsi untuk menulis objek ke dalam file json
				b.close()#Menutup file json yang dibuka tadi

	elif input_awal == "2":
		while True:
			x = input("User\t: ")
			if x == 'keluar':
				break
			if x in data:
				print(f'Bot\t: {data[x]}')
			else:
				print("Bot\t: Itu kata yang baru")

	else:
		passimport
