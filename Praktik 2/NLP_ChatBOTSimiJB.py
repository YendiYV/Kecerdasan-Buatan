import json #Mengimpor ekstensi untuk membaca dan menulis suatu data ke dalam file yang berformat json (JavaScript Object Notation)

a = open('dataBanjar.json')#Mendefinisikan a untuk membuka dataBanjar.json
b = open('dataJawa.json')#Mendefinisikan b untuk membuka dataJawa.json
dataBanjar = json.load(a) #Mendefinisikan dataBanjar untuk membaca file dataBanjar.json
dataJawa = json.load(b)#Mendefinisikan dataJawa untuk membaca file dataJawa.json

print(''' 
1.Melatih BOT(Bahasa Banjar)
2.Melatih BOT(Bahasa Jawa)
3.Bepander lawan BOT(Dalam Bahasa Banjar)
4.Ngomong dengan BOT(Dalam Bahasa Jawa)
5.Keluar Program
''')

while True:
	input_awal = input("Masukan Kode: ")
	if input_awal == "1" :
		while True:
			x = input("User\t: ")
			if x == "keluar":
				break
			else :
				y = input("BOT\t: ")
				dataBanjar[x] = y #melakukan tugas pada data dengan mengatautkan input x dengan input y menggunakan variabel dataBanjar.
				b	 = open('dataBanjar.json',"w")#Berfungsi untuk membuka file dengan nama dataBanjar.json dan dalam mode write(menulis)
				json.dump(dataBanjar,b) #Berfungsi untuk menulis objek ke dalam file json
				b.close()#Menutup file json yang dibuka tadi

	elif input_awal == "2" :
			while True:
				x = input("User\t: ")
				if x == "keluar":
					break
				else :
					y = input("BOT\t: ")
					dataJawa[x] = y
					b = open('dataJawa.json',"w")
					json.dump(dataJawa,b)
					b.close()

	elif input_awal == "3" :
		while True :
			x = input("User\t: ")
			if x == 'keluar' :
				break
			if x in dataBanjar:
				print(f'BOT\t: {dataBanjar[x]}')
			else:
				print("BOT\t: Ulun kd paham apa yang pian maksud")

	elif input_awal == "4" :
		while True :
			x = input("User\t: ")
			if x == 'keluar' :
				break
			if x in dataJawa:
				print(f'BOT\t: {dataJawa[x]}')
			else:
				print("BOT\t: Kulo ora ngerti opo yang Kowe maksud")

	elif input_awal == "5":
		print("Selamat Tinggal :)")
		break

	else:
		pass
