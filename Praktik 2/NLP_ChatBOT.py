import re #Mengimpor ekstensi yang digunakan untuk melakukan pencarian dan manipulasi string dengan menggunakan ekspresi reguler 
# Ekspresi reguler adalah pola karakter yang digunakan untuk mencocokkan string tertentu atau bagian dari string.

import random#Mengimpor ekstensi yang digunakan untuk melakukan pengacakan pada suatu teks atau angka

sapaan = ["Hai juga","Halo juga"]
keluar = ["Sampai jumpa lain waktu","Sampai jumpa!","Sampai bertemu lagi","Senang ngobrol dengan Anda. Mari kita berhubungan/berkomunikasi lagi"]
kabar =["Kabarku baik","Sangat luar biasa baik","Aku baik-baik saja","Tidak buruk"]

while True :
	x = input("User\t: ")
	
	if re.findall(r'hai|halo|haii|hallo', x): #mencari semua kemunculan string yang cocok pada string x.
		print("BOT\t:",random.choice(sapaan)) #Memilih salah satu output secara acak salah satu elemen dari list sapaan

	elif re.findall(r'Selamat tinggal|selamat tinggal', x):
		print("BOT\t:",random.choice(keluar))
		break

	elif re.findall(r'Apa kabar|Bagaimana kabarmu',x):
		print("BOT\t:",random.choice(kabar))
	else:
		print("BOT\t: Aku tidak paham apa yang Anda maksud") 	