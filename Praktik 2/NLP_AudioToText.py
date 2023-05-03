import speech_recognition as sr #mengimpor ekstensi pengenalan suara untuk merubah suara manusia ke teks

engine = sr.Recognizer() #mendefinisikan engine untuk melakukan pengenalan suara , yang dimana Recognizer() adalah class dari speech_recognition
mic = sr.Microphone() #Mendefinisikan mic untuk dapat digunakan mengenali suara melalui mic, 
hasil = ""
engine.pause_treshold = 3 #Mengatur durasi jeda atau pause yang diperbolehkan dalam audio input sebelum pengenalan suara dianggap selesai dalam detik

with mic as source: #Untuk mengatur mikrofon sebagai sumber suara untuk merekam suatu audio
	print("silahkan memulai bicara")
	rekaman = engine.listen(source) #Untuk merekam  audio dari suatu sumber suara yang ditentukan
	print("Waktu habis")

	try:
		hasil = engine.recognize_google(rekaman, language = "id-ID") #untuk mengenali teks dari hasil rekaman audio dengan menggunakan Google Speech Recognition API
		print(hasil)
	except engine.UknownValueError: #Apabila Google Speech Recognition API tidak dapat mengenali maka akan menjalankan perintah dibawahnya 
		print("Maaf tidak bisa di deteksi, mohon coba lagi")
	except Exception as e: 
		print(e)

text_file = open("Hasil.txt", "w")
text_file.write(hasil)
text_file.close()